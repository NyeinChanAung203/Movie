from django.contrib import admin

# Register your models here.
from .models import Movie,MovieLink,ScreenShot

class MovieLinkInline(admin.TabularInline):
    model = MovieLink
    verbose_name = "Add Download link"
    verbose_name_plural = "Add Download links"

class ScreenShotInline(admin.TabularInline):
    model = ScreenShot
    extra = 4
    verbose_name = "Add 4 Photos as screenshoot"
    verbose_name_plural = "Add 4 Photos as screenshoot"
    

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','category','rating']
    list_filter = ['category','status']
    search_fields = ['title','rating']
    readonly_fields = ['slug']
    inlines = [
        MovieLinkInline,ScreenShotInline
    ]
    

   

admin.site.register(Movie,MovieAdmin)
