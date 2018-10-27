import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trialsite.settings')
sys.path = ['/home/danish/virtualenv/trialsite']
application = get_wsgi_application()
