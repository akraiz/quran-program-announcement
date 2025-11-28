#!/usr/bin/env python3
"""
Script to download all audio tracks from a SoundCloud playlist.
"""

import os
import subprocess
import sys
from pathlib import Path

def download_playlist(playlist_url: str, output_dir: str = "audio_files"):
    """
    Download all tracks from a SoundCloud playlist using yt-dlp.
    
    Args:
        playlist_url: URL of the SoundCloud playlist
        output_dir: Directory to save downloaded files
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Prepare yt-dlp command
    # -x: extract audio only
    # --audio-format mp3: convert to mp3
    # --audio-quality 0: best quality
    # -o: output template
    # --no-playlist-reverse: don't reverse playlist order
    cmd = [
        "yt-dlp",
        "-x",  # Extract audio only
        "--audio-format", "mp3",  # Convert to mp3
        "--audio-quality", "0",  # Best quality
        "-o", str(output_path / "%(title)s.%(ext)s"),  # Output filename template
        "--no-playlist-reverse",  # Keep original order
        playlist_url
    ]
    
    print(f"Downloading playlist from: {playlist_url}")
    print(f"Output directory: {output_path.absolute()}")
    print("\nStarting download...\n")
    
    try:
        # Run yt-dlp
        result = subprocess.run(cmd, check=True, capture_output=False)
        print("\n✓ Download completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error downloading playlist: {e}")
        return False
    except FileNotFoundError:
        print("\n✗ Error: yt-dlp not found. Please install it using:")
        print("  pip install yt-dlp")
        return False

if __name__ == "__main__":
    playlist_url = "https://soundcloud.com/msjdaboahmed/sets/bvkdzu92ldq7?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
    
    # Allow custom URL via command line argument
    if len(sys.argv) > 1:
        playlist_url = sys.argv[1]
    
    # Allow custom output directory via command line argument
    output_dir = "audio_files"
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    
    success = download_playlist(playlist_url, output_dir)
    sys.exit(0 if success else 1)

