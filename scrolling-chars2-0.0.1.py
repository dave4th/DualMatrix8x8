#!/usr/bin/python

import sys  # Potrei anche toglierla se non la uso
import spidev
import time

max7221sx=spidev.SpiDev(0,0)
max7221dx=spidev.SpiDev(0,1)

#spival=max7221sx.readbytes(1)
#print("Valore attuale:", spival)

#for arg in sys.argv:
#    print arg

# Shutdown (Spegne)
max7221sx.writebytes([0x0C,0x00])
max7221dx.writebytes([0x0C,0x00])
#time.sleep(1)
# Normal operation (Accende)
max7221sx.writebytes([0x0C,0x01])
max7221dx.writebytes([0x0C,0x01])

# Test Mode ON
#max7221sx.writebytes([0x0F,0x01])
#time.sleep(1)
# Test Mode OFF
#max7221sx.writebytes([0x0F,0x00])

# Decode mode: No decode
max7221sx.writebytes([0x09,0x00])
max7221dx.writebytes([0x09,0x00])

# Scan limit (tutti)
max7221sx.writebytes([0x0B,0x07])
max7221dx.writebytes([0x0B,0x07])

# Intensity
max7221sx.writebytes([0x0A,0x07])
max7221dx.writebytes([0x0A,0x07])

# (Az)Zero matrix
for i in range(1,9):
    max7221sx.writebytes([0x0+i,0x00])
# Per azzeramento anche della seconda matrice (anche se drovbbe bastarne un solo in piu`, range fino a 10)
for i in range(1,9):
    max7221dx.writebytes([0x0+i,0x00])


# Caratteri

CharA = [   '00000',
            '01110',
            '10001',
            '10001',
            '11111',
            '10001',
            '10001',
            '10001']

CharB = [   '00000',
            '11110',
            '10001',
            '10001',
            '11110',
            '10001',
            '10001',
            '11110']

CharC = [   '00000',
            '01110',
            '10001',
            '10000',
            '10000',
            '10000',
            '10001',
            '01110']

CharD = [   '00000',
            '11100',
            '10010',
            '10001',
            '10001',
            '10001',
            '10010',
            '11100']

CharE = [   '00000',
            '11111',
            '10000',
            '10000',
            '11110',
            '10000',
            '10000',
            '11111']

CharF = [   '00000',
            '11111',
            '10000',
            '10000',
            '11110',
            '10000',
            '10000',
            '10000']

CharG = [   '00000',
            '01111',
            '10000',
            '10000',
            '10011',
            '10001',
            '10001',
            '01110']

CharH = [   '00000',
            '10001',
            '10001',
            '10001',
            '11111',
            '10001',
            '10001',
            '10001']

CharI = [   '0',
            '1',
            '1',
            '1',
            '1',
            '1',
            '1',
            '1']

CharJ = [   '00000',
            '00001',
            '00001',
            '00001',
            '00001',
            '00001',
            '10001',
            '01110']

CharK = [   '00000',
            '10001',
            '10010',
            '10100',
            '11100',
            '10010',
            '10001',
            '10001']

CharL = [   '00000',
            '10000',
            '10000',
            '10000',
            '10000',
            '10000',
            '10000',
            '11111']

CharM = [   '00000',
            '10001',
            '11011',
            '10101',
            '10001',
            '10001',
            '10001',
            '10001']

CharN = [   '00000',
            '10001',
            '11001',
            '10101',
            '10011',
            '10001',
            '10001',
            '10001']

CharO = [   '00000',
            '01110',
            '10001',
            '10001',
            '10001',
            '10001',
            '10001',
            '01110']

CharP = [   '00000',
            '11110',
            '10001',
            '10001',
            '11110',
            '10000',
            '10000',
            '10000']

CharQ = [   '00000',
            '01110',
            '10001',
            '10001',
            '10001',
            '10101',
            '10011',
            '01111']

CharR = [   '00000',
            '11110',
            '10001',
            '10001',
            '11110',
            '10010',
            '10001',
            '10001']

CharS = [   '00000',
            '01110',
            '10001',
            '10000',
            '01110',
            '00001',
            '10001',
            '01110']

