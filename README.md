Esse repositório é referente ao projeto de mão robótica como extensão curricular da Universidade Santa Cecília para o curso de Engenharia da Computação.
A mão robótica mistura visão computacional com um Arduino Mega, utilizando programação em Python e a biblioteca PyFirmata Standard para a ponte de comunicação com o microcontrolador.

O código principal main.py é rodado no dispositivo e, utilizando a câmera/webcam conectada, faz reconhecimento da mão e passa o ângulo de dobra dos dedos para o Arduino, que replica esse movimento nos Servomotores conectados.
A configuração dos pinos dos dedos e da COM do Arduino estão no arquivo servo_braco3d.
Para verificar os requisitos necessários do projeto, leia o arquivo requirements.txt.

Esse projeto é inspirado no projeto open-source do vídeo abaixo, embora contenha algumas alterações na estrutura física e no código:
![image](https://github.com/user-attachments/assets/01af0426-7514-437f-aecc-d2267797de2d)
