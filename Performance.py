"""
Test the performance of your Standard Bloom Filter.

To do this, start by completing the code for
"performance_helper" below. The function should

  - Add k elements uniformly at random from
   [1..n] to your filter.
  - Adds the same items to a python set
  -returns the bloom filter, and the python set
"""

def performance_helper(n : int, k: int, hash_func : None):
    #TODO
    pass

"""
With n = 10000, and capacity 10000,
for k = 1000, 2000, ..., 10000

   (0) Get a Bloom filter and set from the
   performance helper method above ...(n=10000, k, None)

   (1) Store the number of entries filled
   in the table divided by k.
 
   (2) Take a random sample of t = 1000 elements
   from [1..n] and (using the set returned by performance_helper)
   store the percentage of false positives when
   querying membership for these elements.

Take the data you gathered from (1) and (2) and
plot it against k.

Save your plot to ./performance_plots_0.jpg

You can use matplotlib.pyplot for this.

Leave a comment in the code with
your findings.
"""

#TODO
"""
Repeat the same experiment with a bloom
filter having capacity 20000.

Save your plot to ./performance_plots_1.jpg
"""

"""
Repeat a similar experiment using a multi-bloom
filter with capacity 5000, and 2 distinct hash
functions (chosen from a family of universal hash
functions).  

Save your plot to ./performance_plots_2.jpg
"""

"""
Repeat a similar experiment using a multi-bloom
filter with capacity 10000, and 2 distinct hash
functions (chosen from a family of universal hash
functions).  

Save your plot to ./performance_plots_3.jpg
"""

#TODO

"""
Repeat a similar experiment using a multi-bloom
filter with capacity 2000, and 5 distinct hash
functions (chosen from a family of universal hash
functions).  

Save your plot to ./performance_plots_4.jpg
"""

"""
Repeat a similar experiment using a multi-bloom
filter with capacity 4000, and 5 distinct hash
functions (chosen from a family of universal hash
functions).  

Save your plot to ./performance_plots_5.jpg
"""

"""
Leave a comment on the differences between the 
three experiments here.
"""