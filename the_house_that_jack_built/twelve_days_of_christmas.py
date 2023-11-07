# twelve_days_of_christmas.py
# m.saunby@exeter.ac.uk
# 03 November 2023

# Dictionary of unique lines in the song.
# Could use a list instead with index replacing keys. 
lines_dict = {
            0: 'On the first day of Christmas my true love sent to me',
            1: 'A partridge in a pear tree',
            2: 'On the second day of Christmas my true love sent to me',
            3: 'Two turtle doves,',
            4: 'And a partridge in a pear tree.',
            5: 'On the third day of Christmas my true love sent to me',
            6: 'Three French hens,',
            7: 'On the fourth day of Christmas my true love sent to me',
            8: 'Four calling birds,',
            9: 'On the fifth day of Christmas my true love sent to me',
            10: 'Five gold rings,',
            11: 'On the sixth day of Christmas my true love sent to me',
            12: 'Six geese a-laying,',
            13: 'On the seventh day of Christmas my true love sent to me',
            14: 'Seven swans a-swimming,',
            15: 'On the eighth day of Christmas my true love sent to me',
            16: 'Eight maids a-milking,',
            17: 'On the ninth day of Christmas my true love sent to me',
            18: 'Nine ladies dancing,',
            19: 'On the tenth day of Christmas my true love sent to me',
            20: 'Ten lords a-leaping,',
            21: 'On the eleventh day of Christmas my true love sent to me',
            22: 'Eleven pipers piping,',
            23: 'On the twelfth day of Christmas my true love sent to me',
            24: 'Twelve drummers drumming,',
        }

# The verses with lines replaced by keys (for lines_dict)
verses = [
            [0, 1], 
            [2, 3, 4],
            [5, 6, 3, 4],
            [7, 8, 6, 3, 4],
            [9, 10, 8, 6, 3, 4],
            [11, 12, 10, 8, 6, 3, 4],
            [13, 14, 12, 10, 8, 6, 3, 4],
            [15, 16, 14, 12, 10, 8, 6, 3, 4],
            [17, 18, 16, 14, 12, 10, 8, 6, 3, 4],
            [19, 20, 18, 16, 14, 12, 10, 8, 6, 3, 4],
            [21, 22, 20, 18, 16, 14, 12, 10, 8, 6, 3, 4],
            [23, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 3, 4]
        ]

# Print all verses
for verse in verses:
    for line in verse:
        print(lines_dict[line])
    # Print a blank line after each verse
    print()
