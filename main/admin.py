from django.contrib import admin
from .models import UserContact, Projects, ContactDetails, Review


admin.site.register(UserContact)
admin.site.register(Projects)
admin.site.register(ContactDetails)
admin.site.register(Review)
