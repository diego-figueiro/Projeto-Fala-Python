# módulo do Google que faz Text-to-Speech
import gtts
# usa pra tocar
from playsound import playsound

# abrir arquivo e abrir para leitura e chamar essa operação de 'arquivo'
with open('frase.txt', 'r') as arquivo:
    # ler cada linha no idioma certo, e guardar essa informação em uma variável
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        # transforar a informação lida em um arquio de audio
        frase.save('frase.mp3')
        playsound('frase.mp3')

