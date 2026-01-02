import json
from io import BytesIO

import qrcode
from PIL import Image
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .defaults import default_character_data
from .forms import CharacterForm
from .models import Character


def character_list(request):
	characters = Character.objects.order_by("code")
	return render(request, "characters/list.html", {"characters": characters})


def character_detail(request, code):
	character = get_object_or_404(Character, pk=code)
	data = character.data or {}
	if request.GET.get("download") == "json":
		pretty = json.dumps(data, indent=2)
		return HttpResponse(
			pretty,
			content_type="application/json",
			headers={"Content-Disposition": f"attachment; filename={character.code}_payload.json"},
		)
	pretty_json = json.dumps(data, indent=2)
	data_json = json.dumps(data)
	return render(
		request,
		"characters/detail.html",
		{
			"character": character,
			"data": data,
			"pretty_json": pretty_json,
			"data_json": data_json,
			"skills": CharacterForm.SKILLS,
		},
	)


def character_create(request):
	if request.method == "POST":
		form = CharacterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("characters:detail", code=form.cleaned_data.get("code"))
	else:
		form = CharacterForm(initial={"code": "CHAR-001"})
	return render(
		request,
		"characters/form.html",
		{
			"form": form,
			"mode": "create",
			"abilities": CharacterForm.ABILITIES,
			"skills": CharacterForm.SKILLS,
		},
	)


def character_edit(request, code):
	character = get_object_or_404(Character, pk=code)
	if request.method == "POST":
		form = CharacterForm(request.POST, instance=character)
		if form.is_valid():
			form.save()
			return redirect("characters:detail", code=character.code)
	else:
		form = CharacterForm(instance=character)
	return render(
		request,
		"characters/form.html",
		{
			"form": form,
			"mode": "edit",
			"character": character,
			"abilities": CharacterForm.ABILITIES,
			"skills": CharacterForm.SKILLS,
		},
	)


def character_qr(request, code):
	character = get_object_or_404(Character, pk=code)
	target_url = request.build_absolute_uri(reverse("characters:detail", args=[character.code]))

	qr = qrcode.QRCode(version=None, box_size=10, border=3)
	qr.add_data(target_url)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

	logo_path = settings.PROJECT_ROOT / "images" / "qr_center.png"
	if logo_path.exists():
		try:
			logo = Image.open(logo_path).convert("RGBA")
			qr_width, qr_height = img.size
			factor = 4
			logo_size = qr_width // factor
			logo.thumbnail((logo_size, logo_size), Image.LANCZOS)
			pos = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)
			img.paste(logo, pos, logo)
		except Exception:
			pass

	buffer = BytesIO()
	img.save(buffer, format="PNG")
	buffer.seek(0)

	response = HttpResponse(buffer.getvalue(), content_type="image/png")
	response["Content-Disposition"] = f"inline; filename={character.code}_qr.png"
	return response

# Create your views here.
