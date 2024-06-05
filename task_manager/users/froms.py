from django import forms
from django.contrib.auth.forms import UserCreationForm
from task_manager.users.models import Users


class UsersViewForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
