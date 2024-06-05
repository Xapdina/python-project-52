from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from task_manager.users.models import Users


class UsersListView(ListView):
    model = Users
    paginate_by = 20
    template_name = 'users/lists.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = Users
    fields = ['nickname', 'fullname', 'created_at']
    success_message = f'User is successfully registered'


class UserDeleteView(DeleteView):
    model = Users
    fields = ['nickname', 'fullname', 'created_at']


class UserUpdateView(UpdateView):
    model = Users
    fields = ['nickname', 'fullname', 'created_at']


def login_view(request):
    return render(request, 'users/login.html')


