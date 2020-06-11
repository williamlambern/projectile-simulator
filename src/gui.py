from tkinter import *
from objects import *
import random

class Gui:

    def __init__(self):
        self.master = Tk()
        self.master.title('Projectile Motion Simulator')
        self.ball = Object(10, [5,5])
        self.ball.setPosition(0,100)
        l = Label(self.master, text = 'Projectile Motion Simulator.')
        b = Button(self.master, text='New Simulation', command = lambda : self.createPopup())
        b.pack()
        self.w = Canvas(self.master, width=500, height=300)
        self.w.pack()

    def createPopup(self):
        self.popup = Toplevel()
        self.popup.title('Simulator Settings')
        self.popup.geometry('225x450')
        l1 = Label(self.popup, text='Start Position  (x,y)')
        l1.pack()
        self.setStartPosition = Entry(self.popup)
        self.setStartPosition.insert(0,'0,100')
        self.setStartPosition.pack()

        l2 = Label(self.popup, text='Mass (kg)')
        l2.pack()
        self.setMass = Entry(self.popup)
        self.setMass.insert(0, self.ball.mass)
        self.setMass.pack()

        l3 = Label(self.popup, text='Initial X Velocity (m/s)')
        l3.pack()
        self.setXVelocity = Entry(self.popup)
        self.setXVelocity.insert(0,5)
        self.setXVelocity.pack()

        l4 = Label(self.popup, text='Initial Y Velocity (m/s)')
        l4.pack()
        self.setYVelocity = Entry(self.popup)
        self.setYVelocity.insert(0,5)
        self.setYVelocity.pack()

        l5 = Label(self.popup, text='Mass Density of Fluid')
        l5.pack()
        self.setMassDensity = Entry(self.popup)
        self.setMassDensity.insert(0,self.ball.mD)
        self.setMassDensity.pack()

        l6 = Label(self.popup, text='Drag Coefficient')
        l6.pack()
        self.setDragCoefficient = Entry(self.popup)
        self.setDragCoefficient.insert(0,self.ball.dC)
        self.setDragCoefficient.pack()

        l7 = Label(self.popup, text='Environment Gravity')
        l7.pack()
        self.setGravity = Entry(self.popup)
        self.setGravity.insert(0,self.ball.g)
        self.setGravity.pack()

        l8 = Label(self.popup, text='Simulation Duration (s)')
        l8.pack()
        self.setDuration = Entry(self.popup)
        self.setDuration.insert(0,50)
        self.setDuration.pack()

        b = Button(self.popup, text='Simulate', command = lambda : self.setupSimulation())
        b.pack()

    def setupSimulation(self):
        self.ball = Object(float(self.setMass.get()), [float(self.setXVelocity.get()), float(self.setYVelocity.get())])
        self.ball.setPosition(float(self.setStartPosition.get().split(',')[0]),float(self.setStartPosition.get().split(',')[1]))
        self.ball.setMassDensity(float(self.setMassDensity.get()))
        self.ball.setDragCoefficient(float(self.setDragCoefficient.get()))
        self.ball.setGravity(float(self.setGravity.get()))
        self.simulate()

    def simulate(self):
        self.w.delete('all')
        
        coords = self.ball.simulate(int(self.setDuration.get())*1000)
        criticalPoints = self.ball.criticalPoints
        self.popup.destroy()
        for i in range(0,len(coords)-1, 10):
            x1, y1 = (int(coords[i][0])*2 - 1), (300 - int(coords[i][1])*2 - 1)
            x2, y2 = (int(coords[i][0])*2 + 1), (300 - int(coords[i][1])*2 + 1)
            self.w.create_oval(x1, y1, x2, y2, outline='blue')
        for i in range(len(criticalPoints)):
            x1, y1 = (criticalPoints[i][0] - 3), (300 - criticalPoints[i][1] - 3)
            x2, y2 = (criticalPoints[i][0] + 3), (300 - criticalPoints[i][1] + 3)
            self.w.create_oval(x1, y1, x2, y2, outline='red')

        mainloop()
