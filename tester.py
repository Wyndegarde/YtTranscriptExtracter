from youtube_transcript_api import YouTubeTranscriptApi

transcript = YouTubeTranscriptApi.get_transcript('MI0HoDiBABc')

search_word = 'eren'

for caption in transcript:
    if search_word in caption['text']:
        print(caption)