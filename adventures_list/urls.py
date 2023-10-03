from django.urls import path
from adventures_list import views

urlpatterns = [
    path('adventureslist/', views.AdventuresList.as_view()),
    path('adventureslist/<int:pk>/', views.AdventureDetail.as_view()),
]
