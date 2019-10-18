import json
import datetime


def create_header(authors_list, loc="Paris"):
    """Creates the header text.
    
    Parameters
    ----------
    authors_list: a list of dict
        each dictionnary should contain "first" and "last" keys
    loc : str, optional, default "Paris"
        The localistaion from where the report is emitted
    
    Returns
    -------
    header_text : str
        The header text
    
    """
    
    today = datetime.date.today()
    date_string = today.strftime(f'{loc}, le %d/%m/%Y')
    author_strings = [date_string, "### Authors", "\n"]
    
    
    for author in authors_list:
        first = author.get("firstname", "")
        last = author.get("lastname", "")
        if not last:
            print('No value for last')
        author_string = f'- {first} {last}'

        author_strings.append(author_string)
    return "\n".join(author_strings)







    # Fonction qui ouvre le fichier JSON, et afficher create_header avec le contenu du JSON
# appel fonction create_header
# retourne le contenu du JSON
def header_from_json(json_path):
    # appel du fichier

    """Creates the header depuis une fichier json.
       Ouvre un fichier json


    """

    with open(json_path, "r") as fh:
        authors = json.load(fh)
    
    result = create_header(authors)
        
    return result

#ci-dessous code pour tester la fonction
path = r"C:\Users\thierry.clavier\Documents\reporter\data\authors.json" # on met r devant le chemin pour indiquer qu'il s'agit d'un chemin windows complet         
header_from_json(path)