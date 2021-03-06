from django.shortcuts import *
from django.http import *
from django.core.context_processors import csrf
from favo.models import Favorite

def success(request):
	if request.method == 'POST':
		f = Favorite(user = request.user.username,
			video = request.POST['video'])
		favorites = Favorite.objects.all()
		v = request.POST['video']
		fs = Favorite.objects.filter(video=v)
		fu = Favorite.objects.filter(user=request.user.username)
		if fs and fu:
			return HttpResponse(v + " is already in your favorites.")
		f.save()
		return HttpResponse("Video: "+ v + " was added to your favorites!")

def list_fav(request):
	if request.user.is_authenticated():
		videos = Favorite.objects.filter(user=request.user.username)
		return render(request, "favorites.html", {"videos": videos})
