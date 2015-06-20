__author__ = "Andy Wong"
__copyright__ = "Copyright 2015, Andy Wong"
__credits__ = "Andy Wong"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Andy Wong"
__email__ = "wong.andy92@gmail.com"
__status__ = "Prototype"

toPrint = input('Enter your data: ')

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
    item_title = myData['country']+" "+myData['material']+" "+Size(toPrint)
    return item_title

def Details(toPrint):
    myData = ParseData(toPrint)
    details = "&bull; "+myData['size']+"<br />&bull; "+myData['material']+"<br />&bull; Each one-of-a-kind item will feature unique variations<br />&bull; Made in "+myData['country']+"<br />&bull; Please allow an additional 3-4 weeks delivery time, depending on your location"
    return details

def Care(toPrint):
    care = "To maintain the condition and extend the life of your rug, vacuum regularly and try our organic cleaning solutions. For hard-to-remove stains professional care is recommended, contact ABC Rug &amp; Carpet Cleaning Service at 212.929.1886"
    return care

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
           ""+'\t'+						#FormSize (Pending)
           ""+'\t'+						#Back Order
           ""+'\t'+						#Blank(1)
           ""+'\t'+						#Blank(2)
           ""+'\t'+						#Blank(3)
           ""+'\t'+						#Blank(4)
           ""+'\t'						#Weight
           )

def CleanInput(toPrint):
    clean = toPrint.split('.jpg')
    count = 0
    while (clean[count] != 'done'):
        ParseData(clean[count])
        Output(clean[count])
        count = count+1

CleanInput(toPrint)