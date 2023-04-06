from django.forms import ModelForm
from main.models import ContactDetails, Review


class ContactDetailsForm(ModelForm):
    
    class Meta:
        model = ContactDetails
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
            
class ReviewForm(ModelForm):
    
    class Meta:
        model = Review 
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        