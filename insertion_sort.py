import random
import time

def sort(v):
    i = 1
    while i < len(v):
        tempo = v[i]
        trocou = False
        j = i - 1
        while j >= 0 and v[j] > tempo:
            v[j+1] = v[j]
            trocou = True
            j -= 1

        if trocou:
            v[j+1] = tempo

        i += 1

vetor = list(range(0, 9999))
random.shuffle(vetor)

print(vetor)

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