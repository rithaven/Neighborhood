from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField


# Create your models here.
class Neighborhood(models.Model):
      neighborhood_name = models.CharField(max_length=30)
      
      def Create_neighborhood(self):
        self.save()

      def delete_neighborhood(self):
         self.delete()

      @classmethod
      def find_neighborhood(cls,neighborhood_id):
          neighborhood =cls.objects.get(id=neighborhood_id)
          return neighborhood

      def update_neighborhood(self,name):
          self.name = name
          self.save()

      def __str__(self):
          return f'{self.neighborhood_name}'

class UserProfile(models.Model):
      first_name =models.CharField(max_length=20, blank=True)
      last_name = models.CharField(max_length=20, blank=True)
      user= models.ForeignKey(User,on_delete= models.CASCADE)
      location= models.CharField(max_length=30, blank=True)
      neighborhood= models.ForeignKey('Neighborhood',on_delete=models.CASCADE,null=True,blank=True)

      def assign_neighborhood(self,neighborhood):
          self.neighborhood = neighborhood
          self.save()
          
      def save_profile(self):
          self.save()
      def delete_profile(self):
          self.delete()
      def __str__(self):
        return f'{self.user.username}'

class Business(models.Model):
      name = models.CharField(max_length=30)
      BusinessOwner = models.ForeignKey(User, on_delete=models.CASCADE)
      B_location = models.CharField(max_length=30, blank=True)
      b_neighborhood= models.ForeignKey('Neighborhood',on_delete=models.CASCADE)
      email = models.EmailField()

      def create_business(self):
            self.save()

      def delete_business(self):
            self.delete()

      @classmethod
      def find_business(cls,business_id):
           business =cls.objects.get(id=business_id)
           return business

      def update_business(self,name):
          self.name =name
          self.save()

      def __str__(self):
          return f'{self.name}'

class Contacts(models.Model):
      name = models.CharField(max_length=30)
      contacts= models.CharField(max_length=30)
      email = models.EmailField()
      neighborhood_contact = models.ForeignKey('Neighborhood',on_delete=models.CASCADE)

      def __str__(self):
          return f'{self.name},{self.email}'

class Post(models.Model):
      title =models.CharField(max_length=40)
      description = HTMLField()
      posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
      neighbors= models.ForeignKey('Neighborhood',on_delete=models.CASCADE)
      postDate= models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return f'{self.title},{self.neighbors.neighborhood_name}'

