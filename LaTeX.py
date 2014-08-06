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
    energy = ''
    #energytex=''
    mu = ''
    chi=''
    #chitex=''
    #mutex= '' #saving this in case we want to be able to copy and paste the latex output code and not have the extra \
    w = 0

  #The following for loop figures out the numerator. Since we don't
  #need to worry about complex conjugates, it is a pretty easy loop.  
    for i in xrange(N):
        if i==0: #making sure the mu starts at the ground level, g
            mu ='\\mu^{'+str(photons[i,1])+'}_{n_0g}'
            #mutex ='\mu^{'+str(photons[i,1])+'}_{n_0g}'
        elif i==N-1: #this is the last photon. Make sure mu goes back to ground level
            mu ='\\mu^{'+str(photons[i,1])+'}_{gn_'+str(i-1)+'}'+mu
            #mutex ='\mu^{'+str(photons[i,1])+'}_{gn_'+str(i-1)+'}'+mutex
        else: #besides the first and last photon, the rest don't need special treatment
            mu ='\\mu^{'+str(photons[i,1])+'}_{n_'+str(i)+'n_'+str(i-1)+'}'+mu
            #mutex ='\mu^{'+str(photons[i,1])+'}_{n_'+str(i)+'n_'+str(i-1)+'}'+mutex
            
    #The following section makes the energy denominator. It is more complicated. :/
    
    freq = np.zeros(N)
    #freq just records the frequency of each photon in the order they came in
    for i in xrange(N):
        freq[i]=photons[i,0]
        
    #a just catches the output from the checker function below. coeff and uniques
    #are then the actual output of the checker. I could skip the 'a' but I'm stupid
    #and don't know how
    a=checker(freq)
    coeff=a[0]
    uniques=a[1]

    #actual loop making the energy denominator. i goes from zero to one less than
    #the number of photons you sent in.
    for i in xrange(N-1):
        w += photons[i,0] #sum of all the incoming and outgoing photons
        if w>=0: #if the photons are all coming in (or the total is zero), no complex conjugate is needed!
            energy = energy +'(\\Omega_{n_{'+str(i)+'}g}' #this line starts the energy denominator
            #energytex= energytex +'(\Omega_{n_{'+str(i)+'}g}'
            for n in xrange(len(uniques)+1):
                if coeff[i,n]==0 or n==len(uniques)+1: #this tells the loop to close the bracket
                    energy= energy +')'
                    #energytex=energytex+')'
                    break
                elif coeff[i,n]==1: #we don't need 1*w, we just want w
                    if uniques[n]<0: #outgoing photon! better add it!
                        energy = energy + '+\\omega_{'+str(-1*int(uniques[n]))+'}'
                   #     energytex = energytex + '+\omega_{'+str(-1*int(uniques[n]))+'}'
                    elif uniques[n]>0: #incoming photon! SUBTRACT! SUBTRACT!
                        energy = energy + '-\\omega_{'+str(int(uniques[n]))+'}'
                  #      energytex = energytex + '-\omega_{'+str(int(uniques[n]))+'}'
                    else: #that's boring. you sent in a photon of zero frequency
                        1
                else: #here is where the non-1 coefficients come in
                    if uniques[n]<0: #outgoing photon! better add it!
                        energy = energy + '+' +str(int(coeff[i,n]))+'\\omega_{'+str(-1*int(uniques[n]))+'}'
                 #       energytex = energytex + '+' +str(int(coeff[i,n]))+'\omega_{'+str(-1*int(uniques[n]))+'}'
                    elif uniques[n]>0: #incoming photon! SUBTRACT! SUBTRACT!
                        energy = energy + '-' +str(int(coeff[i,n]))+'\\omega_{'+str(int(uniques[n]))+'}'
                #        energytex = energytex + '-' +str(int(coeff[i,n]))+'\omega_{'+str(int(uniques[n]))+'}'
                    else: #that's boring. you sent in a photon of zero frequency
                        1
        elif w<0: #ohgodohgodohgod energy is negative! help me!
            energy = energy +'(\\Omega_{n_'+str(i)+'g}^*' #complex conjugate that shit
            #energytex = energytex +'(\Omega_{n_'+str(i)+'g}^*'
            for n in xrange(len(uniques)+1):
                if coeff[i,n]==0 or n==len(uniques)+1: #see above
                    energy= energy +')'
                    #energytex= energytex +')'
                    break
                elif coeff[i,n]==1:
                    if uniques[n]<0: #outgoing photon! better add it!
                        energy = energy + '+\\omega_{'+str(-1*int(uniques[n]))+'}'
                        #energytex = energytex + '+\omega_{'+str(-1*int(uniques[n]))+'}'
                    elif uniques[n]>0: #incoming photon! SUBTRACT! SUBTRACT!
                        energy = energy + '-\\omega_{'+str(int(uniques[n]))+'}'
                        #energytex = energytex + '-\omega_{'+str(int(uniques[n]))+'}'
                    else: #that's boring. you sent in a photon of zero frequency
                        1
                else:
                    if uniques[n]<0: #outgoing photon! better add it!
                        energy = energy + '+' +str(int(coeff[i,n]))+'\\omega_{'+str(-1*int(uniques[n]))+'}'
                        #energytex = energytex + '+' +str(int(coeff[i,n]))+'\omega_{'+str(-1*int(uniques[n]))+'}'
                    elif uniques[n]>0: #incoming photon! SUBTRACT! SUBTRACT!
                        energy = energy + '-' +str(int(coeff[i,n]))+'\\omega_{'+str(int(uniques[n]))+'}'
                        #energytex = energytex + '-' +str(int(coeff[i,n]))+'\omega_{'+str(int(uniques[n]))+'}'
                    else: #that's boring. you sent in a photon of zero frequency
                        1                
        else:
            1 #do nothing.
            
    chi= '\\chi^{('+str(N-1)+')}=\sum_{all}\\frac{'+mu+'}{'+energy+'}'
                                    
# plt.plot;plt.text(0.5,0.5,'$%s$'%chi,fontsize=15)
#   plt.show()
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
    
    #this loop goes through the temporary array and keeps the unique items.
    for i in xrange(len(temp)):
        j=i+1
        while j <len(temp):
            if temp[i] == temp[j]:
                del temp[j]
            else:
                j=j+1
                
    m=np.zeros(shape=(N,len(temp))) #making a matrix
    
    #now, compare the unique items to the original input.
    #i is rows. this is equal to the number of incoming photons
    #j is columns. this is equal to the number of unique incoming photons.
    #m is a matrix that contains the coefficients that need to be in front of
    #the omegas.

    for i in xrange(N):
        w = photons[:i+1]
        for j in xrange(len(temp)):
            m[i,j]=w.count(temp[j])
            
    m = np.array(m) #I've been messing with strings here. this turns them
    temp = np.array(temp) #back in to numpy arrays so the main latex function can deal with them.
                
    return(m,temp)

