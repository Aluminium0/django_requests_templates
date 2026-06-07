from csv import DictReader

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render


def bus_stations(request):
    page_number = request.GET.get('page', 1)

    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csv_file:
        stations = list(DictReader(csv_file))

    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
