from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views import View

# Forms and Models
#from Login_App import models
from Login_App.models import Profile
from Login_App.forms import ProfileForm
# Messages
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

class User_profile(View,LoginRequiredMixin):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=profile)
        return render(request, 'Login_App/change_profile.html', context={'form': form})

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Update Your Profile!!")
                form = ProfileForm(instance=profile)
                return HttpResponseRedirect(reverse('Home_App:home'))
        return render(request, 'Login_App/change_profile.html', context={'form': form})


def profile_details(request):
    profile_list = Profile.objects.get(user=request.user)
    diction = {'profile':profile_list}
    return render(request,'Login_App/profile.html',context=diction)

