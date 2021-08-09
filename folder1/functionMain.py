def separar(strInformada):
    print("Ok")
    strIterar = str(strInformada)
    strVazia = ""
    contador = 0
    repetir = 0
    sigilo = ""
    while contador < len(str(strInformada)):
        try:
            strVazia = strIterar[contador]

            for i in (str(strInformada)):

                if str(i) == strVazia:
                    repetir += 1

                # print("FOR> ", strVazia, " - ", i, " : ", repetir)

            if repetir == 1:
                sigilo = sigilo + str(strVazia)
                contador += 1
                repetir = 0
            else:
                contador += 1
                repetir = 0
        except ValueError as e:
            print("Inválido!", e)
            break
    return sigilo
