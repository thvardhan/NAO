from naoqi import ALProxy
from chatbot import Chat,reflections,multiFunctionCall
import wikipedia
IP = "192.168.43.208"
SPEECH_PROXY = "ALSpeechRecognition"
TTS_PROXY = "ALTextToSpeech"
PORT = 9559

def whoIs(query,sessionID="general"):
    try:
        return wikipedia.summary(query)
    except:
        for newquery in wikipedia.search(query):
            try:
                return wikipedia.summary(newquery)
            except:
                pass
    return "I don't know about "+query

tts = ALProxy(TTS_PROXY, IP, PORT)

while True:
    dat = raw_input("type the query")
    ans = str(whoIs(dat))
    tts.say(ans+"")
