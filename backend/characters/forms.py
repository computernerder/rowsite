from django import forms

from .defaults import default_character_data
from .models import Character


def _slug(name: str) -> str:
    return name.lower().replace(" ", "_")


class CharacterForm(forms.ModelForm):
    # Specs to drive dynamic field creation
    ABILITIES = [
        ("Might", _slug("Might")),
        ("Agility", _slug("Agility")),
        ("Endurance", _slug("Endurance")),
        ("Wisdom", _slug("Wisdom")),
        ("Intellect", _slug("Intellect")),
        ("Charisma", _slug("Charisma")),
    ]
    ABILITY_PARTS = ["mod", "saving_throw", "total", "roll", "race", "misc"]

    SKILLS = [
        ("Acrobatics", _slug("Acrobatics")),
        ("Animal Handling", _slug("Animal Handling")),
        ("Appraisal", _slug("Appraisal")),
        ("Arcana", _slug("Arcana")),
        ("Athletics", _slug("Athletics")),
        ("Crafting", _slug("Crafting")),
        ("Deception", _slug("Deception")),
        ("Diplomacy", _slug("Diplomacy")),
        ("History", _slug("History")),
        ("Insight", _slug("Insight")),
        ("Intimidation", _slug("Intimidation")),
        ("Investigation", _slug("Investigation")),
        ("Medicine", _slug("Medicine")),
        ("Nature", _slug("Nature")),
        ("Perception", _slug("Perception")),
        ("Performance", _slug("Performance")),
        ("Persuasion", _slug("Persuasion")),
        ("Sleight of Hand", _slug("Sleight of Hand")),
        ("Stealth", _slug("Stealth")),
        ("Streetwise", _slug("Streetwise")),
        ("Survival", _slug("Survival")),
        ("Taming", _slug("Taming")),
    ]
    SKILL_PARTS = ["trained", "mod", "rank", "misc", "total"]

    # Top-level character/meta fields (not all are model fields)
    primary_path = forms.CharField(required=False)
    race = forms.CharField(required=False)
    ancestry = forms.CharField(required=False)
    background = forms.CharField(required=False)
    level = forms.IntegerField(required=False, initial=1)
    total_experience = forms.IntegerField(required=False, initial=0)
    stored_advance = forms.CharField(required=False)
    speed = forms.IntegerField(required=False, initial=0)
    initiative = forms.IntegerField(required=False, initial=0)
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 4}))

    # Defense/health blocks
    defense_base = forms.IntegerField(required=False, initial=9)
    defense_agility = forms.IntegerField(required=False, initial=0)
    defense_shield = forms.CharField(required=False)
    defense_misc = forms.IntegerField(required=False, initial=0)
    defense_total = forms.IntegerField(required=False)

    health_max = forms.IntegerField(required=False, initial=0)
    health_current = forms.IntegerField(required=False, initial=0)
    health_wounds = forms.IntegerField(required=False, initial=0)

    armor_hp_max = forms.IntegerField(required=False, initial=0)
    armor_hp_current = forms.IntegerField(required=False, initial=0)

    life_points_max = forms.IntegerField(required=False, initial=0)
    life_points_current = forms.IntegerField(required=False, initial=0)

    focus_max = forms.IntegerField(required=False, initial=0)
    focus_current = forms.IntegerField(required=False, initial=0)

    passive_perception_base = forms.IntegerField(required=False, initial=10)
    passive_perception_skill = forms.IntegerField(required=False, initial=0)
    passive_perception_misc = forms.IntegerField(required=False, initial=0)
    passive_perception_total = forms.IntegerField(required=False, initial=10)

    passive_insight_base = forms.IntegerField(required=False, initial=10)
    passive_insight_skill = forms.IntegerField(required=False, initial=0)
    passive_insight_misc = forms.IntegerField(required=False, initial=0)
    passive_insight_total = forms.IntegerField(required=False, initial=10)

    attack_melee_attr = forms.IntegerField(required=False, initial=0)
    attack_melee_misc = forms.IntegerField(required=False, initial=0)
    attack_melee_total = forms.IntegerField(required=False, initial=0)

    attack_ranged_attr = forms.IntegerField(required=False, initial=0)
    attack_ranged_misc = forms.IntegerField(required=False, initial=0)
    attack_ranged_total = forms.IntegerField(required=False, initial=0)

    # Spellcrafting basics
    spell_save_dc = forms.IntegerField(required=False, initial=0)
    spell_attack_bonus = forms.IntegerField(required=False, initial=0)
    spell_cp_max = forms.IntegerField(required=False, initial=0)
    spell_casting = forms.CharField(required=False)
    spell_spells_text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
        help_text="One spell per line: name|cp|details",
    )

    # Lists
    proficiencies_text = forms.CharField(required=False, help_text="Comma-separated")
    languages_text = forms.CharField(required=False, help_text="Comma-separated")
    attacks_text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
        help_text="One attack per line: action|bonus|damage|type|range",
    )
    talents_text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
        help_text="One talent per line: name|text",
    )
    features_text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
        help_text="One feature per line: name|text",
    )
    inventory_items_text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
        help_text="One item per line",
    )
    inventory_total_weight = forms.CharField(required=False)

    # Physical and personality
    height = forms.CharField(required=False)
    weight = forms.CharField(required=False)
    size = forms.CharField(required=False)
    age = forms.CharField(required=False)
    creature_type = forms.CharField(required=False)
    eyes = forms.CharField(required=False)
    skin = forms.CharField(required=False)
    hair = forms.CharField(required=False)

    personality_traits = forms.CharField(required=False)
    personality_ideal = forms.CharField(required=False)
    personality_bond = forms.CharField(required=False)
    personality_flaw = forms.CharField(required=False)

    alignment_alignment = forms.CharField(required=False)
    alignment_mod = forms.IntegerField(required=False, initial=0)

    reputation_reputation = forms.CharField(required=False)
    reputation_mod = forms.IntegerField(required=False, initial=0)

    qr_payload = forms.CharField(required=False)

    footer_datecode = forms.CharField(required=False)
    footer_config = forms.CharField(required=False)
    footer_id = forms.CharField(required=False)

    class Meta:
        model = Character
        fields = ["code", "name", "player", "profession"]
        help_texts = {
            "code": "Stable identifier, e.g., CHAR-001",
        }

    def __init__(self, *args, **kwargs):
        if "initial" not in kwargs:
            kwargs["initial"] = {}
        base = kwargs.get("instance").data if kwargs.get("instance") else None
        payload = base or default_character_data()
        initial = kwargs["initial"]

        # top-level initial
        for key in [
            "primary_path",
            "race",
            "ancestry",
            "background",
            "stored_advance",
            "qr_payload",
        ]:
            initial.setdefault(key, payload.get(key, ""))
        for key in ["level", "total_experience", "speed", "initiative"]:
            initial.setdefault(key, payload.get(key, 0))
        initial.setdefault("notes", payload.get("notes", ""))

        # defense
        defense = payload.get("defense", {})
        initial.setdefault("defense_base", defense.get("base", 9))
        initial.setdefault("defense_agility", defense.get("agility", 0))
        initial.setdefault("defense_shield", defense.get("shield", ""))
        initial.setdefault("defense_misc", defense.get("misc", 0))
        initial.setdefault("defense_total", defense.get("total", ""))

        # health blocks
        health = payload.get("health", {})
        initial.setdefault("health_max", health.get("max", 0))
        initial.setdefault("health_current", health.get("current", 0))
        initial.setdefault("health_wounds", health.get("wounds", 0))

        armor_hp = payload.get("armor_hp", {})
        initial.setdefault("armor_hp_max", armor_hp.get("max", 0))
        initial.setdefault("armor_hp_current", armor_hp.get("current", 0))

        life_points = payload.get("life_points", {})
        initial.setdefault("life_points_max", life_points.get("max", 0))
        initial.setdefault("life_points_current", life_points.get("current", 0))

        focus = payload.get("focus", {})
        initial.setdefault("focus_max", focus.get("max", 0))
        initial.setdefault("focus_current", focus.get("current", 0))

        # passive
        passive = payload.get("passive", {})
        perception = passive.get("perception", {})
        initial.setdefault("passive_perception_base", perception.get("base", 10))
        initial.setdefault("passive_perception_skill", perception.get("skill", 0))
        initial.setdefault("passive_perception_misc", perception.get("misc", 0))
        initial.setdefault("passive_perception_total", perception.get("total", 10))
        insight = passive.get("insight", {})
        initial.setdefault("passive_insight_base", insight.get("base", 10))
        initial.setdefault("passive_insight_skill", insight.get("skill", 0))
        initial.setdefault("passive_insight_misc", insight.get("misc", 0))
        initial.setdefault("passive_insight_total", insight.get("total", 10))

        # attacks
        attack_mods = payload.get("attack_mods", {})
        melee = attack_mods.get("melee", {})
        initial.setdefault("attack_melee_attr", melee.get("attr", 0))
        initial.setdefault("attack_melee_misc", melee.get("misc", 0))
        initial.setdefault("attack_melee_total", melee.get("total", 0))
        ranged = attack_mods.get("ranged", {})
        initial.setdefault("attack_ranged_attr", ranged.get("attr", 0))
        initial.setdefault("attack_ranged_misc", ranged.get("misc", 0))
        initial.setdefault("attack_ranged_total", ranged.get("total", 0))

        # abilities
        ability_scores = payload.get("ability_scores", {})
        for label, slug in self.ABILITIES:
            parts = ability_scores.get(label, {})
            for part in self.ABILITY_PARTS:
                field_name = f"ability_{slug}_{part}"
                self.base_fields[field_name] = forms.IntegerField(required=False, initial=parts.get(part, 0))
                initial.setdefault(field_name, parts.get(part, 0))

        # skills
        skills = payload.get("skills", {})
        for label, slug in self.SKILLS:
            skill_data = skills.get(label, {})
            self.base_fields[f"skill_{slug}_trained"] = forms.BooleanField(required=False, initial=skill_data.get("trained", False))
            for part in ["mod", "rank", "misc", "total"]:
                fname = f"skill_{slug}_{part}"
                self.base_fields[fname] = forms.IntegerField(required=False, initial=skill_data.get(part, 0))
                initial.setdefault(fname, skill_data.get(part, 0))
            initial.setdefault(f"skill_{slug}_trained", skill_data.get("trained", False))

        # proficiencies / languages
        initial.setdefault("proficiencies_text", ", ".join(payload.get("proficiencies", [])))
        initial.setdefault("languages_text", ", ".join(payload.get("languages", [])))

        # attacks list
        attacks_lines = []
        for atk in payload.get("attacks", []) or []:
            attacks_lines.append(
                "|".join([
                    str(atk.get("attack_action", "")),
                    str(atk.get("bonus", "")),
                    str(atk.get("damage", "")),
                    str(atk.get("type", "")),
                    str(atk.get("range", "")),
                ])
            )
        initial.setdefault("attacks_text", "\n".join(attacks_lines))

        # talents / features
        def _lines(collection):
            lines = []
            for itm in collection or []:
                lines.append("|".join([str(itm.get("name", "")), str(itm.get("text", ""))]))
            return "\n".join(lines)

        initial.setdefault("talents_text", _lines(payload.get("talents", [])))
        initial.setdefault("features_text", _lines(payload.get("features", [])))

        # spellcrafting
        spellcrafting = payload.get("spellcrafting", {})
        initial.setdefault("spell_save_dc", spellcrafting.get("save_dc", 0))
        initial.setdefault("spell_attack_bonus", spellcrafting.get("attack_bonus", 0))
        initial.setdefault("spell_cp_max", spellcrafting.get("crafting_points", {}).get("max", 0))
        initial.setdefault("spell_casting", spellcrafting.get("casting", ""))
        spell_lines = []
        for sp in spellcrafting.get("spells", []) or []:
            spell_lines.append("|".join([str(sp.get("name", "")), str(sp.get("cp", "")), str(sp.get("details", ""))]))
        initial.setdefault("spell_spells_text", "\n".join(spell_lines))

        # inventory
        inv = payload.get("inventory", {})
        initial.setdefault("inventory_total_weight", inv.get("total_weight", ""))
        initial.setdefault("inventory_items_text", "\n".join(inv.get("items", [])))

        # physical traits
        phys = payload.get("physical_traits", {})
        for key in ["height", "weight", "size", "age", "creature_type", "eyes", "skin", "hair"]:
            initial.setdefault(key, phys.get(key, ""))

        # personality
        pers = payload.get("personality", {})
        initial.setdefault("personality_traits", pers.get("traits", ""))
        initial.setdefault("personality_ideal", pers.get("ideal", ""))
        initial.setdefault("personality_bond", pers.get("bond", ""))
        initial.setdefault("personality_flaw", pers.get("flaw", ""))

        # alignment & reputation
        align = payload.get("alignment", {})
        initial.setdefault("alignment_alignment", align.get("alignment", ""))
        initial.setdefault("alignment_mod", align.get("mod", 0))
        rep = payload.get("reputation", {})
        initial.setdefault("reputation_reputation", rep.get("reputation", ""))
        initial.setdefault("reputation_mod", rep.get("mod", 0))

        # footer
        footer = payload.get("footer", {})
        initial.setdefault("footer_datecode", footer.get("datecode", ""))
        initial.setdefault("footer_config", footer.get("config", ""))
        initial.setdefault("footer_id", footer.get("id", ""))

        super().__init__(*args, **kwargs)

    def clean_code(self):
        return self.cleaned_data["code"].strip()

    @staticmethod
    def _int(val):
        try:
            return int(val)
        except (TypeError, ValueError):
            return 0

    @staticmethod
    def _lines_to_list(value):
        if not value:
            return []
        return [line.strip() for line in value.splitlines() if line.strip()]

    @staticmethod
    def _comma_list(value):
        if not value:
            return []
        return [part.strip() for part in value.split(",") if part.strip()]

    def _parse_pairs(self, value):
        lines = []
        for line in self._lines_to_list(value):
            parts = [p.strip() for p in line.split("|", 1)]
            if len(parts) == 2:
                lines.append({"name": parts[0], "text": parts[1]})
            elif parts:
                lines.append({"name": parts[0], "text": ""})
        return lines

    def _parse_spells(self, value):
        spells = []
        for line in self._lines_to_list(value):
            name, cp, details = (line.split("|", 2) + ["", ""])[:3]
            spells.append({"name": name.strip(), "cp": self._int(cp), "details": details.strip()})
        return spells

    def _parse_attacks(self, value):
        attacks = []
        for line in self._lines_to_list(value):
            fields = (line.split("|") + ["", "", "", "", ""])[:5]
            attacks.append(
                {
                    "attack_action": fields[0].strip(),
                    "bonus": self._int(fields[1]),
                    "damage": fields[2].strip(),
                    "type": fields[3].strip(),
                    "range": fields[4].strip(),
                }
            )
        return attacks

    def save(self, commit=True):
        instance = super().save(commit=False)
        cleaned = self.cleaned_data
        payload = default_character_data()

        # top-level
        payload.update(
            {
                "id": instance.code,
                "character_name": cleaned.get("name", ""),
                "player": cleaned.get("player", ""),
                "profession": cleaned.get("profession", ""),
                "primary_path": cleaned.get("primary_path", ""),
                "race": cleaned.get("race", ""),
                "ancestry": cleaned.get("ancestry", ""),
                "background": cleaned.get("background", ""),
                "level": self._int(cleaned.get("level")),
                "total_experience": self._int(cleaned.get("total_experience")),
                "stored_advance": cleaned.get("stored_advance", ""),
                "speed": self._int(cleaned.get("speed")),
                "initiative": self._int(cleaned.get("initiative")),
                "notes": cleaned.get("notes", ""),
            }
        )

        # abilities
        ability_scores = {}
        for label, slug in self.ABILITIES:
            ability_scores[label] = {}
            for part in self.ABILITY_PARTS:
                ability_scores[label][part] = self._int(cleaned.get(f"ability_{slug}_{part}"))
        payload["ability_scores"] = ability_scores

        # defense
        payload["defense"] = {
            "base": self._int(cleaned.get("defense_base")),
            "agility": self._int(cleaned.get("defense_agility")),
            "shield": cleaned.get("defense_shield", ""),
            "misc": self._int(cleaned.get("defense_misc")),
            "total": cleaned.get("defense_total", ""),
        }

        # health blocks
        payload["health"] = {
            "max": self._int(cleaned.get("health_max")),
            "current": self._int(cleaned.get("health_current")),
            "wounds": self._int(cleaned.get("health_wounds")),
        }
        payload["armor_hp"] = {
            "max": self._int(cleaned.get("armor_hp_max")),
            "current": self._int(cleaned.get("armor_hp_current")),
        }
        payload["life_points"] = {
            "max": self._int(cleaned.get("life_points_max")),
            "current": self._int(cleaned.get("life_points_current")),
        }
        payload["focus"] = {
            "max": self._int(cleaned.get("focus_max")),
            "current": self._int(cleaned.get("focus_current")),
        }

        # passive
        payload["passive"] = {
            "perception": {
                "base": self._int(cleaned.get("passive_perception_base")),
                "skill": self._int(cleaned.get("passive_perception_skill")),
                "misc": self._int(cleaned.get("passive_perception_misc")),
                "total": self._int(cleaned.get("passive_perception_total")),
            },
            "insight": {
                "base": self._int(cleaned.get("passive_insight_base")),
                "skill": self._int(cleaned.get("passive_insight_skill")),
                "misc": self._int(cleaned.get("passive_insight_misc")),
                "total": self._int(cleaned.get("passive_insight_total")),
            },
        }

        # attacks
        payload["attack_mods"] = {
            "melee": {
                "attr": self._int(cleaned.get("attack_melee_attr")),
                "misc": self._int(cleaned.get("attack_melee_misc")),
                "total": self._int(cleaned.get("attack_melee_total")),
            },
            "ranged": {
                "attr": self._int(cleaned.get("attack_ranged_attr")),
                "misc": self._int(cleaned.get("attack_ranged_misc")),
                "total": self._int(cleaned.get("attack_ranged_total")),
            },
        }

        # skills
        skills_block = {}
        for label, slug in self.SKILLS:
            skills_block[label] = {
                "trained": bool(cleaned.get(f"skill_{slug}_trained")),
                "mod": self._int(cleaned.get(f"skill_{slug}_mod")),
                "rank": self._int(cleaned.get(f"skill_{slug}_rank")),
                "misc": self._int(cleaned.get(f"skill_{slug}_misc")),
                "total": self._int(cleaned.get(f"skill_{slug}_total")),
            }
        payload["skills"] = skills_block

        payload["proficiencies"] = self._comma_list(cleaned.get("proficiencies_text"))
        payload["languages"] = self._comma_list(cleaned.get("languages_text"))
        payload["attacks"] = self._parse_attacks(cleaned.get("attacks_text"))
        payload["talents"] = self._parse_pairs(cleaned.get("talents_text"))
        payload["features"] = self._parse_pairs(cleaned.get("features_text"))

        payload["spellcrafting"] = {
            "save_dc": self._int(cleaned.get("spell_save_dc")),
            "attack_bonus": self._int(cleaned.get("spell_attack_bonus")),
            "crafting_points": {"max": self._int(cleaned.get("spell_cp_max"))},
            "casting": cleaned.get("spell_casting", ""),
            "spells": self._parse_spells(cleaned.get("spell_spells_text")),
        }

        payload["inventory"] = {
            "items": self._lines_to_list(cleaned.get("inventory_items_text")),
            "total_weight": cleaned.get("inventory_total_weight", ""),
        }

        payload["physical_traits"] = {
            "height": cleaned.get("height", ""),
            "weight": cleaned.get("weight", ""),
            "size": cleaned.get("size", ""),
            "age": cleaned.get("age", ""),
            "creature_type": cleaned.get("creature_type", ""),
            "eyes": cleaned.get("eyes", ""),
            "skin": cleaned.get("skin", ""),
            "hair": cleaned.get("hair", ""),
        }

        payload["personality"] = {
            "traits": cleaned.get("personality_traits", ""),
            "ideal": cleaned.get("personality_ideal", ""),
            "bond": cleaned.get("personality_bond", ""),
            "flaw": cleaned.get("personality_flaw", ""),
        }

        payload["alignment"] = {
            "alignment": cleaned.get("alignment_alignment", ""),
            "mod": self._int(cleaned.get("alignment_mod")),
        }
        payload["reputation"] = {
            "reputation": cleaned.get("reputation_reputation", ""),
            "mod": self._int(cleaned.get("reputation_mod")),
        }

        payload["qr_payload"] = cleaned.get("qr_payload", "")
        payload["footer"] = {
            "datecode": cleaned.get("footer_datecode", ""),
            "config": cleaned.get("footer_config", ""),
            "id": cleaned.get("footer_id", ""),
        }

        instance.data = payload
        instance.name = cleaned.get("name", "")
        instance.player = cleaned.get("player", "")
        instance.profession = cleaned.get("profession", "")
        if commit:
            instance.save()
        return instance
