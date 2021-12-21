with open('input20_2.txt', 'r') as inputFile:
    imageEnhancementAlgorithm = inputFile.readline().strip().replace('.', '0').replace('#', '1')
    inputFile.readline()
    image = ['00' + line.strip().replace('.', '0').replace('#', '1') + '00' for line in inputFile.readlines()]
    image = ['0' * len(image[0])] * 2 + image + ['0' * len(image[0])] * 2
    
    print("Image Enhancement Algorithm")
    print(imageEnhancementAlgorithm)
    print()
    
    litPixels = 0
    for line in image:
        litPixels += line.count('1')
    print("Input image: {} lit pixels".format(litPixels))
        
    for enhancement in range(50):
        litPixels = 0
        if imageEnhancementAlgorithm[0] == '0' or enhancement % 2 == 1:
            buffer = '0'
        else:
            buffer = '1'
            litPixels = float("inf")
        newImage = [buffer * (len(image[0]) + 2), buffer * (len(image[0]) + 2)]
        for row in range(1, len(image) - 1):
            newRow = buffer * 2
            for column in range(1, len(image[row]) - 1):
                binary = ''
                for row2 in range(row - 1, row + 2):
                    for column2 in range(column - 1, column + 2):
                        binary += image[row2][column2]
                newRow += imageEnhancementAlgorithm[int(binary, 2)]
                if newRow[-1] == '1':
                    litPixels += 1
            newRow += buffer * 2
            newImage.append(newRow)
        newImage += [buffer * (len(image[0]) + 2), buffer * (len(image[0]) + 2)]
        image = newImage
        
        print("Enhancement {}: {} lit pixels".format(enhancement + 1, litPixels))
        #for line in image:
            #print(line)
        #print()
