## Download YouTube videos with ease using this Python script(Educational purpose only).

**Features:**

* Download single videos or playlists
* Choose the desired video format and quality
* Extract audio from videos
* Progress bar for tracking download status

**Requirements:**

* Python 3.x
* youtube-dl library

**Installation:**

1. Clone the repository (replace `your-username` with your GitHub username):

```bash
git clone [https://github.com/your-username/youtube-video-downloader.git](https://github.com/your-username/youtube-video-downloader.git)
```
2. Install the required libraries:
```bash
pip install -r requirements.txt
```

**Usage:**

Navigate to the project directory in your terminal.
Run the following command, replacing https://www.youtube.com/ with the URL of the video you want to download:
```bash
python downloader.py [https://www.youtube.com/](https://www.youtube.com/)
```
**For playlists, use the --playlist flag:**
```bash
python downloader.py [https://www.youtube.com/user/YouTube/playlists](https://www.youtube.com/user/YouTube/playlists) --playlist
```
The script will download the video to the current directory.
Options:

-f <format>: Specify the video format (e.g., mp4, bestvideo).
-q <quality>: Set the video quality (e.g., 360p, 720p, best).
-a: Extract audio only (saves as .m4a file).
-o <output_filename>: Specify the output filename.
Example:

**Download a video in the highest available quality and save it as video.mp4:**
```bash
python downloader.py [https://www.youtube.com/](https://www.youtube.com/) -f bestvideo -o video.mp4
```
Additional Notes:
Ensure you have the necessary permissions to download the videos.
Respect copyright laws and only download videos for personal use.
This script is provided for educational purposes only. Use it responsibly.
Feel free to contribute or suggest improvements!

