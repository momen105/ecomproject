from django.contrib import admin
from django.urls import path, include


# To show media files
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home_App.urls')),
    path('account/', include('Login_App.urls')),
    path('shop/', include('Order_App.urls')),
    path('payment/', include('Payment_App.urls')),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)