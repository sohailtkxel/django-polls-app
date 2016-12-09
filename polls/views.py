from django.shortcuts import render, get_object_or_404
from .models import Questions, Choice
from django.db.models import F
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'qlist'

    def get_queryset(self):
        """ returns the last five published questions """
        return Questions.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Questions, pk=question_id)
    try:
        requested_choice = request.POST.get('choice', None)
        # raise Exception({requested_choice})
        if requested_choice is not None:
            selected_choice = p.choice_set.get(pk=requested_choice)
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "Please choose your choice"
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

