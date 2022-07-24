""" Fabric file for automatic deployment of the server project




"""
import random

from fabric.api import cd, env, local, run
from fabric.contrib.files import append, exists

REPO_URL = "https://github.com/judgedev/server.git"  # project repro


def deploy() -> None:
    """Main deployment function"""
    site_folder = f"/home/{env.user}/sites/{env.host}"
    run(f"mkdir -p {site_folder}")  # create with intermediate dirs
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()


def _get_latest_source() -> None:
    """Get source code from Git"""
    if exists(".git"):
        run("git fetch")
    else:
        run(f"git clone {REPO_URL} .")
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f"git reset --hard {current_commit}")  # blow any current changes


def _update_virtualenv() -> None:
    """Create or update ve"""
    # how to tell if ve exists
    # ve is in /home/jd/.cache/pypoetry/virtualenvs/
    # if not exists('virtualenv/bin/pip'):
    # if not exists('run('poetry env info --path')'/bin):
    run("poetry install --no-dev")  # just run this??
    # run('./virtualenv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv() -> None:
    """Create the .env script for environment variables"""
    append(".env", "DJANGO_DEBUG_FALSE=y")  # add line to .env
    append(".env", f"SITENAME={env.host}")
    current_contents = run("cat .env")
    if "DJANGO_SECRET_KEY" not in current_contents:
        new_secret = "".join(
            random.SystemRandom().choices(
                "abcdefghijklmnopqrstuvwxyz0123456789", k=50
            )
        )
        append(".env", f"DJANGO_SECRET_KEY={new_secret}")


def _update_static_files() -> None:
    # how to run ve?
    # run('./virtualenv/bin/python manage.py collectstatic --noinput')
    run("poetry run python manage.py collectstatic --noinput")


def _update_database() -> None:
    # run('./virtualenv/bin/python manage.py migrate --noinput')
    run("poetry run python manage.py migrate --noinput")
