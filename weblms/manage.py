#!/usr/bin/env python
from django.core.management import execute_from_command_line
import os
import sys
try:
    import settings
    # Assumed to be in the same directory.
except ImportError:
    import traceback
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    sys.stderr.write( ''.join('!! ' + line for line in lines)  )# Log it or whatever here
    sys.exit(1)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)