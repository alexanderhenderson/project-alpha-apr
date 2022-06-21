from typing import List
from django.shortcuts import render

from django.urls.base import reverse_lazy

from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):

    model = Task
    template_name = "tasks/create.html"
    context_object_name = "create_task"

    fields = ['name', 'start_date', 'due_date', 'project', 'assignee']

    def get_success_url(self):
        return reverse_lazy("show_project", kwargs={'pk': self.object.pk})


class TaskListView(LoginRequiredMixin, ListView):

    model = Task
    template_name = "tasks/list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(assignee=user)
