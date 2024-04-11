import speech_recognition as sr
import RPi.GPIO as GPIO
import time

r=sr.Recognizer()

s=''
relay_comedor=24
relay_sala=27
relay_dormitorio=16

pin_entrada_sala = 21
pin_entrada_dormitorio = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)

GPIO.setup(relay_comedor, GPIO.OUT)
GPIO.setup(relay_sala, GPIO.OUT)
GPIO.setup(relay_dormitorio, GPIO.OUT)

GPIO.output(relay_comedor, GPIO.HIGH)
GPIO.output(relay_sala, GPIO.LOW)
GPIO.output(relay_dormitorio, GPIO.LOW)

while True:
    
    while s.lower()!='bye':
        
        with sr.Microphone() as source:
            print('Say something!')
            audio=r.listen(source, phrase_time_limit=3)
        try:
            s=r.recognize_google(audio, language="es-ES")
            print('I think you said ' + s)
            #inicio de control casa
            if s == 'encender sala':
                #encender foco 1
                GPIO.output(relay_sala, GPIO.HIGH)
                print ('Se prendio foco sala')
            if s == 'encender dormitorio':
                #encender foco 2
                GPIO.output(relay_dormitorio, GPIO.HIGH)
                print ('Se prendio foco dormitorio')
            if s == 'encender comedor':
                #encender foco 3
                GPIO.output(relay_comedor, GPIO.LOW)
                print ('Se prendio foco comedor')
            if s == 'encender casa':
                #encender casa (encender los 3 focos)
                GPIO.output(relay_comedor, GPIO.LOW)
                GPIO.output(relay_dormitorio, GPIO.HIGH)
                GPIO.output(relay_sala, GPIO.HIGH)
                print('se encendieron todos los focos de la casa')
            if s.lower() == 'apagar comedor':
                #apagar foco 3
                GPIO.output(relay_comedor, GPIO.HIGH)
            if s.lower() == 'apagar sala':
                #apagar foco 1
                GPIO.output(relay_sala, GPIO.LOW)
            if s.lower() == 'apagar dormitorio':
                #apagar foco 1
                GPIO.output(relay_dormitorio, GPIO.LOW)
            if s.lower() == 'apagar casa':
                #encender casa (encender los 3 focos)
                GPIO.output(relay_comedor, GPIO.HIGH)
                GPIO.output(relay_dormitorio, GPIO.LOW)
                GPIO.output(relay_sala, GPIO.LOW)
                print('se apagaron todos los focos de la casa')
        except sr.UnknownValueError:
            
            print('Sorry, try again!')
        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition service; {0}'.format(e))
    print('Have a nice day!')
    break;

