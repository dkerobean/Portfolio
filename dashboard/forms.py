from django.forms import ModelForm
from main.models import ContactDetails, Review, Projects, Socials


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
            
class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' 
            
            
class SocialForm(ModelForm):
    
    class Meta:
        model = Socials
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
    
            
            
        
        
        