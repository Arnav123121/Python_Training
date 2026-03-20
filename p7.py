#Find count of special character in a string

def countSpecialCharacters(s):
    count = 0
    for char in s:
        if not char.isalnum():
            count += 1
    return count
s = input("Enter A String :- ")
result = countSpecialCharacters(s)
print("Count of special characters:", result)