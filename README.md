# Mão Robótica

Este repositório é referente ao projeto de mão robótica desenvolvido como extensão curricular da **Universidade Santa Cecília** para o curso de **Engenharia da Computação**.

A mão robótica integra visão computacional a um **Arduino Mega**, utilizando programação em **Python** e a biblioteca **PyFirmata** (protocolo Firmata Standard) como ponte de comunicação com o microcontrolador.

O código principal, `main.py`, é executado no computador e, por meio da câmera/webcam conectada, realiza o reconhecimento da mão do usuário e envia ao Arduino o estado de cada dedo (aberto ou fechado). O Arduino, por sua vez, replica esse movimento nos servomotores conectados à mão robótica.

Este projeto é inspirado no projeto de código aberto apresentado no vídeo abaixo, embora contenha alterações na estrutura física e no código:
[Vídeo original no YouTube](https://www.youtube.com/watch?v=ebRO4B7bNBE)

---

## Sumário

1. [Visão geral do projeto](#1-visão-geral-do-projeto)
2. [Requisitos](#2-requisitos)
3. [Instalação do Python 3.9](#3-instalação-do-python-39)
4. [Obtenção do projeto](#4-obtenção-do-projeto)
5. [Instalação e configuração do Visual Studio Code](#5-instalação-e-configuração-do-visual-studio-code)
6. [Instalação das bibliotecas (requirements)](#6-instalação-das-bibliotecas-requirements)
7. [Conexão do Arduino e identificação da porta COM](#7-conexão-do-arduino-e-identificação-da-porta-com)
8. [Configuração do arquivo servo_braco3d.py (porta COM)](#8-configuração-do-arquivo-servo_braco3dpy-porta-com)
9. [Configuração do arquivo main.py (webcam)](#9-configuração-do-arquivo-mainpy-webcam)
10. [Execução do projeto](#10-execução-do-projeto)
11. [Encerramento do programa](#11-encerramento-do-programa)
12. [Regravação do StandardFirmata no Arduino](#12-regravação-do-standardfirmata-no-arduino)
13. [Solução de problemas](#13-solução-de-problemas)
14. [Lista de verificação para apresentação](#14-lista-de-verificação-para-apresentação)
15. [Repositório do projeto](#15-repositório-do-projeto)

---

## 1. Visão geral do projeto

### 1.1. Estrutura de arquivos

| Arquivo              | Descrição                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------ |
| `main.py`          | Programa principal. Abre a webcam, detecta a mão do usuário e determina o estado de cada dedo. |
| `servo_braco3d.py` | Responsável pela conexão com o Arduino (porta COM) e pelo controle dos servomotores.           |
| `requirements.txt` | Lista das bibliotecas Python necessárias e suas respectivas versões.                           |
| `README.md`        | Documento de apresentação e tutorial de instalação (este arquivo).                           |

### 1.2. Funcionamento

O sistema opera conforme as seguintes etapas:

1. A webcam captura continuamente a imagem da mão do usuário.
2. A biblioteca **MediaPipe** identifica 21 pontos de referência da mão (articulações e pontas dos dedos).
3. O arquivo `main.py` calcula, a partir desses pontos, se cada dedo está **aberto** ou **fechado**.
4. O arquivo `servo_braco3d.py` envia o comando correspondente ao **Arduino** por meio do cabo USB.
5. O Arduino aciona o **servomotor** correspondente a cada dedo da mão robótica.

> [!IMPORTANT]
> O Arduino **já possui o firmware StandardFirmata gravado** e **não necessita de alterações**. Todo o processamento é realizado pelo Python no computador; o Arduino apenas executa os comandos recebidos.

---

## 2. Requisitos

| Item                                              | Observação                                                                                                |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Computador ou notebook com**Windows**       | O código utiliza recursos específicos do Windows (portas`COM` e o parâmetro `CAP_DSHOW` da câmera). |
| **Python 3.9 (64 bits)**                    | Versão obrigatória. Outras versões podem causar incompatibilidade com as bibliotecas.                    |
| **Visual Studio Code (VS Code)**            | Ambiente de desenvolvimento (IDE) utilizado para executar o projeto.                                        |
| **Webcam**                                  | Integrada ao notebook ou externa (USB).                                                                     |
| **Mão robótica com Arduino Mega**         | Previamente montada e com o StandardFirmata gravado.                                                        |
| **Cabo USB do Arduino**                     | Necessário para a comunicação entre o Arduino e o computador.                                            |
| **Fonte de alimentação dos servomotores** | A alimentação externa dos servomotores deve estar ligada durante a execução.                            |
| **Conexão com a internet**                 | Necessária apenas durante a instalação inicial.                                                          |

---

## 3. Instalação do Python 3.9

> [!WARNING]
> **É fundamental atentar-se à versão do Python instalada.** As bibliotecas do projeto (em especial `mediapipe` e `protobuf`) foram testadas na versão **3.9**. Recomenda-se **remover todas as demais versões do Python** do computador e manter **somente a versão 3.9**, a fim de evitar que o comando `pip` ou a IDE utilizem uma versão incorreta.

### 3.1. Remoção de outras versões (recomendado)

1. Abra o menu Iniciar e pesquise por **"Adicionar ou remover programas"**.
2. No campo de busca da lista de aplicativos, digite **Python**.
3. Para cada versão diferente da 3.9 (por exemplo, `Python 3.11` ou `Python 3.12`), clique sobre o item, selecione **Desinstalar** e confirme a operação.
4. Opcionalmente, desinstale também o item **Python Launcher**, para uma instalação totalmente limpa. Ele será reinstalado juntamente com o Python 3.9.

### 3.2. Download e instalação do Python 3.9

1. Acesse o endereço: **https://www.python.org/downloads/release/python-3913/**
2. Role a página até a seção **Files** e faça o download do arquivo **Windows installer (64-bit)**.
3. Execute o instalador baixado.
4. **Na primeira tela do instalador, antes de prosseguir**, marque obrigatoriamente a opção **"Add Python 3.9 to PATH"**.
5. Clique em **"Install Now"** e aguarde a conclusão da instalação.
6. Caso seja exibida, ao final, a opção **"Disable path length limit"**, clique sobre ela e confirme.
7. Clique em **Close** para finalizar o instalador.

### 3.3. Verificação da instalação

1. Abra o **Prompt de Comando** (menu Iniciar, digite `cmd` e pressione Enter).
2. Execute o comando abaixo:

```bash
python --version
```

O resultado esperado é semelhante a:

```
Python 3.9.13
```

3. Em seguida, verifique o gerenciador de pacotes `pip`:

```bash
pip --version
```

O resultado deve terminar com `(python 3.9)`, como no exemplo:

```
pip 22.0.4 from C:\Users\...\Python39\lib\site-packages\pip (python 3.9)
```

> [!NOTE]
> Caso seja exibida outra versão, ou a mensagem `'python' não é reconhecido como um comando interno`, consulte a seção [13. Solução de problemas](#13-solução-de-problemas).

---

## 4. Obtenção do projeto

O projeto pode ser obtido por uma das duas formas descritas a seguir.

### 4.1. Opção A: download do arquivo ZIP pelo GitHub

1. Acesse o repositório: **https://github.com/yasmim-rayane/mao-robotica**
2. Clique no botão verde **Code** e, em seguida, em **Download ZIP**.
3. Localize o arquivo baixado (geralmente na pasta **Downloads**).
4. Clique com o botão direito do mouse sobre o arquivo e selecione **Extrair tudo...**.
5. Escolha um local de fácil acesso (por exemplo, a **Área de Trabalho**) e clique em **Extrair**.
6. Será criada uma pasta denominada `mao-robotica-main` (ou nome semelhante), contendo os arquivos `main.py`, `servo_braco3d.py`, `requirements.txt` e `README.md`.

> [!CAUTION]
> **Não execute o projeto diretamente de dentro do arquivo ZIP.** A pasta deve ser extraída antes de ser aberta no VS Code.

### 4.2. Opção B: clonagem com Git

Caso o computador possua o [Git](https://git-scm.com/download/win) instalado:

1. Abra o Prompt de Comando na pasta onde o projeto deverá ser salvo.
2. Execute o comando:

```bash
git clone https://github.com/yasmim-rayane/mao-robotica.git
```

3. Será criada a pasta `mao-robotica` com todos os arquivos do projeto.

---

## 5. Instalação e configuração do Visual Studio Code

### 5.1. Instalação

1. Acesse **https://code.visualstudio.com/** e faça o download da versão para Windows.
2. Execute o instalador, aceite os termos de licença e mantenha as opções padrão.
3. Recomenda-se marcar as opções **"Adicionar ação 'Abrir com Code'"** durante a instalação, para facilitar a abertura de pastas.

### 5.2. Instalação da extensão Python

1. Abra o VS Code.
2. Clique no ícone **Extensions** (Extensões) na barra lateral esquerda, ou pressione `Ctrl + Shift + X`.
3. No campo de pesquisa, digite **Python**.
4. Selecione a extensão **Python**, publicada pela **Microsoft**, e clique em **Install**.

### 5.3. Abertura da pasta do projeto

1. No menu superior, clique em **File > Open Folder...** (ou **Arquivo > Abrir Pasta...**).
2. Selecione a pasta do projeto (aquela que contém diretamente o arquivo `main.py`) e clique em **Selecionar pasta**.
3. Caso seja exibida a mensagem *"Do you trust the authors of the files in this folder?"*, clique em **Yes, I trust the authors**.
4. Os arquivos do projeto serão exibidos no painel **Explorer**, à esquerda.

### 5.4. Seleção do interpretador Python 3.9

Este procedimento garante que o VS Code utilize a versão correta do Python:

1. Pressione `Ctrl + Shift + P` para abrir a paleta de comandos.
2. Digite **Python: Select Interpreter** e pressione Enter.
3. Selecione a opção correspondente ao **Python 3.9.x**.
4. Confirme a versão selecionada no **canto inferior direito** da janela do VS Code, onde deverá constar `3.9.x`.

---

## 6. Instalação das bibliotecas (requirements)

1. No VS Code, abra o terminal integrado pelo menu **Terminal > New Terminal** (ou pelo atalho ``Ctrl + ` ``).
2. Certifique-se de que o terminal está posicionado na **pasta raiz do projeto** (a mesma que contém os arquivos `main.py` e `requirements.txt`). O caminho é exibido antes do cursor, por exemplo:

```
PS C:\Users\NomeDoUsuario\Desktop\mao-robotica>
```

3. Execute o comando:

```bash
pip install -r requirements.txt
```

4. Aguarde a conclusão da instalação, que pode levar alguns minutos. Serão instaladas as seguintes bibliotecas:

| Biblioteca        | Versão  | Finalidade                                                                      |
| ----------------- | -------- | ------------------------------------------------------------------------------- |
| `opencv-python` | 4.9.0.80 | Captura e exibição da imagem da webcam.                                       |
| `mediapipe`     | 0.10.11  | Reconhecimento dos pontos de referência da mão.                               |
| `pillow`        | 10.2.0   | Manipulação de imagens (dependência).                                        |
| `protobuf`      | 3.20.3   | Dependência do MediaPipe (versão específica para evitar incompatibilidades). |
| `pyFirmata`     | 1.1.0    | Comunicação entre o Python e o Arduino.                                       |

5. Ao término, deverá ser exibida uma mensagem semelhante a `Successfully installed ...`.

> [!TIP]
> Caso o comando `pip` não seja reconhecido, ou esteja instalando as bibliotecas em outra versão do Python, utilize uma das alternativas abaixo:
>
> ```bash
> python -m pip install -r requirements.txt
> ```
>
> ```bash
> py -3.9 -m pip install -r requirements.txt
> ```

> [!NOTE]
> A instalação das bibliotecas precisa ser realizada **apenas uma vez** em cada computador.

---

## 7. Conexão do Arduino e identificação da porta COM

1. **Conecte o Arduino ao computador por meio do cabo USB.**
2. Abra o **Gerenciador de Dispositivos**, por uma das formas a seguir:
   - Clique com o botão direito do mouse sobre o menu Iniciar e selecione **Gerenciador de Dispositivos**; ou
   - Pressione `Win + X` e selecione **Gerenciador de Dispositivos**.
3. Expanda a categoria **Portas (COM e LPT)**.
4. Localize um item semelhante a um dos exemplos abaixo:

```
Arduino Mega 2560 (COM6)
```

```
USB-SERIAL CH340 (COM3)
```

5. **Anote o número da porta** indicado entre parênteses (por exemplo, `COM6`).

> [!TIP]
> Caso haja dúvida sobre qual porta pertence ao Arduino, desconecte o cabo USB e observe qual item deixa de ser exibido na lista. Ao reconectar o cabo, o item que reaparecer corresponde à porta do Arduino.

> [!WARNING]
> O número da porta COM **pode variar** caso o Arduino seja conectado a outra entrada USB ou a outro computador. Recomenda-se conferi-lo sempre antes de executar o projeto.

---

## 8. Configuração do arquivo servo_braco3d.py (porta COM)

1. No painel **Explorer** do VS Code, abra o arquivo **`servo_braco3d.py`**.
2. Localize a **linha 6**, cujo conteúdo é:

```python
board = Arduino('COM6')
```

3. Substitua `COM6` pela porta identificada na seção anterior. Por exemplo, caso a porta identificada seja `COM3`, a linha deverá ficar da seguinte forma:

```python
board = Arduino('COM3')
```

4. Salve o arquivo pelo atalho `Ctrl + S`.

> [!IMPORTANT]
> Mantenha as aspas simples ao redor do nome da porta e escreva `COM` em letras maiúsculas.

> [!NOTE]
> As demais configurações deste arquivo (pinos dos servomotores e ângulos de movimento) **não devem ser alteradas**.

---

## 9. Configuração do arquivo main.py (webcam)

1. No painel **Explorer** do VS Code, abra o arquivo **`main.py`**.
2. Localize a **linha 8**, cujo conteúdo é:

```python
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
```

3. O **primeiro valor** entre parênteses (`0`) indica qual webcam será utilizada, conforme descrito nos comentários das linhas 5 a 7 do próprio código:

| Valor             | Situação de uso                                                                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`             | Webcam padrão do dispositivo (por exemplo, a câmera integrada do notebook) ou, caso o computador não possua câmera integrada, a primeira webcam conectada.                      |
| `1`             | Webcam secundária. Geralmente utilizada em notebooks que já possuem câmera integrada, quando se deseja utilizar uma webcam externa (USB) com melhor qualidade ou posicionamento. |
| `2`, `3`, ... | Utilizados caso existam mais câmeras conectadas ao computador.                                                                                                                     |

4. Exemplo de configuração para utilizar uma webcam externa em um notebook:

```python
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
```

5. Salve o arquivo pelo atalho `Ctrl + S`.

> [!TIP]
> Caso a janela da câmera seja exibida em preto, exiba a câmera incorreta ou o programa apresente erro logo ao iniciar, altere o valor (de `0` para `1`, ou vice-versa) e execute o programa novamente.

---

## 10. Execução do projeto

> [!IMPORTANT]
> **O Arduino deve estar conectado ao computador pelo cabo USB ANTES da execução do arquivo `main.py`.** Caso contrário, o programa não conseguirá estabelecer comunicação com a mão robótica e será encerrado com erro.

### 10.1. Sequência de execução

Siga rigorosamente a ordem abaixo:

1. Verifique se a mão robótica está montada e se a fonte de alimentação dos servomotores (caso exista) está ligada.
2. Conecte o Arduino ao computador por meio do cabo USB.
3. Confirme que a porta COM está corretamente configurada no arquivo `servo_braco3d.py` (seção 8).
4. Confirme que a webcam está corretamente configurada no arquivo `main.py` (seção 9).
5. No VS Code, abra o arquivo **`main.py`**.
6. Clique no botão **Run Python File**, representado por um triângulo no canto superior direito da janela do editor.
   - Alternativamente, execute o seguinte comando no terminal do VS Code:

```bash
python main.py
```

7. Aguarde alguns segundos. Será aberta uma janela denominada **"Imagem"**, exibindo a imagem capturada pela webcam.
8. Posicione **uma única mão** diante da câmera, com a **palma voltada para a câmera** e os dedos apontados para cima.
9. Os pontos de referência da mão serão desenhados na imagem, e a mão robótica passará a **abrir e fechar os dedos** de acordo com os movimentos realizados.

### 10.2. Recomendações para o reconhecimento

- Utilize um ambiente bem iluminado e evite luz intensa atrás da mão (contraluz).
- Mantenha a mão a uma distância aproximada de 40 cm a 80 cm da câmera.
- O sistema reconhece **apenas uma mão** por vez.
- Um fundo liso e sem muitos elementos contribui para um reconhecimento mais preciso.

> [!NOTE]
> A exibição contínua de números no terminal durante a execução é um comportamento esperado. Trata-se de um valor de depuração referente à posição do dedo polegar.

---

## 11. Encerramento do programa

O programa **não possui uma tecla de saída**, e o fechamento da janela "Imagem" pelo botão de fechar (X) **não encerra a execução** (a janela poderá ser reaberta automaticamente). Para encerrar corretamente, utilize uma das opções abaixo:

- No painel do terminal do VS Code, clique no ícone de **lixeira (Kill Terminal)**; ou
- Clique dentro do terminal do VS Code e pressione **`Ctrl + C`**.

> [!WARNING]
> Encerre sempre o programa antes de desconectar o cabo USB do Arduino e antes de executar o arquivo `main.py` novamente. Caso uma execução anterior ainda esteja ativa, a porta COM permanecerá ocupada e a nova execução apresentará erro.

---

## 12. Regravação do StandardFirmata no Arduino

Em condições normais, **este procedimento não é necessário**, uma vez que o Arduino da mão robótica já possui o StandardFirmata gravado. Ele deve ser realizado **somente** nas seguintes situações:

- O Arduino foi substituído por outro;
- O Arduino foi regravado com outro código;
- O Python não consegue se comunicar com o Arduino, mesmo com a porta COM corretamente configurada.

### 12.1. Procedimento

1. Faça o download e instale a **Arduino IDE**, disponível em: https://www.arduino.cc/en/software
2. Conecte o Arduino ao computador por meio do cabo USB.
3. Abra a Arduino IDE e configure a placa e a porta:
   - **Tools (Ferramentas) > Board (Placa) > Arduino AVR Boards > Arduino Mega or Mega 2560**
   - **Tools (Ferramentas) > Port (Porta) >** porta COM do Arduino (por exemplo, `COM6`)
4. Abra o exemplo do Firmata:
   - **File (Arquivo) > Examples (Exemplos) > Firmata > StandardFirmata**
5. Clique no botão **Upload** (ícone de seta para a direita) e aguarde a mensagem **"Done uploading"** ou **"Carregamento concluído"**.
6. **Feche a Arduino IDE** antes de executar o arquivo `main.py`, pois ela pode manter a porta COM ocupada.

> [!NOTE]
> Caso o exemplo **Firmata** não esteja disponível, instale a biblioteca por meio do menu **Sketch > Include Library > Manage Libraries...**, pesquisando por **Firmata** e clicando em **Install**.

---

## 13. Solução de problemas

| Problema ou mensagem de erro                                                                 | Causa provável                                                                              | Solução                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `'python' não é reconhecido como um comando interno` ou `'pip' não é reconhecido...` | O Python não foi adicionado ao PATH do sistema.                                             | Reinstale o Python 3.9 marcando a opção**"Add Python 3.9 to PATH"** (seção 3.2). Em seguida, feche e abra novamente o terminal e o VS Code.                                                        |
| O comando`python --version` exibe outra versão (por exemplo, 3.12).                       | Existem múltiplas versões do Python instaladas.                                            | Remova as demais versões (seção 3.1), ou utilize`py -3.9 -m pip ...` e selecione o interpretador 3.9 no VS Code (seção 5.4).                                                                          |
| `ModuleNotFoundError: No module named 'cv2'` (ou `mediapipe`, `pyfirmata`)             | As bibliotecas não foram instaladas, ou foram instaladas em outra versão do Python.        | Verifique o interpretador selecionado no VS Code (seção 5.4) e execute novamente`pip install -r requirements.txt`.                                                                                       |
| Erro na instalação do`mediapipe` (`No matching distribution found`)                    | Versão do Python incompatível.                                                             | Utilize o**Python 3.9 (64 bits)**.                                                                                                                                                                     |
| `could not open port 'COM6'`, `FileNotFoundError` ou `SerialException`                 | Porta COM incorreta ou Arduino desconectado.                                                 | Verifique a porta no Gerenciador de Dispositivos (seção 7) e atualize a linha 6 do arquivo`servo_braco3d.py`.                                                                                            |
| `could not open port 'COMx': PermissionError(13, 'Acesso negado.')`                        | A porta está sendo utilizada por outro programa.                                            | Encerre execuções anteriores do`main.py` (seção 11), feche a Arduino IDE e o Monitor Serial e tente novamente. Persistindo o erro, desconecte e reconecte o cabo USB.                                  |
| O Arduino não é exibido em "Portas (COM e LPT)".                                           | Cabo USB apenas de alimentação, driver ausente ou mau contato.                             | Teste outro cabo ou outra entrada USB. Caso o dispositivo seja exibido como "Dispositivo desconhecido", instale o driver adequado (por exemplo, o driver**CH340** para placas compatíveis).           |
| `cv2.error: ... (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'`          | A webcam não foi encontrada ou não pôde ser aberta.                                       | Altere o valor da webcam na linha 8 do arquivo`main.py` (de `0` para `1`, ou vice-versa). Verifique também se outro programa (Teams, Meet, Zoom, Câmera do Windows) não está utilizando a câmera. |
| A janela da câmera é exibida em preto.                                                     | Câmera incorreta, em uso por outro programa ou com a tampa de privacidade fechada.          | Altere o valor da webcam, feche outros programas que utilizem a câmera e verifique a tampa física da câmera do notebook.                                                                                  |
| Erros relacionados ao`protobuf` (por exemplo, `Descriptors cannot be created directly`)  | Versão incorreta da biblioteca`protobuf`.                                                 | Execute`pip install protobuf==3.20.3`.                                                                                                                                                                     |
| A mão é reconhecida na imagem, mas a mão robótica não se movimenta.                     | Alimentação dos servomotores desligada, Arduino sem o StandardFirmata ou conexões soltas. | Verifique a fonte de alimentação e as conexões dos servomotores. Se necessário, regrave o StandardFirmata (seção 12).                                                                                  |
| Os dedos se movimentam de forma irregular ou trêmula.                                       | Iluminação inadequada ou mão mal posicionada.                                             | Melhore a iluminação, mantenha a palma voltada para a câmera e utilize um fundo liso (seção 10.2).                                                                                                      |

---

## 14. Lista de verificação para apresentação

Para computadores nos quais a instalação já foi realizada, segue o resumo dos procedimentos a serem executados no dia da apresentação:

- [ ] Ligar a fonte de alimentação da mão robótica.
- [ ] **Conectar o Arduino ao computador por meio do cabo USB.**
- [ ] Verificar a porta COM no Gerenciador de Dispositivos e ajustar a **linha 6** do arquivo `servo_braco3d.py`.
- [ ] Verificar a webcam e ajustar a **linha 8** do arquivo `main.py` (`0` ou `1`).
- [ ] Abrir a pasta do projeto no VS Code e confirmar o **Python 3.9** no canto inferior direito da janela.
- [ ] Executar o arquivo `main.py` pelo botão **Run Python File**.
- [ ] Ao término, encerrar o programa pelo terminal (ícone de **lixeira** ou **`Ctrl + C`**) antes de desconectar o cabo USB.

---

## 15. Repositório do projeto

O código-fonte completo e atualizado está disponível no GitHub:
**https://github.com/yasmim-rayane/mao-robotica**
