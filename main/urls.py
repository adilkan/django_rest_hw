from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/director/',views.director_list),
    path('api/v1/director/<int:id>/', views.director),
    path('api/v1/movie/', views.movie_list),
    path('api/v1/movie/<int:id>', views.movie),
    path('api/v1/review/', views.review_list),
    path('api/v1/review/<int:id>/', views.review),

]
