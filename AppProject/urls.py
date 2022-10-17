from django.urls import path
from AppProject.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home),
    path('create_driver/', create_driver),
    path('create_movile/', create_movile),
    path('create_passenger/', create_passenger), 
    path('read_passenger/', read_passenger),
    path('update_passenger/<passenger_id>', update_passenger),
    path('delete_passenger/<passenger_id>', delete_passenger),
    path('search_passenger/', search_passenger),
    path('login/', login_request),
    path('register/', register),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name="Logout" ),
    path('profile/', profileView),
    path('profile/editUser', editUser),
    path('profile/changepass', changepass),
    path('profile/addAvatar', SubmitAvatar)
]


