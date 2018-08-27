from gurobipy import *
import numpy as np
import math
import readIn


def solve(full_path_instance):
    
    n, r, b, d, g, h, s = readIn.readFile(full_path_instance)
    
    # indexshifting so that i lands at 1 instead of 0, as demanded in the exercise
    n=n+1
    
    
    #-Define model variables----------------------------------------------
    
    model = Model("scheduling")

    # at which time does plane i land?
    x = {}
    for i in range(1,n):
        x[i] = model.addVar(lb=r[i],vtype=GRB.INTEGER, obj=0, name="x_"+str(i))
        
    # penalty cost for landing too early       
    y = {}
    for i in range(1,n):
        y[i] = model.addVar(lb=0,vtype=GRB.INTEGER, obj=0, name="y_"+str(i))
            
    # penalty cost for landing too late
    z = {}
    for i in range(1,n):
        z[i] = model.addVar(lb=0,vtype=GRB.INTEGER, obj=0, name="z_"+str(i))
        
    # does i land before j?
    u = {}
    for i in range(1,n):
       for j in range(1,n):
          if j != i:
             u[i,j] = model.addVar(lb=0,ub=1,vtype=GRB.INTEGER, obj=0, name="u_"+str(i)+"_"+str(j))
    
    # big M
    M={}
    M = max(r)
    for i in range(1,n):
       for j in range(1,n):
           if(i < j):
               M = M + s[i][j]
               
 
    model.update()
  
    
    #-Add constraints-----------------------------------------------
    
    # earliest possible landing point
    for i in range(1,n):
        model.addConstr(x[i] >= r[i], name = 'c0')
        
    # latest possible landing point
    for i in range(1,n):
        model.addConstr(x[i] <= d[i], name = 'c1')
    
    # assign costs for landing too early        
    for i in range(1,n):
        model.addConstr(y[i] >= (b[i] - x[i])*g[i], name = 'c2')
        
    # assign costs for landing too late
    for i in range(1,n):
        model.addConstr(z[i] >= (x[i] - b[i])*h[i], name = 'c3')

    # buffer times between two landings
    for i in range(1,n):
       for j in range(1,n):
           if i != j:
               # buffer times is at least s[i][j]
               model.addConstr(x[i] - x[j] + M*u[i,j] <= (M-s[i][j]), name = 'c4')
           if i < j:
               # either i lands before j, or the other way around
               model.addConstr(u[i,j] + u[j,i] == 1, name = 'c5')

                         
               
    # set the objective to the sum of all costs (starting early + starting late penalties)
    model.setObjective(quicksum(y[i]+z[i] for i in range(1,n)))
            
    
    
    model.optimize()
    
    
    
    #-Print result----------------------------------------------
    if model.status == GRB.status.OPTIMAL:
        for i in range(1,n):
            #print('Flugzeug %s landet bei Zeitschritt %s' % (i, x[i].x))
            #print('z: %s' % (z[i].x))
            pass
            
            
    return model
            

# call the method to see the results
solve('airland1.txt')

