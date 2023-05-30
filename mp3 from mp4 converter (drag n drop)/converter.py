import os
import sys
from moviepy import *

# Get the list of input file paths from command line arguments
input_paths = sys.argv[1:]

# Convert each input file to MP3
for input_path in input_paths:
    # Create an output file path with a .mp3 extension
    output_path = os.path.splitext(input_path)[0] + ".mp3"
    
    # Load the input video file using MoviePy
    video_clip = VideoFileClip(input_path)
    
    # Extract the audio from the video clip
    audio_clip = video_clip.audio
    
    # Write the audio to the output file as an MP3
    audio_clip.write_audiofile(output_path)
    
    # Clean up the video and audio clips
    audio_clip.close()
    video_clip.close()

# Wait for user input so the terminal window doesn't close immediately
input("Press Enter to exit...")