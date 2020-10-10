"""webdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Qbank import views
from Qbank.views import QbankListView
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url('about/', views.about, name='about'),
    url('pricing/', views.pricing, name='pricing'),
    url('results/', views.results, name='results'),
    url('alevelbio/', views.ABIO, name='ABIO'),
    url('register/', user_views.register, name='register'),
    url('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url('profile/', user_views.profile, name='profile'),
    url('qbank/', QbankListView.as_view(), name='qbankview') 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)