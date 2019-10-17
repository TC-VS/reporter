
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
        first = author.get("first", "")
        last = author.get("last", "")
        if not last:
            print('No value for last')
        author_string = f'- {first} {last}'

        author_strings.append(author_string)
    return "\n".join(author_strings)