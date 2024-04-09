from django.contrib import admin

from myproject import notes
from .models import *
admin.site.register(user) # type: ignore
admin.site.register(notes)
# Register your models here.