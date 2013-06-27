from django.shortcuts import render
from django.http import *
from django.core.context_processors import csrf
from fav.models import Favorite
import datetime

def success(request):
	if request.method == 'GET':
		f = Favorite(user = request.GET['user'],
			video = request.GET['video_id'],
			date = datetime.datetime.now())
		f.save()
		return HttpResponse("Video: "+ request.GET['video_id'] + " was added to your favorites!")
