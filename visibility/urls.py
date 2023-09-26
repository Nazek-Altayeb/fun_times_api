from django.urls import path
from visibility import views

urlpatterns = [
    path('VisibilityList/', views.VisibilityList.as_view())
]
