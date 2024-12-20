"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,re_path
from first import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup_view,name='signup'),
    path('post/',views.post_view,name='post'),
    path('post_list/',views.post_list_view,name='post_list'),
    path('latest_post/',views.latest_posts_view,name='latest_post'),
    path('<year>/<month>/<day>/<title>/<username>/',views.post_detail_view,name='post_detail'),
    path('profile/',views.profile_view,name='profile'),
    path('logout/',views.logout_view,name='logout'),
    re_path('^.*$', views.login_view, name='login'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
