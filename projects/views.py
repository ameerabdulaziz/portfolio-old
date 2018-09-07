from django.views.generic import ListView

from .models import Project


class ProjectListView(ListView):
    queryset = Project.objects.all()
