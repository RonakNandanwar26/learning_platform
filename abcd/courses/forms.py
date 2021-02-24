from django import forms
from .models import Course,Video
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, disabled=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    class Meta:
        model = User
        fields = ['username']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),

        }