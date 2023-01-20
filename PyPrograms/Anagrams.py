from Clear import clear

clear()

def find_anagrams(arg):
    target = arg.split(" ")
    length = len(target)

    for i in range(0, length):
        for j in range(i+1, length):
            if sorted(target[i]) == sorted(target[j]):
                print(f"{target[i]} = {target[j]} ")




param = "race bear thing care keen trap tweet earth knee heart  neek tewt"
find_anagrams(param)