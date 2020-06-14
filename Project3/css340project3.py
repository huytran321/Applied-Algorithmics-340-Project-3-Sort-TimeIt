# Made by Huy Tran
#Driver Code to find timit

#This code uses the data size of 100, 500, and 1000
#To implement the rest of the points I would change the range size because
#Implementing each iteration would take to a lot of time to load in the results since 
#I repeated the timit 3 times to find the best time

# importing the required modules 
import timeit 
import random
 
# All function trys to find a number out of bounds from the list
def find1_time_100(): 
    SETUP_CODE = ''' 
from bigo import find1
from random import randint
import random
testList = []
for i in range(100):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find1(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('find1_100: {}'.format(min(times)))         
 
def find2_time_100(): 
    SETUP_CODE = ''' 
from bigo import find2
from random import randint
import random
testList = []
for i in range(100):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find2(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('find2_100: {}'.format(min(times))) 

def find3_time_100(): 
    SETUP_CODE = ''' 
from bigo import find3
from random import randint
import random
testList = []
for i in range(100):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find3(testList, find)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000)

    # priniting minimum exec. time 
    print('find3_100: {}'.format(min(times))) 

def find4_time_100(): 
    SETUP_CODE = ''' 
from bigo import find4
from random import randint
import random
testList = []
for i in range(100):
    testList.append(random.randint(0,1000))
testList.sort()
find = 90000'''
  
    TEST_CODE = ''' 
find4(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000)

    # priniting minimum exec. time 
    print('find4_100: {}'.format(min(times)))
    
def find1_time_500(): 
    SETUP_CODE = ''' 
from bigo import find1
from random import randint
import random
testList = []
for i in range(500):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find1(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('find1_500: {}'.format(min(times)))         
 
def find2_time_500(): 
    SETUP_CODE = ''' 
from bigo import find2
from random import randint
import random
testList = []
for i in range(500):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find2(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('find2_500: {}'.format(min(times))) 

def find3_time_500(): 
    SETUP_CODE = ''' 
from bigo import find3
from random import randint
import random
testList = []
for i in range(500):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find3(testList, find)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000)

    # priniting minimum exec. time 
    print('find3_500: {}'.format(min(times))) 

def find4_time_500(): 
    SETUP_CODE = ''' 
from bigo import find4
from random import randint
import random
testList = []
for i in range(500):
    testList.append(random.randint(0,1000))
testList.sort()
find = 90000'''
  
    TEST_CODE = ''' 
find4(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000)

    # priniting minimum exec. time 
    print('find4_500: {}'.format(min(times))) 

def find1_time_1000(): 
    SETUP_CODE = ''' 
from bigo import find1
from random import randint
import random
testList = []
for i in range(1000):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find1(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('find1_1000: {}'.format(min(times)))         
 
def find2_time_1000(): 
    SETUP_CODE = ''' 
from bigo import find2
from random import randint
import random
testList = []
for i in range(1000):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find2(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('find2_1000: {}'.format(min(times))) 

def find3_time_1000(): 
    SETUP_CODE = ''' 
from bigo import find3
from random import randint
import random
testList = []
for i in range(1000):
    testList.append(random.randint(0,1000))
find = 90000'''
  
    TEST_CODE = ''' 
find3(testList, find)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000)

    # priniting minimum exec. time 
    print('find3_1000: {}'.format(min(times))) 

def find4_time_1000(): 
    SETUP_CODE = ''' 
from bigo import find4
from random import randint
import random
testList = []
for i in range(1000):
    testList.append(random.randint(0,1000))
testList.sort()
find = 90000'''
  
    TEST_CODE = ''' 
find4(testList, find)'''
      
    # timeit.repeat statement 3 times
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000)

    # priniting minimum exec. time 
    print('find4_1000: {}'.format(min(times))) 
    

find1_time_100() 
find2_time_100()
find3_time_100()
find4_time_100()
print()
find1_time_500() 
find2_time_500()
find3_time_500()
find4_time_500()
print()
find1_time_1000() 
find2_time_1000()
find3_time_1000()
find4_time_1000()




