def printList(myList):
  for index, item in enumerate(myList):
    print(f"index {index}: {item}")

myList = [17, 38, 10, 25, 72]

sortedList = sorted(myList)

print("Liste triée:")
print(sortedList)

print("Liste triée avec ajout:")
sortedList.append(12)
print(sortedList)

reversedList = sorted(sortedList, reverse=True)
print("Liste triée inversée:")
print(reversedList)

print(sortedList.index(17))

sortedList.remove(38)
print("Liste triée avec suppression:")
print(myList)

print(sortedList[1:4])
print(sortedList[0:2])
print(sortedList[2:])
print(sortedList[0:len(sortedList)])

print(sum(sortedList))

# Comprehension de liste
print("----------------Comprehension de liste----------------")
print([i for i in range(0, 10)])
liste = [i for i in range(0, 11)]
listeCarree = [nb**2 for nb in liste]
listePaire = [nb for nb in liste if nb % 2 == 0]
print(liste)
print(listeCarree)
print(listePaire)




one, two, three = (1, "toto", "joe")
print(one)
print(two)
