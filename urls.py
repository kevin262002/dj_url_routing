from django.urls import path
from . import views

urlpatterns = [
    path('/original-url/', views.original_view),
    path('/another-url/<some_arg>/', views.another_view, name='named-url')
]