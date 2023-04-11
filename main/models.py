from django.db import models
import uuid 

    
class UserContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    class Meta:
        ordering = ['-created']
    
    
    def __str__(self):
        return self.name
       
class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    project_link = models.CharField(max_length=200, blank=True)
    project_description = models.CharField(
        max_length=250, null=True, blank=True)
    
    CATEGORY_CHOICES = [
        ('IT', 'IT'), 
        ('MARKETING', 'Marketing')
    ]
    project_category = models.CharField(max_length=150, choices = CATEGORY_CHOICES)
    
    project_image = models.ImageField(
        null=True, blank=True, upload_to='project_img', default="avatar.svg")
    project_date = models.CharField(max_length=150)
    project_industry = models.CharField(max_length=150)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.project_name
    
    
class Review(models.Model):
    reviewer_name = models.CharField(max_length=150)
    reviewer_position = models.CharField(max_length=150)
    reviewer_message = models.TextField()
    reviewer_image = models.ImageField(
        null=True, blank=True, upload_to='review_img', default="review_img/avatar.svg")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.reviewer_name
    

class ContactDetails(models.Model):
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    phone_2 = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.email   
    
class Socials(models.Model):
    github = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    
    def __str__(self):
        return self.facebook
    
    
    
      
        
    


    

  
     
    
    
    
    
      
     
                 


     