from sigiloFolder.funtionMain import separar
import unicodedata

preparo = input(
    str("Preparação do sigilo: Escreva uma afirmação no presente: ")).lower()
processamento_2 = unicodedata.normalize("NFD", preparo)
processamento_2 = processamento_2.encode("ascii", "ignore")
processamento_2 = processamento_2.decode("utf-8")

ativo = True

while ativo:
    print(separar(processamento_2))
    break
