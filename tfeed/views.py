from django.http import HttpResponse
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
