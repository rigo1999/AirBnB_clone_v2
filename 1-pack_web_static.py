#!/usr/bin/python3
"""
    Generates a .tgz archive from the contents of the web_static folder.
    
    Returns:
        str: The archive path if the archive has been correctly generated.
        None: If the archive has not been generated correctly.
"""


from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
