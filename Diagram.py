######################################################
#Matplot_casade_diagram_module:
#
#Program description: This module consists of many small programs 
#   that are called in the main program chain_diagram.  The purpose
#   of this program is to draw feynmann diagrams that show the 
#   process of casading.
#
#Last update: 5/9/14 (Goler)
#
#####################################################


import matplotlib.pyplot as plt; plt.rcdefaults()

from matplotlib.pyplot import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from matplotlib.path import Path
import matplotlib.lines as mlines
import matplotlib.patches as patches


def molecule (vertices):
    """
    input:
        vertices = the number of vertices in the desired Feynmann diagram
    output:
        molecule = a picture of the molecule
        verts = the locations where photons interact with the molecule
    How to run:
        type molecule(vertices): except replace vertices with any positive 
        integer e.g. molecule(5)
        
        hit enter
    """
    
    # define font array for labels
    font = {'family': 'Bitstream Vera Sans',
            'color':'darkred',
            'weight':'normal',
            'size':16}

    #create excited state labels       
    dummy = []
    
    #fill the dummy array with apropriate labels
    for i in range(0,vertices):
        num = str(i)
        label = 'n'+num
        dummy = np.append(dummy,label)
    
    # create a two deminsional array of an appropriate length
    verts = [[0. , 0.] for i in range(1,vertices+3)]
    
    plt.text(2,0,'',fontdict=font)
    
    # fill the values in verts
    for j in range (1, vertices+1):
        verts[j][0] = 3
        verts[j][1] = 3 * j
        rise = j  
        if (j != vertices):  
            plt.text(2.3,3*j+ 1.5, '',fontdict=font)
        else:
            plt.text(2,3*j + 2,'',fontdict=font)
            
    verts[vertices+1][0] = 0 
    verts[vertices+1][1] = (rise + 1)*3
       
    # create arrays xs and ys for ploting    
    xs,ys = zip(*verts)
    
    # plot values in verts
    plt.plot(xs,ys)
    
    plt.show()
    
    return verts

#module that rotates an array of numbers about the origin
def rotate_it (sign,xs,ys):
    """
    inputs:
        sign = positive or negative one, indicates direction of the rotation
        xs = array of numbers for the x values 
        ys = array of numbers for the y values
    outputs:
        newx = rotated array for x values
        newy = rotated array for y values
    """
    
    #loop that applies the rotation matrix to each value of the array
    if (sign < 0):
        angle = np.pi/4
    else:
        angle = -1 * np.pi/4
    newx = xs * np.cos(angle) - ys * np.sin(angle)
    newy = xs * np.sin(angle) + ys * np.cos(angle)
    
    return (newx,newy)

#module that draws a rotated sign wave
def photon_v3(sign, vert, labels,vertual):
    """
    input:
        sign = any real number
        vert = a tuple e.g. (1.0,2.0)
        labels = array of strings to label the wave
        vertual = determins wether or not to extend the wave
            and connect it to another diagram
    output:
        draws a tilted sine wave
    example run:
        type "photon_v3(20,(1,1))" see the tilted sign wave.
        ^ ## The above example doesn't work! - Adam ##
    """
    
    newx = []
    newy = []
    
    x = np.linspace(0, 1.5*np.pi, num = 200)
    xsin = np.linspace(0, len(x), num = 200)
    sines = .1 * np.sin(.25*xsin)
    
    for i in range(0, len(x)):
        value = rotate_it(sign,x[i],sines[i])
        newx = np.append(newx,value[0]+vert[0])
        newy = np.append(newy,value[1]+vert[1])
        
    #plot the sinewave in the appropriate place
    line = plt.plot(newx,
                     newy,
                     linewidth = 2,
                     label = labels)
        

    #legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    legend()
    plt.show()
    
    if (vertual == 1):
        connector = photon_v3(sign,(newx[-1],newy[-1]),'',2)
        return connector
    if (vertual == 2):
        return (newx[-1],newy[-1])

def diagram (array):
    """
    inputs:
        array = a multideminsional ordered array containing the frequencies and 
            polarizations of photons.
    outputs:
        picture = a Feynmann diagram consisting of the single molecule 
            interaction with the photons
    """
    # define font array for labels
    font = {'family': 'Bitstream Vera Sans',
            'color':'darkred',
            'weight':'normal',
            'size':16}
    
    #create labels for the photons
    dummy = [] 
      
    for i in range(0,len(array)):
        w = str(array[i][0]) 
        p = str(array[i][1]) 
        label = 'E' + '('+ w +','+ p + ')'
        dummy = np.append(dummy,label)
    
    # define input value for functions
    vertices = len(array)
    
    # build the molecule and obtain returned value
    verts = molecule(vertices)
    
    # call function photons the correct number of times and input values
    for i in range(1,len(verts)-1):
        
        if( array[i-1][0] < 0):
            sign = -1
        else:
            sign = 1
        if(array[i-1][1] != 3):
            photon_v3(sign,verts[i],'',0)  
        else:
            connector = photon_v3(sign,verts[i],'',1)  
        
         
    
    plt.xlim(-2,verts[len(verts)-1][1])
    plt.ylim(-2,verts[len(verts)-1][1]+3)   
    plt.show()

def chain_molecule (vertices, connector,vert_num):
    """
    input:
        vertices = the number of vertices in the desired Feynmann diagram
        connector = the vertex where the virtual photon interacts (1,2)
        vert_num = the order of the vertex that contains the virtual photon
    output:
        molecule = a picture of the molecule
        verts = the locations where photons interact with the molecule
    How to run:
        type molecule(vertices): except replace vertices with any positive 
        integer e.g. molecule(5)
        
        ^ ## The above example doesn't work! -Adam ##
        
        hit enter
    """
    vert_num = vert_num+1
    
    # define font array for labels
    font = {'family': 'Bitstream Vera Sans',
            'color':'darkred',
            'weight':'normal',
            'size':16}

    #create excited state labels       
    dummy = []
    
    #for i in range(0,vertices+1):
    #    num = str(i)
    #    label = 'n'+num
    #    dummy = np.append(dummy,label)
    
    
    # create a two deminsional array of an appropriate length
    verts = [[connector[0]+3 , connector[1]-3*vert_num] for i in range(1,vertices+3)]
    
    plt.text(2,0,'o',fontdict=font)
    
    # fill the values in verts
    for j in range (1, vertices+1):
        verts[j][0] = connector[0]
        verts[j][1] = connector[1]-3*vert_num + 3 * j
        rise = j  
        if (j != vertices):  
            plt.text(2.3,3*j+ 1.5, '',fontdict=font)
        else:
            plt.text(2,3*j + 2,'',fontdict=font)
            
    verts[vertices+1][0] = connector[0]-3
    verts[vertices+1][1] = connector[1]-3*vert_num + (rise + 1)*3
       
    # create arrays xs and ys for ploting    
    xs,ys = zip(*verts)
    
    # plot values in verts
    plt.plot(xs,ys)
    
    plt.show()
    
    return verts[0:vert_num] + verts[1+vert_num:vertices+2]

def chain_diagram (photons_1,photons_2,connector,vert_num):
    """
    inputs:
        photons_1 = a multideminsional ordered array containing the frequencies and 
            polarizations of photons. e.g. ((1,1),(1,1),(-1,3))
        photons_2 = same as photons_1, will be applied to the second 
            diagram.  
        connector = currently does nothing(eventually will extend the diagram)
        ^ ## Says it does nothing, but the code is used below...? -Adam ##
        
        vert_num = integer value less than len(photons_2)
            determines which vertex the virtual photon will hit 
    outputs:
        picture = a Feynmann diagram consisting of the single molecule 
            interaction with the photons
    Example:
        input below command:
            chain_diagram(((1,1),(-1,3),(1,1)),((1,3),(-1,3),(-1,1),(1,3),(1,1),(1,1)),1,0)
            
            note: The program does not check if energy is conserved during the 
                  cascade.  Also, the list of second photons needs to include
                  a virtual, incoming photon.  If it does not then the module 
                  will break.
                  
                  The program does not check to make sure that vert_num is 
                  less than the length of the second array of photon tuples.
                  The program will still run.
                  
                  The window needs to be adjusted for some of the values of
                  vert_num.
                  
        wait and look at the picture the module drew

    """
    # define font array for labels
    font = {'family': 'Bitstream Vera Sans',
            'color':'darkred',
            'weight':'normal',
            'size':16}
    
    #create labels for the photons
    dummy = [] 
      
    #for i in range(0,len(photons_1)+len(photons_2)):
    #    w = str(array[i][0]) 
    #    p = str(array[i][1]) 
    #    label = 'E' + '('+ w +','+ p + ')'
    #    dummy = np.append(dummy,label)
    
    # define input value for functions
    vertices_1 = len(photons_1)
    
    # build the molecule and obtain returned value
    verts_1 = molecule(vertices_1)
    
    # call function photons the correct number of times and input values
    for i in range(1,len(verts_1)-1):
        
        if( photons_1[i-1][0] < 0):
            sign = -1
        else:
            sign = 1
        if(photons_1[i-1][1] != 3):
            photon_v3(sign,verts_1[i],'',0)  
        else:
            connector = photon_v3(sign,verts_1[i],'',1)
    
    #define input value for functions   
    vertices_2 = len(photons_2)
    
    #build the cascading molecule
    verts_2 = chain_molecule(vertices_2,connector,vert_num) 
    
    #Delete the correct virtual photon from the list to make room for 
    #  the plot of the virtual photon
    for i in range(len(photons_2)):
        
        if(photons_2[i][1] == 3 and photons_2[i][0] > 0):
            new_photons_2 = photons_2[0:i] + photons_2[1+i:]
            
    #call function for plotting photons the correct number of times
    if(vert_num != 0):
        photon_v3(-1,[verts_2[0][0]-2*np.pi,verts_2[0][1]],'',0)
    else:
        photon_v3(1,verts_2[1],'',0)
    
    for i in range(2,len(verts_2)-1):
        
        if( new_photons_2[i-1][0] < 0):
            sign = -1
        else:
            sign = 1
        if(new_photons_2[i-1][1] != 3):
            photon_v3(sign,verts_2[i],'',0)  
        else:
            connector = photon_v3(sign,verts_2[i],'',1)     
    
    plt.xlim(-2,verts_2[len(verts_2)-1][1])
    plt.ylim(-2,verts_2[len(verts_2)-1][1]+3)   
    plt.show()