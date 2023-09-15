from django.shortcuts import render
from django.views.generic import ListView, DetailView

from boat.models import Boat, BoatHistory


class BoatListView(ListView):
    model = Boat


class BoatDetailView(DetailView):
    model = Boat
