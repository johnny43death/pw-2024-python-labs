def reversor(prompt):
    promptlist = prompt.split()
    reversedprompt = []

    print(promptlist)
    promptlist.sort()
    for i in range(len(promptlist)):
        reversedprompt.append((promptlist[i][::-1]))
    return print(reversedprompt)

if __name__ == "__main__":
    sentence = str(input("Podaj zdanie: "))
    reversor(sentence)