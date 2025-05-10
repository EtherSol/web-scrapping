from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import json  # Ensure the json module is imported
import os

# def get_youtube_id(url):
#     parsed_url = urlparse(url)
    
#     # Example for standard URL
#     if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
#         query = parse_qs(parsed_url.query)
#         return query.get("v", [None])[0]
    
#     # Example for short URL
#     if parsed_url.hostname == "youtu.be":
#         return parsed_url.path[1:]
    
#     return None

# # Example usage:
# url = "https://www.youtube.com/watch?v=jORFHuGIvVI&t=71s"
# print(get_youtube_id(url))  # Output: jORFHuGIvVI


###############################################


# video_url = input("What is the YouTube URL")
# Fetch the transcript for the video
video_id = "7Frri8u8A4M"
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Prepare the transcript data in JSON format
transcript_data = [{"timestamp": f"{entry['start']:.2f}s", "text": entry['text']} for entry in transcript]

folder = "datasets"
os.makedirs(folder, exist_ok=True)  # Creates the folder if it doesn't exist

# Save the data to a JSON file
base_filename = "youtube_transcript"

i = 1
while True:
    filename = os.path.join(folder,f"{base_filename}_{i}.json")
    if not os.path.exists(filename):
        break
    i += 1

with open(filename, "w", encoding="utf-8") as f:
    json.dump(transcript_data, f, indent=4)

print(f"Transcript saved to {filename}")
