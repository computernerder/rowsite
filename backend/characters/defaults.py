from copy import deepcopy

DEFAULT_CHARACTER = {
    "id": "CHAR-001",
    "character_name": "",
    "player": "",
    "profession": "",
    "primary_path": "",
    "race": "",
    "ancestry": "",
    "background": "",
    "level": 1,
    "total_experience": 0,
    "stored_advance": "",
    "ability_scores": {
        "Might":     {"mod": 0, "saving_throw": 0, "total": 10, "roll": 10, "race": 0, "misc": 0},
        "Agility":   {"mod": 0, "saving_throw": 0, "total": 10, "roll": 10, "race": 0, "misc": 0},
        "Endurance": {"mod": 0, "saving_throw": 0, "total": 10, "roll": 10, "race": 0, "misc": 0},
        "Wisdom":    {"mod": 0, "saving_throw": 0, "total": 10, "roll": 10, "race": 0, "misc": 0},
        "Intellect": {"mod": 0, "saving_throw": 0, "total": 10, "roll": 10, "race": 0, "misc": 0},
        "Charisma":  {"mod": 0, "saving_throw": 0, "total": 10, "roll": 10, "race": 0, "misc": 0},
    },
    "defense": {
        "base": 9,
        "agility": 0,
        "shield": "",
        "misc": 0,
        "total": "",
    },
    "speed": 0,
    "initiative": 0,
    "health": {"max": 0, "current": 0, "wounds": 0},
    "armor_hp": {"max": 0, "current": 0},
    "life_points": {"max": 0, "current": 0},
    "focus": {"max": 0, "current": 0},
    "passive": {
        "perception": {"base": 10, "skill": 0, "misc": 0, "total": 10},
        "insight": {"base": 10, "skill": 0, "misc": 0, "total": 10},
    },
    "attack_mods": {
        "melee": {"attr": 0, "misc": 0, "total": 0},
        "ranged": {"attr": 0, "misc": 0, "total": 0},
    },
    "skills": {
        "Acrobatics": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Animal Handling": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Appraisal": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Arcana": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Athletics": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Crafting": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Deception": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Diplomacy": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "History": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Insight": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Intimidation": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Investigation": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Medicine": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Nature": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Perception": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Performance": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Persuasion": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Sleight of Hand": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Stealth": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Streetwise": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Survival": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
        "Taming": {"trained": False, "mod": 0, "rank": 0, "misc": 0, "total": 0},
    },
    "proficiencies": [],
    "languages": [],
    "attacks": [
        {"attack_action": "", "bonus": 0, "damage": "", "type": "", "range": ""}
    ],
    "talents": [
        {"name": "", "text": ""}
    ],
    "features": [
        {"name": "", "text": ""}
    ],
    "spellcrafting": {
        "save_dc": 0,
        "attack_bonus": 0,
        "crafting_points": {"max": 0},
        "casting": "",
        "spells": [
            {"name": "", "cp": 0, "details": ""}
        ],
    },
    "inventory": {
        "items": [],
        "total_weight": "",
    },
    "notes": "",
    "physical_traits": {
        "height": "",
        "weight": "",
        "size": "",
        "age": "",
        "creature_type": "",
        "eyes": "",
        "skin": "",
        "hair": "",
    },
    "personality": {
        "traits": "",
        "ideal": "",
        "bond": "",
        "flaw": "",
    },
    "alignment": {"alignment": "", "mod": 0},
    "reputation": {"reputation": "", "mod": 0},
    "qr_payload": "",
    "footer": {
        "datecode": "",
        "config": "",
        "id": "",
    },
}


def default_character_data():
    """Return a fresh copy of the default character payload."""
    return deepcopy(DEFAULT_CHARACTER)
