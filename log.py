"""Fichier log"""
class Log:
    """La classe Log permet de représenter une ligne de log contenue dans un fichier"""
    def __init__(self, text, source):
        """
        Constructeur de la classe Log
        :param text: String - Contenu de la ligne de log
        :param source: String - Chemin vers le fichier qui contenait
        cette ligne de log
        """

        self.text = str(text)
        self.source = source
        self.program = self.get_program()

    def get_program(self):
        """
        :return: Le nom du programme contenu dans la ligne de log.
        Si la ligne ne contient
        pas de nom, "Unknown" sera renvoyé
        """
        program = self.text.replace(" ","[").replace(":","[").split("[")
        return program[6]

    def __str__(self):
        """
        :return: String - renvoie le contenu du log
        """
        return self.text
