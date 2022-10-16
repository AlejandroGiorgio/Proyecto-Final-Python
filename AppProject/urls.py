from django.urls import path
from AppProject.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home),
    path('create_driver/', create_driver),
    path('create_movile/', create_movile),
    path('create_user/', create_user), 
    path('read_user/', read_user),
    path('update_user/<user_id>', update_user),
    path('delete_user/<user_id>', delete_user),
    path('search_user/', search_user),
    path('login/', login_request),
    path('register/', register),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name="Logout" ),
    path('profile/', profileView),
    path('profile/editUser', editUser),
    path('profile/changepass', changepass),
    path('profile/addAvatar', SubmitAvatar)
]


