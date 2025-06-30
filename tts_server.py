from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from gtts import gTTS
import os

app = FastAPI()

# ✅ Allow requests from React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # safer
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate-voice/")
def generate_voice(text: str):
    filename = "output.mp3"
    
    # ✅ Clean old file if exists
    if os.path.exists(filename):
        os.remove(filename)

    # 🎤 Generate new voice
    tts = gTTS(text=text, lang='ta')
    tts.save(filename)

    # 📤 Send back to frontend
    return FileResponse(path=filename, media_type='audio/mpeg', filename=filename)
