# basicRemoteSensing v0.0
# author: Jason Yi
# jtyi@ucdavis.edu
# Last Revised: August 11, 2020
# Description: This file simulates a basic topological remote sensor. A n x n 3D
# surface represented by a n x n array. The values in the array represent the z values.
# The x and y values are represented by the length of the array. The surface is
# assumed to reflect 100% and the wave used reflects at zero degrees.
# The sensor will be placed at a constant z value and will scan only when 
# directly above a point. The speed of the wave is constant.

# This is a basic remote sensor simulation and is not intended to accurately
# simulate an actual remote sensor. This simulation is more of a proof of
# concept. This simulation does not yet account for the wave striking an angled
# surfaces nor absorption. This functionality will be added in later versions.

# To improve accuracy, either decrease the waveSpeed, or decrease the time step.

# CODE BELOW

#for stochastic surface
import random

#initalize global variables
sensorHeight = 100 # units; what z value the sensor scans from.
waveSpeed = 1 # units/second; the faster the wave, the more accurate the scan.
surfaceSize = 10    # units; defines length and width of the surface
                    # for surfaceSize, I had issues with displaying the
                    # array's for surfaceSize > 10. It works with larger
                    # numbers, but results are difficult to see
minimumZ = 100
MAXIMUMZ = 0    # the minimum is larger than the maximum as the minimumZ is defined as the
                # closest z value the surface can be to the scanner, and the maximumZ is defined
                # as the furthet z value the surface can be to the scanner.

# generates surface with stochastic elevation
def surfaceGenerator(n,minZ,maxZ):
    generate = [[0 for x in range(n)]for y in range(n)]
    for i in range(n):
        for j in range(n):
            z = random.randint(minZ,maxZ)
            generate[i][j] = z
    return generate

# scans surface with remote sensor and generates "image"
def scan(toScan):
    # initalizes the array which will store the scan
    scan = [[0 for x in range(len(toScan))]for y in range(len(toScan))]
    # grabs and stores the distance at the point of the scan
    # this value is used to simulate the wave travelling to the point
    for i in range(len(toScan)):
        for j in range(len(toScan[i])):
            toTravel = toScan[i][j] + sensorHeight
            received = False
            seconds = 0
            # starts wave simulation, checking the distance travelled each second
            while(not received):
                seconds += 1
                travelled = waveSpeed * seconds
                # checks distance travelled and stops if it has collided with
                # the surface
                if travelled >= toTravel:
                    seconds *= 2
                    received = True
            scan[i][j] = (waveSpeed * (seconds/2)) - sensorHeight
    return scan

# to print arrays in a readable fashion
def arrayPrint(toPrint):
    for i in range(len(toPrint)):
        print(toPrint[i])
    return

# prints out the surfaces
surface = surfaceGenerator(surfaceSize,MAXIMUMZ,minimumZ)
scanned = scan(surface)
print("Actual Surface")
arrayPrint(surface)
print("Scan of Surface")
arrayPrint(scanned)

# END CODE

