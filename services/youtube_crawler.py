from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY


def get_comments(video_id, max_results=100):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    comments = []

    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )

    response = request.execute()
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments
