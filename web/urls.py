from django.urls import path
from . import views
from .views import (
    HomePageView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('explore/', PostListView.as_view(), name='explore'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('vcard/cid0<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
]
