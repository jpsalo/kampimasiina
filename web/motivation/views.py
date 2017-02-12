from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.


class IndexView(generic.TemplateView):
# class IndexView(generic.ListView):
    template_name = 'motivation/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class BackgroundQuestionsView(generic.TemplateView):
    template_name = 'motivation/background_questions.html'

    def get_context_data(self, **kwargs):
        context = super(BackgroundQuestionsView, self).get_context_data(
                **kwargs
                )
        context['ages'] = list(range(18, 100))
        return context


class InstructionsView(generic.TemplateView):
    template_name = 'motivation/instructions.html'


class DetailView(generic.DetailView):
    model = Question
    template_name = 'motivation/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'motivation/results.html'


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


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'motivation/detail.html', {
            'question': question,
            'error_message': 'No questlove',
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
                reverse('motivation:results', args=(question.id,))
                )
    # return HttpResponse('Vote or die %s' % question_id)
