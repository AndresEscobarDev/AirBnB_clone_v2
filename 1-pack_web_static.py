#!/usr/bin/python3
""" Script that generates a .tgz archive from
the contents of the web_static folder """

from fabric.operations import local
from datetime import datetime


def do_pack():
    """ Function that compress files """
    local("mkdir -p versions")
    r = local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
              capture=True)
    if r.failed:
        return None
    return r
