"""
This question is asked by Amazon. Given two strings representing sentences, 
return the words that are not common to both strings (i.e. the words that 
only appear in one of the sentences). You may assume that each sentence is 
a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""

from typing import List

def countWords(sentence: str):
  table = dict()
  sentence = sentence.split()
  
  for word in sentence:
    if table.get(word) == None:
      table[word] = 0
    table[word] += 1

  return table

def uncommonWords(sentence1: str, sentence2: str) -> List[str]:
  #Time: O(m+n)
  #Space: O(n+m)
  output = []
  
  strConcat = sentence1 + " " + sentence2
  hashmap = countWords(strConcat)
  
  for k, v in hashmap.items():
    if v == 1:
      output.append(k)

  return output

assert uncommonWords("the quick", "brown fox") == ["the", "quick", "brown", "fox"]
assert uncommonWords("the tortoise beat the haire", "the tortoise lost to the haire") == ['beat', 'lost', 'to']
assert uncommonWords("copper coffee pot", "hot coffee pot") == ["copper", "hot"]
