"""jigsblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^blog/admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^blog/accounts/login/', auth_views.login, name='login'),
    url(r'^blog/accounts/logout/', auth_views.logout, name='logout'),
    url(r'^blog/accounts/profile/', include('blog.urls')),
    url('',include ('social.apps.django_app.urls', namespace='social')),
    url(r'^$', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
