from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from gtts import gTTS
import os

app = FastAPI()

# ✅ Allow requests from frontend (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can limit later to your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Gnani Voice Server is running ✅"}

@app.get("/generate-voice")
def generate_voice(text: str):
    filename = "output.mp3"
    
    # ✅ Remove old file if exists
    if os.path.exists(filename):
        os.remove(filename)

    # 🎤 Generate voice
    tts = gTTS(text=text, lang='ta')
    tts.save(filename)

    # 📤 Return audio file
    return FileResponse(path=filename, media_type='audio/mpeg', filename=filename)
