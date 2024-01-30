from django.urls import path, include
from .views import ChooseTeamView

urlpatterns = [
    path("team_chooser/", ChooseTeamView.as_view()),
]
