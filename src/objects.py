


class Object:

    def __init__(self, mass, vel): # e.g Object(kg, [Vx,Vy])
        self.mass = mass
        self.velocity = vel
        
        self.g = -9.80665
        self.mD = 1 # air at 0 degrees
        self.dC = 0.047  # a sphere
        self.acceleration = [0,self.g]
        
        self.positions = []
        self.criticalPoints = [] # record bounces/turning points

    def setPosition(self, x,y):
        self.position = [x,y]
        return self.position

    def setMassDensity(self, mD):
        self.mD = mD

    def setGravity(self, g):
        self.g = g

    def setDragCoefficient(self, dC):
        self.dC = dC

    def simulateDrag(self):
        # x
        fx = self.mass * self.acceleration[0]
        df = 0.5 * self.mD * (self.velocity[0]**2) * (3.14159) * self.dC # drag force according to https://en.wikipedia.org/wiki/Drag_equation
        if fx >= 0:
            rf = fx - df
            self.acceleration[0] = (rf/self.mass)
            self.velocity[0] += self.acceleration[0]/1000
        else:
            rf = fx + df
            self.acceleration[0] = (rf/self.mass)
            self.velocity[0] += self.acceleration[0]/1000
        
        # y
        fy = self.mass * self.g
        df = 0.5 * self.mD * (self.velocity[1]**2) * (3.14159) * self.dC
        if self.velocity[1] >= 0:
            rf = fy - df
        else:
            rf = fy + df
        self.acceleration[1] = (rf/self.mass)
        self.velocity[1] += self.acceleration[1]/1000
        

    def simulate(self,time):   # eg simulate(ms)
        self.criticalPoints = []
        for i in range(time):
            # Vy
            if self.position[1] > 0:
                self.position[1] += self.velocity[1]/1000
            else:
                self.criticalPoints.append([i,0])
                self.velocity[1] = -1*self.velocity[1]
                self.position[1] = 0.1
            # Vx
            self.position[0] += self.velocity[0]/1000

            # y collision
            if self.position[1] < 0:
                self.position[1] = 0
                
            self.positions.append([self.position[0], self.position[1]])
            self.simulateDrag()
            
        return self.positions


ball = Object(5, [0,0])
ball.setPosition(0,10)

