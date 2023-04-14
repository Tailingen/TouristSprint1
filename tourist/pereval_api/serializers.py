from .models import *
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
#    email = serializers.CharField(required=True)
#    name = serializers.CharField(source='name')
#    fam = serializers.CharField(source='last_name')
#    otc = serializers.CharField(source='patronymic')
#    phone = serializers.CharField()

    class Meta:
        model = Users
        fields = '__all__'

class CoordsSerializer(serializers.ModelSerializer):
#    latitude = serializers.FloatField()
#    longitude = serializers.FloatField()
#    height = serializers.IntegerField()

    class Meta:
        model = Coords
        fields = '__all__'

class ImageSerializer(serializers.Serializer):
#    data = serializers.CharField()

    class Meta:
        model = Pereval_images
        fields = '__all__'

class PerevalSerializer(serializers.ModelSerializer):
#    user = UsersSerializer(required=True)
#    beauty_title = serializers.CharField(allow_blank=True)
#    title = serializers.CharField(allow_blank=True)
#    other_titles = serializers.CharField(max_length=300)
#    connect = serializers.CharField(max_length=50, allow_blank=True)
#    date_added = serializers.DateTimeField()
#    coords = CoordsSerializer(required=True)
#    winter_level = serializers.CharField(max_length=5)
#    spring_level = serializers.CharField(max_length=5)
#    summer_level = serializers.CharField(max_length=5)
#    autumn_level = serializers.CharField(max_length=5)
#    images = ImageSerializer(many=True)
#    status = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = Pereval_added
        fields = ('users', 'beautyTitle', 'title', 'other_titles', 'connect', 'coord_id', 'winter_level', 'spring_level',
                  'summer_level', 'autumn_level', 'status')
