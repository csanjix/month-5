from django.urls import path
from movie_app.views import *

urlpatterns = [
    path('api/v1/directors/', DirectorListCreateAPIView.as_view()),
    path('api/v1/directors/<int:pk>/', DirectorRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/movies/', MovieListCreateAPIView.as_view()),
    path('api/v1/movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/reviews/', ReviewListCreateAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view()),
]