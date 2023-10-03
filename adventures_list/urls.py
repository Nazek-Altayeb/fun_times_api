from django.urls import path
from adventures_list import views

urlpatterns = [
    path('adventureslist/', views.AdventureList.as_view()),
    path('adventureslist/<int:pk>/', views.AdventureDetail.as_view()),
]
