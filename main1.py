from mybox import MyBox as mybox
from myclass import Person as person
from child import Student as student
#from myboxiterator import MyIterator as myboxiterator

print("Objects:")
john = person('Brain', 'Kevin')
print(john)

josh_student = student('Kely', 'Adam', 123)
print(josh_student)

print("|Task 3|")

myBox = mybox()

myBox.add(kely)
myBox.add(kely_student)
myBox.add(brain)

print('Add 3 items: ' + str(myBox))
print('Length = ' + str(len(myBox)))
myBox.remove(josh_student)
print('Remove Kely: ' + str(myBox))
print('Length = ' + str(len(myBox)))
print('Contains Kely? ' + str(myBox.contains(josh_student)))

print('Iterator:')
myIterator = myBox.iterator()
print(myIterator)
