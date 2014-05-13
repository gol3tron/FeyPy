############################################################
#Programmer: Kyle Schademan,Ted Delikatny, and Adam Goler
# 
#Created: 16 April, 2014 Most recent update:  9 May 2014 (Goler)
# 
#Program description: Permutation program 
############################################################ 
  
import numpy as np 
import math 
import pylab as py
import itertools as it
  

def permute(Warrray):
    """ Converts the list of photons into a numbered list in which similar photons have the same lable. ex [1,1,2,5,2] -> [0,0,2,3,2] """
    uniW = [i for i in range(len(Warrray))]
    for i in range(0,len(Warrray)):
        for j in range(i+1,len(Warrray)):
            if(np.array_equal(Warrray[i],Warrray[j])):
                uniW[j] = uniW[i]
    return uniW

def unique(iterable):
    """Eliminates duplicates from a list """
    seen = set()
    for x in iterable:
        if x in seen:
            continue
        seen.add(x)
        yield x


def getPermutations(Warray):
    """ Records all possible unique permutations of w in an array """
    permutearray = []
    for a in unique(it.permutations(permute(Warray))):
        urple = [Warray[x] for x in a]
        permutearray.append(urple)

    
    return np.array(permutearray)


def permutations_array (array):
    """ 
    inputs: 
        array = two dimensional array 
    outputs: 
        permutations = an array containing all the permutation  
            arrays of the input array 
    """
    # initialize variables 
    unique = 0 
    myorder = [i for i in range(0,len(array))] 
    order = [] 
    temp1 = 0
    temp2 = 0
    temp3 = 0
    index = 0  
    check = 0 
    m = 0
    n = 0
    elements = []  
    integer_order = [] 
              
    # find the number of unique elements in the input array 
    # and create an array to label their locations in the array
    for i in range(0, len(array)): 
          
        for j in range(i+1, len(array)): 
              
            if(np.array_equal(array[i],array[j])): 
                check = 1
              
        if(check == 0): 
            unique = unique +1
            order = py.append(order, i) 
        check = 0
      
    # change elements in order into integers because python
    #needs me to tell it to do this.
    for n in order: 
        integer_order.append(int(n)) 
    order = integer_order 
      
    #put the unique elements of array in an array 
    elements = [array[i] for i in order]
    
    #create an array to count the number of times an element 
    #occurs in the input array 
    degen = [0 for i in range(unique)] 
      
    # find the number of degeneracies of each element of array 
    for k in range(0, len(degen)): 
              
        for j in range(0, len(array)): 
                      
            if(np.array_equal(elements[k],array[j])): 
                degen[k] = degen[k] +1
        
    # find the k-permutation number  
    kpermutation = math.factorial(len(array))              
    for i in range(len(degen)):             
        kpermutation = kpermutation/math.factorial(degen[i]) 
      
    #construct an output array of the corret size 
    permutations = [array for i in range (kpermutation)] 
      
    # permute all of the rotation permutations 
    while(True): 
          
        index = index + 1
        temp1 = myorder[0] 
          
        for i in range(0,len(array)): 
              
            if(i+1<len(array)):         
                myorder[i] = myorder[i+1] 
            else: 
                myorder[i] = temp1 
    
        if(index >= len(permutations)): 
            break  
                      
        permutations[index] = [permutations[index][j] for j in myorder] 
  
  
    # permute the swapping permutations 
    if (unique > 1): 
          
        m = 0
        n = 1
        index = 0
        temp3 = len(array) - 1
          
        while(True): 
                   
            #checks if every element in permutations is unique 
            check = 0                
            for j in range(0, len(permutations)): 
                      
                if(j != temp3): 
                          
                    if(np.array_equal(permutations[temp3],permutations[j])): 
                        check = 1
              
            if(check == 0): 
                temp3 = temp3+1
                index = 0
            else: 
                  
                if(m == len(array)- 1): 
                    m = m-len(array)-1
                else: 
                    m = m+1
                if(n == len(array)-1): 
                    n = n-len(array)-1
                else: 
                    n = n+1
              
            #ends loop if every element is unique 
            if(temp3 == len(permutations)): 
                break
                  
            temp1 = myorder[m] 
            temp2 = myorder[n] 
            myorder[m] = temp2 
            myorder[n] = temp1 
              
            permutations[temp3] = [permutations[temp3][j] for j in myorder] 
            
            index = index+1
            
            if (index >len(permutations)):
                
                if(n == len(array)-1): 
                    n = n-len(array)-1
                else: 
                    n = n+1
                index = 0
                  
      
    return permutations 
  