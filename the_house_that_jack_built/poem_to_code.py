# Read a poem with repeated lines and output
# a Python program that recreate the poem.

poem_dict = {}
verses = []

with open("poem.txt") as poem:
    verse = []
    lines = poem.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            verses.append(verse)
            verse = []
            continue
        verse.append(line)
        # Use a dict to store unique lines
        poem_dict[line] = True
    verses.append(verse)


# Give each line a unique index. These then
# replace the lines in the verses list.
lines_dict = {}
lines_rev = {}
lines_ref = 0

for k in poem_dict.keys():
    lines_dict[lines_ref] = k
    lines_rev[k] = lines_ref
    lines_ref += 1

for v in range(len(verses)):
    nv = []
    for l in verses[v]:
        nv.append(lines_rev[l])
    verses[v] = nv

print(f"lines_dict = {lines_dict}")
print()
print(f"verses = {verses}")

print("""
for verse in verses:
    for line in verse:
        print(lines_dict[line])
    print()
""")

 