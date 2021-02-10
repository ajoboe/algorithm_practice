string = "abcabcbb"
s = {}
for i, c in enumerate(string):
    s[i] = c
print(s)
longest = 0
for i in range(len(s)):
    print("Starting at " + str(i))
    j = i
    while j < len(s) and s[j] not in s[i:j]:
        print("  checking if " + s[j] + " is in " + s[i:j])
        j += 1
    longest = max(j-i, longest)
    print("  current longest is " + str(longest))
print(longest)
