from pattern import *
from grid import *

p = Pattern()
p.add_operation('+1')
p.add_operation('+5')
p.add_operation('+4')

g = Grid(10, 10, 0, 123, p)
g.generate_grid()
g.print_grid()

print(p.humanize())
