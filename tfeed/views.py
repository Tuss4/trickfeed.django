from django.http import HttpResponse
import gdata.docs.service
import gdata.youtube
import gdata.youtube.service
def docs(request):
	client = gdata.docs.service.DocsService()
	client.ClientLogin('','')
	documents_feed = client.GetDocumentListFeed()
	dlist = []
	for document_entry in documents_feed.entry:
		dlist.append(document_entry.title.text+"<br>")
	return HttpResponse(dlist)


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
