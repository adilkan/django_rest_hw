from .models import Director, Movie, Review
from rest_framework import serializers


class SerializerDirektor(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class SerializerMovie(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SerializerReview(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
