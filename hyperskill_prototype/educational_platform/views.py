from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import PrototypeTask


class IndexView(generic.ListView):
    template_name = 'educational_platform/index.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return PrototypeTask.objects.all()


class DetailView(generic.DetailView):
    template_name = 'educational_platform/task.html'
    model = PrototypeTask
