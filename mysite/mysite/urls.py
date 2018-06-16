
from django.contrib import admin
from django.urls import path,include
from polls import views

urlpatterns = [
	path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
