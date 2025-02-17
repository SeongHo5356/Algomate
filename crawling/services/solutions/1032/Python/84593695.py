n = int(input())

first_word = list(input())

for _ in range(n-1):
  word = input()
  for i in range(len(word)):
    if word[i] != first_word[i]:
      first_word[i] = "?"

print("".join(first_word))