from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Task


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class TaskForm(forms.ModelForm):
    task_title = forms.CharField(
        error_messages={'required': "This filed is required! Please fill the 'Task title' field."})
    task_description = forms.CharField(
        error_messages={'required': "This filed is required! Please fill the 'Task description' field."})
    time_estimated = forms.DateField(required=False)
    status = forms.CharField(required=False)
    priorities = forms.CharField(required=False)

    class Meta:
        model = Task
        fields = (
            'task_title',
            'task_description',
            'time_estimated',
            'status',
            'priorities',
        )


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )
