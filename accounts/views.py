from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import FormView

from django.urls.base import reverse_lazy
from django.http.response import HttpResponseRedirect

# Create your views here.


class SigninView(FormView):

    form_class = UserCreationForm
    template_name = "registration/signup.html"

    def form_valid(self, form):

        form.save()
        user = form.save()
        login(
            self.request,
            user,
            backend='django.contrib.auth.backends.ModelBackend'
            )

        return HttpResponseRedirect(reverse_lazy('home'))
