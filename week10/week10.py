# mylist = [76, 92, 3, "hello", True, 4, 76]
# print(mylist)
# mylist.append("apple")
# mylist.append(76)
# print(mylist)
#
#
# mylist.insert(3, "cat")
# print(mylist)
# mylist.insert(0. 99)
# print(mylist)
# print(mylist.index("hello"))
# print(mylist.count(76))
# mylist.remove(76)
# print(mylist)
# mylist.pop(mylist.index(True))
# print(mylist)
#
# def sum_of_squares(numbers):
#     sum = 0
#     for number i in numbers:
#         sum += number** 2
#     return sum
#
# mylist = [3, 4, 5]
# print(sum_of_squares(mylist))
#
# def sum_evens(num_list):
#     sum = 0
#     for num in num_list:
#         if num & 2 == 0:
#             sum += num
#     return sum
#
#
# print(sum_evens(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
#
#
#
# def count_five_letter(words):
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# print(count_five_letter(["apple", "hello", "world"]))
#
#
# def sum_until_even(numlist):
#     total = 0
#     for num in numlist:
#         if num ·½ 2 == 0:
#             break
#         total += num
#     return total
#
# print(sum_until_even([1, 3, 5, 7, 6]))



# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count == 1
#         if word == 'sam' :
#         break
#     return count
# my_list = ["ali", "ahmet", "mehmet", "sam"]
# print(count_until_sam(my_list))



# def replace(s, old, new):
#     pieces = s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
#
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAİLED")
#
# test(replace("missisippi", "i", "ı"),"mıssısıppı")



def find_max(num_list):
    max_value = num_list[0]
    for num in num_list:
        if num > max_value:
            max_value = num
    return max_value

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_max(my_list))



