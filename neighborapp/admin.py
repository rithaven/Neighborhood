from django.contrib import admin
from .models import UserProfile,Business,Neighborhood,Contacts,Post
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Neighborhood)
admin.site.register(Contacts)
admin.site.register(Post)
