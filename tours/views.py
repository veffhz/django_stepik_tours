from django.conf import settings
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound, HttpResponseServerError

from data import tours, departures
from tours.data_helper import find_min_max
from tours.data_helper import random_limit, filter_tours


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        tours_count = settings.RANDOM_TOURS_COUNT
        context['tours'] = random_limit(tours, tours_count)
        return context


class DepartureView(TemplateView):
    template_name = 'departure.html'

    def get_context_data(self, **kwargs):
        context = super(DepartureView, self).get_context_data(**kwargs)
        departure = kwargs['departure']
        filtered_tours = filter_tours(departure, tours)
        context['tours'] = filtered_tours
        context['from'] = departures[departure]
        context['departure'] = departure
        context['nights'] = find_min_max(filtered_tours, 'nights')
        context['prices'] = find_min_max(filtered_tours, 'price')
        return context


class TourView(TemplateView):
    template_name = 'tour.html'

    def get_context_data(self, **kwargs):
        context = super(TourView, self).get_context_data(**kwargs)
        tour = tours[kwargs['tour_id']]
        context['tour'] = tour
        context['stars'] = tour['stars'] * '★'
        context['from'] = departures[tour['departure']]
        return context


def custom_handler404(request, exception):
    return HttpResponseNotFound(render_to_string('404.html'))


def custom_handler500(request):
    return HttpResponseServerError(render_to_string('500.html'))
