from django import template

register = template.Library()


@register.filter
def field(form, name):
    # Helper to access dynamic form fields safely
    if not hasattr(form, "__getitem__"):
        return ""
    try:
        return form[name]
    except Exception:
        return ""
