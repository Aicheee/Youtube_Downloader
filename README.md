# YouTube Downloader

This is a simple YouTube downloader application built using Python. It allows users to input a YouTube video URL, choose the desired file format (MP4 or MP3), and download the video or audio accordingly.

## Features

- Input YouTube video URL
- Choose between MP4 and MP3 file formats
- Download videos in the highest resolution (MP4) or convert to MP3 (audio-only)
- Display download progress and logs

## Prerequisites (Not needed if you dont wanna run the raw python code)

- Python 3.x to run
- Required Python packages (install using `pip install -r requirements.txt`):
  - customtkinter
  - pytube
  - pyinstaller

## Run / Build

Make sure you are in the right directory `Downloader`

### Run

Command: `python .\main.py`

### Build

Command: `pyinstaller --onefile --noconsole main.py`

You can find the exe in: `./dist`

## Desktop Shortcut

There is a desktop shortcut called `Downloader` in `./dist` which you can move on to the desktop.
