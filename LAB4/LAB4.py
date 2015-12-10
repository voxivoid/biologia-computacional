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
        r = self.removeUnknowns(unzipped)
        centroidCoords = [math.fsum(dList)/numPoints for dList in r]
        return Point(centroidCoords)

    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        shift = getDistance(oldCentroid, self.centroid)
        return shift

    def removeUnknowns(self, unzipped):
        result = []
        for i in range(len(unzipped)):
            n = 1
            sum = 0
            result.append([])
            for j in range(len(unzipped[i])):
                if(unzipped[i][j] == "?"):
                    result[i].append("")
                    continue
                result[i].append(float(unzipped[i][j]))
                n += 1
                sum += result[i][j]
            avg = sum / float(n)
            for j in range(len(unzipped[i])):
                if(unzipped[i][j] == "?"):
                    result[i][j] = avg
        return result

def kmeans(points, k, cutoff):
    centroids = random.sample(points, k) #k random points to be the centroids
    clusters = [Cluster([p]) for p in centroids]

    while True:
        lists = [[]] * k

        for p in points:
            smallestDistance = getDistance(p, clusters[0].centroid)
            clusterIndex = 0
            for i in range(1, k - 1):
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
    return clusters


def getDistance(a, b):
    ret = reduce(lambda x,y: x + pow((a.coords[y]-b.coords[y]), 2),range(a.n - 1),0.0)
    return math.sqrt(ret)


def readFromFile():
    f = open(u".\\LAB4\\input", "r")
    lines = int(f.readline())
    columns = int(f.readline())

    points = []

    for i in range(lines):
        line = str(f.readline())[:-1]
        coords = line.split(',')
        points.append(Point(coords))

    clusters = kmeans(points, 2, 0.5)

readFromFile()