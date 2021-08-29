from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from Login_App.forms import SignUpForm
# Messages
from django.contrib import messages

from django.views import View

# Create your views here.
class Sign_up(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'Login_App/sign_up.html',context={'form': form})
    def post(self,request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Created Successfully!")
                return HttpResponseRedirect(reverse('Login_App:login'))
        return render(request, 'Login_App/sign_up.html', context={'form': form})



