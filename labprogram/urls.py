"""
URL configuration for labprogram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from lab1.views import current_time
from lab2.views import increase,decrease
from lab3.views import fruit_student
from lab4.views import aboutus,home,contactus
from lab5.views import reg,course_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/',current_time),
    path('time1/<int:offset>',increase),
    path('time2/<int:offset>',decrease),
    path('list/',fruit_student),
    path('home/', home),
    path('aboutus/', aboutus),
    path('contactus/', contactus),
    path('reg/', reg),
    path('course_search/', course_search),
]

