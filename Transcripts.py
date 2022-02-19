import json
from tkinter import N
import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi

file = open('result.json')

data = json.load(file)

jre_links = data['JRE']

# for link in jre_links:
#     print(link.replace('https://www.youtube.com/watch?v=',''))

video_tags = [tag.replace('https://www.youtube.com/watch?v=','') for tag in jre_links]


for video in jre_links:
    try:
        video_tag = video.replace('https://www.youtube.com/watch?v=','')
        transcript = YouTubeTranscriptApi.get_transcript(video_tag)

        search_word = 'nigger'
    # print(f'Video link: {video}\n')
        for caption in transcript:
            if search_word in caption['text']:
                text = caption['text']
                timestamp = caption['start']
                print(f'Video link: {video}')
                print(f'Caption: {text}; begins at: {timestamp}\n')
    except (youtube_transcript_api._errors.NoTranscriptFound,youtube_transcript_api._errors.TranscriptsDisabled):
        pass


