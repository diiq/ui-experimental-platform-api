from fabric.api import task, local


@task(default=True)
def jobs():
    """Runs the job queue."""
    local("honcho run celery -A app.queue worker "
          "--autoreload --loglevel=warning -B")


@task()
def monitor(port=5555):
    """Runs the job queue."""
    local("honcho run celery -A app.queue flower -p%s" % port)
