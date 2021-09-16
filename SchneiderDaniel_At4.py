def full_name(nom:str, prenom:str):

    message = nom.upper() + " " + prenom.capitalize()
    return(message)

print(full_name("schneider", "daniel"))

def is_mail(str_arg:str):
    tuple = []
    