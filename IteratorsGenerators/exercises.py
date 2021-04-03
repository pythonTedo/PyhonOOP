# class take_skip:
#     def __init__(self, step, count):
#         self.step = step
#         self.count = count
#         self.counter = 0
#         self.curr_num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = 0
#
#         if self.counter < self.count:
#
#             temp = self.curr_num
#             self.curr_num += self.step
#
#             self.counter += 1
#
#             return temp
#
#         raise StopIteration
#
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
########################################################################################################################
# class dictionary_iter:
#     def __init__(self, item):
#         self.item = item
#         self.current_index = 0
#         self.keys = list(self.item.keys())
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = 0
#         if self.current_index < len(self.item):
#
#             temp = self.current_index
#             self.current_index += 1
#
#             return (self.keys[temp], self.item[self.keys[temp]])
#
#         raise StopIteration
#
#
# result = dictionary_iter({1: "1", 2: "2", "petur": 598})
# for x in result:
#     print(x)
########################################################################################################################
# class countdown_iterator:
#     def __init__(self, nums):
#         self.nums = nums
#         self.current_num = self.nums
#         self.curr_count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.curr_count <= self.nums:
#             temp = self.current_num
#             self.current_num -= 1
#
#             self.curr_count += 1
#
#             return temp
#
#         raise StopIteration
#
#
# iterator = countdown_iterator(20)
# for item in iterator:
#     print(item, end=" ")
########################################################################################################################
# class sequence_repeat:
#
#     def __init__(self, text, number):
#
#         self.text = text
#         self.number = number
#         self.count = 0
#         self.curr_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.count <= self.number:
#             temp_index = self.curr_index
#
#             if self.curr_index == len(self.text):
#                 self.curr_index = 0
#                 temp_index = self.curr_index
#                 self.curr_index += 1
#             else:
#                 self.curr_index += 1
#
#             self.count += 1
#             return self.text[temp_index]
#
#         raise StopIteration
#
# result = sequence_repeat('abc', 6)
# for item in result:
#     print(item, end ='')
########################################################################################################################
import random

# def solution():
#     def integers():
#         # random.randrange(start=1)
#         start_num = 1
#         while True:
#             yield start_num
#             start_num += 1
#
#     def halves():
#         for i in integers():
#              yield i/2
#
#     def take(n, seq):
#         my_list = []
#         for num in seq:
#             if len(my_list) == n:
#                 return my_list
#             my_list.append(num)
#
#     return (take, halves, integers)
#
# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))
########################################################################################################################
# def fibbonacci():
#
#     n1 = 1
#     n2 = 0
#     count = 0
#     previous_num = 0
#     curr_num = 1
#
#     while True:
#         # nth = n1 + n2
#         # # update values
#         # n1 = n2
#         # n2 = nth
#         # count += 1
#         # yield n1
#         yield previous_num
#         previous_num, curr_num = curr_num, curr_num+previous_num
#
# f = fibbonacci()
# for i in range(7):
#     print(next(f))
########################################################################################################################
# def read_next(*args):
#     for el in args:
#         for a in el:
#             yield a
#
#
# for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
#     print(item, end='')
########################################################################################################################
# def get_primes(list):
#
#     for i in list:
#
#         if i < 2:
#             continue
#
#         is_prime = True
#         for num in range(2, i):
#             if i % num == 0:
#                 is_prime = False    # if we find we break the loop
#                 break
#
#         if is_prime:
#             yield i
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
########################################################################################################################
import itertools
def possible_permutations(elements):
    for per in itertools.permutations(elements):
        yield list(per)

[print(n) for n in possible_permutations([1, 2, 3])]

