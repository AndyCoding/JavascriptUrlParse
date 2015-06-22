__author__ = "Andy Wong"
__copyright__ = "Copyright 2015, Andy Wong"
__credits__ = "Andy Wong"
__license__ = "GPL"
__version__ = "0.0.2"
__maintainer__ = "Andy Wong"
__email__ = "wong.andy92@gmail.com"
__status__ = "Prototype"

user_input = input('Enter your data: ')

def RemoveProperNames(user_input):
    toPrint = user_input.replace('berber_','').replace('beni_','').replace('talsint_','').replace('vintage_','')
    return toPrint

toPrint = RemoveProperNames(user_input)

navigation = "Carpet & Rugs"
category = "Vintage Rugs"

def ParseData(toPrint):
    data = toPrint.split('_')

    d = {}
    d['sku'] = data[0]
    d['country'] = data[1].capitalize()
    d['material'] = data[2].capitalize()
    d['size'] = data[3]
    d['retail_price'] = data[4]
    d['sale_price'] = data[5]
    return d

def Sku(toPrint):
    myData = ParseData(toPrint)
    sku = myData['sku']
    return sku

def Country(toPrint):
    myData = ParseData(toPrint)
    country = myData['country']
    return country

def Material(toPrint):
    myData = ParseData(toPrint)
    material = myData['material']
    return material

def Size(toPrint):
    myData = ParseData(toPrint)
    size = myData['size']
    return size

def RetailPrice(toPrint):
    myData = ParseData(toPrint)
    retail_price = myData['retail_price']
    return retail_price

def ItemTitle(toPrint):
    myData = ParseData(toPrint)
    item_title = myData['country']+" "+myData['material']+" Rug - "+SizeFormat(toPrint)
    return item_title

def Details(toPrint):
    myData = ParseData(toPrint)
    details = "&bull; "+SizeFormat(toPrint)+"<br />&bull; "+myData['material']+"<br />&bull; Each one-of-a-kind item will feature unique variations<br />&bull; Made in "+myData['country']+"<br />&bull; Please allow an additional 3-4 weeks delivery time, depending on your location"
    return details

def Care(toPrint):
    care = "To maintain the condition and extend the life of your rug, vacuum regularly and try our organic cleaning solutions. For hard-to-remove stains professional care is recommended, contact ABC Rug &amp; Carpet Cleaning Service at 212.929.1886"
    return care

def Size(toPrint):
    myData = ParseData(toPrint)
    size = myData['size']
    return size

#Size Formulas

def SizeSpliter(toPrint):
    sample = Size(toPrint)
    dimensions = sample.split('x')

    d = {}
    d['width'] = dimensions[0]
    d['length'] = dimensions[1]

    return d

def CleanUpWidth(toPrint):
    myData = SizeSpliter(toPrint)
    width = myData['width']
    return width

def CleanUpLength(toPrint):
    myData = SizeSpliter(toPrint)
    length = myData['length']
    return length

def WidthFeetInch(toPrint):
    myData = CleanUpWidth(toPrint)
    number = myData.split('-')

    d = {}
    d['foot'] = number[0]
    d['inch'] = number[1]
    return d

def LengthFeetInch(toPrint):
    myData = CleanUpLength(toPrint)
    number = myData.split('-')

    d = {}
    d['foot'] = number[0]
    d['inch'] = number[1]
    return d

def SizeFilter(toPrint):
    myData = WidthFeetInch(toPrint)
    width_ft = myData['foot']
    width_in = myData['inch']

    myData = LengthFeetInch(toPrint)
    length_ft = myData['foot']
    length_in = myData['inch']

#Over-estimation of feet
    if width_in > 0:
        width = int(width_ft)+1

    if length_in > 0:
        length = int(length_ft)+1

