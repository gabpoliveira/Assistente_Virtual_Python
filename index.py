import speech_recognition as sr #Biblioteca para reconhecimento de fala
import re # Biblioteca para expressões regulares
import pyttsx3 # Biblioteca para conversão de texto em fala

engine = pyttsx3.init() # Inicializa o mecanismo de conversão de texto em fala
engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana") #Define a voz a ser usada

def falar(texto):# Função para falar um texto
    print("Assistente:", texto)
    engine.say(texto)
    engine.runAndWait()

while(True): # Loop infinito para continuar ouvindo
    
    mic = sr.Recognizer() # Inicializa o reconhecedor de fala
    with sr.Microphone() as source: # Usa o microfone como fonte de áudio
        mic.adjust_for_ambient_noise(source) # Ajusta o ruído ambiente
        falar("Olá, qual seu nome?") # Fala uma mensagem de saudação
        audio = mic.listen(source) # Escuta o áudio do microfone

        try:
            frase = mic.recognize_google(audio, language='pt-BR')# Reconhece o áudio usando o Google Speech Recognition e define o idioma como português do Brasil
            print("Você disse:", frase)# Exibe o que o usuário disse
            match = re.search(r"meu nome é (.*)", frase.lower())# Procura por uma expressão regular que capture o nome
            if match:
                nome = match.group(1)# Se encontrou o nome na frase
            else:
                nome = frase  # Assume que o usuário só disse o nome

            falar(f"Olá {nome}! Como posso ajudar?") # Fala o nome do usuário
            break  # Encerra o loop se quiser parar após saber o nome

        except sr.UnknownValueError:# Se não conseguiu entender o áudio
            falar("Desculpe, não entendi. Pode repetir, por favor?")