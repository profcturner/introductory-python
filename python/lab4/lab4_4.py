# A turtle listing from the docs
# Import everything in exactly the way we advised against
# put your name here
from turtle import *

color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        # this is new, it stops a loop
        break
end_fill()
done()
