sentence = "way a is there will a is there Where"

result = []

def reverse_sentence(sentence):
  word = sentence.split(' ')
  for i in word[::-1]:
      result.append(i)
  return " ".join(result)  

print(reverse_sentence(sentence))
