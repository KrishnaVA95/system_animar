# from django.contrib import admin
from django.urls import path
from .views import AccountView, AccountDetailView

urlpatterns = [
    path('accounts/', AccountView.as_view()),
]
    # path('accounts/<id>/', AccountView.as_view()),