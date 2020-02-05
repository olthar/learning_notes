vowels = "aeiou"

def disemvowel(word):
    new_word = (list(word))
    for i in word:
      if i.lower() in vowels:
          new_word.remove(i)
    word = "".join(new_word)           
    print (word)
disemvowel("eCEJ")

