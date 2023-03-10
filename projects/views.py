from django.urls.base import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "project_list"
    login_url = reverse_lazy("login")

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(members=user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project_list"
    login_url = reverse_lazy("login")


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    context_object_name = "project_list"
    fields = ["name", "description", "members"]

    def get_success_url(self):
        return reverse_lazy("show_project", kwargs={"pk": self.object.pk})
