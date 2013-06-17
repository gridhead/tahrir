import os

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from .app import get_root
from tahrir_api.model import DBSession
from .widgets import SavingFileField


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    required_keys = [
        'tahrir.pngs.uri',
        'tahrir.admin',
        'tahrir.title',
        'tahrir.base_url',
    ]

    # validate the config
    for key in required_keys:
        if key not in settings:
            raise ValueError("%s required in settings." % key)

    # Make data dir if it doesn't already exist.
    settings['tahrir.pngs.uri'] = os.path.abspath(settings['tahrir.pngs.uri'])
    if not os.path.exists(settings['tahrir.pngs.uri']):
        os.makedirs(settings['tahrir.pngs.uri'])

    # Set that directory on the filefield widget.
    SavingFileField.png_dir = settings['tahrir.pngs.uri']

    # start setting things up
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    # Load secret stuff from secret.ini.
    try:
        from paste.deploy.loadwsgi import appconfig
        secret_config = appconfig('config:secret.ini',
                'tahrir', relative_to='.')
    except IOError:
        # There is a better way to log this message than print.
        print 'Failed to load secret.ini.'
        return 0
    
    settings.update({
        'session.secret':
                secret_config['session.secret'],
        'authnsecret':
                secret_config['authnsecret'],
    })

    authn_policy = AuthTktAuthenticationPolicy(
        secret=settings['authnsecret'],
        callback=groupfinder, # groupfinder callback checks for admin privs
    )
    authz_policy = ACLAuthorizationPolicy()
    session_factory = UnencryptedCookieSessionFactoryConfig(
            settings['session.secret'])
    config = Configurator(
            settings=settings,
            root_factory=get_root,
            session_factory=session_factory,
            authentication_policy=authn_policy,
            authorization_policy=authz_policy)

    config.include('velruse.providers.openid')
    config.add_openid_login(realm="http://localhost:6543/")

    config.add_static_view(
        'static',
        settings.get('tahrir.static.uri', 'static'),
        cache_max_age=3600,
    )
    config.add_static_view(
        'pngs',
        settings['tahrir.pngs.uri'],
        cache_max_age=3600,
    )

    config.add_route('home', '/')
    config.add_route('admin', '/admin')
    config.add_route('qrcode', '/qrcode')
    config.add_route('badge', '/badge/{id}')
    config.add_route('badges', '/badges')
    config.add_route('user', '/user/{id}')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    config.scan()

    return config.make_wsgi_app()


# I think this is fine here...
def groupfinder(userid, request):
    """Currently, this function simply checks if the user
    is listed as an admin in the config file (tahrir.ini).
    This is the callback function used by the authorization
    policy."""
    admins = map(
        str.strip,
        request.registry.settings['tahrir.admin'].split(','),
    )
    if userid in admins:
        return ['group:admins']
