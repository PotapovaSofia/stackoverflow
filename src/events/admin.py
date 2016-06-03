from django.contrib import admin

from .models import Event
from .models import Tag

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ['id', 'title']
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
