from django.conf.urls import url

from . import views

app_name = 'motivation'
urlpatterns = [
    url(
        r'^$',
        views.index,
        name='index'
        ),
    url(
        r'^instructions$',
        views.instructions,
        name='instructions'
        ),
    url(
        r'^experiment$',
        views.experiment,
        name='experiment'
        ),
    url(
        r'^thank-you$',
        views.thank_you,
        name='thank-you'
        ),
]
