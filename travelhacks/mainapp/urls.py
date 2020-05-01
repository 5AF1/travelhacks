from django.urls import path
from . import views

urlpatterns=[
    path('<int:i>',views.index,name='index'),
    path('',views.intro)
]