from django.urls import path

from . import views

app_name = "characters"

urlpatterns = [
    path("", views.character_list, name="list"),
    path("new/", views.character_create, name="create"),
    path("<str:code>/", views.character_detail, name="detail"),
    path("<str:code>/edit/", views.character_edit, name="edit"),
    path("<str:code>/qr/", views.character_qr, name="qr"),
]
