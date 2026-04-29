import sys
import os
<<<<<<< HEAD
import youtube_transcript_api

def get_video_id(url):
    """Extracts the YouTube Video ID from various URL formats."""
=======
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
>>>>>>> bc3711896fd7a037815f9098e99cfe764740d207
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "be/" in url:
        return url.split("be/")[1].split("?")[0]
    return url

def main():
    if len(sys.argv) < 2:
<<<<<<< HEAD
        print("Usage: python yt_ingest.py <YouTube_URL>")
=======
        print("Usage: python yt_ingest.py <URL>")
>>>>>>> bc3711896fd7a037815f9098e99cfe764740d207
        return

    url = sys.argv[1]
    video_id = get_video_id(url)
    
    try:
<<<<<<< HEAD
        print(f"🚀 Fetching transcript for: {video_id}...")
        
        # Using the full path to the method to avoid "attribute" errors
        transcript_list = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)
        
        text = "\n".join([t['text'] for t in transcript_list])
        
=======
        print(f"Fetching transcript for: {video_id}...")
        # Simpler method that works across versions
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine text into one block
        text = "\n".join([t['text'] for t in transcript_list])
        
        # Save to Storytelling/sources/
>>>>>>> bc3711896fd7a037815f9098e99cfe764740d207
        output_dir = "Storytelling/sources"
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{output_dir}/YT_{video_id}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# YouTube Transcript: {video_id}\n\n")
            f.write(f"Source: {url}\n\n---\n\n")
            f.write(text)
            
        print(f"✅ Success! Saved to {filename}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
<<<<<<< HEAD
        print("\n💡 Troubleshooting: If you see 'no attribute', try running: pip install --upgrade youtube-transcript-api")

if __name__ == "__main__":
    main()
=======

if __name__ == "__main__":
    main()
>>>>>>> bc3711896fd7a037815f9098e99cfe764740d207
