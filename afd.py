#!/usr/bin/envpython3
# coding: utf-8

import sys
import re

def main():
    if len(sys.argv) < 2:
        return print("Parâmetros Inválidos")
    else:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            f = f.read().splitlines()

        #for x in f:
        #    print(x)


        f[2] = re.sub(r'\(|\)|\,','',f[2])

        f[2] = f[2].split(' ')
        f[2] = [tuple(i) for i in f[2]]
        f[4] = f[4].split(' ')

        if(validate(f,input("Entrada: "))):
            return print("Deu bom")
        else:
            return print("Deu ruim")

def validate(f, word):
    if check_automaton(f):
        print("Automato Valido!")
        if(recognition(f[2],word,f[3],f[4])):
            return True

def recognition(t, word, inital, final):
    #print("Estado atual -> simbolo lido -> Estado alcancado")
    w = list(word)
    state = inital
    for c in w:
        flag = 0
        for x in t:
            if state == x[0] and c == x[1]:
                print(x[0],'->',x[1],'->',x[2])
                state = x[2]
                flag = 1
                break;
        if flag == 0:
            print('Simbolo \'', c, '\' não era esperado')
            return False
    #print(state,final)
    if state in final:
        return True
    return False

def check_automaton(f):
    if(is_afd(f[2]) and states(f[0],f[2],f[3],f[4])):
        return True

def check_definition(arg):
    pass

def is_afd(t):
    for i, x in enumerate(t):
        for j, y in enumerate(t):
            if i != j and x[0] == y[0] and x[1] == y[1] and x[2] != y[2]:
                return False
    return True

def states(s,t,q0,f):
    if q0 in s:
        for x in t:
            if not x[0] in s:
                print("Estado", x[0], "é invalido")
                return False
            if not x[2] in s:
                print("Estado", x[2], "é invalido")
                return False
    for x in f:
        if not x in s:
            print("Estado", x, "é invalido")
            return False

    return True

if __name__ == "__main__":
    main()
