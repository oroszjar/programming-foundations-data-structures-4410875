def has_unique_characters(data):
    # characterSet = set?
    # isUnique = True
    # for character in data:
    #     if character not in characterSet:
    #         characterSet.add(character)
    #     else:
    #         isUnique = False
    # return isUnique
    # :((((
    unique_data = set(data)
    return len(data) == len(unique_data)

# use a set
# has unique characters?

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
