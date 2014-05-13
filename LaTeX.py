def latex(photons):
    """Generates some latex code that shows chi^n all nice and pretty
    Input:
        photons == the photons interacting with the system in the order
        they interact with the system
    Output:
        chi == this is the python version of latex used to make a pic of the
        equation.
        
    How to use:
        ~make an array of your incoming photons! It should look like this:
        myphotons = [[frequency, polarization],[frequency,polarization],...]
        ~run the code like this:
        latex(myphotons)
        ~wait impatiently.
        If you want to copy/paste the output to latex, make sure to delete
        the extra \ in each \\. Python will not do this for you. :( Sorry.
    """
    #if you are reading this, I'm sorry.
    #I've commented my code as best I can. Hopefully it is
    #understandable. If not, well, that sucks.
    
    import pylab as py
    import numpy as np
    import matplotlib.pyplot as plt
    
    photons = np.array(photons) #changing the input to np arrays
    
    #Find how many photons we be using.
    N = len(photons)
    #Initialize the output strings
    mu = ''
    chi=''
    w = 0
    
  #  for i in xrange(N):
   #     if photons[i,1]==3:
    #        moleone=photons[:i]
    #       moletwo=photons[i+1:]
     #   else:
     #       1 #beep boop do nothing.
            
    #print moleone
    #print moletwo
            
  #The following for loop figures out the numerator. Since we don't
  #need to worry about complex conjugates, it is a pretty easy loop.  
    for i in xrange(N):
            #making sure the mu starts at the ground level, g:
        if i==0:
            mu ='\\mu^{'+str(photons[i,1])+'}_{n_0g}'
            #this is the last photon. Make sure mu goes back to ground level:
        elif i==N-1:
            mu ='\\mu^{'+str(photons[i,1])+'}_{gn_'+str(i-1)+'}'+mu
            #besides the first and last photon, the rest 
            #don't need special treatment:
        else:
            mu ='\\mu^{'+str(photons[i,1])+'}_{n_'+str(i)+'n_'+str(i-1)+'}'+mu
            
    #The following section makes the energy denominator.
    #It is more complicated. :/
    
    freq = np.zeros(N-1)
    #freq just records the frequency of each photon in the order they came in
    #don't need the last photon for the energy denominator.
    for i in xrange(N-1):
        freq[i]=photons[i,0]
        
    #a just catches the output from the checker function below. coeff and uniques
    #are then the actual output of the checker. I could skip the 'a' but I'm stupid
    #and don't know how
    a=checker(freq)
    coeff=a[0]
    uniques=a[1]
    
    #initialize the energy denominator string
    energy=''

    #actual loop making the energy denominator. i goes from zero to one less than
    #the number of photons you sent in.
    for i in xrange(len(freq)):
        w += photons[i,0]    #sum of all the incoming and outgoing photons
        energy +='('         #start the energy denominator term
                   #if the photons are all coming in (or the total is zero),
                   #no complex conjugate is needed!
        if w>=0:
            energy+='\\Omega_{n_{'+str(i)+'}g}'  #put the Omega in the term
            for n in xrange(len(uniques)):
                      #if the photon does not appear, don't add it to the term!
                if coeff[i,n]==0.0:
                   1#do nothing
                      #we don't need 1*w, we just want w:
                elif coeff[i,n]==1.0 and uniques[n]!=0:
                    energy+='+\\omega_{'+str(int(uniques[n]))+'}'
                      #we don't need -1*w, just -w:
                elif coeff[i,n]==-1.0 and uniques[n]!=0:
                    energy+='-\\omega_{'+str(int(uniques[n]))+'}'
                      #Finally, a non-1, non-zero coefficient! It is less than
                      #zero, so we don't need to add a subtract sign since
                      #the coefficient does that for us! Yippee:
                elif coeff[i,n]<-1.0 and uniques[n]!=0:
                    energy+=str(int(coeff[i,n]))+'\\omega_{'+str(int(uniques[n]))+'}'
                      #Finally, a non-1, non-zero coefficient! It is greater
                      #than zero, so we need to add a plus sign since
                      #the coefficient does not have that:
                elif coeff[i,n]>1.0 and uniques[n]!=0:
                    energy+='+'+str(int(coeff[i,n]))+'\\omega_{'+str(int(uniques[n]))+'}'
                else: #that's boring. you sent in a photon of zero frequency
                    1
        else:
            #Looks like the total energy is negative. Need the complex conjugate
            #on the Omega:
            energy+='\\Omega^*_{n_{'+str(i)+'}g}'
            for n in xrange(len(uniques)): #see comments above
                if coeff[i,n]==0:
                   1#do nothing
                elif coeff[i,n]==1.0 and uniques[n]!=0:
                    energy+='+\\omega_{'+str(int(uniques[n]))+'}'
                elif coeff[i,n]==-1.0 and uniques[n]!=0:
                    energy+='-\\omega_{'+str(int(uniques[n]))+'}'
                elif coeff[i,n]<-1.0 and uniques[n]!=0:
                    energy+=str(int(coeff[i,n]))+'\\omega_{'+str(int(uniques[n]))+'}'
                elif coeff[i,n]>1.0 and uniques[n]!=0:
                    energy+='+'+str(int(coeff[i,n]))+'\\omega_{'+str(int(uniques[n]))+'}'
                else:
                    1 #twiddle thumbs
        energy+=')'   #close energy denominator term!
    
    #let's make the chi equation all pretty:        
    chi= '\\sum_{all}\\frac{'+mu+'}{\\hbar^{'+str(N-1)+'}'+energy+'}'

    #we can plot it:                           
    plt.plot;plt.text(0.5,0.5,'$%s$'%chi,fontsize=28)
    plt.show()
    
    return chi
    
