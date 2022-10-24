from django.contrib import admin
from .models import *

admin.site.register(Coordinator)
admin.site.register(CG)
admin.site.register(Task)
admin.site.register(Progress)