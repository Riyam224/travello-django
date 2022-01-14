from django.contrib import admin

# Register your models here.
from .models import Destination , Contact

admin.site.register(Destination)
admin.site.register(Contact)