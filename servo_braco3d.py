from pyfirmata import Arduino,SERVO
import time

# Entrada que o Arduino está conectado no dispositivo
# Pode (e possivelmente vai) variar
board = Arduino('COM5')

# Pinos dos dedos nos servos da mão
pin1 = 3
pin2 = 4
pin3 = 5
pin4 = 9
pin5 = 11

board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO
board.digital[pin3].mode = SERVO
board.digital[pin4].mode = SERVO
board.digital[pin5].mode = SERVO

def rotateServo(pino,angle):
    board.digital[pino].write(angle)
    time.sleep(0.015)

def abrir_fechar(pin,on_off):
    if on_off==1:
        rotateServo(pin, 0)
    elif on_off==0 and pin!=11 and pin!=9:
        rotateServo(pin, 140)
    elif on_off == 0 and pin == 11:
        rotateServo(pin, 150)
    elif on_off == 0 and pin == 9:
        rotateServo(pin, 180)

def testeTodos():
    rotateServo(pin1,0)
    rotateServo(pin2,0)
    rotateServo(pin3,0)
    rotateServo(pin4,0)
    rotateServo(pin5,0)
    time.sleep(1)

    rotateServo(pin1,150)
    time.sleep(1)
    rotateServo(pin1,0)
    time.sleep(1)

    rotateServo(pin2,130)
    time.sleep(1)
    rotateServo(pin2,0)
    time.sleep(1)

    rotateServo(pin3,130)
    time.sleep(1)
    rotateServo(pin3,0)
    time.sleep(1)

    rotateServo(pin4,130)
    time.sleep(1)
    rotateServo(pin4,0)
    time.sleep(1)

    rotateServo(pin5,130)
    time.sleep(1)
    rotateServo(pin5,0)
    time.sleep(2)