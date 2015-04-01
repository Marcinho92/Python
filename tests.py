__author__ = 'Marcin'

import unittest
import Flight


class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Flight.Plane()

    def testPlaneIsCenter(self):
        assert self.plane.isCenter() == True, "plane isCenter() failed"

    def testPlaneSideIsString(self):
        assert type(self.plane.side) == type(str()), "plane side is not a string"

    def testPlaneIsAngleInPartition(self):
        assert 0 <= self.plane.angle <= 30, "plane angle is not in partition"


class TestSimulate(unittest.TestCase):

    def setUp(self):
        self.simulate = Flight.Simulate()

    def testSimulateGenerateParams(self):
        assert self.simulate.generateParams() == True, "simulate generateParams() generates wrong values"



if __name__ == "__main__":
    unittest.main()

