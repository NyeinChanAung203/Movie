from .models import Movie

def slider_movies(request):
    movies = Movie.objects.all().order_by('created')[:6]
    return {'showcases':movies}