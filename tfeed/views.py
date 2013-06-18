from django.http import HttpResponse
import gdata.docs.service
import gdata.youtube
import gdata.youtube.service

def trick(request):
	a = []
	def GetAndPrintVideoFeed(uri):
		yt_service = gdata.youtube.service.YouTubeService()
		feed = yt_service.GetYouTubeVideoFeed(uri)
		for entry in feed.entry:
			a.append("<a href='"+entry.GetSwfUrl()+"'>"+entry.media.title.text+"</a><br />")
	datafeed = "http://gdata.youtube.com/feeds/api/videos?q=tricking&orderby=published&category=tricking&max-results=30"
	GetAndPrintVideoFeed(datafeed)
	return HttpResponse(a)
