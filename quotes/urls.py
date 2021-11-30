from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.index, name="index"),
    path('get_quotes', view=views.get_quotes_ajax, name="get_quotes"),
]
