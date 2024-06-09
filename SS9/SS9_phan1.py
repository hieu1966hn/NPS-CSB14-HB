def reverse_str(s):
    reversed_s = ''
    for char in s:
        print(char)
        # print(reversed_s)
        reversed_s = char + reversed_s
    return reversed_s


print(reverse_str("hello"))

