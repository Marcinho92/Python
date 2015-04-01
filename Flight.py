#!/usr/bin/python

import random
import time
import sys
import unittest


class Plane:
	def __init__(self):
		self.side = "centre"
		self.angle = 0

	def isCenter(self):
		if self.angle == 0 and self.side == "centre":
			return True


class Simulate:
	def __init__(self):
		self.randAngle = -1
		self.randSide = -1

	def generateParams(self):
		self.randAngle = random.randint(1, 30)
		self.randSide = random.randint(0, 1)

		if 0 < self.randAngle < 31 and -1 < self.randSide < 2:
			return True
		else:
			return False

	def checkTrajectory(self, plane):
		while plane.angle > 0:
			if plane.angle < 6:
				plane.angle = 0
				plane.side = "centre"
			else:
				plane.angle = plane.angle - 5

			print("\t Tilting: " + str(plane.angle))
			time.sleep(0.2)


'''
myPlane = Plane()
mySimulation = Simulate()

while 1:

	goodGenerating = mySimulation.generateParams()

	if goodGenerating:
		newSide = mySimulation.randSide
		newAngle = mySimulation.randAngle

	if newSide == 0:
		myPlane.side = "left"
	else:
		myPlane.side = "right"

	myPlane.angle = newAngle

	print("Plane tilted in " + myPlane.side + " side by " + str(myPlane.angle) + " degrees.")

	mySimulation.checkTrajectory(myPlane)

	if myPlane.isCenter():
		print("New plane position: " + str(myPlane.side) + ", " + str(myPlane.angle) + "\n")

	time.sleep(1)


'''