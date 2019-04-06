"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from users.views import register, profile,userlayout,friendprofile,commentpage,mycommentpage,searchfriends
from django.contrib.auth import views as auth_views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/',register),
    path('user/profile/',profile),
    path('user/userlayout/',userlayout),
    path('user/friendprofile/<slug:username>/',friendprofile,name="fp"),
    path('user/searchfriends/', searchfriends),
    path('user/commentpage/<slug:username>/',commentpage),
    path('user/comments/',mycommentpage),
    path('user/login/',auth_views.LoginView.as_view(template_name = 'user/login.html'), name="login"),
    path('user/logout/',auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name="logout"),
    path('api/', include('api.urls')),
    path('home/', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()