from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)

urlpatterns=[
    path('<int:i>',views.index,name='index'),
    #path('',views.intro)
    path('',PostListView.as_view(),name = 'mainapp-home'),
    path('user/<str:username>',UserPostListView.as_view(),name = 'user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('intro/',views.intro,name = 'mainapp-intro'),
]