#Filter into Website filters

    website_size = "null" #Debug value

    if ((width_ft*12+width_in) == (length_ft*12+length_in)):
        website_size = "square"

    elif (width <= 3):
        if (length <= 5):
            website_size = "3x5"
        elif (length <= 6):
            website_size = "4x6"
        elif (length <= 7):
            website_size = "5x7"
        elif (length <= 8):
            website_size = "5x8"
        elif (length <= 9):
            website_size = "6x9"
        else:
            website_size = "runner"

    elif (width <= 4):
        if (length <= 6):
            website_size = "4x6"
        elif (length <= 7):
            website_size = "5x7"
        elif (length <= 8):
            website_size = "5x8"
        elif (length <= 9):
            website_size = "6x9"
        elif (length <= 10):
            website_size = "8x10"
        elif (length < 12):
            website_size = "8x12"
        else:
            website_size = "runner"

    elif (width <= 5):
        if (length <= 7):
            website_size = "5x7"
        elif (length <= 8):
            website_size = "5x8"
        elif (length <= 9):
            website_size = "6x9"
        elif (length <= 10):
            website_size = "8x10"
        elif (length <= 12):
            website_size = "8x12"
        elif (length <= 14):
            website_size = "10x14"
        elif (length < 15):
            website_size = "10x14+"
        else:
            website_size = "runner"

    elif (width <= 6):
        if (length <= 8):
            website_size = "6x8"
        elif (length <= 9):
            website_size = "6x9"
        elif (length <= 10):
            website_size = "8x10"
        elif (length <= 12):
            website_size = "8x12"
        elif (length <= 14):
            website_size = "10x14"
        elif (length < 18):
            website_size = "10x14+"
        else:
            website_size = "runner"

    elif (width <= 8):
        if (length <= 9):
            website_size = "8x9"
        elif (length <= 10):
            website_size = "8x10"
        elif (length <= 12):
            website_size = "8x12"
        elif (length <= 14):
            website_size = "10x14"
        elif (length < 24):
            website_size = "10x14+"
        else:
            website_size = "runner"

    elif (width <= 9):
        if (length <= 12):
            website_size = "9x12"
        elif (length <= 14):
            website_size = "10x14"
        elif (length < 27):
            website_size = "10x14+"
        else:
            website_size = "runner"

    elif (width <=10):
        if (length <= 14):
            website_size = "10x14"
        elif (length < 30):
            website_size = "10x14+"
        else:
            website_size = "runner"

    else:
        website_size = "10x14+"

    return website_size

#End of Size Formulas

def SizeFormat(toPrint):
    myData = WidthFeetInch(toPrint)
    width_ft = myData['foot'].lstrip("0")
    width_in = myData['inch'].lstrip("0")

    myData = LengthFeetInch(toPrint)
    length_ft = myData['foot'].lstrip("0")
    length_in = myData['inch'].lstrip("0")

    format_width = (width_ft+"'"+width_in+'"').replace('\'"',"'")
    format_length = (length_ft+"'"+length_in+'"').replace('\'"',"'")

    return (format_width+"x"+format_length)

def Weight(toPrint):
    myData = WidthFeetInch(toPrint)
    width_ft = myData['foot']
    width_in = myData['inch']
    total_width = (float(width_ft)*12+float(width_in))

    myData = LengthFeetInch(toPrint)
    length_ft = myData['foot']
    length_in = myData['inch']
    total_length = (float(length_ft)*12+float(length_in))

    total_weight = float(total_width)*float(total_length)/288 #Converts to Feet then /2
    return total_weight

def Output(toPrint):
    print (Sku(toPrint)+'\t'+ 			#Master SKU
           Sku(toPrint)+'\t'+ 			#SKU
           ""+'\t'+						#Brand
           ItemTitle(toPrint)+'\t'+		#Item Title
           ""+'\t'+						#Display Title
           ""+'\t'+						#Overview
           ""+'\t'+						#Slide 1
           ""+'\t'+						#Slide 2
           Details(toPrint)+'\t'+		#Details
           Care(toPrint)+'\t'+			#Care
           navigation+'\t'+				#1st Nav
           category+'\t'+				#Cat
           ""+'\t'+						#Subcat
           ""+'\t'+						#Cross Merch
           ""+'\t'+						#CM Cat
           ""+'\t'+						#CM Sub Cat
           ""+'\t'+						#Brand Page
           RetailPrice(toPrint)+'\t'+	#Retail
           ""+'\t'+						#Color
           Material(toPrint)+'\t'+		#Material
           SizeFilter(toPrint)+'\t'+	#FormSize
           ""+'\t'+						#Back Order
           ""+'\t'+						#Blank(1)
           ""+'\t'+						#Blank(2)
           ""+'\t'+						#Blank(3)
           ""+'\t'+						#Blank(4)
           str(Weight(toPrint))+'\t'	#Weight
           )

def CleanInput(toPrint):
    clean = toPrint.split('.jpg')
    count = 0
    while (clean[count] != 'done'):
        ParseData(clean[count])
        Output(clean[count])
        count = count+1

CleanInput(toPrint)