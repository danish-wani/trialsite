"""
WSGI config for trialsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


#sys.path.append('/home/danish/virtualenv/trialsite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trialsite.settings')

application = get_wsgi_application()

