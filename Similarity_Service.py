import numpy as np
from scipy.interpolate import interp1d

def similiar(currency, compare, linespaces, linespace_max, threshold):
        
    x = np.linspace(0, linespaces, num=linespace_max)
    x2 = np.linspace(0, linespaces, num=linespace_max)                      
    same = False                  
    f = interp1d(x, currency)
    f2 = interp1d(x2, compare)
    points = 15
    xnew = np.linspace ( min(x), max(x), num = points)
    xnew2 = np.linspace ( min(x2), max(x2), num = points)
    ynew = f(xnew)
    ynew2 = f2(xnew2)                      
    sim = (np.corrcoef(ynew, ynew2)) 

    similarity = str(sim[0][1])
    similarity = float(similarity)
    
    if (similarity >= threshold):
        same = True                          
    return same