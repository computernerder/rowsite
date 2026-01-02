from django.contrib import admin

from .models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
	list_display = ("code", "name", "player", "profession", "updated_at")
	search_fields = ("code", "name", "player", "profession")

# Register your models here.
