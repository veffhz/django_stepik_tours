from tours.data.tours_data import departures
from tours.data.tours_data import title, subtitle, description


def titles(request):
    return {
        'title': title,
        'subtitle': subtitle,
        'description': description,
    }


def departures_data(request):
    return {
        'departures': departures,
    }