CharT = [   '00000',
            '11111',
            '00100',
            '00100',
            '00100',
            '00100',
            '00100',
            '00100']

CharU = [   '00000',
            '10001',
            '10001',
            '10001',
            '10001',
            '10001',
            '10001',
            '01110']

CharV = [   '00000',
            '10001',
            '10001',
            '10001',
            '10001',
            '10001',
            '01010',
            '00100']

CharW = [   '00000',
            '10001',
            '10001',
            '10001',
            '10001',
            '10101',
            '10101',
            '01010']

CharX = [   '00000',
            '10001',
            '10001',
            '01010',
            '00100',
            '01010',
            '10001',
            '10001']

CharY = [   '00000',
            '10001',
            '10001',
            '10001',
            '01010',
            '00100',
            '00100',
            '00100']

CharZ = [   '00000',
            '11111',
            '00001',
            '00010',
            '00100',
            '01000',
            '10000',
            '11111']

Chara = [   '00000',
            '00000',
            '11110',
            '00001',
            '01111',
            '10001',
            '01111',
            '00000']

Charb = [   '00000',
            '10000',
            '10000',
            '11110',
            '10001',
            '10001',
            '11110',
            '00000']

Charc = [   '00000',
            '00000',
            '01111',
            '10000',
            '10000',
            '10000',
            '01111',
            '00000']

Chard = [   '00000',
            '00001',
            '00001',
            '01111',
            '10001',
            '10001',
            '01111',
            '00000']

Chare = [   '00000',
            '00000',
            '01110',
            '10001',
            '11111',
            '10000',
            '01111',
            '00000']

Charf = [   '0000',
            '0011',
            '0100',
            '1110',
            '0100',
            '0100',
            '0100',
            '0000']

Charg = [   '00000',
            '00000',
            '01110',
            '10001',
            '10001',
            '01111',
            '00001',
            '01110']

Charh = [   '00000',
            '10000',
            '10000',
            '10110',
            '11001',
            '10001',
            '10001',
            '00000']

Chari = [   '0',
            '1',
            '0',
            '1',
            '1',
            '1',
            '1',
            '0']

Charj = [   '00000',
            '00001',
            '00000',
            '00001',
            '00001',
            '00001',
            '10001',
            '01110']

Chark = [   '0000',
            '1000',
            '1001',
            '1010',
            '1100',
            '1010',
            '1001',
            '0000']

Charl = [   '0',
            '1',
            '1',
            '1',
            '1',
            '1',
            '1',
            '0']

Charm = [   '00000',
            '00000',
            '01010',
            '10101',
            '10101',
            '10001',
            '10001',
            '00000']

Charn = [   '00000',
            '00000',
            '10110',
            '11001',
            '10001',
            '10001',
            '10001',
            '00000']

Charo = [   '00000',
            '00000',
            '01110',
            '10001',
            '10001',
            '10001',
            '01110',
            '00000']

Charp = [   '00000',
            '00000',
            '11110',
            '10001',
            '10001',
            '11110',
            '10000',
            '10000']

Charq = [   '00000',
            '00000',
            '01111',
            '10001',
            '10001',
            '01111',
            '00001',
            '00001']

Charr = [   '0000',
            '0000',
            '1011',
            '1100',
            '1000',
            '1000',
            '1000',
            '0000']

Chars = [   '00000',
            '00000',
            '01111',
            '10000',
            '01110',
            '00001',
            '11110',
            '00000']

Chart = [   '0000',
            '0100',
            '1111',
            '0100',
            '0100',
            '0100',
            '0011',
            '0000']

Charu = [   '00000',
            '00000',
            '10001',
            '10001',
            '10001',
            '10001',
            '01110',
            '00000']

Charv = [   '00000',
            '00000',
            '10001',
            '10001',
            '10001',
            '01010',
            '00100',
            '00000']

Charw = [   '00000',
            '00000',
            '10001',
            '10001',
            '10101',
            '10101',
            '01010',
            '00000']

Charx = [   '00000',
            '00000',
            '10001',
            '01010',
            '00100',
            '01010',
            '10001',
            '00000']

Chary = [   '00000',
            '00000',
            '10001',
            '10001',
            '01111',
            '00001',
            '10001',
            '01110']

