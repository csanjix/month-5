from django.urls import path
from .views import DirectorListCreateView, DirectorRetrieveUpdateDestroyView, \
    MovieListCreateView, MovieRetrieveUpdateDestroyView, \
    ReviewListCreateView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('directors/', DirectorListCreateView.as_view(), name='director-list-create'),
    path('directors/<int:pk>/', DirectorRetrieveUpdateDestroyView.as_view(), name='director-detail'),
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
]