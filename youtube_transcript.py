from youtube_transcript_api import YouTubeTranscriptApi
import json  # Ensure the json module is imported

# Fetch the transcript for the video
video_id = "jORFHuGIvVI"
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Prepare the transcript data in JSON format
transcript_data = [{"timestamp": f"{entry['start']:.2f}s", "text": entry['text']} for entry in transcript]

# Save the data to a JSON file
output_path = "youtube_transcript.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(transcript_data, f, indent=4)

print(f"Transcript saved to {output_path}")
