import json
from pprint import pprint

json_string = input()
dicc = json.loads(json_string)
cultivos = input()
listaCultivos = cultivos.split(" ")

cultivosEncontrados = []


def hallarPrecios(listaCul, dic):
    totalCultivos = 0
    for cultivo in listaCul:
        if cultivo in dic:
            cultivosEncontrados.append(cultivo)
            totalCultivos += dic.get(cultivo)
        

    return print(totalCultivos, cultivosEncontrados)

hallarPrecios(listaCultivos, dicc)

#diccionario = {"papa": 11347, "cebolla": 14017, "habichuela": 4068, "frijol": 5128}
