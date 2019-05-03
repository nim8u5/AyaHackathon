# benchmark word: "recommends"
# acceptable words: "recommend", "reccommends", "recmmends"

# delta is the difference in percentage between
# length of the word I input and that of the benchmark word
def delta(length1, length2):
  d = length1 - length2
  return abs(d) / float(length2)


# the function compare is to compare leter by letter
# accuracy is the matching percentage of letters minus
# the inaccuracy of the word length
def compare(string1, string2):
  counter = 0
  length1 = len(string1)
  length2 = len(string2)

  for i in range(length1):
    if i < (length2-1):
      if string1[i] == string2[i]:
        counter += 1
      elif string1[i] == string2[i+1]:
        counter += 1
      elif b[i+1] == w[i]:
        counter += 1

    if i == (length2-1) :
      if string1[i] == string2[i]:
        counter += 1

      elif string1[i+1] == string2[i]:
        counter += 1
    
  off = delta(length1, length2)
  accuracy = counter / float(length1) - off
  accuracy = round(accuracy,2)
  print("Accuracy is :", accuracy)



if __name__ == "__main__":
  compare("recommends","reccommends")
