"""Fichier program_not_found"""
import os
class ProgramNotFound(Exception):
    """Exception customisée pour représenter le fait qu’un programme n’a
    pas été trouvé dans notre CLI"""
    def __init__(self, searched_program, available_programs):
        self.searched_program = searched_program
        self.available_programs = available_programs

    def __str__(self):
        available_programs_list = os.linesep.join(list(self.available_programs))
        return f"Impossible de trouver le programme {self.searched_program} dans la liste :{os.linesep}{available_programs_list}"
