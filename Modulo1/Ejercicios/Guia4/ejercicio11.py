word = input("Ingresá una palabra: ")
last_character_index = len(word) - 1
for i in range(last_character_index, -1, -1):
    print(word[i])
