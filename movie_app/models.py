from django.db import models

RATTING_CHOICES = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),

)


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies(self):
        movie = self.movie.all()
        count = self.movie.count()
        return count


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name='movie')

    def __str__(self):
        return self.title

    @property
    def stars2(self):
        reviews = self.reviews2.all()
        count_ = reviews.count()
        midle = 0
        for i in reviews:
            midle += i.stars
        try:
            return midle / count_
        except Exception:
            return 0

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='reviews2')
    stars = models.IntegerField(choices=RATTING_CHOICES)

    def __str__(self):
        return (f'коментарий для:  {self.movie}')
