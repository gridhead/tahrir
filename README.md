# Tahrir
> fedora-badges https://badges.fedoraproject.org/

Tahrir is an application used by the Fedora Project for issuing [Open
Badges][open-badges].  As per the [about][ob-about] page:

> The concept of Open Badges originated among those working at the Mozilla and
> MacArthur foundations, and out of the research of Erin Knight, founding
> director of the Open Badges project at Mozilla.

Originally, information was hosted on the [Mozilla Wiki][moz-badges].

Tahrir is [Arabic for Liberation][wikipedia-tahrir]

## Contributing

Welcome! Thank you for taking the time to contribute. This project relies on an active and involved community, and we really appreciate your support.

### Quickstart

1. Look for an [existing issue](https://github.com/fedora-infra/tahrir/issues)
   about the bug or feature you're interested in. If you can't find an existing issue, create a [new one](https://github.com/fedora-infra/tahrir/issues/new).

2. Fork the [repository on GitHub](https://github.com/fedora-infra/tahrir).

3. Fix the bug or add the feature, and then write one or more tests which show the bug is fixed or the feature works.

4. Submit a pull request and wait for a maintainer to review it.

More detailed guidelines to help ensure your submission goes smoothly are below.

### Guidelines

#### Python Support

Tahrir supports Python 2.7 version. This is automatically enforced by the continuous integration (CI) suite.

#### Code Style

We follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide
for Python. This is automatically enforced by the CI suite.

#### Tests

The test suites can be run using [tox](http://tox.readthedocs.io/) by simply
running ``tox`` from the repository root. We aim for all code to have test coverage or be explicitly marked as not covered using the ``# no-qa`` comment. We encourage the [Test Driven Development Practice](http://www.extremeprogramming.org/rules/testfirst.html)

Your pull request should contain tests for your new feature or bug fix. If you're not certain how to write tests, we will be happy to help you.

#### Setup a local development environment

To quickly start hacking on tahrir we provide a vagrant setup.

First, install Ansible, Vagrant, the vagrant-sshfs plugin, and the vagrant-libvirt plugin from the official Fedora repos

```
$ sudo dnf install ansible vagrant vagrant-libvirt vagrant-sshfs
```

Now, from within main directory (the one with the Vagrantfile in it) of your git checkout of tahrir, copy the Vagrantfile.example file to Vagrantfile

```
$ cp Vagrantfile.example Vagrantfile
```

Run the ``vagrant up`` command to provision your dev environment

```
$ vagrant up
```

When this command is completed (it may take a while) start tahrir with the following command:

```
$ vagrant ssh -c"cd /vagrant/; pserve --reload development.ini"
```

Once that is running, simply go to http://localhost:8000/ in your browser on your host to see your running tahrir test instance.

[open-badges]: https://openbadges.org
[ob-about]: https://openbadges.org/about/
[moz-badges]: https://wiki.mozilla.org/index.php?title=Badges&oldid=1170927
[wikipedia-tahrir]: http://en.wikipedia.org/wiki/Tahrir_Square
[contributing]: https://github.com/fedora-infra/tahrir/blob/develop/CONTRIBUTING.md
[developing]: https://github.com/fedora-infra/tahrir/blob/develop/DEVELOPING.md
