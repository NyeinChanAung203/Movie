from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Movie,MovieLink
# Create your views here.

import random

class MovieListView(ListView):
    model = Movie
    paginate_by = 8
    ordering = ['-created']


class MovieDetailView(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetailView,self).get_object()
        return object

    def get_context_data(self,**kwargs):
        context = super(MovieDetailView,self).get_context_data(**kwargs)
        print(object)
        context['links'] = self.get_object().movie_watch_link.all()
        movie = self.get_object()
        context['screenshots'] = movie.screenshot_set.all()
        return context

class MovieCategory(ListView):
    model = Movie
    template_name = 'movie/movie_category.html'
    paginate_by = 8

    def get_queryset(self):
        self.category_name = self.kwargs['category_name']
        return Movie.objects.filter(category=self.category_name)

    def get_context_data(self,**kwargs):
        context = super(MovieCategory,self).get_context_data(**kwargs)
        context['category_name'] = self.category_name
        return context 



class MovieSearch(ListView):
    model = Movie
    paginate_by = 8
    ordering = ['title',]
    template_name = 'movie/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        # print(query)
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
            # print(object_list)
        else:
            object_list = self.model.objects.all()
            # print(object_list)
        return object_list

def genre(request):
    return render(request,'movie/genre.html',{})