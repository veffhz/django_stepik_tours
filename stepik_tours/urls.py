from django.urls import path

from tours.views import MainView, DepartureView, TourView
from tours.views import custom_handler404, custom_handler500

urlpatterns = [
    path('', MainView.as_view()),
    path('departure/<str:departure>/', DepartureView.as_view()),
    path('tour/<int:tour_id>/', TourView.as_view())
]

handler404 = custom_handler404
handler500 = custom_handler500
