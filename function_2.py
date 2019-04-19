
# coding: utf-8

# In[ ]:


import numpy as np
from scipy.special import comb

def false_positive(r, b, s = 0):   
    if s != 0: 
        t = s
    else: 
        t = np.power((1/b),(1/r))    
    ub, lb = probability_function(lb = 0, ub = t, b = b, r= r)    
    return ub - lb 
    
def false_negative(r, b, s = 0): 
    if s != 0: 
        t = s
    else: 
        t = np.power((1/b),(1/r))    
    
    ub, lb = probability_function(lb = t, ub = 1, b = b, r = r)
    return (1 - t - (ub - lb) )
    
def probability_function(lb ,ub ,b ,r):
    
    #lb = lower bound
    #ub = upper bound 
    #b = number of bands   
    #r = number of rows
    
    #F(ub)
    s = ub    
    f_ub = s - sum([np.power(-1,p) * comb(b,p) * (1/((r*p)+1)) * np.power(s, r*p+1) for p in range(0,b)])    
    
    #F(lb)    
    s = lb     
    f_lb = s - sum([np.power(-1,p) * comb(b,p) * (1/((r*p)+1)) * np.power(s, r*p+1) for p in range(0,b)])        
    
    return f_ub, f_lb    
    

