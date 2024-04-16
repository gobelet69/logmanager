"""Fichier log_manager"""
import os
from log import Log
from program_not_found import ProgramNotFound
class LogManager:
    """classe permettant de gérer les logs et de faire des opérations
    sur ses logs"""
    @staticmethod
    def sort_by_program(logs):
        """
        Renvoie un dictionnaire où chaque clé est un programme et la valeur
        associée à la clé est une liste contenant les logs du programme.
        :param logs: Une liste de Logs
        :return: Un dictionnaire
        """
        logs_by_program = {}
        for line in logs:
            log_instance = Log(str(line), logs)
            program = log_instance.get_program()
            if program not in logs_by_program.keys():
                logs_by_program[program] = []
            logs_by_program[program].append(line)
        return logs_by_program

    def __init__(self, logs=None):
        """
        :param logs: Une liste de logs (string) - Optionnel
        """
        self.logs = logs
        if self.logs is None:
            self.logs = {}
        else:
            self.logs = LogManager.sort_by_program(logs)

    def clear(self):
        """
        Remplace le contenu de self.logs par {}
        :return: None
        """
        self.logs ={}

    def add_logs(self, logs):
        """
        Rajoute les logs à self.logs
        :param logs: Une liste de Logs
        :return: None
        """
        new_logs = LogManager.sort_by_program(logs)
        for key, value in new_logs.items():
            for value in new_logs[key]:
                if key not in self.logs.keys():
                    self.logs[key] = []
                self.logs[key].append(value)


    def search_logs(self, program_name):
        """
        Renvoie la liste de Logs associés au programme. Si le
        programme n'existe pas dans self.logs, la fonction renvoie une
        erreur ProgramNotFound !
        :param program_name - String
        :return: Liste de Logs
        """
        if program_name in self.logs.keys():
            logs = self.logs[program_name]
            log_list = []
            for log in logs:
                log_list.append(log)
            return log_list
        else:
            raise ProgramNotFound(program_name, list(self.logs.keys()))

    @property
    def nbr_logs(self):
        """
        Renvoie la totalité des logs stockés dans le log_manager
        :return: Un entier représentant la totalité des logs dans le
        log_manager
        """
        count = 0
        for value in self.logs.values():
            count += len(value)
        return count

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du
        log_manager et le nombre total de logs  
        stockés dans le log_manager
        """
        message = ""
        for key,values in self.logs.items():
            message += f"{key}:{os.linesep}======={os.linesep}"
            for value in values:
                message += (f"{value}")
        message += (f"\nTOTAL LOGS: {self.nbr_logs}")
        return message
