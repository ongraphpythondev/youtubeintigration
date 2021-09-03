# Google related import
import google_auth_oauthlib
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
# django related import
from django.shortcuts import render, redirect
from django.conf import settings
# Python related import
import requests
import pickle


def like_comments(request):
    """
        This is for like and dislike the video.
        you have to just click on the like or dislike button.
        It will automatically liked or disliked it.
    """

    credential = pickle.load(open("token.pkl", "rb"))
    video_id = request.GET.get('vid')
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_DATA_API_KEY, credentials=credential)
    youtube.videos().rate(rating=request.GET.get('submit'), id=str(video_id)).execute()

    for i in data['data']:
        if i['id'] == video_id:
            i['count'] = request.GET.get('submit')

    return render(request, 'index.html', data)


def index(request):
    """
        This function named as index function because it interact with index template.
        This support GET and POST method..
        In GET method, this will generate the token or credentials for perform the operation.
        In POST method, this will show the content based on the search text you enter. If you didn't enter anything
        then it will show random videos.
    """

    # Post request
    if request.method == "POST":
        search_text = request.POST['search_text']
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'
        search_params = {
            'part': 'snippet',
            'q': search_text,
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 10,
            'type': 'video'
        }

        # This is for making the request based on search criteria
        r = requests.get(search_url, params=search_params)

        # hold video's id
        search_ids = []
        for i in range(10):
            search_ids.append(r.json()['items'][i]['id']['videoId'])

        # video parameter for searching the video based on video id's(search_id)
        video_params = {
                'part': 'snippet, contentDetails',
                'key': settings.YOUTUBE_DATA_API_KEY,
                'id': ','.join(search_ids)
            }

        # This is for making the request for videos
        r = requests.get(video_url, params=video_params)

        # temporary variable for storing the items of particular video
        videos = []
        for i in range(10):
            video_id = r.json()["items"][i]["id"]
            video_data = {
                'title': r.json()['items'][i]['snippet']['title'],
                'url': 'https://www.youtube.com/watch?v='+video_id,
                'id': video_id,
                'count': '0'
            }
            videos.append(video_data)

        # This is the main dictionary which will use by template to show the content
        global data
        data = {
            'data': videos
        }

        # rendering to the index.html with data to show
        return render(request, 'index.html', data)

    # if request.method == 'GET'
    else:

        # if the state is not none then
        if request.GET.get('state') is not None:
            state = request.GET.get('state')
            flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                'client_secret.json',
                scopes=['https://www.googleapis.com/auth/youtube.force-ssl'],
                state=state)
            flow.redirect_uri = 'http://127.0.0.1:8000/search_youtube'
            flow.fetch_token(code=request.GET.get('code'))
            credentials = flow.credentials
            pickle.dump(credentials, open("token.pkl", "wb"))
        try:
            pickle.load(open("token.pkl", "rb"))
        except Exception as e:
            return redirect('/')
        return render(request, 'index.html')


def auth(request):
    """
    This will use for generating the url and verify the url also.
            In the GET method, you found an authenticate button to authenticate this application.
            In POST method, it will redirect you to authentication url and you have to sign in the app.
    """

    if request.method == 'POST':
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            'client_secret.json',
            scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
        flow.redirect_uri = 'http://127.0.0.1:8000/search_youtube'
        global authorization_url
        authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
        return redirect(authorization_url)

    if request.method == 'GET':
        return render(request, 'authenticate.html')




