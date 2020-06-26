import time
from threading import Timer
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Speak("Welcome")