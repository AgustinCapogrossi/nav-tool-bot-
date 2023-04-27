import asyncio
import os
from modules.embed import D_Embeds
from modules.dictionary import D_Dict


months = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]

dictionary = D_Dict()
embeds = D_Embeds()


class Schedules:
    def __init__(self):
        pass

    def add(self, year, month, day, event, user):
        fecha = str(day) + " de " + months[month - 1] + " de " + str(year)
        f = open("schedule/schedule" + str(user) + ".md", "a")
        f.write("[" + fecha + "]" + ";" + "(" + event + ")" + "\n")
        f.close()

    async def remind(self, timer: str):
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        rmnder = int(timer[:-1]) * (time_convert[timer[-1]])
        await asyncio.sleep(int(rmnder))

    def list(self, user):
        data = {}
        with open("schedule/schedule" + str(user) + ".md", "r") as file:
            for line in file.readlines():
                key, value = line.strip().split(";")
                if key in data:
                    data[key].append(value)
                else:
                    data[key] = [value]
        file.close()
        response = dictionary.sort_dict(data)
        stringponse = dictionary.format_dict(response)
        return stringponse

    def drop(self, user):
        os.remove("schedule/schedule" + str(user) + ".md")
