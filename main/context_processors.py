from .models import *


def countries(request):
    countries_id = Club.objects.all().values_list('country', flat=True).distinct()
    countries = Country.objects.filter(id__in=countries_id)
    l = len(countries)
    if l % 2 == 0:
        countries_left = countries[:l // 2]
        countries_right = countries[l // 2:]
    else:
        countries_left = countries[:l // 2 + 1]
        countries_right = countries[l // 2 + 1:]
    return {
        'countries_left': countries_left,
        'countries_right': countries_right,
    }
