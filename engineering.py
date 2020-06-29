#Unit Conversion Classes
class unit_c:
    
    def __init__(self,x):
        
        self.x = x
        
    def mm_m(self):
        
        #Millimeters to Metres
        
        self.l = self.x/1000
        
        return(self.l)


class rec:
    
    #Rectangular Shape Calculations
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
    def area(self):
        
        return(self.x * self.y)
    
    def perimeter(self):
        
        return(2 * self.x + 2 * self.y)
    
class circle_r:
    
    #Circle Shape Calculations using Radius
    
    def __init__(self,radius):
        
        self.radius = radius
        
    def area(self):
        
        p = 3.141
        
        return(p*self.radius**2)
    
    def perimeter(self):
        
        pi = 3.141
        
        return(pi*2*self.radius)
    
class cuboid:
    
    #3D Cuboid Calculations
    
    def __init__(self,x,y,z):
    
        self.x = x
        self.y = y
        self.z = z
        
    def volume(self):
        
        return(self.x * self.y * self.z)

    
class i_beam:
    
    def __init__(self,D,B,t,T,r):
        
        self.D = D
        self.B = B
        self.t = t
        self.T = T
        self.r = r
        
    def area(self):
        
        return(2*(rec(self.B,self.T).area()) + (rec((self.D-2*self.T),self.t).area()) + (rec(2*self.r,2*self.r).area() - circle_r(self.r).area()))

    def depth_b_fillet(self):
        
        self.d_b_f = self.D - (2*self.r) - (2*self.T)
        
        return(self.d_b_f)
    
    def ratio_loc_buck_flange(self):
        
        return(self.B/(2*self.T))
    
    def ratio_loc_buck_web(self):
    
        self.rlb_w = self.depth_b_fillet()/self.t
        
        return(self.rlb_w)
        
class volume_3d:
    
    #3D Shape Volume Calculation (Requires Cross-Sectional Area and Length)
    
    def __init__(self,area,length):
        
        self.area = area
        self.length = length
        
    def volume(self):
        
        self.v = self.area * self.length
        
        return(self.v)
    
    
#Basic Structural Calculations (Moments, UDL's,TDL's, etc.)
    
class point_load:
    
    def __init__(self,force,length):
        
        self.force = force
        self.length = length
        
    def moment(self):
        
        #Effective Force at Centroid of Universal Load
        
        self.m = self.force * self.length
        
        return(self.m)
    
class uni_tri_load:
    
    #Force per unit of Length
    
    def __init__(self,force,length):
         
        self.force = force
        self.length = length
        
    def uni_eff_force(self):
            
        self.ef = self.force * self.length
        
        return(self.ef)
        
    def uni_eff_distance(self):
        
        self.ed = self.length/2
        
        return(self.ed)
    
    def tri_eff_force(self):
        
        self.ef = (self.force * self.length)/2
        
        return(self.ef)
    
    def tri_eff_distance(self):
        
        self.ed = self.length/3
        
        return(self.ed)
    
    def tri_eff_distance_inv(self):
        
        self.ed = (2*self.length)/3
        
        return(self.ed)