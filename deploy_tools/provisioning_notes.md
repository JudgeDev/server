Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.9 (Ubuntu on Digital Ocean comes with 3.10)
* poetry + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.9  # if needed
    (python3.9 -V)
    curl −sSL https://raw.githubusercontent.com/python−poetry/poetry/master/get−poetry.py | python
    source $HOME/.poetry/env  # apply changes for current shell
    sudo apt install nginx git

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
