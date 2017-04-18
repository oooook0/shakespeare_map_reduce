from multiprocessing import Pool

import time

t0 = time.time()

def load(path):
 
  word_list = []
  f = open(path, "r")
  for line in f:
    word_list.append (line)
 
  # Efficiently concatenate Python string objects
  return (''.join(word_list)).split ()

def sanitize(w):
 
  # Strip punctuation from the front
  while len(w) > 0 and not w[0].isalnum():
    w = w[1:]
 
  # String punctuation from the back
  while len(w) > 0 and not w[-1].isalnum():
    w = w[:-1]
 
  return w

def chunks(l, n):
  for i in range(0, len(l), n):
    yield l[i:i+n]

def Partition(L):
  tf = {}
  for sublist in L:
    for p in sublist:
      # Append the tuple to the list in the map
      try:
        tf[p[0]].append (p)
      except KeyError:
        tf[p[0]] = [p]
  return tf

def Reduce(Mapping):
  return (Mapping[0], sum(pair[1] for pair in Mapping[1]))

#my version of Map function
def Map(L):
 
  results = []
  for w in L:
    if not w.isalnum():
        w = sanitize (w)
 

    if w.istitle():
        results.append ((w.lower(), 1))
 
  return results

#set the number of processors used
pool = Pool(processes=8,)

#load file
"""
Answer to homework D 1
"""
tokens=load('shakespeare.txt')

#divide file into 8 parts(use int incase )
partitioned_text = list(chunks(tokens, int(len(tokens) / 8)))

#Multiprocess the Mapping(sanitize the data and make them lower case)
single_count_tuples = pool.map(Map, partitioned_text)

#count the list and get 8 partitions together
token_to_tuples = Partition(single_count_tuples)

#reduce the map
term_frequencies = pool.map(Reduce, token_to_tuples.items())

#sort the frequencies in descending order
""""
Answer to homework D 2
"""
sorted_frequencies = sorted(term_frequencies, key=lambda tup: -tup[1])


t1 = time.time()

total = t1-t0
    
print("runtime is "+ str(total)+".")
