class Packet:
    def __init__(self, binaryString):
        self.version = int(binaryString[0:3], 2)
        self.packetType = int(binaryString[3:6], 2)
        self.fullBinary = binaryString[0:6]
        self.subPackets = []
        if self.packetType == 4:
            self.leftover = self.read_literal(binaryString[6:])
        else:
            self.lengthType = binaryString[6]
            self.fullBinary += self.lengthType
            
            # The next 15 bits contain the total length of the subpackets contained
            if self.lengthType == '0':
                self.read_type_zero(binaryString[7:])    
                
            # The next 11 bits are the number of subpackets contained
            else:
                self.read_type_one(binaryString[7:])
            self.value = self.calculate_value()
    
    def read_literal(self, binaryString):
        iterator = 0
        keepReading = True
        self.value = ''
        while keepReading:
            if binaryString[iterator] == '0':
                keepReading = False
            self.value += binaryString[iterator + 1 : iterator + 5]
            self.fullBinary += binaryString[iterator : iterator + 5]
            iterator += 5
        self.value = int(self.value, 2)
        return binaryString[iterator:]
                    
    def read_type_zero(self, binaryString):
        subPacketLength = int(binaryString[0:15], 2)
        unreadSubpackets = binaryString[15:15 + subPacketLength]
        self.fullBinary += unreadSubpackets
        self.leftover = binaryString[15 + subPacketLength:]
        while len(unreadSubpackets) > 0:
            subPacket = Packet(unreadSubpackets)
            unreadSubpackets = subPacket.leftover
            subPacket.leftover = ''
            self.subPackets.append(subPacket)
    
    def read_type_one(self, binaryString):
        numSubpackets = int(binaryString[0:11], 2)
        unreadSubpackets = binaryString[11:]
        while len(self.subPackets) != numSubpackets:
            subPacket = Packet(unreadSubpackets)
            unreadSubpackets = subPacket.leftover
            subPacket.leftover = ''
            self.fullBinary += subPacket.fullBinary
            self.subPackets.append(subPacket)
        self.leftover = unreadSubpackets
        
    def version_sum(self):
        total = self.version
        for subPacket in self.subPackets:
            total += subPacket.version_sum()
        return total
    
    def calculate_value(self):
        if self.packetType == 0:
            return sum([packet.calculate_value() for packet in self.subPackets])
        elif self.packetType == 1:
            product = 1
            for packet in self.subPackets:
                product *= packet.calculate_value()
            return product
        elif self.packetType == 2:
            return min([packet.calculate_value() for packet in self.subPackets])
        elif self.packetType == 3:
            return max([packet.calculate_value() for packet in self.subPackets])
        elif self.packetType == 4:
            return self.value
        elif self.packetType == 5:
            if len(self.subPackets) != 2:
                return "ERROR"
            return int(self.subPackets[0].calculate_value() > self.subPackets[1].calculate_value())
        elif self.packetType == 6:
            if len(self.subPackets) != 2:
                return "ERROR"
            return int(self.subPackets[0].calculate_value() < self.subPackets[1].calculate_value())
        elif self.packetType == 7:
            if len(self.subPackets) != 2:
                return "ERROR"
            return int(self.subPackets[0].calculate_value() == self.subPackets[1].calculate_value())
    
    def __repr__(self):
        if self.packetType == 4:
            return "{{\"Value\": {}, \"Version\": {}, \"Type\": {}}}".format(self.value, self.version, self.packetType)
        else:
            return "{{\"Value\": {}, \"Version\": {}, \"Type\": {}, \"Length Type\": {}, \"Subpackets\": {}}}".format(self.value, self.version, self.packetType, self.lengthType, self.subPackets)
        

with open('input16_1.txt', 'r') as inputFile:
    hexData = inputFile.readline().strip()
    print("Hex data:", hexData)
    binaryData = bin(int('1' + hexData, 16))[3:]
    print("Binary translation:", binaryData)
    packetData = Packet(binaryData)
    print("Packet information:", packetData)
    print("Total sum of versions: {}".format(packetData.version_sum()))
    print("Value of outermost packet:", packetData.value)