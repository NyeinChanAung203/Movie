from django.urls import path
from .views import MovieListView,MovieDetailView,MovieCategory,MovieSearch,genre

urlpatterns = [
    path('',MovieListView.as_view(),name='movie_list'),
    path('search/',MovieSearch.as_view(),name="search"), 
    path('category/<str:category_name>/',MovieCategory.as_view(),name="movie-category"),
    path('genre/',genre,name="genre"),
    path('<slug:slug>/',MovieDetailView.as_view(),name='movie_detail'),
    
]