import sys
import random

def CFG():
    V = set() #nterminale
    Sigma = set() #terminale
    R = {} #production rules
    S = '' #start
    #$ - epsilon

    input = sys.argv[1]
    
    with open(input, "r") as f:
        for line in f:
            prod = line.strip().split("->")
            NT = prod[0].strip()
            V.add(NT)
            if S == '':
                S = NT
            aux = prod[1].strip().split("|")
            for part in aux:
                part = part.strip()
                if NT not in R:
                    R[NT] = []
                R[NT].append(part)
                for ch in part:
                    if ch >= 'a' and ch <= 'z':
                        Sigma.add(ch)

    return V, Sigma, R, S

def StringGen(V, R, S):
    word = S
    i = 0
    while i < len(word):
        if word[i] in V:
            rand = random.choice(R[word[i]])
            if rand == '$':
                rand = ''
            if len(word) - 1 + len(rand) > 9:
                break
            word = word[:i] + rand + word[i + 1:]
            i = 0
        else:
            i += 1
    for elem in V:
      word = word.replace(elem, '')
    return word

def Derivation(current_string, target, depth, V, R):
    if depth > 20:
        return None #opresc daca se ajunge la 20 pasi
    
    if current_string == target:
        for ch in current_string:
            if ch in V:
                return None
        return [current_string]
    
    for i in range(len(current_string)):
        symbol = current_string[i]
        if symbol in V: 
            for production in R[symbol]:
                if production == '$':
                    production = ''
                new_string = current_string[:i] + production + current_string[i+1:]
                result = Derivation(new_string, target, depth + 1, V, R)
                if result is not None:
                    return [current_string] + result 
    
    return None

def Membership(S, string, V, R):
    return Derivation(S, string, 0, V, R) is not None 

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Nu ai specificat niciun fisier pentru input")
    elif len(sys.argv) == 2:
        #Task 1. Define a CFG
        print("Test functia CFG:")
        V, Sigma, R, S = CFG()
        #print(CFG())

        #Task 2. String Generator
        print("Test functia StringGen:")
        strings = []
        for i in range(10):
            string = StringGen(V, R, S)
            print(string)
            strings.append(string)

        #Task 3. Derivation
        print("Test functia Derivation:")
        target = random.choice(strings)
        rez = Derivation(S, target, 0, V, R)
        if rez is None:
            print("Nu se poate deriva")
        else:
            for step in rez:
                print(step)
                
        #Task 4. Membership Tester 
        print("Test functia Membership:")
        target = random.choice(strings)
        if Membership(S, target, V, R):
            print("Merge")
        else:
            print("Nu merge")

    else:
        print("Prea multe fisiere")

                
                


            

