from django.urls import path
from AppProject.views import *

urlpatterns = [
    path('', home),
    path('create_driver/', create_driver),
    path('create_movile/', create_movile),
    path('create_user/', create_user), 
    path('read_user/', read_user),
    path('update_user/', update_user),
    path('delete_user/', delete_user ),
    path('create_driver/', create_driver),
    path('create_movile/', create_movile),
    path('search_user/', search_user)
]


