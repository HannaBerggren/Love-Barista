from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path("user_page", views.User.as_view(), name="user-page"),
    path("add_post", views.AddPost.as_view(), name="add-post"),
    path("update_post/<slug:slug>/", views.update_post, name="update-post"),
    path(
        "delete_post/<slug:slug>/",
        views.DeletePost.as_view(),
        name="delete-post",
    ),
    path(
        "user_post_list/", views.UserPostList.as_view(), name="user-post-list"
    ),
    
]