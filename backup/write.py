import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)

print("Starting!")

while True:
      comando = input('Introduce un comando: ') #Input
      comando_enc = comando.encode()
      arduino.write(comando_enc) #Mandar un comando hacia Arduino
      if comando == 'H':
            print('LED ENCENDIDO')
      elif comando == 'L':
            print('LED APAGADO')
      else:
            print('Comando invalido')

arduino.close() #Finalizamos la comunicacion
