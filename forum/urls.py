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
<<<<<<< HEAD
=======
from django.contrib.auth import views as auth_views
>>>>>>> 46886b0 (updated)
from forumapp import views  # Import views to use the user_profile view

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    # Add a URL pattern for the user profile that expects a username.
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    # Include all other URLs from the forumapp.
    path('', include("forumapp.urls")),
]
=======
    # Login URL using Django's built-in LoginView.
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Logout URL using Django's built-in LogoutView. You can specify a next_page if desired.
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    # User profile URL that expects a username.
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    # Include Django's built-in authentication URLs. This includes password reset URLs.
    path('accounts/', include('django.contrib.auth.urls')),
    # Include all other URLs from forumapp.
    path('', include("forumapp.urls")),
]

>>>>>>> 46886b0 (updated)
