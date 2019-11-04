from .models import Neighborhood,Business,UserProfile,Post
from django.contrib.auth.models import User
from django.forms import ModelForm


class NeighborhoodForm(ModelForm):
  class Meta:
        model = Neighborhood
        fields= ('neighborhood_name',)
class UpdateProfileForm(ModelForm):
     class Meta:
          model = Neighborhood
          fields= ('first_name','last_name','location')
