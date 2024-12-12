from functools import reduce

list1 = []
list2 = []
distance_list = []

# Processing the data
with open('./data.txt', 'r') as data:
   for line in data.read().split('\n'):
        elements = line.split('   ')
        list1.append(int(elements[0]))
        list2.append(int(elements[1]))

# Sorting the lists
list1.sort()
list2.sort()

# Getting distance
for index in range(0, len(list1)):
    distance_list.append(abs(list1[index] - list2[index]))

# Processing Total Distance
total_distance = reduce(lambda accum, curr: accum+curr, distance_list)

# Processing Similarity Score
similarity_score = 0
for element in list1:
    occurrences = list2.count(element)
    if occurrences > 0:
        similarity_score += element * occurrences

# Printing Results
print('Result 1:')
print(total_distance)
print('\n')

print('Result 2:')
print(similarity_score)
