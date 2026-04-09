import speech_recognition as sr

def transcrever_audio(caminho_audio):
    recognizer = sr.Recognizer()

    with sr.AudioFile(caminho_audio) as source:
        audio = recognizer.record(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-PT")
        return texto
    except:
        return ""