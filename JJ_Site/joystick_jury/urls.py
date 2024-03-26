from django.urls import path

from . import views

urlpatterns = [
    path("", views.add_game, name ="add_game"),
    path("games", views.game_list, name= "game_list"),
    path('remove', views.remove_game, name='remove_game')
]