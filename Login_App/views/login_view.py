from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

# Authetication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate


from django.views import View
# Messages
from django.contrib import messages

# Create your views here.
class Login_user(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'Login_App/login.html',context={'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('Login_App:profile'))
        return render(request, 'Login_App/login.html', context={'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are logged out!!")
    return HttpResponseRedirect(reverse('Home_App:home'))
