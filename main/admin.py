from django.contrib import admin
from .models import UserContact, Projects, ContactDetails


admin.site.register(UserContact)
admin.site.register(Projects)
admin.site.register(ContactDetails)