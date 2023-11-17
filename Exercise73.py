input_string = input("Enter a string: ")
input_string = ''.join(e for e in input_string if e.isalnum()).lower()

is_palindrome = True
start = 0
end = len(input_string) - 1
while start < end:
    if input_string[start] != input_string[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if is_palindrome:
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")