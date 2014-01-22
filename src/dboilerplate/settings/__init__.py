"""
Main trigger for the settings. This file determines what subset of the settings
should be loaded.
"""

import defaults

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STAGING = False # Only valid if DEBUG=True. Sets the staging settings.

if DEBUG:
    from development import *
elif DEBUG and STAGING:
    from staging import *
else:
    from production import *
