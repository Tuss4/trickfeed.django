from django.shortcuts import render
from django.http import *
from django.core.context_processors import csrf
from fav.models import Favorite
import datetime

def success(request):
	if request.method == 'POST':
		f = Favorite(user = request.user.username,
			video = request.POST['video'],
			date = datetime.datetime.now())
		f.save()
		return HttpResponse("Video: "+ request.POST['video'] + " was added to your favorites!")
