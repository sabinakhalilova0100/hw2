from django import forms
from .models import List



class CreateTodosForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True,
                            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your title'
                                                          }))


    description = forms.CharField(min_length=1, max_length=3000, required=True,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': 'Enter your description'
                                             }))

    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    status = forms.BooleanField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your status'
                                                          }))


class EditTodosForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title', 'description', 'due_date', 'status']

