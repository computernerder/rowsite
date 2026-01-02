from django.urls import path

from . import views

app_name = "characters"

urlpatterns = [
    path("", views.character_list, name="list"),
    path("characters/new/", views.character_create, name="create"),
    path("characters/<str:code>/", views.character_detail, name="detail"),
    path("characters/<str:code>/edit/", views.character_edit, name="edit"),
    path("characters/<str:code>/qr/", views.character_qr, name="qr"),
]
