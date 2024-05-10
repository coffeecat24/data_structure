class Car:
    def __init__(self,color,speed=0):
        self.color=color 
        self.speed=speed
        
    def speedUp(self): 
        self.speed+=10
        
    def speedDown(self):
        self.speed-=10
    
    def isEqual(self, other):
        if self.color==other.color: return True
        else: return False
    
    def __eq__(self,other):
        return "YES" if self.color==other.color else "NO"
    
    def __str__(self) -> str:
        return "color = %s, speed = %d"%(self.color,self.speed)

    def __ge__(self,other):
        return "Faster" if self.speed>=other.speed else "Slower"
        
if __name__ =='__main__':
    car1=Car('black')
    car2=Car('red',120)
    car3=Car('yellow')
    
    car1.speedUp()
    car2.speedDown()
    
    print("color : %s - speed : %d" %(car1.color,car1.speed))
    print("color : %s - speed : %d" %(car2.color,car2.speed))
    print("color : %s - speed : %d" %(car3.color,car3.speed))
    
    print(car1.isEqual(car2))
    print(car1>=car2)
    
    print(car1)