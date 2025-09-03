from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
from typing import *
from collections import *

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the number of beats for each note
    beats = []
    
    # Iterate over each note in the list
    for note in notes:
        if note == 'o':
            # If the note is a whole note, append 4 to the beats list
            beats.append(4)
        elif note == 'o|':
            # If the note is a half note, append 2 to the beats list
            beats.append(2)
        elif note == '.|':
            # If the note is a quarter note, append 1 to the beats list
            beats.append(1)
    
    # Return the list of beats
    return beats

# Test the function with the provided example