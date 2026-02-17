characters = set(["hinako", "ayato", "raiden", "kaeya", "zhongli"])

game = "gta"

games = {"silent hill", "genshin impact"}

games.add("gta")

games.update("ghost of tsushima", "black myth wukong")

games.remove("gta")

games.discard("gta")

if game in games: 
    print("yes")
else: 
    print("no")

s = "tuppleware"

unique = set([])
duplicate = list([])

for i in s: 
    unique.update(i)
    duplicate.append(i)

# efficient solution: return len(unique) == len(s)
    
if len(unique) == len(duplicate):
        print(True)
elif len(s) == 0:
        print(True)
else: 
        print(False)

a = set(["controller"])
b = set(["control"])
c = frozenset(["controlling"])

union = b.symmetric_difference(b)

# print(union)

# mutual friend problem ez