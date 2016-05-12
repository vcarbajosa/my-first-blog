from django.contrib import admin

# Register your models hefre.

from .models import Question

admin.site.register(Question)
