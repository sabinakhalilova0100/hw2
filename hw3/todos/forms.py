from django import forms


class CreateTodosForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True)
    description = forms.CharField(min_length=1, max_length=3000, required=True)
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    status = forms.BooleanField()


