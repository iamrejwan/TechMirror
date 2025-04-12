"""
URL configuration for forum project.

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
from django.urls import path, include
from forumapp import views  # Import views to use the user_profile view

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add a URL pattern for the user profile that expects a username.
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    # Include all other URLs from the forumapp.
    path('', include("forumapp.urls")),
]
