from django.shortcuts import render
from models import User, Video, Image, Event
from rest_framework import serializers
#from serializers import ModelSerializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video

class EventSerializer(serializers.ModelSerializer):
    video = serializers.PrimaryKeyRelatedField(read_only=True)
    photo = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Event

class UserSerializer(serializers.ModelSerializer):
    #event = EventSerializer(read_only=True)
    events = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = User
        

        
