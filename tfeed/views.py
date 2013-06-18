from django.http import HttpResponse
import gdata.docs.service
import gdata.youtube
import gdata.youtube.service
def docs(request):
	client = gdata.docs.service.DocsService()
	client.ClientLogin('tuss4dbfn@gmail.com','tomjos')
	documents_feed = client.GetDocumentListFeed()
	dlist = []
	for document_entry in documents_feed.entry:
		dlist.append(document_entry.title.text+"<br>")
	return HttpResponse(dlist)


def trick(request):
	yt_service = gdata.youtube.service.YouTubeService()

	yt_service.ssl = True

	yt_service.developer_key = 'AIzaSyDCDSuNggEx-ouiWg5hKxPmf3b09SrKRBA'
	yt_service.client_id = '861387077789.apps.googleusercontent.com'
	def PrintEntryDetails(entry):
		vT = 'Video title: %s' % entry.media.title.text
		vU = 'Video flash player URL: %s' % entry.GetSwfUrl()
	def PrintVideoFeed(feed):
		for entry in feed.entry:
			PrintEntryDetails(entry)
	def SearchAndPrintVideosByKeywords(list_of_search_terms):
		yt_service = gdata.youtube.service.YouTubeVideoQuery()
		query = gdata.youtube.service.YouTubeVideoQuery()
		query.orderby = 'published'
		query.racy = 'include'
		for search_term in list_of_search_terms:
			new_term = search_term.lower()
			query.categories.append('/%s' % new_term)
		feed = yt_service.YouTubeQuery(query)
		PrintVideoFeed(feed)

	t = "Welcome to trickFEED"
	return HttpResponse(SearchAndPrintVideosByKeywords(["tricking"]))
def hello(request):
	theater = """<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
	<script>
		function getThisId(datum){
			var newUrl = "http://youtube.com/embed/"+datum+"?autoplay=1&allowFullScreen=true";
			return newUrl;
		}
		function changeThisId(datum){
			document.getElementById("ytplayer").setAttribute("src",getThisId(datum));
		}
		$(document).ready(function(){
			var vidList = "http://gdata.youtube.com/feeds/api/videos?q=tricking&alt=json&format=5&max-results=30&orderby=published&callback=?&v=2&category=tricking";
			var output = "<ul>";
			$.getJSON(vidList, function(data){
				for(var i in data.feed.entry){
					entries = data.feed.entry[i];
					vidId = entries.id.$t.substring(27,38);
					output += "<a href='#"+vidId+"' onclick=changeThisId('"+vidId+"')><li id='"+vidId+"'><img src='"+entries.media$group.media$thumbnail[1].url+"' alt='"+entries.title.$t+"' title='"+entries.title.$t+"' /></li></a>";
				}
				output += "</ul>";
				document.getElementById("ytThumbs").innerHTML = output;
				$("#ytThumbs li").click(function(){
					$("#overlay").show();
				});
				$("#overlay").click(function(){
					$("#overlay").hide();
					$("#ytplayer").attr("src","http://www.youtube.com/embed/")
				});
			})

		})
	</script>
	<style>
		#ytThumbs li {
			display: inline-block;
			padding: .25%;
		}
		#ytThumbs li:hover {
			background-color: #CCC;
		}
		#overlay {
			position: fixed;
			z-index: 100;
			display: none;
			background-color: rgba(0,0,0,0.8);
			color: #FFF;
			left: 0%;
			right: 0%;
			top: 0%;
			bottom: 0%;
			text-align: center;
		}
		iframe {
			border: 0;
			max-width: 100%;
			max-height: 100%;
		}
		img {
			max-width: 100%;
		}
	</style>
</head>
<body>
	<div id="overlay">
		<h1>Tricking Theater</h1>
		<h4>Click outside video to close</h4>
		<iframe id="ytplayer" width="720" height="480"
  src="http://www.youtube.com/embed/"></iframe>
	</div>
	<div id="ytThumbs"></div>
</body>
</html>"""
	return HttpResponse(theater)
