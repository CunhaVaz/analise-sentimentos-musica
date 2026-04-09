import os
import pandas as pd
from transcricao import transcrever_audio
from sentimento import analisar_sentimento


def processar_pasta(pasta, epoca):
    dados = []

    for ficheiro in os.listdir(pasta):
        if ficheiro.endswith(".wav"):  # 🔥 só processar WAV

            caminho = os.path.join(pasta, ficheiro)

            print(f"Processando: {ficheiro}")

            # 🎧 Transcrição
            texto = transcrever_audio(caminho)

            # 😊 Sentimento
            sentimento = analisar_sentimento(texto)

            dados.append({
                "ficheiro": ficheiro,
                "epoca": epoca,
                "texto": texto,
                "sentimento": sentimento["label"],
                "score": sentimento["score"]
            })

    return dados


def main():
    dados = []

    # 📂 anos 80
    dados += processar_pasta("data/anos_80", "anos_80")

    # 📂 atuais
    dados += processar_pasta("data/atuais", "atuais")

    # 📊 DataFrame
    df = pd.DataFrame(dados)

    # 💾 guardar CSV
    df.to_csv("resultados/resultados.csv", index=False)

    # 📈 resumo no terminal
    print("\nResumo:")
    print(df.groupby(["epoca", "sentimento"]).size())


if __name__ == "__main__":
    main()


# 📊 GRÁFICO (fora da função main)
import matplotlib.pyplot as plt

df = pd.read_csv("resultados/resultados.csv")

df.groupby(["epoca", "sentimento"]).size().unstack().plot(kind="bar")

plt.title("Comparação de Sentimentos: Anos 80 vs Atual")
plt.xlabel("Época")
plt.ylabel("Número de músicas")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("resultados/grafico.png")
plt.show()