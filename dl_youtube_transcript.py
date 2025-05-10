import whisperx

model = whisperx.load_model("large-v2", device="cuda" or "cpu")

# transcribe the mp4
audio = whisperx.load_audio("your_file.mp4")
result = model.transcribe(audio)

print(result["segments"])  # See transcribed segments

# Optional: download pretrained speaker diarization model
diarize_model = whisperx.DiarizationPipeline(use_auth_token="your_hf_token")

# Apply diarization
diarize_segments = diarize_model(audio, min_speakers=2, max_speakers=4)
result = whisperx.assign_speakers(result["segments"], diarize_segments)

for segment in result["segments"]:
    print(f"[{segment['speaker']}] {segment['text']}")