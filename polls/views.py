from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import CreateView, DeleteView, TemplateView
from django.shortcuts import render, redirect

from .forms import RegisterUserForm
from .models import Question, Choice, AbsUser
from django.template import loader, TemplateDoesNotExist
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'вы не сделали выбор'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class RegisterViews(CreateView):
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main/login')


class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('polls/index')


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class BBLoginView(LoginView):
    template_name = 'main/login.html'


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')
