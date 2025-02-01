from random import choice, randint


#ici y'a les réponses pour random motiv
reponses = ["""1""",
            
            """2""",
            
            """3""",
            
            """4""",
            
            '5',
            
            '6',
            
            '7',
            
            '8',
            
            '9',
            
            '10']


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'wtf'
    elif '!motive' in lowered:
        
        #Chiffre aléatoire pour dire un truc
        number = randint(0, 9)
        return reponses[number]
