import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "be/" in url:
        return url.split("be/")[1].split("?")[0]
    return url

def main():
    if len(sys.argv) < 2:
        print("Usage: python yt_ingest.py <URL>")
        return

    url = sys.argv[1]
    video_id = get_video_id(url)
    
    try:
        print(f"Fetching transcript for: {video_id}...")
        # Simpler method that works across versions
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine text into one block
        text = "\n".join([t['text'] for t in transcript_list])
        
        # Save to Storytelling/sources/
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

if __name__ == "__main__":
    main()
