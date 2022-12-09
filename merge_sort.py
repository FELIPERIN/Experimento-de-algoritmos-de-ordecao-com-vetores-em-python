import random
import time

def sort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        sort(lefthalf)
        sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

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