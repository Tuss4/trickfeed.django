import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()

yt_service.ssl = True

yt_service.developer_key = 'AIzaSyDCDSuNggEx-ouiWg5hKxPmf3b09SrKRBA'
yt_service.client_id = '861387077789.apps.googleusercontent.com'
def PrintEntryDetails(entry):
    return HttpResponse('Video title: %s' % entry.media.title.text)
    return HttpResponse('Video flash player URL: %s' % entry.GetSwfUrl())
def PrintVideoFeed(feed):
    for entry in feed.entry:
        PrintEntryDetails(entry)
def SearchAndPrintVideosByKeywords(list_of_search_terms):
    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.orderby = 'published'
    query.racy = 'include'
    for search_term in list_of_search_terms:
        new_term = search_term.lower()
        query.categories.append('/%s' % new_term)
    feed = yt_service.YouTubeQuery(query)
    PrintVideoFeed(feed)

