import whisperx
import torch

# Path to your video file
audio_file = "dl_youtube/aubrey_conan.mp4"

# Set device to CPU since CUDA is not available for Intel GPUs
device = "cpu"

# Load the model, forcing it to use CPU
model = whisperx.load_model("large-v2", device="cpu", compute_type="float32")



# Step 1: Transcribe audio
transcription = model.transcribe(audio_file)
segments = transcription["segments"]

# Step 2: Align with word timestamps
model_a, metadata = whisperx.load_align_model(language_code=transcription["language"], device="cpu")
aligned_segments = whisperx.align(segments, model_a, metadata, audio_file, device="cpu")

# Step 3: Add speaker diarization
diarize_model = whisperx.DiarizationPipeline(use_auth_token=True)  # You’ll need HuggingFace token if private
diarized_segments = diarize_model(audio_file, aligned_segments["segments"])

# Output example
for segment in diarized_segments:
    print(f"{segment['start']} - {segment['end']} | Speaker {segment['speaker']} : {segment['text']}")
