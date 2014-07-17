from fabric.api import local, task


@task(default=True)
def deploy(name=""):
    """Deploys to an EB environment"""
    branch_name = "`git rev-parse --symbolic-full-name --abbrev-ref HEAD`"
    commit_hash = "`git rev-parse HEAD | head -c6`"
    local("eb deploy -l %s:%s %s" % (branch_name, commit_hash, name))


@task()
def status(name=""):
    """Shows status of an EB environment.

    Includes the deployed branch and abbreviated commit hash."""

    local("eb status %s" % name)


@task
def new(name):
    """Creates a new EB environment"""
    command = ("eb create -db"
               " -db.engine postgres"
               " -db.i db.m3.medium"
               " -i m3.medium"
               " -p 'Python 2.7'"
               " %s") % name
    local(command)
    print "Don't forget to update the environment variables!"
    # TODO: Look for env.name and copy the environment variables over.


@task
def ssh(name=""):
    """Connects to an EB instance. Lame ATM."""
    local("eb ssh %s" % name)
