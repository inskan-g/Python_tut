import sys
sys.path.append('C:/WPy64-3980/python-3.9.8.amd64/Lib/site-packages')

import pandapower as pp
import pandapower.networks as nw
net = nw.simple_four_bus_system()

pp.runpp(net)
print(net.res_bus)
# print(net.res_line)
# print(net.res_trafo)


