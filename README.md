# circleAreaIteration

### About
This is a program I worked on during my first year of university. It takes a fairly common theory on deriving the area of a circle and demonstrates the algorithm practically.

### The Mathsy Part
The program uses a technique which involves the ratio of areas between two 2-Dimensional shapes: a square and a circle. The ratio between these two shapes can be derived by first assigning a side length, `2r` where `r` is the radius of the circle and half the length of a side of the square. With these values in mind we can calculate the areas of both shapes: `4r^2` and `πr^2` for the square and circle respectively. Next we calculate the area of the overlapping regions. The circle makes up exactly `πr^2` SA, and the square cut-out is `4r^2 - πr^2`. 

Therefore, the ratio of the two regions simplifies down to `4 : π`. 

We then use random number generation to select random coordinates. We use the ratio of these points as such; `PiEstimation = 4 * InC / (InC + OsC)` where `InC` stand for 'inside circle' and `Osc`, 'outside circle.'

### How to use
Simpily download the program and run through a Python IDE or, for a faster result, through command like `% Python{3} PythonPiFinder.py`

For greater iterations, change the size of the parameter given to `EstimatePi(Int)`

### To Do's
* Change the iteration number to be given by a sys.argv
* Refine the program for better estimates
* Create a GUI to visualise the process