Charz = [   '00000',
            '00000',
            '11111',
            '00010',
            '00100',
            '01000',
            '11111',
            '00000']


Char0 = [   '00000',
            '01110',
            '10001',
            '10011',
            '10101',
            '11001',
            '10001',
            '01110']

Char1 = [   '000',
            '001',
            '011',
            '101',
            '001',
            '001',
            '001',
            '001']

Char2 = [   '00000',
            '01110',
            '10001',
            '00010',
            '00100',
            '01000',
            '10000',
            '11111']

Char3 = [   '00000',
            '01110',
            '10001',
            '00001',
            '00110',
            '00001',
            '10001',
            '01110']

Char4 = [   '00000',
            '00001',
            '00011',
            '00101',
            '01001',
            '11111',
            '00001',
            '00001']

Char5 = [   '00000',
            '11110',
            '10000',
            '10000',
            '11110',
            '00001',
            '10001',
            '01110']

Char6 = [   '00000',
            '01110',
            '10001',
            '10000',
            '11110',
            '10001',
            '10001',
            '01110']

Char7 = [   '00000',
            '11111',
            '00001',
            '00010',
            '00100',
            '01000',
            '10000',
            '10000']

Char8 = [   '00000',
            '01110',
            '10001',
            '10001',
            '01110',
            '10001',
            '10001',
            '01110']

Char9 = [   '00000',
            '01110',
            '10001',
            '10001',
            '01111',
            '00001',
            '10001',
            '01110']

CharDot = [ '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '1',
            '0']

CharPipe = [  '1',
              '1',
              '1',
              '1',
              '1',
              '1',
              '1',
              '1']

CharEsclamativo = [   '0',
                      '1',
                      '1',
                      '1',
                      '1',
                      '0',
                      '1',
                      '0']

CharSlash = [   '000000',
                '000001',
                '000010',
                '000100',
                '001000',
                '010000',
                '100000',
                '000000']

CharBackslash = [   '000000',
                    '100000',
                    '010000',
                    '001000',
                    '000100',
                    '000010',
                    '000001',
                    '000000']

CharUnderscore = [  '00000',
                    '00000',
                    '00000',
                    '00000',
                    '00000',
                    '00000',
                    '00000',
                    '11111']

CharMeno = [  '00000',
              '00000',
              '00000',
              '00000',
              '11111',
              '00000',
              '00000',
              '00000']

CharPiu = [ '00000',
            '00000',
            '00100',
            '00100',
            '11111',
            '00100',
            '00100',
            '00000']

CharSpace = [   '00000000',
                '00000000',
                '00000000',
                '00000000',
                '00000000',
                '00000000',
                '00000000',
                '00000000']

