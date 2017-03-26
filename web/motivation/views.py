from random import randint

from django.shortcuts import redirect, render, reverse

from .models import Questionnaire

from django import forms


def index(request):
    form = QuestionnaireForm()
    worker_id = request.GET.get('workerId')

    context = {'form': form}

    if worker_id is not None:
        context['mturk'] = worker_id

    return render(request, 'motivation/index.html', context)


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

            existing_questionnaire = Questionnaire.objects.filter(mturk=mturk)
            if existing_questionnaire.exists():
                return redirect(
                        reverse('motivation:index') + '?workerId=' + mturk
                        )
            else:
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

    def get_experiment_text(experiment_type):
        if experiment_type == -1:
            return 'antisocial'
        elif experiment_type == 0:
            return 'neutral'
        else:
            return 'prosocial'

    django_to_javascript = 'from django'

    return render(
            request,
            'motivation/experiment.html',
            {
                'experiment_type': get_experiment_text(experiment_type),
                'djangoToJavascript': django_to_javascript
                }
            )


def thank_you(request):
    if request.method == 'POST':
        earnings = request.POST.get('earnings')

        questionnaire_id = request.session.get('id')
        questionnaire = Questionnaire.objects.get(id=questionnaire_id)
        questionnaire.earnings = earnings
        questionnaire.save()

    return render(request, 'motivation/thank_you.html')


class QuestionnaireForm(forms.Form):
    model = Questionnaire
    mturk = forms.CharField(label='mturk', max_length=100)
