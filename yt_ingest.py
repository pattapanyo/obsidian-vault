import sys

try:
    from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
except Exception:
    print("Missing dependency: youtube-transcript-api. Install with: pip install youtube-transcript-api", file=sys.stderr)
    raise

try:
    from pytube import YouTube
except Exception:
    print("Missing dependency: pytube. Install with: pip install pytube", file=sys.stderr)
    raise


def slugify(title: str) -> str:
    """Make a filesystem-safe filename from the title."""
    s = title.strip()
    s = re.sub(r"[\\/:*?\"<>|]+", "", s)
    s = re.sub(r"\s+", "_", s)
    s = re.sub(r"_+", "_", s)
    return s[:200] or "untitled"


def format_timestamp(seconds: float) -> str:
    s = int(seconds)
    m = s // 60
    s = s % 60
    return f"{m:02d}:{s:02d}"


def extract_video_id(url: str) -> str:
    """Fallback extraction for video id if pytube fails."""
    # Common patterns: v=VIDEO_ID or youtu.be/VIDEO_ID
    m = re.search(r"v=([\w-]{11})", url)
    if m:
        return m.group(1)
    m = re.search(r"youtu\.be/([\w-]{11})", url)
    if m:
        return m.group(1)
    # As a last resort, return the whole url (pytube will likely fail)
    return url


def main() -> None:
    p = argparse.ArgumentParser(description="Fetch YouTube transcript and save as markdown in Storytelling/sources")
    p.add_argument("url", help="YouTube video URL")
    p.add_argument("-o", "--output", help="Output directory (default: Storytelling/sources)", default=None)
    args = p.parse_args()

    url = args.url

    try:
        yt = YouTube(url)
        title = yt.title
        video_id = yt.video_id
    except Exception:
        # fallback
        video_id = extract_video_id(url)
        title = video_id

    transcript = None
    try:
        # Preferred (older) convenience API
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except AttributeError:
        # Newer versions use list_transcripts(...) which returns objects that must be fetched
        try:
            transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
            # Prefer English when available
            try:
                en = transcripts.find_transcript(["en"])
                transcript = en.fetch()
            except Exception:
                # Fallback: fetch first available transcript
                for t in transcripts:
                    try:
                        transcript = t.fetch()
                        break
                    except Exception:
                        continue
            if transcript is None:
                raise Exception("No transcript could be fetched")
        except Exception as e:
            print(f"Failed to fetch transcript: {e}", file=sys.stderr)
            sys.exit(5)
    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.", file=sys.stderr)
        sys.exit(3)
    except NoTranscriptFound:
        print("No transcript found for this video.", file=sys.stderr)
        sys.exit(4)
    except Exception as e:
        print(f"Failed to fetch transcript: {e}", file=sys.stderr)
        sys.exit(5)

    filename = slugify(title) + ".md"
    repo_root = os.path.dirname(__file__)
    if args.output:
        if os.path.isabs(args.output):
            out_dir = args.output
        else:
            out_dir = os.path.join(repo_root, args.output)
    else:
        out_dir = os.path.join(repo_root, "Storytelling", "sources")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename)

    date = datetime.date.today().isoformat()

    frontmatter = (
        "---\n"
        f"title: \"{title}\"\n"
        f"date: {date}\n"
        "tags: [youtube, transcript]\n"
        "source_type: source\n"
        "---\n\n"
    )

    lines = [frontmatter, f"# {title}\n\n", f"Source: {url}\n\n", "## Transcript\n\n"]

    for seg in transcript:
        start = seg.get("start", 0)
        text = seg.get("text", "").strip()
        ts = format_timestamp(start)
        lines.append(f"- [{ts}] {text}\n")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.writelines(lines)

    # Print output path for callers
    print(out_path)


                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                main()
                                                                                                                                                                                                                                                                