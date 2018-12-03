from django.contrib import admin

from .models import Trial
from .models import Country
from .models import City
from .models import Operator

admin.site.register([Trial, Country, City, Operator])