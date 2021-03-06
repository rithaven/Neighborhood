from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile,Business,Post,Neighborhood,Contacts
# Create your tests here.
class UserProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='wecode',password='moxx')
        self.new_profile = UserProfile(id=1,first_name='ritha',last_name='kuku',user=self.new_user,location='kimironko')
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Beza')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,UserProfile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_assign_neighborhood(self):

        self.new_profile.save_profile()
        profile = UserProfile.objects.filter(id=1).first()
        self.new_neighborhood.save()
        neighborhood = Neighborhood.objects.filter(id=1).first()
        profile.assign_neighborhood(neighborhood)

        self.assertEqual(profile.neighborhood.id,1)

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Beza')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    def test_Create_neighborhood(self):
        self.new_neighborhood.Create_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_neighborhood(self):
        self.new_neighborhood.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)

    def test_find_neighborhood(self):
        self.new_neighborhood.Create_neighborhood()
        neighborhood = Neighborhood.find_neighborhood(1)
        self.assertEqual(neighborhood.neighborhood_name,'Beza')

    def test_update_neighborhood(self):
        self.new_neighborhood.Create_neighborhood()
        neighborhood = Neighborhood.find_neighborhood(1)
        neighborhood.neighborhood_name = 'Kabosi'
        self.assertEqual(neighborhood.neighborhood_name,'Kabosi')


class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='wecode',password='moxx')
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Beza')
        self.new_neighborhood.save()
        self.new_business = Business(id = 1,name='me2you',BusinessOwner=self.new_user,B_location='kimironko',b_neighborhood=self.new_neighborhood,email='ME@email.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_create_business(self):
        self.new_business.create_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):
        self.new_business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)

    def test_find_business(self):
        self.new_business.create_business()
        business = Business.find_business(1)
        self.assertEqual(business.name,'me2you')

    def test_update_business(self):
        self.new_business.create_business()
        business = Business.find_business(1)
        business.update_business('resto')
        self.assertEqual(business.name,'resto')