class rec:
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
    def area(self):
        
        self.a = self.x * self.y
        
        return(self.a)
    
    def area_mm_m(self):
        
        self.a = (self.x)/1000 * (self.y)/1000
        
        return(self.a)
    
    def perimeter(self):
        
        self.p = 2 * self.x + 2 * self.y
        
        return(self.p)
    
class cuboid_vol:
    
    def __init__(self,x,y,z):
    
        self.x = x
        self.y = y
        self.z = z
        
    def v_calc(self):
        
        self.v = self.x * self.y * self.z
        
        return(self.v)
    
    
class volume:
    
    def __init__(self,area,length):
        
        self.area = area
        self.length = length
        
    def v_calc(self):
        
        self.v = self.area * self.length
        
        return(self.v)
    
class point_load:
    
    def __init__(self,force,length):
        
        self.force = force
        self.length = length
        
    def eff_force(self):
        
        #Effective Force at Centroid of Universal Load
        self.ef = self.force * self.length
        
        return(self.ef)
    
class uniform_load:
    #force per unit of length
    def __init__(self,force,length):
         
        self.force = force
        self.length = length
        
    def eff_force(self):
            
        self.ef = self.force * self.length
        
        return(self.ef)
        
    def eff_distance(self):
        
        self.ed = self.length/2
        
        return(self.ed)
    
