from pydub import AudioSegment
import os

def converter_mp3_para_wav(pasta):
    for ficheiro in os.listdir(pasta):
        if ficheiro.endswith(".mp3"):
            caminho_mp3 = os.path.join(pasta, ficheiro)
            caminho_wav = caminho_mp3.replace(".mp3", ".wav")

            audio = AudioSegment.from_mp3(caminho_mp3)

            # 🔥 CORREÇÃO IMPORTANTE
            audio = audio.set_channels(1)       # mono
            audio = audio.set_frame_rate(16000) # sample rate correto

            audio.export(caminho_wav, format="wav")

            print(f"Convertido (OK): {ficheiro}")

converter_mp3_para_wav("data/anos_80")
converter_mp3_para_wav("data/atuais")