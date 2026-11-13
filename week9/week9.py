# def 1s_odd(n):
#     return n % 2 == 1
# print(1s_odd(5))
#
#
# def 1s_leayear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# print(1s_leayear(2024))
#
#
# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + 1
#         print(i, total)
#
# print(print_triangular_numbers(5))
#
#
#
# def 1s_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(1s_prime(2))
#
#
# def reverse(s):
#     result = ""
#     for i in s:
#         result = result + ch
#         return result
#
#
# print(reverse("abcd"))
#
#
#
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("abcd"))

# def remove_all(sub, s):
#     return s.replace(sub, "")
# print(remove_all("l", "hello world"))



# def substitute(message, key6):
#     alphabet = "abcdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qtgjdhoekduşğiojhgjfrseadcbnv"
# print(len(key))
#
# print(substitute("hello, world", key))

def remove_dups(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result


print(remove_dups("anne"))