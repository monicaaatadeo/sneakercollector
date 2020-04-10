from django.contrib import admin

from .models import Sneaker, Wearing, Box

# Register your models here.
admin.site.register(Sneaker)
admin.site.register(Wearing)
admin.site.register(Box)
