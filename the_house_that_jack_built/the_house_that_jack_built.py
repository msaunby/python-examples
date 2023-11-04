# the_house_that_jack_built.py
# m.saunby@exeter.ac.uk
# 03 November 2023

# Dictionary of unique lines in the poem.
# Could use a list instead with index replacing keys. 
lines_dict = {
            0: 'This is the house that Jack built.',
            1: 'This is the malt',
            2: 'That lay in the house that Jack built.',
            3: 'This is the rat',
            4: 'That ate the malt',
            5: 'This is the cat',
            6: 'That killed the rat',
            7: 'This is the dog',
            8: 'That worried the cat',
            9: 'This is the cow with the crumpled horn',
            10: 'That tossed the dog',
            11: 'This is the maiden all forlorn',
            12: 'That milked the cow with the crumpled horn',
            13: 'This is the man all tattered and torn',
            14: 'That kissed the maiden all forlorn',
            15: 'This is the priest all shaven and shorn',
            16: 'That married the man all tattered and torn',
            17: 'This is the cock that crowed in the morn',
            18: 'That woke the priest all shaven and shorn',
            19: 'This is the farmer sowing his corn',
            20: 'That kept the cock that crowed in the morn',
            21: 'This is the horse and the hound and the horn',
            22: 'That belonged to the farmer sowing his corn'
        }

# The verses with lines replaced by keys (for lines_dict)
verses = [
            [0], 
            [1, 2],
            [3, 4, 2],
            [5, 6, 4, 2],
            [7, 8, 6, 4, 2],
            [9, 10, 8, 6, 4, 2],
            [11, 12, 10, 8, 6, 4, 2],
            [13, 14, 12, 10, 8, 6, 4, 2],
            [15, 16, 14, 12, 10, 8, 6, 4, 2],
            [17, 18, 16, 14, 12, 10, 8, 6, 4, 2],
            [19, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2],
            [21, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
        ]

# Print all verses
for verse in verses:
    for line in verse:
        print(lines_dict[line])
    # Print a blank line after each verse
    print()

print("========================")

# Print only the first and last verses
for verse in [verses[0], verses[-1]]:
    for line in verse:
        print(lines_dict[line])
    # Print a blank line after each verse
    print()