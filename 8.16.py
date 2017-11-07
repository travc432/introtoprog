
#Travis and Ron

weights = []
i = 0
while i < 4:
    weight = float(input('Enter weight %i:\n' % (i+1)))
    weights.append(weight)
    i += 1
    
print('Weights:', weights)
print('\nAverage weight: %.2f' % (sum(weights)/len(weights)))
print('Max weight: %.2f' % (max(weights)))

index = int(input('\nEnter a list index (1 - 4):\n'))
print('Weight in pounds: %.2f' % (weights[index - 1]))
print('Weight in kilograms: %.2f' % (weights[index - 1] / 2.2))

print('\nSorted list:', sorted(weights))



