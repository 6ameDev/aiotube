import json
from .patterns import _FindPatterns as Patterns
from typing import Optional, Dict, Any, List
from .https import find_videos

def extract_metadata(video_json: str):
    """Parses extracted videoRenderer JSON to get metadata."""
    try:
        video_data = json.loads(video_json)
        video = video_data.get("videoRenderer", {})

        return {
            "videoId": video.get("videoId"),
            "thumbnail": video.get("thumbnail"),
            "title": video.get("title", {}).get("runs", [{}])[0].get("text"),
            "published": video.get("publishedTimeText", {}).get("simpleText"),
            "duration": video.get("lengthText", {}).get("simpleText"),
            "views": video.get("shortViewCountText", {}).get("simpleText"),
            "owner": video.get("ownerText", {}).get("runs", [{}])[0].get("text"),
        }

    except json.JSONDecodeError as e:
        return None

class Find:
    @staticmethod
    def videos(keywords: str, limit: int = 20) -> Optional[List[str]]:
        video_blocks = Patterns.videoRenderer.findall(find_videos(keywords))
        return [metadata for block in video_blocks if (metadata := extract_metadata(block)) is not None]
        print(f"Searching videos for: {keywords}")
