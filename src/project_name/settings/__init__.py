"""
Main trigger for the settings. This file determines what subset of the settings
should be loaded.
"""

from defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STAGING = False # Only valid if DEBUG=True. Sets the staging settings.

if DEBUG and not STAGING:
    from development import *
elif DEBUG and STAGING:
    from staging import *
else:
    from production import *
