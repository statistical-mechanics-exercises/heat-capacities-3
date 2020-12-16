import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_y)==9, "you do not have the correct number of data points in your graph" )
        filedata = np.loadtxt("md_results.txt")
        for i in range(len(this_x) ) :
            tmid = ( filedata[i,0] + filedata[i+1,0] ) / 2
            self.assertTrue( np.abs(tmid - this_x[i])<1E-6, "one or more of the temperatures on the x-axis of your graph are incorrect"  )
            tmid = (filedata[i+1,1] - filedata[i,1]) / (filedata[i+1,0] - filedata[i,0]) 
            self.assertTrue( np.abs(tmid - this_y[i])<1E-6, "one or more of the heat capacities you have calculated is incorrect" )
