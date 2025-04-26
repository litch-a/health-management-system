from django import forms
from django.forms.widgets import DateInput
from .models import Client, HealthProgram, ClientEnrollment

# Form for registering a client
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'address']
        widgets = {
            'date_of_birth':  DateInput(attrs={'type': 'date', 'class': 'form-control p-2 border border-gray-300 rounded-md'}),
        }

# Form for creating a health program
class HealthProgramForm(forms.ModelForm):
    class Meta:
        model = HealthProgram
        fields = ['name', 'description']

# Form for enrolling a client in a health program
class ClientEnrollmentForm(forms.ModelForm):
    class Meta:
        model = ClientEnrollment
        fields = ['client', 'program', 'notes']
def __init__(self, *args, **kwargs):
        super(ClientEnrollmentForm, self).__init__(*args, **kwargs)
        # Adding client name to the form to display in the template
        self.fields['client_name'] = forms.CharField(initial=self.instance.client.name, disabled=True)