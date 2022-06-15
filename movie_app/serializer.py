from .models import Director, Movie, Review
from rest_framework import serializers


class SerializerReview(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class SerializerDirektor(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies'.split()


class SerializerMovie(serializers.ModelSerializer):
    reviews2 = SerializerReview(many=True)
    class Meta:
        model = Movie
        fields = ['title','description','director','stars2','reviews2',]
