from django.shortcuts import render
from django.http import *
from django.core.context_processors import csrf
from fav.models import Favorite
import datetime

def success(request):
	if request.method == 'POST':
		f = Favorite(user = request.user.username,
			video = request.POST['video'])
		favorites = Favorite.objects.all()
		v = request.POST['video']
		if f in favorites:
			return HttpResponse(v + " is already in your favorites.")
		f.save()
		return HttpResponse("Video: "+ v + " was added to your favorites!")
