from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreateForm


class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('book:index')
    template_name = 'signup.html'
