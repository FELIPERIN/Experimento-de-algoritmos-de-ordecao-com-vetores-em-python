import random
import time

def sort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]


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
sort(sorted_array)
depois1 = time.time()
total1 = (depois1 - antes1)*1000
print("1... %0.2f ms" % total1)

antes2 = time.time()
sort(sorted_array)
depois2 = time.time()
total2 = (depois2 - antes2)*1000
print("2... %0.2f ms" % total2)

antes3 = time.time()
sort(sorted_array)
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
sort(reversed_array)
depois1 = time.time()
total1 = (depois1 - antes1)*1000
print("1... %0.2f ms" % total1)

reversed_array = sorted(normal_array, reverse=True)
antes2 = time.time()
sort(reversed_array)
depois2 = time.time()
total2 = (depois2 - antes2)*1000
print("2... %0.2f ms" % total2)

reversed_array = sorted(normal_array, reverse=True)
antes3 = time.time()
sort(reversed_array)
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