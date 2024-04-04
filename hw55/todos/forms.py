from django import forms
from .models import List, Category


class EditTodosForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title', 'description', 'due_date', 'status']


class CreateTodosForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter product title'
    }))
    description = forms.CharField(min_length=0, max_length=2000, required=False, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter description'
    }))
    due_date = forms.IntegerField(min_value=0, max_value=1000, required=True, widget=forms.DateInput(attrs={'type':'date'}))
    status = forms.BooleanField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your status'
                                                          }))


class TodosForm(forms.ModelForm):
    class Meta:
        model = List
        # fields = ['name', 'price', 'description']
        fields = '__all__'
        widgets = {
            'title': forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'due_date': forms.DateInput({
                'class': 'form-control',
                'placeholder': 'Enter product amount'
            }),
            'description': forms.Textarea({
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),


            'category': forms.Select({
                'class': 'form-select',
            }),
        }


class CategoryTodosForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'title': forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'due_date': forms.DateInput({
                'class': 'form-control',
                'placeholder': 'Enter product amount'
            }),
            'description': forms.Textarea({
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'status': forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Enter price in KZT'
            }),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Enter category name'
            })
        }
