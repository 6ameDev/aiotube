from fastapi import FastAPI, HTTPException
from aiotube import Search, Find

from aiotube.errors import TooManyRequests, InvalidURL, RequestError

app = FastAPI()

@app.get("/search")
async def search_videos(query: str, limit: int = 10):
    """Search YouTube videos using the aiotube library."""
    try:
        videos = Search.videos(query)
        return {"results": videos}
    
    except InvalidURL:
        raise HTTPException(status_code=400, detail="Invalid URL provided.")
    
    except TooManyRequests:
        raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")
    
    except RequestError:
        raise HTTPException(status_code=500, detail="Request to YouTube failed.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/find")
async def find_videos(query: str, limit: int = 10):
    """Search YouTube videos using the aiotube library."""
    try:
        videos = Find.videos(query)
        return {"results": videos}
    
    except InvalidURL:
        raise HTTPException(status_code=400, detail="Invalid URL provided.")
    
    except TooManyRequests:
        raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")
    
    except RequestError:
        raise HTTPException(status_code=500, detail="Request to YouTube failed.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

# For local running (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
