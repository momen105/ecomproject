from django.conf.urls import url
from django.urls import path
from .views.signup_view import Sign_up
from .views.profile_view import User_profile, profile_details
from .views.login_view import Login_user, logout_user


app_name = "Login_App"

urlpatterns = [
    path('signup/', Sign_up.as_view(), name = 'signup'),
    path('login/', Login_user.as_view(), name = 'login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', User_profile.as_view(), name = 'profile'),
    path('profile_details/', profile_details, name = 'profile_details'),


]