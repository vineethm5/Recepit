from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name='home'),
    path("signup/",signup,name='signup'),
    path('login/',login,name='login'),
    path("billpage/",billpage,name='billpage'),
    path("delete/<id>/",delete,name="delete"),
    path("update/<id>/",update,name='update')
]