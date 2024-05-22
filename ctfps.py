# Computationtal Thinking for Problem Solving Week 3 Project Part 3: Writing Pseudocode
# pseudocode link to "# Computational Thinking for Problem Solving Week 4 Project Part 4: Implementing the Solution in Python"
#Part 1: create list name "all_words" that contain [keyword, synonyms1, synonyms2, ...]
Input: keyword, Thesaurus
Output: list name "all_words"

all_words <- [keyword]
for entry in Thesaurus
__if entry.word = keyword
____for word in entry.synonyms
______all_words <- all_words + word
____break

output: all_words

#Part 2: count search_word and create (search_word, count) #tuple
Input: all_words, document in Corpus
Output: (search_word, count) #tuple

for search_word in all_words
__count <- 0
__for document in Corpus
____for word in document
______if word = search_word
________count <- count + 1
__result = (search_word, count)

output: (search_word, count) #tuple





# Computational Thinking for Problem Solving Week 4 Lists Programming Assignment
def test() : # do not change this line!
  values = [4, 7, 8, 9, -5] # do not change this line!

  # write your code here so that it modifies values
  if values[-1] < 0:
    #values.remove(values[-1])
    values.pop(-1)
    sum = values[0] + values[1]
    avg = sum/2
    values.insert(1, avg)
    values[0], values[-1] = values[-1], values[0]

  # be sure to indent your code!

  print(values)
  return values # do not change this line!
# do not write any code below here

test()  # do not change this line!
# do not remove this line!





# Computational Thinking for Problem Solving Week 4 Loops Programming Assignment
# 1
def test() : # do not change this line!
  list = [4, 5, 1, 9, -2, 0, 3, -5] # do not change this line!
  min1 = list[0]
  min2 = list[1]

  # write your code here so that it sets
  # min1 and min2 to the two smallest numbers
  # be sure to indent your code!
  for i in list:
    if i < min1:
      if min1 < min2:
        min2 = i
      else:
        min1 = i
    elif i < min2:
      min2 = i

  print(min1, min2)
  return (min1, min2) # do not change this line!
# do not write any code below here

test() # do not change this line!
# do not remove this line!



# 2
def test() : # do not change this or the next line!
  numbers = [11.5, 28.3, 23.5, -4.8, 15.9, -63.1, 79.4, 80.0, 0, 67.4, -11.9, 32.6]
  average = 0
  pos_numbers = []
  sum = 0

  # create new list
  for number in numbers:
    if number >= 0:
      pos_numbers.append(number)
      #print(pos_numbers)
    else:
      continue

  denominator = len(pos_numbers)
  #print(denominator)

  # sum list
  for number in pos_numbers:
    sum = sum + number
    #print(sum)

  average = sum/denominator

  print(average)
  return average # do not change this line!
  # do not write any code below here

test()  # do not change this line!
# do not remove this line!





# Computational Thinking for Problem Solving Week 4 Functions Programming Assignment
def verify(number) : # do not change this line!

  # write your code here so that it verifies the card number
  #print(number) # print input
  #Testing Rule 1
  if int(number[0]) == 4:
    #print('Rule #1 is pass')
    #if pass Rule 1
    #Start Testing Rule 2
    if int(number[3]) > int(number[5]):
      #print('Rule #2 is pass')
      #if pass Rule 2
      #Start Testing Rule 3
      pure_number = number[0:4] + number[5:9] + number[10:14]
      #print(pure_number)
      num_list = []
      for n in pure_number:
        num_list.append(int(n))
      #print(num_list)
      total = sum(num_list)
      #print(total)
      if total % 4 == 0:
        #print('Rule #3 is pass')
        #if pass Rule 3
        #Start Testing Rule 4
        #print(pure_number)
        #print(int(pure_number[0:2]) + int(pure_number[6:8]))
        if int(pure_number[0:2]) + int(pure_number[6:8]) == 100:
          #print('Rule #4 is pass')
          return True
        else:
          #print('Error code: 4')
          return 4
      else:
        #print('Error code: 3')
        return 3
    else:
      #print('Error code: 2')
      return 2
  else:
    #print('Error code: 1')
    return 1

  # be sure to indent your code!

  return True # modify this line as needed

input = "4094-3460-2754" # change this as you test your function
output = verify(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!





# Computational Thinking for Problem Solving Week 4 Classes and Objects Programming Assignment
# implement County class here
class County:
  def __init__(self, init_name, init_population, init_voters):
    self.name = init_name
    self.population = init_population
    self.voters = init_voters
    self.turnout = self.voters/self.population

def highest_turnout(data) :
  highest_turnout_county = ''
  highest_turnout = 0
  for county in data:
    if county.turnout > highest_turnout:
      highest_turnout_county = county
      highest_turnout = county.turnout
    else:
      continue

  # implement the function here
  #print(highest_turnout_county.name, highest_turnout)
  return (highest_turnout_county.name, highest_turnout)# modify this as needed

# your program will be evaluated using these objects
# it is okay to change/remove these lines but your program
# will be evaluated using these as inputs
allegheny = County("allegheny", 1000490, 645469)
philadelphia = County("philadelphia", 1134081, 539069)
montgomery = County("montgomery", 568952, 399591)
lancaster = County("lancaster", 345367, 230278)
delaware = County("delaware", 414031, 284538)
chester = County("chester", 319919, 230823)
bucks = County("bucks", 444149, 319816)
data = [allegheny, philadelphia, montgomery, lancaster, delaware, chester, bucks]

result = highest_turnout(data) # do not change this line!
print(result) # prints the output of the function
# do not remove this line!

###playground###
#print(data[0].turnout)
#print(data[1].turnout)

#if data[0].turnout > data[1].turnout:
  #print('Yes')
#else:
  #print('No')





# Computational Thinking for Problem Solving Week 4 Project Part 4: Implementing the Solution in Python
def search(keyword) :
  all_words = [keyword]
  for entry in Thesaurus:
    if entry.word == keyword:
      for word in entry.synonyms:
        all_words.append(word)
  #print(all_words)
   # implement the function here
  tup_list = []
  for search_word in all_words:
    count = 0
    for Document in Corpus:
      for word in Document:
        if word == search_word:
          count = count + 1
    result = (search_word, count)
    tup_list.append(result)
    #print(tup_list)
  return (tup_list) # modify to return a list of tuples

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!

###playground###
#Thesaurus
#for word in Thesaurus:
  #print(word.word)
#Corpus
#print(Corpus)