def checker(photons):
    """The energy denominator can't have terms like E-hw1-hw1 because it should
    be E-2hw1. This function determines the coefficient in front of the
    input frequency (w1 in the example).
    Input:
        photons == the photons interacting with the system in the order
        they interact with the system, frequency only!
    Output:
        m == a matrix of size mXn where m is the number of incoming photons
        and n is the number of UNIQUE incoming photons. This matrix contains
        coefficients for calculating the energy denominator
        
        temp == a vector of the unique photons in your system
        
    How to use:
        ~make an array of your incoming photons! It should look like this:
        myphotons = [frequency1, frequency2, ...] (NO POLARIZATION!)
        ~run the code like this:
        checker(myphotons)
        ~wait impatiently.
    """
    import numpy as np
    
    N=len(photons)
    temp=list(photons)
    photons = list(photons) #changing the input to a list
    
        #make all the terms positive.
    for i in xrange(len(temp)):
        if temp[i]<0:
            temp[i]=-1*temp[i]
        else:
            1 #do nothing

        #this loop goes through the temporary array and keeps the unique items:    
    for i in xrange(len(temp)):
        j=i+1
        while j <len(temp):
                #if two items are equal, that means a repeating photon
                #and the second occurance is deleted:
            if temp[i] == temp[j]:
                del temp[j]
                #further, if one photon is the negative of the other, delete
                #the negative photon:
            else:
                j=j+1
                
        #making a matrix:        
    m=np.zeros(shape=(N,len(temp)))
    
    #now, compare the unique items to the original input.
    #i is rows. this is equal to the number of incoming photons
    #j is columns. this is equal to the number of unique incoming photons.
    #m is a matrix that contains the coefficients that need to be in front of
    #the omegas:
    for i in xrange(N):
        w = photons[:i+1]
        for j in xrange(len(temp)):
            #since I didn't count w-1 as a unique photon if w1 was sent in,
            #this counts both occurences of w1 and w-1 so we don't end up
            #with terms like w1-w1.
                m[i,j]=-1*w.count(temp[j])+w.count(-1*temp[j])
            
    m = np.array(m)         #I've been messing with strings here. this turns
    temp = np.array(temp)   #them back to numpy arrays so the main 
                            #latex function can deal with them.
                
    return(m,temp)