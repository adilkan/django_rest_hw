from django.contrib import admin
from .models import Director,Review,Movie

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)