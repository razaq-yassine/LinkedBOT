import colorama
import random

def bannerTop():
    banner = '''
    __    _       __            ______  ____  ______
   / /   (_)___  / /_____  ____/ / __ )/ __ \/_  __/
  / /   / / __ \/ //_/ _ \/ __  / __  / / / / / /   
 / /___/ / / / / ,< /  __/ /_/ / /_/ / /_/ / / /    
/_____/_/_/ /_/_/|_|\___/\__,_/_____/\____/ /_/     
                                                    
                                                                               
                                                                               
'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET', 'RED']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color.upper() not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]

    return ''.join(colored_chars)