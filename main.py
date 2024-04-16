"""Fichier main"""
import os
from log_manager import LogManager
def load_log_from_file(relative_path):
    """
    La fonction permet de récupérer les logs se trouvant dans un
    fichier grâce au chemin relatif passé en argument de la fonction.
    La fonction NE peut PAS lancer d’erreur. Si le chemin n'existe
    pas, la fonction affiche "Le chemin n'existe pas" et donne le chemin
    ABSOLU du fichier demandé.
    S'il y a eu une exception, renvoyez explicitement un "None"
    :param relative_path: String représentant un chemin relatif
    (vers un fichier) par rapport au dossier courant.
    :return: Renvoie un tableau de strings qui sont les logs
    contenant les logs.
    """
    try :
        with open(relative_path) as file:
            log = file.readlines()
        return log
    except FileNotFoundError :
        print("Le chemin du fichier n'existe pas:",os.path.abspath(relative_path))
    except :
        return None

def load_logs_from_folder(folder_path):
    """
    La fonction permet de charger les logs de tous les fichiers
    présents dans un dossier. Le chemin
    relatif en argument de la fonction est le chemin relatif
    vers un dossier.
    La fonction NE peut PAS lancer d’erreur. Si le chemin
    n'existe pas, la fonction affiche "Le chemin n'existe pas" et
    retourne le chemin ABSOLU du dossier demandé.
    S'il y a eu une exception, renvoyez explicitement un "None".
    :param folder_path: String représentant un chemin relatif
    (vers un dossier) par rapport au
    dossier courant
    :return: Renvoie un tableau de strings qui sont les logs
    contenant les logs ou None en cas d’erreur
    """
    try:
        logs = []
        with os.scandir(folder_path) as scan_iterator:
            for elem in scan_iterator:
                if elem.is_file():
                    log = load_log_from_file(elem.path)
                    if log is not None:
                        logs.extend(log)
        return logs
    except FileNotFoundError:
        print("Le chemin du dossier n'existe pas:",os.path.abspath(folder_path))
    except:
        return None

def get_folders_and_subfolders(folder_path):
    """
    La fonction renvoie une liste de chemins relatifs avec le chemin
    folder_path et ses sous-dossiers.
    La fonction NE peut PAS lancer d’erreur. Si le chemin n'existe pas, la
    fonction affiche "Le chemin n'existe pas" et donne le chemin ABSOLU du
    dossier demandé.
    S'il y a eu une exception, renvoyez explicitement un "None".
    :param folder_path: String représentant le chemin relatif vers le
    dossier cible
    :return: une liste de chemins relatifs avec le chemin folder_path et
    ses sous-dossiers
    """
    try:
        dossiers = []
        dossiers.append(folder_path)
        with os.scandir(folder_path) as folderlist:
            for elem in folderlist:
                print(folderlist)
                if elem.is_dir():
                    if isinstance(elem.path, str) is True:
                        dossiers.append(elem.path)
                    if isinstance(get_folders_and_subfolders(elem.path), str) is True:
                        dossiers.append(get_folders_and_subfolders(elem.path))
        return dossiers

    except FileNotFoundError:
        print("Le chemin du dossier n'existe pas:",os.path.abspath(folder_path))
    except:
        return None

def load(path_folder):
    """
    La fonction renvoie un tableau de logs à partir des fichiers
    dans le dossier (obtenu via le chemin relatif) et les sousdossiers de ce dossier.
    :param path_folder: String représentant le chemin relatif
    vers un dossier
    :return: Renvoie un tableau de string contenant les logs
    """
    try:
        logs = []
        dossiers = get_folders_and_subfolders(path_folder)

        for directories in dossiers:
            logs.extend(load_logs_from_folder(directories))
        return logs
    except:
        return None

available_choices = {
    1 : "Affiche les logs d’un programme",
    2 : "Charger un autre dossier contenant des fichiers de logs (anciens logs = supprimés)",
    9 : "Termine le programme"
}
def menu(available_choices):
    """
    Affiche un menu et demande à l'utilisateur de taper un
    nombre correspondant à l'un des choix.
    La fonction repose la question tant que l'utilisateur
    n'entre pas un nombre parmi les choix possibles.
    :param available_choices: Un dictionnaire où les clés sont
    des nombres et les valeurs sont du texte.
    :return: Renvoie un entier correspond au choix de
    l'utilisateur.
    """

    for key in available_choices.keys():
        print(f"Choix {key} : {available_choices[key]}")
    choix = input("Que voulez-vous faire ?")
    while choix not in ["1","2","9"]:
        if choix.isnumeric() is True:
            choix = input("Que voulez-vous faire ?")
        else:
            print("Entrez un entier")
            choix = input("Que voulez-vous faire ?")
    return int(choix)

def main():
    """
    Fonction principale du programme qui permet d'afficher le
    menu avec les différents choix possibles ainsi que la gestion de
    ses choix.
    :return: None
    """
    choix = menu(available_choices)
    logs = LogManager(logs = None)
    while choix != 9:
        if choix == 1:
            program = str(input("les logs de quel programme voulez-vous ?"))
            searchlogs = logs.search_logs(program)
            print(searchlogs)
            choix = menu(available_choices)
        elif choix == 2:
            logs.clear()
            folder = input("Quel autre dossier contenant des logs, voulez-vous charger ?")
            logs.add_logs(load_logs_from_folder(folder))
            choix = menu(available_choices)
    if choix == 9:
        return

if __name__ == "__main__":
    main()
