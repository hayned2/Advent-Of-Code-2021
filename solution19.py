class Scanner:
    def __init__(self, number):
        self.number = number
        self.beacons = []
        self.mapped = False
        self.position = "Unknown"
        self.nonOverlappingBeacons = []
    
    def addBeacon(self, beacon):
        self.beacons.append(beacon)
        
    def rotatePerspective(self, rotation):
        return [pointRotations(beacon, rotation) for beacon in self.beacons]
        
    def __repr__(self):
        return "{}             \t{}              \t{}".format(self.number, len(self.beacons), self.position)
    
    def mapScanner(self, scannerPosition, beaconPositions):
        self.mapped = True
        self.position = scannerPosition
        self.beacons = beaconPositions

def pointRotations(point, rotation):
    (x, y, z) = point
    if rotation == 0: return (x, y, z)
    if rotation == 1: return (y, z, x)
    if rotation == 2: return (z, x, y)
    if rotation == 3: return (z, y, -x)
    if rotation == 4: return (y, x, -z)
    if rotation == 5: return (x, z, -y)
    if rotation == 6: return (x, -y, -z)
    if rotation == 7: return (y, -z, -x)
    if rotation == 8: return (z, -x, -y)
    if rotation == 9: return (z, -y, x)
    if rotation == 10: return (y, -x, z)
    if rotation == 11: return (x, -z, y)
    if rotation == 12: return (-x, y, -z)
    if rotation == 13: return (-y, z, -x)
    if rotation == 14: return (-z, x, -y)
    if rotation == 15: return (-z, y, x)
    if rotation == 16: return (-y, x, z)
    if rotation == 17: return (-x, z, y)
    if rotation == 18: return (-x, -y, z)
    if rotation == 19: return (-y, -z, x)
    if rotation == 20: return (-z, -x, y)
    if rotation == 21: return (-z, -y, -x)
    if rotation == 22: return (-y, -x, -z)
    if rotation == 23: return (-x, -z, -y)
    
def calculateOffset(knownBeacon, unknownBeacon):
    return (knownBeacon[0] - unknownBeacon[0], knownBeacon[1] - unknownBeacon[1], knownBeacon[2] - unknownBeacon[2])

def applyOffset(position, offset):
    return (position[0] + offset[0], position[1] + offset[1], position[2] + offset[2])

def translateBeacons(beacons, offset):
    return [applyOffset(beacon, offset) for beacon in beacons]

def attemptToMap(unknownScanner, allScanners):
    
    # We need to compare our unknown scanner to all scanners that have been mapped
    # If we already attempted to map an unknown scanner with a specific known scanner, there's no need to try again, they don't overlap
    for knownScanner in allScanners or knownScanner.number in unknownScanner.nonOverlappingBeacons:
        if not knownScanner.mapped:
            continue
        
        # We will try to change our perspective between all 24 possible orientations until we can find the same one as our mapped scanner
        for rotation in range(24):
            
            # Once we have our beacons in a given orientation, we need to attempt to find matches between pairs of beacons
            unknownBeacons = unknownScanner.rotatePerspective(rotation)
            for unknownBeacon in unknownBeacons:
                
                # Calculate the shift necessary to match a given known and unknown beacon.
                # Apply that same shift to all unknown beacons.
                # If we get 12 or more matches, we can map the unknown beacon.
                for knownBeacon in knownScanner.beacons:
                    offset = calculateOffset(knownBeacon, unknownBeacon)
                    translatedUnknownBeacons = translateBeacons(unknownBeacons, offset)
                    if len(translatedUnknownBeacons + knownScanner.beacons) - len(set(translatedUnknownBeacons + knownScanner.beacons)) >= 12:
                        unknownScanner.mapScanner(applyOffset((0, 0, 0), offset), translatedUnknownBeacons)
                        return True
        unknownScanner.nonOverlappingBeacons.append(knownScanner.number)
    return False
            
with open('input19_3.txt', 'r') as inputFile:
    
    lines = inputFile.readlines()
    scanners = []
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
        if lines[x][0:3] == '---':
            scanners.append(Scanner(int(lines[x].replace('--- scanner ', '').replace(' ---', ''))))
        elif len(lines[x]) > 0:
            scanners[-1].addBeacon(tuple(int(num) for num in lines[x].strip().split(',')))
    scanners[0].mapScanner((0, 0, 0), scanners[0].beacons)
    x = 0
    while x < len(scanners):
        if scanners[x].mapped:
            x += 1
            continue
        if attemptToMap(scanners[x], scanners):
            x = 0
            continue
        else:
            x += 1
            continue
        
    print("Scanner Number\tBeacons In Range\tPosition")
    print("--------------\t----------------\t--------")
    allBeacons = []
    allPositions = []
    for scanner in scanners:
        print(scanner)
        allBeacons += scanner.beacons
    print("There are a total of {} beacons detected by these scanners".format(len(set(allBeacons))))
    
    furthestDistance = 0
    furthestScanners = []
    for scanner1 in scanners:
        for scanner2 in scanners:
            distance = sum([abs(distance) for distance in calculateOffset(scanner1.position, scanner2.position)])
            if distance > furthestDistance:
                furthestDistance = distance
                furthestScanners = [scanner1.number, scanner2.number]
    print("The two scanners that are farthest apart are Scanner {} and Scanner {}, with a distance of {}".format(furthestScanners[0], furthestScanners[1], furthestDistance))
    
    
        
    
