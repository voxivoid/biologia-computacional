import random
import math

class Point:
    def __init__(self, coords):
        self.coords = coords
        self.n = len(coords)

class Cluster:
    def __init__(self, points):
        self.points = points
        self.centroid = self.calculateCentroid()

    def calculateCentroid(self):
        numPoints = len(self.points)
        coords = [p.coords[:-1] for p in self.points]
        unzipped = zip(*coords)
        centroidCoords = [math.fsum(dList)/numPoints for dList in unzipped]
        return Point(centroidCoords)

    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        shift = getDistance(oldCentroid, self.centroid)
        return shift

def kmeans(points, k, cutoff, maxItereations):
    centroids = random.sample(points, k) #k random points to be the centroids
    clusters = [Cluster([p]) for p in centroids]
    iterations = 1

    while True:
        lists = [[] for c in range(k)]
        print iterations

        for p in points:
            smallestDistance = getDistance(p, clusters[0].centroid)
            clusterIndex = 0
            for i in range(1, k):
                distance = getDistance(p, clusters[i].centroid)
                if distance < smallestDistance:
                    smallestDistance = distance
                    clusterIndex = i
            lists[clusterIndex].append(p)

        biggestShift = 0.0

        for i in range(k):
            shift = clusters[i].update(lists[i])
            biggestShift = max(biggestShift, shift)

        if biggestShift < cutoff:
            break

        if iterations > maxItereations:
            break

        iterations += 1
    return clusters


def getDistance(a, b):
    ret = reduce(lambda x,y: x + pow((a.coords[y]-b.coords[y]), 2),range(a.n - 1),0.0)
    return math.sqrt(ret)


def main():
    f = open(u".\\LAB4\\input", "r")
    lines = int(f.readline())
    columns = int(f.readline())

    points = []
    for i in range(lines):
        line = str(f.readline())[:-1]
        coords = line.split(',')
        points.append(coords)

    f.close()

    processedPoints = processPoints(points)
    processedPoints = [Point(c) for c in processedPoints]
    clusters = kmeans(processedPoints, 2, 1, 500)

    f = open(u".\\LAB4\\output", "w")
    for i in range(len(clusters)):
        f.write("CLUSTER " + str(i) + "\n")
        f.write("Centroid: " + str(clusters[i].centroid.coords) + "\n")
        for j in range(len(clusters[i].points)):
            f.write(str(clusters[i].points[j].coords[-1]) + " " + str(clusters[i].points[j].coords) + "\n")
    f.close()

def processPoints(points):
    transposedPoints = [list(a) for a in zip(*points)]
    transposedProcessedPoints = []
    for i in range(len(transposedPoints) - 1):
        transposedProcessedPoints.append([])
        n = 0
        sum = 0
        for j in range(len(transposedPoints[0])):
            if points[j][i] == "?":
                transposedProcessedPoints[i].append(points[j][i])
                continue
            n += 1
            sum += float(points[j][i])
            transposedProcessedPoints[i].append(float(points[j][i]))
        avg = sum / float(n)
        for j in range(len(transposedPoints[0])):
            if points[j][i] == "?":
                transposedProcessedPoints[i][j] = avg
    transposedProcessedPoints.append(transposedPoints[-1])

    processedPoints = [list(a) for a in zip(*transposedProcessedPoints)]

    return processedPoints

main()