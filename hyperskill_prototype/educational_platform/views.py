from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import PrototypeTask


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tasks = PrototypeTask.objects.all().count()
    num_users = 0
    num_events = 0

    context = {
        'num_tasks': num_tasks,
        'num_users': num_users,
        'num_events': num_events,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class TaskListView(generic.ListView):
    model = PrototypeTask
    context_object_name = 'task_list'   # your own name for the list as a template variable
    template_name = 'educational_platform/task_list.html'
    paginate_by = 30


class TaskDetailView(generic.DetailView):
    model = PrototypeTask
    template_name = 'educational_platform/task_detail.html'
    context_object_name = 'task'
