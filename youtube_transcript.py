from youtube_transcript_api import YouTubeTranscriptApi

video_id = "YOUTUBE_VIDEO_ID_HERE"  # Just the ID, not the full URL
transcript = YouTubeTranscriptApi.get_transcript(video_id)

for entry in transcript:
    print(f"{entry['start']:.2f}s: {entry['text']}")