# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagrams(word1, word2):
# [assignment] Add your code here
    if(sorted(word1)==sorted(word2)):
      return True
    else:
      return False

find_anagrams("hello", "ello")
find_anagrams("kok", "kok")
find_anagrams("cool", "cool")

print(find_anagrams("hello", "ello")) 
print(find_anagrams("kok", "kok")) 
print(find_anagrams("cool", "cool"))
