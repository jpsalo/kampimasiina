# from random import randint

# from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.views import generic

# from .models import Choice, Question, Questionnaire
from .models import Questionnaire

from django import forms

# Create your views here.


# class IndexView(generic.TemplateView):
# class IndexView(generic.ListView):
#     template_name = 'motivation/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]
#
#     # def get_context_data(self, **kwargs):
#     #     context = super(IndexView, self).get_context_data(**kwargs)
#     #     context['asd'] = 'asd'
#     #     return context


def index(request):
    form = QuestionnaireForm()

    return render(request, 'motivation/index.html', {'form': form})


# class BackgroundQuestionsView(generic.TemplateView):
#     template_name = 'motivation/background_questions.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(BackgroundQuestionsView, self).get_context_data(
#                 **kwargs
#                 )
#         context['ages'] = list(range(18, 100))
#         return context


# http://stackoverflow.com/a/14729363
def instructions(request):
    # if request.method == 'POST':
    #     form = NameForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data['mturk'])

    # age = request.GET.get('age')
    # return render(request, 'motivation/instructions.html', {'event': age})
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            mturk = form.cleaned_data['mturk']
            questionnaire = Questionnaire(questionnaire_mturk=mturk)
            questionnaire.save()

    # model = Questionnaire
    return render(request, 'motivation/instructions.html', {'mturk': mturk})


# class InstructionsView(generic.TemplateView):
#
#     @staticmethod
#     def get_experiment_type():
#         random_experiment = randint(-1, 1)
#         if random_experiment == -1:
#             return 'negative'
#         elif random_experiment == 0:
#             return 'neutral'
#         else:
#             return 'positive'
#
#     def get_context_data(self, **kwargs):
#         context = super(InstructionsView, self).get_context_data(
#                 **kwargs
#                 )
#         context['experiment_type'] = self.get_experiment_type()
#         return context
#
#     template_name = 'motivation/instructions.html'


# class ExperimentView(generic.TemplateView):
def experiment(request):
    mturk = request.GET.get('mturk')
    print('experiment', mturk)
    # template_name = 'motivation/experiment.html'
    return render(request, 'motivation/experiment.html', {'mturk': mturk})


# class QuestionnaireView(generic.TemplateView):
#     template_name = 'motivation/questionnaire.html'


class ThankYouView(generic.TemplateView):
    template_name = 'motivation/thank_you.html'


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'motivation/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'motivation/results.html'


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#             'latest_question_list': latest_question_list,
#             }
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('No this kind of question')
#     return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse('This question %s' % question_id)


# def results(request, question_id):
#     # response = 'This result %s'
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'motivation/detail.html', {
#             'question': question,
#             'error_message': 'No questlove',
#             })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(
#                 reverse('motivation:results', args=(question.id,))
#                 )
#     # return HttpResponse('Vote or die %s' % question_id)


class QuestionnaireForm(forms.Form):
    model = Questionnaire
    mturk = forms.CharField(label='mturk', max_length=100)
