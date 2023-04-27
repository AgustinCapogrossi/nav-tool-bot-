class D_Dict:
    def __init__(self):
        pass

    def sort_dict(self, data):
        response = {}
        for _ in range(len(data)):
            for i in data:
                minimo = i
                break
            for i in data:
                valor = i.split(" de ")
                # Agarro el año mas chico si son distintos
                if valor[2] < minimo.split(" de ")[2]:
                    minimo = i
                # Agarro el mes mas chico si los años son iguales
                elif valor[2] == minimo.split(" de ")[2]:
                    if valor[1] < minimo.split(" de ")[1]:
                        minimo = i
                    # Agarro el dia mas chico si meses y años son iguales
                    elif valor[1] == minimo.split(" de ")[1]:
                        if valor[0] < minimo.split(" de ")[0]:
                            minimo = i
            response[minimo] = data[minimo]
            del data[minimo]
        return response

    def format_dict(self, data):
        stringponse = ""
        value = ""
        for i in data:
            for j in range(0, len(data[i])):
                value += data[i][j].replace("(", "").replace(")", "") + ", "
            s = i.replace("[", "")
            s = s.replace("]", "")
            stringponse += s + ": " + value + "\n"
            value = ""
        return stringponse
