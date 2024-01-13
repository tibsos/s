from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [

    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),

    path('check-username/', check_username, name = 'check-username'),
    path('check-email/', check_email, name = 'check-email'),

]