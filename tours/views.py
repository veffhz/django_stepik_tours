from django.conf import settings
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound, HttpResponseServerError

from data import tours
from tours.data_helper import random_limit


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        tours_count = settings.RANDOM_TOURS_COUNT
        context['tours'] = random_limit(tours, tours_count)
        return context


class DepartureView(TemplateView):
    template_name = 'departure.html'


class TourView(TemplateView):
    template_name = 'tour.html'

    def get_context_data(self, **kwargs):
        context = super(TourView, self).get_context_data(**kwargs)
        tour = tours[1]
        context['tour'] = tour
        context['stars'] = tour['stars'] * '★'
        return context


def custom_handler404(request, exception):
    return HttpResponseNotFound(render_to_string('404.html'))


def custom_handler500(request):
    return HttpResponseServerError(render_to_string('500.html'))
