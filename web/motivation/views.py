from random import randint

from django.shortcuts import render
from django.views import generic

from .models import Questionnaire

from django import forms


def index(request):
    form = QuestionnaireForm()

    return render(request, 'motivation/index.html', {'form': form})


# http://stackoverflow.com/a/14729363
def instructions(request):

    def get_experiment_type():
        random_experiment = randint(-1, 1)

        questionnaire_id = request.session.get('id')
        questionnaire = Questionnaire.objects.get(id=questionnaire_id)
        questionnaire.experiment_type = random_experiment
        questionnaire.save()

        request.session['experiment_type'] = random_experiment

        if random_experiment == -1:
            return 'antisocial'
        elif random_experiment == 0:
            return 'neutral'
        else:
            return 'prosocial'

    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            mturk = form.cleaned_data['mturk']
            questionnaire = Questionnaire(mturk=mturk)
            questionnaire.save()
            request.session['mturk'] = mturk
            request.session['id'] = questionnaire.id

    return render(
            request,
            'motivation/instructions.html',
            {'mturk': mturk, 'experiment_type': get_experiment_type(), }
            )


def experiment(request):
    experiment_type = request.session.get('experiment_type')
    print(experiment_type)

    def get_experiment_text(experiment_type):
        if experiment_type == -1:
            return 'antisocial'
        elif experiment_type == 0:
            return 'neutral'
        else:
            return 'prosocial'

    return render(
            request,
            'motivation/experiment.html',
            {'experiment_type': get_experiment_text(experiment_type)}
            )


class ThankYouView(generic.TemplateView):
    template_name = 'motivation/thank_you.html'


class QuestionnaireForm(forms.Form):
    model = Questionnaire
    mturk = forms.CharField(label='mturk', max_length=100)
