from django import forms
from django.forms import TextInput

from profesor.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'cnp', 'date_of_birth', 'email', 'adress' ]
        # fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name',
                                           'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name',
                                          'class': 'form-control'}),
            'cnp': TextInput(attrs={'placeholder': 'Please enter your cnp',
                                    'class': 'form-control'}),
            'date_of_birth': TextInput(attrs={'placeholder': 'Please enter your date of birth',
                                              'class': 'form-control', 'type': 'date'
                #datetime-local pentru a afisa si ora#
                }),
            'email': TextInput(attrs={'placeholder': 'Please enter your email',
                                      'class': 'form-control'}),
            'adress': TextInput(attrs={'placeholder': 'Please enter your adress',
                                      'class': 'form-control'})
        }