# Questa la devo fare di grandezza della matrice, potrei pure
# farla 8x8 .. cosi` faccio prima o no ?
# Comunque sarebbe riutilizzabile per altro.
Clear8x8Letter = [  '00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '00000000']

# La piena deve sempre contenere qualcosa ?
# Comunque, appena riempita la vuota, riempio questa per poter svuotare la vuota
# (Questa fondamentalmente contiene i precedenti vaolri e non puo` mai essere vuota)
Piena8x8Letter = Clear8x8Letter[:]

# Mi sa che questa sara` da svuotare ad ogni ciclo, probabilmente e` quella da stampare
Matrice8x8LetterSX = [ "", "", "", "", "", "", "", ""]
Matrice8x8LetterDX = [ "", "", "", "", "", "", "", ""]

Matrice8x8LetterSX = Clear8x8Letter[:]
Matrice8x8LetterDX = Clear8x8Letter[:]


# Parola da stampare
Parola="MAX7221 .. .. Ok! Ora funziona.    Non so quante lettere ho messo ne\` quanti caratteri speciali .."
#Parola="+ Linux Day 2015 - RELug - Reggio Emilia Linux User Group +  "
# Tempo di ritardo dello "scroll"
TimeScroll=.3

# Programma
for Lettera in Parola:
    if Lettera == 'A':
        Second8x8Letter = CharA[:]
    elif Lettera == 'B':
        Second8x8Letter = CharB[:]
    elif Lettera == 'C':
        Second8x8Letter = CharC[:]
    elif Lettera == 'D':
        Second8x8Letter = CharD[:]
    elif Lettera == 'E':
        Second8x8Letter = CharE[:]
    elif Lettera == 'F':
        Second8x8Letter = CharF[:]
    elif Lettera == 'G':
        Second8x8Letter = CharG[:]
    elif Lettera == 'H':
        Second8x8Letter = CharH[:]
    elif Lettera == 'I':
        Second8x8Letter = CharI[:]
    elif Lettera == 'J':
        Second8x8Letter = CharJ[:]
    elif Lettera == 'K':
        Second8x8Letter = CharK[:]
    elif Lettera == 'L':
        Second8x8Letter = CharL[:]
    elif Lettera == 'M':
        Second8x8Letter = CharM[:]
    elif Lettera == 'N':
        Second8x8Letter = CharN[:]
    elif Lettera == 'O':
        Second8x8Letter = CharO[:]
    elif Lettera == 'P':
        Second8x8Letter = CharP[:]
    elif Lettera == 'Q':
        Second8x8Letter = CharQ[:]
    elif Lettera == 'R':
        Second8x8Letter = CharR[:]
    elif Lettera == 'S':
        Second8x8Letter = CharS[:]
    elif Lettera == 'T':
        Second8x8Letter = CharT[:]
    elif Lettera == 'U':
        Second8x8Letter = CharU[:]
    elif Lettera == 'V':
        Second8x8Letter = CharV[:]
    elif Lettera == 'W':
        Second8x8Letter = CharW[:]
    elif Lettera == 'X':
        Second8x8Letter = CharX[:]
    elif Lettera == 'Y':
        Second8x8Letter = CharY[:]
    elif Lettera == 'Z':
        Second8x8Letter = CharZ[:]
    elif Lettera == 'a':
        Second8x8Letter = Chara[:]
    elif Lettera == 'b':
        Second8x8Letter = Charb[:]
    elif Lettera == 'c':
        Second8x8Letter = Charc[:]
    elif Lettera == 'd':
        Second8x8Letter = Chard[:]
    elif Lettera == 'e':
        Second8x8Letter = Chare[:]
    elif Lettera == 'f':
        Second8x8Letter = Charf[:]
    elif Lettera == 'g':
        Second8x8Letter = Charg[:]
    elif Lettera == 'h':
        Second8x8Letter = Charh[:]
    elif Lettera == 'i':
        Second8x8Letter = Chari[:]
    elif Lettera == 'j':
        Second8x8Letter = Charj[:]
    elif Lettera == 'k':
        Second8x8Letter = Chark[:]
    elif Lettera == 'l':
        Second8x8Letter = Charl[:]
    elif Lettera == 'm':
        Second8x8Letter = Charm[:]
    elif Lettera == 'n':
        Second8x8Letter = Charn[:]
    elif Lettera == 'o':
        Second8x8Letter = Charo[:]
    elif Lettera == 'p':
        Second8x8Letter = Charp[:]
    elif Lettera == 'q':
        Second8x8Letter = Charq[:]
    elif Lettera == 'r':
        Second8x8Letter = Charr[:]
    elif Lettera == 's':
        Second8x8Letter = Chars[:]
    elif Lettera == 't':
        Second8x8Letter = Chart[:]
    elif Lettera == 'u':
        Second8x8Letter = Charu[:]
    elif Lettera == 'v':
        Second8x8Letter = Charv[:]
    elif Lettera == 'w':
        Second8x8Letter = Charw[:]
    elif Lettera == 'x':
        Second8x8Letter = Charx[:]
    elif Lettera == 'y':
        Second8x8Letter = Chary[:]
    elif Lettera == 'z':
        Second8x8Letter = Charz[:]
    elif Lettera == '0':
        Second8x8Letter = Char0[:]
    elif Lettera == '1':
        Second8x8Letter = Char1[:]
    elif Lettera == '2':
        Second8x8Letter = Char2[:]
    elif Lettera == '3':
        Second8x8Letter = Char3[:]
    elif Lettera == '4':
        Second8x8Letter = Char4[:]
    elif Lettera == '5':
        Second8x8Letter = Char5[:]
    elif Lettera == '6':
        Second8x8Letter = Char6[:]
    elif Lettera == '7':
        Second8x8Letter = Char7[:]
    elif Lettera == '8':
        Second8x8Letter = Char8[:]
    elif Lettera == '9':
        Second8x8Letter = Char9[:]
    elif Lettera == '.':
        Second8x8Letter = CharDot[:]
    elif Lettera == '|':
        Second8x8Letter = CharPipe[:]
    elif Lettera == '_':
        Second8x8Letter = CharUnderscore[:]
    elif Lettera == '!':
        Second8x8Letter = CharEsclamativo[:]
    elif Lettera == '/':
        Second8x8Letter = CharSlash[:]
    elif Lettera == '\\':
        Second8x8Letter = CharBackslash[:]
    elif Lettera == '-':
        Second8x8Letter = CharMeno[:]
    elif Lettera == '+':
        Second8x8Letter = CharPiu[:]
    elif Lettera == ' ':
        Second8x8Letter = CharSpace[:]
    else:
        Second8x8Letter = CharSpace[:]

    # Calcolo lunghezza lettere
    Lunghezza = len(Second8x8Letter[0])
    # Il primo giro prendo le variabili dalla prima riga prima colonna e le scarto, riempiendo
    # contemporaneamente l'ultima colonna con la prima della variabile successiva, via cosi`
    # fino ad esaurimento della seconda lettera, che poi preleva una lettera successiva e riparte
    # finche` non sono terminate. (Non so semi sono spiegato).
    for j in range(1,Lunghezza + 1):	# Questo e` lo scan della colonna
        for i in range(8):	# Questo e` lo scan della riga in realta` da 0 a 7
            Piena8x8Letter = Matrice8x8LetterDX[:]
            # [1:] Scarta la prima lettera, [j-1:j] per prelevare una sola lettera nel range
            Matrice8x8LetterSX[i] = Matrice8x8LetterSX[i][1:]+Matrice8x8LetterDX[i][0]
            Matrice8x8LetterDX[i] = Piena8x8Letter[i][1:]+Second8x8Letter[i][j-1:j]
            # [::-1] Inverte la stringa, l'ho trovato e l'ho preso per buono, visto che funziona ;)
            max7221sx.writebytes([i+1,int(Matrice8x8LetterSX[i][::-1],2)])
            max7221dx.writebytes([i+1,int(Matrice8x8LetterDX[i][::-1],2)])
#            Piena8x8Letter = Matrice8x8LetterDX[:] # Ho tirato quasi a caso, spostandola da questa posizione all'inizio, perche` ho visto che secondo me stampava un passaggio in piu`
        time.sleep(TimeScroll)
    for i in range(8):	# Questo e` lo scan della riga in realta` da 0 a 7
        # [1:] Scarta la prima lettera, [j-1:j] per prelevare una sola lettera nel range
        Matrice8x8LetterSX[i] = Matrice8x8LetterSX[i][1:]+Matrice8x8LetterDX[i][0]
        Matrice8x8LetterDX[i] = Matrice8x8LetterDX[i][1:]+ "0"
        # [::-1] Inverte la stringa, l'ho trovato e l'ho preso per buono, visto che funziona ;)
        max7221sx.writebytes([i+1,int(Matrice8x8LetterSX[i][::-1],2)])
        max7221dx.writebytes([i+1,int(Matrice8x8LetterDX[i][::-1],2)])
    # Come scrivevo .. questa deve sempre essere svuotata prima di ricominciare
    Piena8x8Letter = Clear8x8Letter[:]
    time.sleep(TimeScroll)
#    for i in range(8):	# Questo e` lo scan della riga in realta` da 0 a 7
        # [1:] Scarta la prima lettera, [j-1:j] per prelevare una sola lettera nel range
#        Matrice8x8LetterSX[i] = Matrice8x8LetterSX[i][1:]+Matrice8x8LetterDX[i][0]
#        Matrice8x8LetterDX[i] = Matrice8x8LetterDX[i][1:]+ "0"
        # [::-1] Inverte la stringa, l'ho trovato e l'ho preso per buono, visto che funziona ;)
#        max7221sx.writebytes([i+1,int(Matrice8x8LetterSX[i][::-1],2)])
#        max7221dx.writebytes([i+1,int(Matrice8x8LetterDX[i][::-1],2)])
