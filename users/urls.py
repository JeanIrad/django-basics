from django.urls import path
from users.views import home, createUser, loginUser, logoutUser


app_name= 'users'
urlpatterns = [
    path('', home, name='home'),
    path('login/', loginUser, name='loginUser'),
    path('create/', createUser, name='create'),
    path('logout', logoutUser, name='logout')
    
]