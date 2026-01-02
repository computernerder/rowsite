from django.core.validators import RegexValidator
from django.db import models

from .defaults import default_character_data


class Character(models.Model):
	code = models.CharField(
		max_length=32,
		primary_key=True,
		validators=[RegexValidator(r"^[A-Za-z0-9_-]+$", "Use letters, numbers, dashes, or underscores.")],
		help_text="Stable ID such as CHAR-001",
	)
	name = models.CharField(max_length=120, blank=True)
	player = models.CharField(max_length=120, blank=True)
	profession = models.CharField(max_length=120, blank=True)
	data = models.JSONField(default=default_character_data, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["code"]

	def __str__(self) -> str:
		label = self.name or self.data.get("character_name") or "Unnamed"
		return f"{self.code} — {label}"

	def get_absolute_url(self):
		from django.urls import reverse

		return reverse("characters:detail", args=[self.code])

# Create your models here.
