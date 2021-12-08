with open('input8_2.txt', 'r') as inputFile:
    
    uniqueValues = 0
    totalSum = 0
    
    for line in inputFile:
        inputs = line.strip().split('|')
        unique10 = inputs[0].strip().split()
        undecipheredValue = inputs[1].strip().split()
        
        # We need to figure out which display value corresponds to which actual number
        # We know right off the bat that 8 is going to be all 7 segments active.
        hashMap = {}
        for x in range(0, 10):
            hashMap[str(x)] = ''
        hashMap['8'] = 'abcdefg'

        # In order to differentiate some digits, we need to figure out which letter 
        # corresponds to some of the segments.
        segments = {
            "top-left": '',
            "middle": '',
            "bottom-right": '',
            "bottom-left": ''
        }
        
        # 2 segments = 1
        # 3 segments = 7
        # 4 segments = 4
        # 5 segments = 2, 3, 5
        # 6 segments = 0, 6, 9
        # 7 segments = 8            
                
        #   aaa    a appears 8 times (0, 2, 3, 5, 6, 7, 8, 9)
        #  b   c   b appears 6 times (0, 4, 6, 6, 8, 9)
        #  b   c   c appears 8 times (0, 1, 2, 3, 4, 7, 8, 9)
        #  b   c  
        #   ddd    d appears 7 times (2, 3, 4, 5, 6, 8, 9)
        #  e   f   e appears 4 times (0, 2, 6, 8)
        #  e   f   f appears 9 times (0, 1, 3, 4, 5, 6, 7, 8, 9)
        #  e   f   
        #   ggg    g appears 7 times (0, 2, 3, 5, 6, 8, 9)
        
        # Looking at the above data, if we figure out how many times each segment appears, we can
        # determine some of the segments we need. (i.e. we know the bottom-left segment is the one
        # that appears 4 times)
        
        counts = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0
        }
        
        # We also know that based on the number of segments that appear, there are 3 numbers
        # with 5 segments lit and 3 numbers with 6 segments lit, so let's group those together.
        
        fives = []
        sixes = []
        
        for number in sorted(unique10, key = len):
            
            # This is where we count the number of times each segment is lit up.
            for letter in counts:
                if letter in number:
                    counts[letter] += 1
                    
            # This is where we count how many segments are lit up for each value
            # We know that if 2 segments are lit up, the value is meant to be 1
            # Similarly we can find the values for 4 and 7. We can also grab the
            # values with 5 or 6 segments lit up.
            length = len(number)
            if length == 2:
                hashMap['1'] = "".join(sorted(number))
            elif length == 3:
                hashMap['7'] = "".join(sorted(number))
            elif length == 4:
                hashMap['4'] = "".join(sorted(number))
            elif length == 5:
                fives.append("".join(sorted(number)))
            elif length == 6:
                sixes.append("".join(sorted(number)))
                        
        # Now that we have counted the segment appearances, we can determine some segments
        for count in counts:
            if counts[count] == 4:
                segments['bottom-left'] = count
            elif counts[count] == 6:
                segments['top-left'] = count
            elif counts[count] == 9:
                segments['bottom-right'] = count
                
        # Finding the value for the middle segment is a little harder.
        # We take the value for 4, remove the known top-left value, and then the
        # values that we know correspond to 1. This leaves us with the middle.
        segments['middle'] = hashMap['4']
        segments['middle'] = segments['middle'].replace(segments['top-left'], '')
        for segment in hashMap['1']:
            segments['middle'] = segments['middle'].replace(segment, '')
            
        # We have everything we need to differentiate the fives and sixes now.
        # 2, 5, and 3 each have 5 segments.
        # 2 is the only one without the bottom-right segment lit up.
        # 5 is the only one with the top-left segment lit up.
        for number in fives:
            if segments['bottom-right'] not in number:
                hashMap['2'] = number
            elif segments['top-left'] in number:
                hashMap['5'] = number
            else:
                hashMap['3'] = number
                
        # 0, 6, and 9 each have 6 segments
        # 9 is the only one without the bottom-left segment lit up.
        # 0 is the only one without the middle segment lit up.
        for number in sixes:
            if segments['bottom-left'] not in number:
                hashMap['9'] = number
            elif segments['middle'] not in number:
                hashMap['0'] = number
            else:
                hashMap['6'] = number
        
        # Now that we know the value for each number, reverse the dictionary so we can get
        # the number from the display value.
        hashMap = {v: k for k, v in hashMap.items()}
            
        # Start deciphering the unknown values!
        # Also count the number of times the unique-length values appear for pt. 1
        decipheredValue = ''
        for value in undecipheredValue:
            decipheredValue += hashMap["".join(sorted(value))]
            if len(value) in [2, 3, 4, 7]:
                uniqueValues += 1
        
        totalSum += int(decipheredValue)           
    
    print("The numbers 1, 4, 7, or 8 appear {} times in the input".format(uniqueValues))
    print("The sum of all the undeciphered numbers is {}".format(totalSum))
