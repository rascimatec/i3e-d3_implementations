from word2number import w2n
import speech_recognition as sr


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def comando(imprimir=1):  # Serve para ouvir uma frase e retorná-la como uma string
    try:
        r = sr.Recognizer()
        while True:  # Continuará neste loop até que a fala seja entendida
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, 0.75)  # Se 'adapta' aos ruídos externos
                if imprimir == 1:
                    print('Listening...')
                audio = r.listen(source)

            try:
                if imprimir == 1:
                    print('Recognizing...')
                pergunta = r.recognize_google(audio, language='en-US')
                print('You said:{}'.format(pergunta))
                break

            except Exception as e:  # Caso não compreenda o que foi dito
                print('Speak again please')

        return str(pergunta)
    except:
        print(colored(255, 0, 0, "Connect a microphone"))
        comando()


def get_coords(debug=0):
    # Modelo de frase esperado: go to x (number) and y (number)
    # 'go to x' e 'and y' são usados como marcadores das coordenas x e y
    text = comando()
    text.lower().strip()
    xtemp = text.find("go to x")
    ytemp = text.find("and y")

    xcoord = text[xtemp:ytemp]
    xcoord = xcoord.replace("go to x", "").strip()
    xnum = w2n.word_to_num(xcoord)

    ycoord = text[ytemp:]
    ycoord = ycoord.replace("and y", "").strip()
    ynum = w2n.word_to_num(ycoord)

    if debug:
        print(f'raw input {text}')
        print(f'x = {xcoord}, y = {ycoord}')
        print(f'x = {xnum}, y = {ynum}')
    coords = [xnum, ynum]
    return coords


#get_coords()


