# Time-stamp : Thu Nov 29 12:09:04 CST 2007 angenent
from grapher import *
from math import *

roundPoint(

setViewBox(-1.7,-4,2.5,1.5)
openOutputFile("09bowl",220)

line([-0.25, 0], [2.25, 0])
line([0, -0.25], [0, 1.5])
plot(lambda x:1+x, lambda x:x*x, -1,1)
h=0.25
a=1-sqrt(h)
b=1+sqrt(h)
linewidth(2)
line([a,h], [b,h])
linewidth(1)
C = [0, -2]
roundPoint(C, b, fillcolor='lightGray')
roundPoint(C, a, fillcolor='white')
aa, bb = a-0.03, b-0.03
arrow(C, [C[0]+0.5*aa, C[1]+0.5*sqrt(3)*aa], 5, 2)
arrow(C, [C[0]+0.5*sqrt(3)*bb, C[1]-0.5*bb], 5, 2)

setdash("[3] 0")
linewidth(0.5)
line([0, h], [a, h])
line([a, 0], [a, h])
line([a,-0.25], [a, -2])
line([b,0], [b, h])
line([b,-0.25], [b, -2])
line([0, -0.25], C)
line([0,1], [2,1])
line([2,0], [2,1])
setdash("[] 0")
roundPoint([a,h], 0.025, fillcolor='white')
roundPoint([b,h], 0.025, fillcolor='white')
roundPoint(C, 0.025, fillcolor='white')

annotate([2,1], [-12,4], "$y=(x-1)^2$")
annotate([a, h], [0, 4], "$A$")
annotate([b, h], [-4, 4], "$B$")
annotate([a, 0], [-2, -10], "$r_{\\mathrm{in}}$")
annotate([C[0]+0.25*a, C[1]+0.25*sqrt(3)*a], [2, -6], "$r_{\\mathrm{in}}$")
annotate([b, 0], [-2, -10], "$r_{\\mathrm{out}}$")
annotate([C[0]+0.25*sqrt(3)*b, C[1]-0.25*b], [6, 0], "$r_{\\mathrm{out}}$")
annotate([2.3, 0], [0, 0], "$x$")
annotate([0, 1], [-7, -1], "1")
annotate([1, 0], [-2, -10], "1")
annotate([2, 0], [-2, -10], "2")
annotate([0, h], [-7, -1], "$y$")
annotate([-sqrt(b*b-a*a), C[1] - a], [12, -12],
         "Area$=\\pi r_{\\mathrm{out}}^2-\\pi r_{\\mathrm{in}}^2$")

annotate([-1,1], [0,0], makeboxc("SIDE VIEW:") )
annotate([-1,C[1]+b], [0,0], makeboxc("TOP VIEW:") )

closeOutputFile()


