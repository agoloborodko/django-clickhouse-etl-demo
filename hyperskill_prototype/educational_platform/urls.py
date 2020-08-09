from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from .forms import PrototypeUserForm

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',
         RegistrationView.as_view(form_class=PrototypeUserForm),
         name='django_registration_register', ),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('convert/', include('lazysignup.urls')),
    # TODO: только lazy uzer может переходить по convert
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('guest/', views.enter_as_guest, name='enter-as-guest'),
]
