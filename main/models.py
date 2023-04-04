from django.db import models

    
class UserContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    def __str__(self):
        return self.name
       
class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    project_link = models.CharField(max_length=200, null=True, blank=True)
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
    
    def __str__(self):
        return self.project_name
    
    
class Review(models.Model):
    reviewer_name = models.CharField(max_length=150)
    reviewer_position = models.CharField(max_length=150)
    reviewer_message = models.TextField()
    reviewer_image = models.ImageField(
        null=True, blank=True, upload_to='project_img', default="avatar.svg")
    
    def __str__(self):
        return self.reviewer_name
    

class ContactDetails(models.Model):
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    phone_2 = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    
    
        
    


    


    
    
    
    
    
    
    
