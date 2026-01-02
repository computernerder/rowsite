from django import forms

from .defaults import default_character_data
from .models import Character


class CharacterForm(forms.ModelForm):
    data = forms.JSONField(widget=forms.Textarea(attrs={"rows": 18, "spellcheck": "false"}))

    class Meta:
        model = Character
        fields = ["code", "name", "player", "profession", "data"]
        help_texts = {
            "code": "Stable identifier, e.g., CHAR-001",
            "data": "Full character payload; you can paste/edit JSON here.",
        }

    def __init__(self, *args, **kwargs):
        if "initial" not in kwargs:
            kwargs["initial"] = {}
        kwargs["initial"].setdefault("data", default_character_data())
        super().__init__(*args, **kwargs)

    def clean_code(self):
        code = self.cleaned_data["code"].strip()
        return code
