'''Write a list comprehension that takes the following list and creates a new list containing the 
   names of students whose names are four letters long:
students = [“Hannah”, “Peter”, “Luke”,"Alyssa","mary"] '''

students = ["Hannah","Peter","Luke","Alyssa","mary"]
new_list = []
class MyListWork():
    def __init__(self, st_list):
        self.st_list = st_list

    def list_comp(self):
        # expression for elementes in iterable if condition           
        new_list = [name for name in self.st_list if len(name) == 4 ]           
        print(new_list)

obj = MyListWork(students)
obj.list_comp()