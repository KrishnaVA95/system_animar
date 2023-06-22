from django.urls import path
from .views import PostView, PostDetailsView

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:post_id>/', PostDetailsView.as_view()),
]