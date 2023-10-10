import random
import math
def EstimatePi(IterationCount):
    CurrentCount = 0
    OutsideCircle = 0
    InsideCircle = 0
    while CurrentCount < IterationCount:
        XRandom = random.random() - 0.5 #Between [-0.5, 0.5]
        YRandom = random.random() - 0.5
        #Finding distance of point to see if it lies in the circle
        Distance = math.sqrt(XRandom**2 + YRandom**2)
        #Checking if it lies in the circle
        if (Distance > 0.5):
            OutsideCircle+=1
        else:
            InsideCircle+=1
        # Ratio is 4R^2 : pi*R^2 = 4 : pi = Point landed in Inside+Outside : Inside
        PiEstimate = 4*(InsideCircle/(InsideCircle+OutsideCircle))
        print("Estimate number: "+str(CurrentCount + 1)+ ": "+str(PiEstimate))
        CurrentCount+=1
    return PiEstimate
EstimatePi(10000)