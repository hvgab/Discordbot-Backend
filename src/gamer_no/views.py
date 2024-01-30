from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, View, TemplateView

import logging
import requests

logger = logging.getLogger(__name__)


class ChooseTeamView(TemplateView):
    template_name = "gamer_no/choose_team.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Hubs
        hubs = requests.get("https://www.gamer.no/api/paradise/hub/")
        context["hubs"] = hubs.json()

        return context

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        logger.debug(request.GET)
        return super().get(request, *args, **kwargs)
