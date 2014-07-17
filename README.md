# UX Experimental Platform API

## Setup

Before you start, you'll need some tools installed on your host system. You may already have Python setup how you like it on your system, but this assumes a pretty stock Mac OS installation.

*If you have Python and virtualenv (with virtualenvwrapper) setup on your system, you can skip to step 4.*

1. Install [Homebrew](http://brew.sh).

2. Install Homebrew's version of Python (which comes with pip ready to go):

        brew install python

3. Install [virtualenv](http://virtualenv.readthedocs.org/en/latest/) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/).

        pip install virtualenv virtualenvwrapper

4. Setup your shell to work with virtualenvwrapper. [Here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file) are the full instructions. For reference, here's roughly what you need in your `.bashrc` or `.zshrc`:

        export WORKON_HOME=$HOME/.virtualenvs
        source /usr/local/bin/virtualenvwrapper.sh

5. Install [PostgreSQL](http://www.postgresql.org/). If you want, configure Postgres to start on boot based on the caveats section in Homebrew (`brew info postgresql`).

        brew install postgresql

6. Run `install.sh` to setup the virtualenv:

        source scripts/install.sh

7. Move .env.sample to .env and .env.test; change variables as necessary.

        cp .env.sample .env
        cp .env.sample .env.test


## Developing

Activate the virtual environment (if you just installed, it's already active; see [Time Savers] for how to have this happen automatically when you cd into the project directory).

    workon ui-experimental-platform-api

Get set up by running:

    fab db.reset
    fab server

You're now running a development server! Yay!


## Time savers

To automatically activate the virualenv when you cd into the project directory, put https://gist.github.com/clneagu/7990272#file-bashrc-L22 in your .profile, .bashrc or .zshrc.


## Contributing

### Style:

Set up your editor to use:

- 4-space tabs.
- No trailing whitespace.
- One trailing newline at the end of the file.

Keep lines < 80 characters. I know. I'm a freak and a tyrant.

One space should be the largest number of spaces between characters within a single line. No fussy alignment of assignments, please.

The test suite will check source for any styles contrary to those defined in PEP8 (https://www.python.org/dev/peps/pep-0008).

## Deploying:

Uses heroku.
