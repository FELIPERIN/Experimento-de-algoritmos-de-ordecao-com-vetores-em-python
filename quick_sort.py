import random
import time


def sort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


normal_array = list(range(1, 10000))
random.shuffle(normal_array)

reversed_array = sorted(normal_array, reverse=True)
sorted_array = sorted(normal_array)

#print(normal_array)

print("Ordenando vetor de 10000 posições com números aleatórios...")
print("-" * 50)
antes1 = time.time()
sort(normal_array)
depois1 = time.time()
total1 = (depois1 - antes1)*1000
print("1... %0.2f ms" % total1)

random.shuffle(normal_array)
antes2 = time.time()
sort(normal_array)
depois2 = time.time()
total2 = (depois2 - antes2)*1000
print("2... %0.2f ms" % total2)

random.shuffle(normal_array)
antes3 = time.time()
sort(normal_array)
depois3 = time.time()
total3 = (depois3 - antes3)*1000
print("3... %0.2f ms" % total3)

totalf = ((total1 + total2 + total3) / 3)

print("")
print ("Ta... Da!")
time.sleep(1)
print ("A ordenação demorou %0.2f ms em média de três execuções." % totalf)
print("-" * 50)

print("Ordenando vetor de 10000 posições com números já ordenados em forma crescente...")
print("-" * 50)
antes1 = time.time()
#sort(sorted_array)
print("CRASH")
depois1 = time.time()
total1 = (depois1 - antes1)*1000
print("1... %0.2f ms" % total1)

antes2 = time.time()
#sort(sorted_array)
print("CRASH")
depois2 = time.time()
total2 = (depois2 - antes2)*1000
print("2... %0.2f ms" % total2)

antes3 = time.time()
#sort(sorted_array)
print("CRASH")
depois3 = time.time()
total3 = (depois3 - antes3)*1000
print("3... %0.2f ms" % total3)

totalf = ((total1 + total2 + total3) / 3)

print("")
print ("Ta... Da!")
time.sleep(1)
print ("A ordenação demorou %0.2f ms em média de três execuções." % totalf)
print("-" * 50)

print("Ordenando vetor de 10000 posições com números ordenados de forma decrescente...")
print("-" * 50)
antes1 = time.time()
#sort(reversed_array)
print("CRASH")
depois1 = time.time()
total1 = (depois1 - antes1)*1000
print("1... %0.2f ms" % total1)

reversed_array = sorted(normal_array, reverse=True)
antes2 = time.time()
#sort(reversed_array)
print("CRASH")
depois2 = time.time()
total2 = (depois2 - antes2)*1000
print("2... %0.2f ms" % total2)

reversed_array = sorted(normal_array, reverse=True)
antes3 = time.time()
#sort(reversed_array)
print("CRASH")
depois3 = time.time()
total3 = (depois3 - antes3)*1000
print("3... %0.2f ms" % total3)

totalf = ((total1 + total2 + total3) / 3)

print("")
print ("Ta... Da!")
time.sleep(1)
print ("A ordenação demorou %0.2f ms em média de três execuções." % totalf)
print("-" * 50)

input("Pressione ENTER para finalizar.")