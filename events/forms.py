from django import forms
from .models import Event,Participant,Category
from django.forms import DateTimeInput,DateInput,TimeInput


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date' : DateInput(attrs={'type' : 'date','class':'form-control'}),
            'time' : TimeInput(attrs={'type' : 'date','class':'form-control'}),
            'description' : forms.Textarea(attrs={'rows' : 4}),
        }
        
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['Category'].queryset = Category.objects.all()
            self.fields['participants'].queryset = Participant.objects.all() 
        
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
        }
        
        
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'description' : forms.Textarea(attrs={'rows' : 3}),
        }
        
        
