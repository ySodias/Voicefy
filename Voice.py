import speech_recognition as sr

class Voice:

    def __init__(self, frase, audio):
        self.frase = frase
        self.audio = audio

    # Função para ouvir e reconhecer a fala
    def ouvir_microfone(self):
        # Habilita o microfone do usuário
        microfone = sr.Recognizer()

        # usando o microfone
        with sr.Microphone() as source:

            # Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)

            # Armazena o que foi dito numa variavel
            audio = microfone.listen(source)

        try:

            self.frase = microfone.recognize_google(audio, language='pt-BR')

            return self.frase

        except sr.UnkownValueError:
            return sr.UnkownValueError

        return frase
