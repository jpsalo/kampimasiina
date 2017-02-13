from django.conf.urls import url

from . import views

app_name = 'motivation'
urlpatterns = [
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
        ),
    url(
        r'^background-questions$',
        views.BackgroundQuestionsView.as_view(),
        name='background-questions'
        ),
    url(
        r'^instructions$',
        views.InstructionsView.as_view(),
        name='instructions'
        ),
    url(
        r'^experiment$',
        views.ExperimentView.as_view(),
        name='experiment'
        ),
    url(
        r'^questionnaire$',
        views.QuestionnaireView.as_view(),
        name='questionnaire'
        ),
    url(
        r'^thank-you$',
        views.ThankYouView.as_view(),
        name='thank-you'
        ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.DetailView.as_view(),
        name='detail'
        ),
    url(
        r'^(?P<pk>[0-9]+)/results/$',
        views.ResultsView.as_view(),
        name='results'
        ),
    url(
        r'^(?P<question_id>[0-9]+)/vote/$',
        views.vote,
        name='vote'
        ),
]
