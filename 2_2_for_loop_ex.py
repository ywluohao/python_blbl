
a_long_string = 'an apple a day keeps doctor away!'

ans = {}  # the ans is to store the answer

for char in a_long_string:
    if char not in ans:     # if char not in ans
        ans[char] = 1       # add char to ans as a new key
    else:                   # if char is already in ans
        ans[char] += 1      # add the value of ans by 1
print(ans)


# more advanced ans suggested:
from collections import Counter
print(Counter(a_long_string))
