import os
from modules.embed import D_Embeds

embeds = D_Embeds()


class Resources:
    def __init__(self):
        pass

    def add(self, user, resource_name, resource_value):
        """Añade un recurso a tu lista

        Args:
            user (String): "String con el nombre del usuario"
            resource_name (String): "String con el nombre del recurso"
            resource_value (String): "String con el valor del recurso"
        """
        f = open("resources/resources" + str(user) + ".md", "a")
        f.write("[" + resource_name + "]" + ";" + "(" + resource_value + ")" + "\n")
        f.close()

    def drop(self, user):
        """Elimina tu lista de recursos

        Args:
            user (String): "String con el nombre del usuario"
        """
        os.remove("resources/resources" + str(user) + ".md")

    def delete(self, user, data, resource_name):
        """Elimina un elemento de tu lista de recursos

        Args:
            user (String): "String con el nombre del usuario"
            data (List): "Lista de recursos parseados"
            resource_name (String): "String con el nombre del recurso"
        """
        with open("resources/resources" + str(user) + ".md", "r") as file:
            for line in file.readlines():
                key, value = line.strip().split(";")
                data[key] = value
        file.close()
        if "[" + resource_name + "]" in data:
            data.pop("[" + resource_name + "]")
        os.remove("resources/resources" + str(user) + ".md")
        file = open("resources/resources" + str(user) + ".md", "w")
        for i in data:
            new_line = i + ";" + data[i] + "\n"
            file.write(new_line)
        file.close()

    def find(self, user, data, resource_name):
        """Encuentra un elemento de tu lista

        Args:
            user (String): "String con el nombre del usuario"
            data (List): "Lista de recursos parseados"
            resource_name (String): "String con el nombre del recurso"

        Returns:
            Embed: "Embed con la información encontrada"
        """
        with open("resources/resources" + str(user) + ".md", "r") as file:
            for line in file.readlines():
                key, value = line.strip().split(";")
                data[key] = value
        file.close()
        if "[" + resource_name + "]" in data:
            response = (
                "[" + resource_name + "]" + data["[" + resource_name + "]"] + "\n"
            )
            em = embeds.pass_embed(response)
        else:
            em = embeds.fail_embed(
                "La entrada que desea encontrar no existe, verifique los elementos existentes con $resource_list."
            )
        return em

    def list(self, user, data):
        """Lista todos los recursos de un usuario

        Args:
            user (String): "String con el nombre del usuario"
            data (List): "Lista de recursos parseados"

        Returns:
            String: "String con los recursos"
        """
        with open("resources/resources" + str(user) + ".md", "r") as file:
            for line in file.readlines():
                key, value = line.strip().split(";")
                data[key] = value
        file.close()
        response = ""
        for key in data:
            response = response + key + data[key] + "\n"
        return response
