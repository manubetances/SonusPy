import os
import ffmpeg

# Get the directories that the program uses.
dir = os.path.dirname(os.path.abspath(__file__))

input_folder = os.path.join(dir, "input_music")
output_folder = os.path.join(dir, "output_music")

# Making sure the output folder exists.
os.makedirs(output_folder, exist_ok = True)

# Convert FLAC to MP3 Function.
def convert_flac_to_mp3(input_file, output_file):
    try: 
        (
        ffmpeg
        .input(input_file)
        .output(output_file, **{'b:a': '320k'})
        .run()
    )
        print(f"Successfully converted {input_file} to {output_file}")
    except ffmpeg.Error as event:
        print(f"Error converting {input_file}: {event}")

if __name__ == "__main__":
    # Loop through all .flac files in the input folder 
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".flac"):
            input_file = os.path.join(input_folder, file_name)

            output_file_name = file_name.replace(".flac", ".mp3")
            output_file = os.path.join(output_folder, output_file_name)

            convert_flac_to_mp3(input_file, output_file)
