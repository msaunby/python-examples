
poem_dict = {}
verses = []

with open("poem.txt") as poem:
    line_no = 0
    verse_no = 0
    verse = []
    for line in poem:
        line = line.strip()
        if not line:
            verses.append(verse)
            verse_no += 1
            verse = []
            continue
        verse.append(line)
        if line in poem_dict:
            poem_dict[line].append(line_no)
        else:
            poem_dict[line] = [line_no]
        line_no += 1

lines_dict = {}
lines_rev = {}
index_dict = {}

lines_ref = 0
for (k,v) in poem_dict.items():
    lines_dict[lines_ref] = k
    lines_rev[k] = lines_ref
    for n in v:
         index_dict[n] = lines_ref
    lines_ref += 1

last_line = sorted(index_dict.keys())[-1]+1

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

 