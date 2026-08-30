import time
from hashmap import HashMap

def read_birds_hashmap(filename):
   bird_count = HashMap()
   with open(filename, 'r') as file:
      for line in file:
         bird = line.strip()
         if bird in bird_count:
            bird_count[bird] += 1
         else:
            bird_count[bird] = 1

   for bird in bird_count.get_keys():
      print(f"{bird} {bird_count[bird]}")
         


   """
   :param filename: the name of the file to open.
   :return: the HashMap containing the count of bird species
   """
   ...


def read_birds_dictionary(filename):
   bird_count = {}
   with open(filename, 'r') as file:
      for line in file:
         bird = line.strip()
         if bird in bird_count:
            bird_count[bird] += 1
         else:
            bird_count[bird] = 1

   for bird, count in bird_count.items():
        print(f"{bird} {count}")
   """
   :param filename: the name of the file to open.
   :return: the dictionary containing the count of bird species
   """
   ...



if __name__ == "__main__":
   # You can add lines of code here to help you test.

   # ---- DO NOT MODIFY THE LINES BELOW ----
   # start = time.perf_counter()
   # print('-' * 3, "Reading bird_observations_small.txt with Python dictionary", '-' * 3)
   # results = read_birds_dictionary("bird_observations_small.txt")

   # print('\n', '-' * 3, "Reading bird_observations_large.txt with Python dictionary", '-' * 3)
   # results = read_birds_dictionary("bird_observations_large.txt")
   # read_time = time.perf_counter() - start
   # print('-' * 3, "Total time for reading bird_observations_large.txt with Python dictionary = ", read_time, '-' * 3, '\n')


   # start = time.perf_counter()
   # print('-' * 3, "Reading bird_observations_small.txt with my HashMap implementation", '-' * 3)
   # results = read_birds_hashmap("bird_observations_small.txt")

   # print('\n', '-' * 3, "Reading bird_observations_large.txt with my HashMap implementation", '-' * 3)
   # results = read_birds_hashmap("bird_observations_large.txt")
   # read_time = time.perf_counter() - start
   # print('-' * 3, "Total time for reading bird_observations_large.txt with my HashMap implementation = ", read_time, '-' * 3, '\n')




#I had to mddify the print command a little bit so the code could find my .txt files. Even though they are in the same directory they couldn't seem to be able to
#find each other until I added "Lab7/" in front of each .txt call. I believe this is the same issue that occured with my Homework3 files being unable to call
#router.py, but I will look into this in the coming days since I have not heard anything from you.

   start = time.perf_counter()
   print('-' * 3, "Reading bird_observations_small.txt with my HashMap implementation", '-' * 3)
   results = read_birds_hashmap("Lab7/bird_observations_small.txt")


   print('\n', '-' * 3, "Reading bird_observations_large.txt with my HashMap implementation", '-' * 3)
   results = read_birds_hashmap("Lab7/bird_observations_large.txt")
   read_time = time.perf_counter() - start
   print('-' * 3, "Total time for reading bird_observations_large.txt with my HashMap implementation = ", read_time, '-' * 3, '\n')


   start = time.perf_counter()
   print('-' * 3, "Reading bird_observations_small.txt with Python dictionary", '-' * 3)
   results = read_birds_dictionary("Lab7/bird_observations_small.txt")

   print('\n', '-' * 3, "Reading bird_observations_large.txt with Python dictionary", '-' * 3)
   results = read_birds_dictionary("Lab7/bird_observations_large.txt")
   read_time = time.perf_counter() - start
   print('-' * 3, "Total time for reading bird_observations_large.txt with Python dictionary = ", read_time, '-' * 3, '\n')