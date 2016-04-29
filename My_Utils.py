# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:07:00 2016

@author:
Maximilian N. Guenther
Battcock Centre for Experimental Astrophysics,
Cavendish Laboratory,
JJ Thomson Avenue
Cambridge CB3 0HE
Email: mg719@cam.ac.uk
"""

import numpy as np
from scipy import stats
import time
import os, glob
#from mpl_toolkits.axes_grid1 import AxesGrid

        
        
def medsig(a):
    '''Compute median and MAD-estimated scatter of array a'''
    med = stats.nanmedian(a)
    sig = 1.48 * stats.nanmedian(abs(a-med))
    return med, sig   
    
    

def mystr(x,digits=0):
    if np.isnan(x): return '.'
    elif digits==0: return str(int(round(x,digits)))
    else: return str(round(x,digits))
    
    

def version_control(files='*.py', printing=True):
    #    last_created_file = max(glob.iglob(files), key=os.path.getctime)
    last_updated_file = max(glob.iglob(files), key=os.path.getmtime)
    if printing == True: 
    #    print "# Last created script: %s, %s" % ( last_created_file, time.ctime(os.path.getmtime(last_created_file)) )
    #    print "# Last updated script: %s, %s" % ( last_updated_file, time.ctime(os.path.getmtime(last_updated_file)) )
        print "# Last update: %s" % time.ctime(os.path.getmtime(last_updated_file))
        
        
        
def table_view(dic):
    from astropy.table import Table 
    dic_table = {}
    subkeys = ['OBJ_ID', 'SYSREM_FLUX3_median', 'PERIOD', 'DEPTH', 'WIDTH', 'NUM_TRANSITS']
    for key in subkeys:
            dic_table[key] = dic[key]
    dic_table = Table(dic_table)
    dic_table = dic_table[subkeys]
    print dic_table