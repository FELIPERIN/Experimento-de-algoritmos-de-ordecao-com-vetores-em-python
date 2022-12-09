import random
import time

def sort(v):

    h = len(v) // 2 #distancia
    while h > 0:
        i = h
        while i < len(v):
            tempo = v[i]
            trocou = False
            j = i - h
            while j >= 0 and v[j] > tempo:
                v[j+h] = v[j]
                trocou = True
                j -= h

            if trocou:
                v[j+h] = tempo

            i += 1

        h = h // 2

vetor = list(range(0, 10000))
random.shuffle(vetor)

#print(vetor)

print("Realizando ordenações...")
print("")
antes1 = time.time()
sort(vetor)
depois1 = time.time()
total1 = (depois1 - antes1)*1000
print("1... %0.2f ms" % total1)

random.shuffle(vetor)
antes2 = time.time()
sort(vetor)
depois2 = time.time()
total2 = (depois2 - antes2)*1000
print("2... %0.2f ms" % total2)

random.shuffle(vetor)
antes3 = time.time()
sort(vetor)
depois3 = time.time()
total3 = (depois3 - antes3)*1000
print("3... %0.2f ms" % total3)

totalf = ((total1 + total2 + total3) / 3)

print("")
print ("Ta... Da!")
time.sleep(1)
print ("A ordenação demorou %0.2f ms em média de três execuções." % totalf)

input("Pressione ENTER para finalizar.")