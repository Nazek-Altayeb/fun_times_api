from django.urls import path
from favourite_followers import views

urlpatterns = [
    path('favouritefollowers/', views.FavouriteFollowersList.as_view()),
    path('favouritefollowers/<int:pk>/', views.FavouriteFollowerDetail.as_view())
]
