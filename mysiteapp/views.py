from models import User, Image, Event, Video
from serializers import UserSerializer, ImageSerializer, VideoSerializer, EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from django.db import models
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
import os

class UserList(APIView):
	
	def get(self, request):
		import pdb; pdb.set_trace()
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class UserProfile(APIView):
	
	permission_classes = (IsOwnerOrReadOnly, )
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format='json'):
		#import pdb; pdb.set_trace()
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format='json'):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format='json'):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	
class ImageList(APIView):
	
	def get(self, request):
		images = Image.objects.all()
		serializer = ImageSerializer(images , many=True)
		return Response(serializer.data)
	
	def post(self, request):
		serializer = ImageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(APIView):
	permission_classes = (IsOwnerOrReadOnly, )
	def get(self, request, pk):
		image = Image.objects.get(id=pk)
		serializer = ImageSerializer(image)
		return Response(serializer.data)

	def put(self, request, pk):
		image = Image.objects.get(id=pk)
		serializer = ImageSerializer(image)
		if serializer.is_valid():
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format='json'):
		image = self.get_object(pk)
		image.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class VideoList(APIView):
	
	def get(self, request):
		videos = Video.objects.all()
		serializer = VideoSerializer(videos, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = VideoSerializer(data=request.data, many=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoDetail(APIView):
	
	def get(self, request, pk):
		video = Video.objects.get(id=pk)
		serializer = VideoSerializer(video)
		return Response(serializer.data)

	def put(self, request, pk):
		video = Video.objects.get(id=pk)
		serializer = VideoSerializer(video)
		return Response(serializer.data)

	def delete(self, request, pk, format='json'):
		video = Video.objects.get(id=pk)
		video.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	
class EventList(APIView):

	def get(self, request):
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = EventSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventPage(APIView):
    
    renderer_classes = (TemplateHTMLRenderer,)
    
    def get(self, request, pk):
        event = Event.objects.get(id=pk)
        event_json = EventSerializer(event)
        #import pdb; pdb.set_trace()
        x = Video.objects.get(id=event_json.data['video'])
        dictionary = {"event":event_json.data, "path": str(os.path.split(x.video.name)[1])}
        video = Video.objects.get(id=event_json.data['video'])
        #import pdb; pdb.set_trace()
        return render(request,'event_detail.html', dictionary)
    
class HomePage(APIView):
   
   renderer_classes = (TemplateHTMLRenderer, )
   
   def get(self, request, pk):
       # videos= Video.objects.all()
       # videos_json = VideoSerializer(videos, many=True)
       # #import pdb; pdb.set_trace()
       # paths_list = list([])
       # for video in videos_json:
       x = Video.objects.get(id=video.data['video'])
       dictionary = {"event":event_json.data, "path": str(os.path.split(x.video.name)[1])}
       video = Video.objects.get(id=event_json.data['video'])
       #import pdb; pdb.set_trace()
       return render(request,'event_detail.html', dictionary)   


class EventDetail(APIView):

	def get(self, request, pk):
		event = Event.objects.get(id=pk)
		serializer = EventSerializer(event)
		return Response(serializer.data)

	def put(self, request, pk):
		event = Event.objects.get(id=pk)
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def delete(self, request, pk, format='json'):
		event = Event.objects.get(id=pk)
		event.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
