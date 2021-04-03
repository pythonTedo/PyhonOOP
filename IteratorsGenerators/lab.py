# class custom_range:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.curr_start = self.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.start <= self.stop:
#             temp = self.start
#             self.start += 1
#             return temp
#
#         raise StopIteration
#
# c = custom_range(1,10)
#
# for num in c:
#     print(num)
########################################################################################################################
# class reverse_iter:
#     def __init__(self, element):
#         self.element = element
#         self.curr_index = len(self.element) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.curr_index >= 0:
#             temp = self.curr_index
#             self.curr_index -= 1
#             return self.element[temp]
#
#         raise StopIteration
#
# a = reverse_iter([1, 2 ,3, 4, 5])
#
# for num in a:
#     print(num)
########################################################################################################################
# class vowels:
#     vow = ['a', 'e', 'i', 'o', 'u', 'y']
#
#     def __init__(self, text):
#         self.text = text
#         self.curr_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.curr_index < len(self.text):
#             temp_index = self.curr_index
#             self.curr_index += 1
#
#             if self.text[temp_index].lower() in self.vow:
#                 return self.text[temp_index]
#             else:
#                 return self.__next__()  ### go back in next, rise index and check again
#
#         raise StopIteration
#
# t = vowels("eijwpjdnnpaqiuATsmOSMA")
#
# for i in t:
#     print(i)
############################# GENERATORS ###############################################################################
# def first_n(n):
#     num = 0
#     while num < n: ## nqmame __next__ kudeto ne pomni i da go zapazvame temp
#         yield num  ### yield is return bot saves the state and dont't stop the execution
#         num += 1
#
# sum_first_n = sum(first_n(5))
# print(sum_first_n)
########################################################################################################################
# def squares(n):
#     for i in range(1, n+1):
#         yield i**2
#
# print(list(squares(5)))

# class squares_iter:
#     def __init__(self, n):
#         self.n = n
#         self.curr_num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.curr_num <= self.n:
#             temp = self.curr_num
#             self.curr_num += 1
#             return temp ** 2
#         raise StopIteration
#
# print(list(squares_iter(5)))

# my_list = ['happy', 'not', 'angry', 'disguist', 'sad', 'surprise']
#
# dict = {}
#
# for index, label in enumerate(my_list):
#     dict[label] = index
#
#
# print(dict)
st1 = "Senior Front-End".lower()
st2 = "Senior Front-end".lower()

st2 == st1


