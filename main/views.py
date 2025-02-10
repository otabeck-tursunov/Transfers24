from django.db.models import ExpressionWrapper, F, FloatField, PositiveSmallIntegerField, Func
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import *


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()

        country_id = request.GET.get('country')
        if country_id is not None:
            clubs = clubs.filter(country__id=country_id)

        context = {'clubs': clubs}
        return render(request, 'clubs.html', context)


class TransfersView(View):
    def get(self, request):
        transfers = Transfer.objects.order_by('-created_at')
        context = {'transfers': transfers}
        return render(request, 'latest-transfers.html', context)


class ClubInfoView(View):
    def get(self, request, pk):
        club = get_object_or_404(Club, id=pk)
        players = club.player_set.all()
        context = {'club': club, 'players': players}
        return render(request, 'club-info.html', context)


class Accurate150View(View):
    def get(self, request):
        transfers = Transfer.objects.annotate(
            price_difference=ExpressionWrapper(
                Func(F("price") - F("price_tft"), function="ABS"), output_field=PositiveSmallIntegerField()
            )
        ).order_by('price_difference')
        context = {'transfers': transfers}

        return render(request, 'stats/150-accurate-predictions.html', context)
