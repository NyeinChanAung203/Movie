from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


CATEGORY_CHOICES = (
    ('action','ACTION'),
    ('drama','DRAMA'),
    ('comedy','COMEDY'),
    ('romance','ROMANCE'),
)

LANGUAGE_CHOICES = (
    ('EN','ENGLISH'),
    ('GR','GERMAN'),
)

STATUS_CHOICES = (
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCH'),
    ('TR','TOP RATED'),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=2)
    status = models.CharField(choices=STATUS_CHOICES,max_length=2)
    year_of_production = models.DateField()
    cast = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    slug = models.SlugField(blank=True,null=True)
    trailer = models.URLField(blank=True,null=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail',kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie,self).save(*args,**kwargs)

            

class ScreenShot(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(upload_to="screen_shots",blank=True,null=True)

    def __str__(self):
        return f'{self.movie}'


class MovieLink(models.Model):
    movie = models.ForeignKey(Movie,related_name="movie_watch_link",on_delete=models.CASCADE)
    link = models.URLField(help_text='Download link')
    quality = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return f'{self.movie.title} | Download Link'