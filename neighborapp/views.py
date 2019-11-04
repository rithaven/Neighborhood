from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .models import UserProfile, Neighborhood, Business,EmergencyContacts,Post
from .forms import NeighborhoodForm,UpdateProfileForm,AddBusinessForm,PostForm
from django.contrib.auth.models import User
import datetime

# Create your views here.
def home(request):
    if no request.user.is_authenticated:
          return redirect('signout')
    else:
      if request.user.id==1:
         if request.method == 'POST':
            form= NeighborhoodForm(request.POST)
            if form.is_valid():
                neighborhood= Neighborhood(neighborhood_name=request.POST['neighborhood_name'],neighborhood_location=request.POST['neighborhood_location'])
                neighborhood.save()
            return redirect('index')
         else:
              form= NeighborhoodForm()
         neighborhoods = Neighborhood.objects.all()
         return render(request,'Home.html',{'neighborhoods,'form':form})
      elif request.user !=1:
          user = UserProfile.objects.filter(user=request.user).first()
          if user is None:
              user = UserProfile(user=request.user) 
              user.save()
          if user.neighborhood is None:
               title='Neighborhood'
               neighbors= Neighborhood.objects.all()
               return render(request,'Home.html',{'neighbors':neighbors})
          else: 
              user= UserProfile.objects.filter(user= request.user).first()
              return redirect(reverse('neighborhood',args=[user.neighborhood.id]))
def neighborhood(request, neighborhood_id):
    if request.user.id == 1:
         neighborhood = Neighborhood.objects.get(id = neighborhood_id)
         partners = UserProfile.objects.filter(neighborhood =neighborhood).all()
         emergencies = Contacts.objects.filter(neighborhood_contact = neighborhood).all()
         return render(request,'neighbors.html',{'neighborhood':neighborhood,'members':members,'emergencies':emergencies})
    else:
        neighborhood = Neighborhood.objects.get(id = neighborhood_id)
        user= UserProfile.objects.filter(user = request.user).first()
        businesses = Business.objects.filter(business_neighborhood=neighborhood).all()
        emergencies = Contacts.objects.filter(neighborhood_contact = neighborhood).all()
        user.neighborhood = neighborhood
        user.save()

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = Post(title=request.POST['title'],post_description=request.POST['post_description'],posted_by=request.user,post_hood=neighborhood,posted_on=datetime.datetime.now())
                post.save()
                return redirect(reverse('neighborhood',args=[neighborhood.id]))
            else:
                 form=PostForm()
            posts= Post.objects.filter(post_hood= neighborhood).all()
            return render(request,'neighbors.html',{'posts':posts,'form':form,'user':user,'businesses':businesses,'neighborhood':neighborhood,'emergencies':emergencies})

def profile(request,user_id):
    user = User.objects.get(id= user_id)
    profile = UserProfile.objects.filter(user=user).filter()
    if request.method =='Post':
        form =UpdateProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile.first_name =request.POST['first_name']
            profile.last_name =request.POST['last_name']
            profile.location = request.POST['location']
            profile.save()
        return redirect(reverse'profile',args=[user.id])
    else:
         form: UpdateProfileForm(instance=profile)
         