from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:post_slug>/', views.PostDetailView.as_view(), name='post'),
    path('addpost/', views.PostCreateView.as_view(), name='add_post'),
    path('contact/', views.contact, name='contact'),
    path('update_post/<slug:post_slug>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<slug:post_slug>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('post/<slug:post_slug>/comments/<int:comment_id>/delete', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('post/<slug:post_slug>/comments/<int:comment_id>/update', views.CommentUpdateView.as_view(), name='update_comment'),
    path('post/<slug:post_slug>/comments/<int:comment_id>/answer', views.CommentAnswerCreateView.as_view(), name='answer_comment'),
    path('post/<slug:post_slug>/comments/', views.CommentAddView.as_view(), name='add_comment'),
]
