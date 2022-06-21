from django.shortcuts import render

from django.urls.base import reverse_lazy

from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):

    model = Task
    template_name = "tasks/create.html"
    context_object_name = "create_task"

    fields = ['name', 'start_date', 'due_date', 'project', 'assignee']

    def get_success_url(self):
        return reverse_lazy("show_project", kwargs={'pk': self.object.pk})
