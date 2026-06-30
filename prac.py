digits = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(digits)
for i in range(length):
    print(digits[i])

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
# Concatenate the two lists
combined_list = list1 + list2
sum_combined = sum(combined_list)
print("Combined List:", combined_list)


# class methods
class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print("Value:", self.value) 
    @classmethod
    def class_method(cls):
        print("This is a class method.")
class1 = MyClass(10)
class1.display_value()  # Output: Value: 10
MyClass.class_method()  # Output: This is a class method.