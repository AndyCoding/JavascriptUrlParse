brands = [
    '1921_10001010_vintage_', 'aquasilk_10111100_silk_overdyed', 
    'ashbury_10101011_moroccan_', 'aura_10111100_silk_', 
    'barabara_10011110_vintage_', 'cablearan_10001001_contemp_moroccan', 
    'cascade_10001000_contemp_', 'chimera_10011000_silk_', 
    'cinqueterre_10101000_contemp_', 'colorreform_10001010_overdyed_vintage', 
    'crpatchwork_10001010_overdyed_', 'crsilk_10001010_silk_overdyed', 
    'crspectrum_10001000_overdyed_', 'dama_10001010_vintage_', 
    'dlb_10001010__', 'ethos_10111100_silk_', 'fez_10011000_flatweave_', 
    'fresco_10001010_vintage_', 'kinetic_10101000_contemp_', 
    'lumina_10001000_contemp_silk', 'manzara_10111110_contemp_', 
    'masana_11101101_flatweave_', 'maza_10001000_flatweave_', 
    'nabati_10011100_flatweave_', 'nandi_11101110_flatweave_', 
    'nuvibrant_10101000_contemp_silk', 'orion_10001000_contemp_', 
    'ovas_10001000_contemp_', 'petra_10001000_flatweave_', 
    'prism_10101000_contemp_silk', 'rio_10101010_contemp_silk', 
    'samoke_10001000_classic_silk', 'sunclipse_10111000_silk_', 
    'terra_10001000_contemp_', 'tesselation_10001000_contemp_', 
    'thera_10001000_contemp_', 'tulu_10011111_vintage_moroccan', 
    'umbra_10001000_contemp_',
            ] # List of all the Brands
materials = [
    'Aloe', 'Alpaca', 'Bamboo', 'Banana', 'Cotton',
    'Cowhide', 'Fiber', 'Hemp', 'Jute', 'Lambskin',
    'Leather', 'Linen', 'Paper', 'Polyester', 'Polypropylene',
    'Seagrass', 'Shearling', 'Sheepskin', 'Silk', 'Sisal',
    'Tencel', 'Viscose', 'Wool' , 'Yard'
               ] # List of all Materials
countries = [
    ['Afghanistan','Afghan'], ['Belgium','Belgium'], ['China','Chinese'], 
    ['India','Indian'], ['Iran','Persian'], ['Mongolia','Mongolian'], 
    ['Morocco','Moroccan'], ['Nepal','Nepal'], ['Pakistan','Pakistani'], 
    ['Philippines','Filipinos'], ['Romania','Romanian'], ['Russia','Russian'], 
    ['South Africa','South African'], ['Tibet','Tibetan'], ['Turkey','Turkish'], 
    ['Uzbekistan''Uzbekistani']
                ]	#List of all Countries

def FindBrandIcon(toPrint,database):

    data = toPrint.split('_')

    for x in range (0,len(database)):
        data = database[x].split('_')
        if data[0] in toPrint:
            # Brand | Icons | Cat | CMCat | String
            return [data[0],data[1],data[2],data[3],
                    toPrint.replace(data[0].rstrip('\n')+'_','')]
def FindSKU(toPrint):
    data = toPrint.split('_',1)
    
    return data
def FindMaterial(toPrint,database):
    material_list = []
    for x in range (0,len(database)):
        if database[x].lower() in toPrint.lower():
            material_list.append(database[x])
            
    #Special cases for certain combinations of materials
    def SpecialCases(mat1,mat2):
        if mat1 and mat2 in material_list:
            material_list.remove(mat1)
            material_list.remove(mat2)
            material_list.append(mat1+' '+mat2)
    SpecialCases('Aloe','Fiber')
    SpecialCases('Bamboo','Silk')
    SpecialCases('Banana','Silk')   
    SpecialCases('Wool','Sisal')
    
    if len(material_list) == 1:
        material_string = (material_list[0],material_list[0])
    else:
        material_string = (material_list[0]+' & '+material_list[1]),(material_list[0]+'/'+material_list[1])
    
    return material_string
def SortIcons(toPrint): 
    icons_list = []
    for x in range (0,len(str(toPrint))):
        icons_list.append(toPrint[x])
        
    return icons_list
def CompilePrint(toPrint):
    data = FindBrandIcon(toPrint)
    icons = SortIcons(data[1])
    
    if data[3] != '':
        cross_merch = "Carpet & Rugs"
    else:
        cross_merch = ''
        
    def BinaryConvert(binary_input):
        if binary_input == '1':
            return "yes"
        else:
            return ""
    
    d={}
    
    d['brand'] = data[0]
    d['first_nav'] = "Carpet & Rugs"
    d['cat'] = data[2]
    d['cm'] = cross_merch
    d['cm_cat'] = data[3]
    d['exclusive'] = BinaryConvert(icons[0])
    d['community'] = BinaryConvert(icons[1])
    d['fairsquare'] = BinaryConvert(icons[2])
    d['goodcolor'] = BinaryConvert(icons[3])
    d['handmade'] = BinaryConvert(icons[4])
    d['indigenous'] = BinaryConvert(icons[5])
    d['recycled'] = BinaryConvert(icons[6])
    
    return d
def FindCountry(toPrint,database):
    country_list = []
    for x in range (0,len(database)):
        if str(database[x][0]).lower() in toPrint:
            country_list.append(database[x])
            
    #Special cases for certain Countries
    def SpecialCases(before,after):
        if before in country_list:
            before = after
            
    SpecialCases('Afghanistan','Pakistan')
    
    return country_list

#Family of Size Functions Begin
def LocateSize(toPrint):
    data = toPrint.split('_')

    for x in range (0,len(data)):
        if data[x][3] == 'x':
            return data[x]
def SizeSpliter(toPrint): # Seperates width & length
    dimensions = toPrint.split('x')
    
    d = {}
    d['width'] = dimensions[0]
    d['length'] = dimensions[1]
    
    return d
def FeetInchFormat(toPrint): # Formats measurements
    measurement = toPrint.split('-')
    
    d={}
    d['feet'] = measurement[0]
    d['inch'] = measurement[1]
    return d
def FindSize(toPrint):
    
    d={}
    d['width_feet'] = FeetInchFormat(SizeSpliter(LocateSize(toPrint))['width'])['feet']
    d['width_inch'] = FeetInchFormat(SizeSpliter(LocateSize(toPrint))['width'])['inch']
    d['length_feet'] = FeetInchFormat(SizeSpliter(LocateSize(toPrint))['length'])['feet']
    d['length_inch'] = FeetInchFormat(SizeSpliter(LocateSize(toPrint))['length'])['inch']
    return d
def DisplaySize(toPrint):
    width = (FindSize(toPrint)['width_feet']).lstrip("0")+"'"+(FindSize(toPrint)['width_inch']).lstrip("0")+'"'
    length = (FindSize(toPrint)['length_feet']).lstrip("0")+"'"+(FindSize(toPrint)['length_inch']).lstrip("0")+'"'
    size_format = width.replace('\'"',"'")+'x'+length.replace('\'"',"'")
    return size_format

def SizeFilter(toPrint): # Format to website filters
    website_size = 'null' # Debug value
    
    width_feet = int(FindSize(toPrint)['width_feet'])
    width_inch = int(FindSize(toPrint)['width_inch'])
    length_feet = int(FindSize(toPrint)['length_feet'])
    length_inch = int(FindSize(toPrint)['length_inch'])
    
    if (length_feet*12+length_inch)-(width_feet*12+width_inch) < 1:
        website_size = "square"
        
    elif (width_feet*3 <= length_feet):
        website_size = "runner"
        
    elif (width_feet+1 <= 3):
        if (length_feet+1 <= 5):
            website_size = "3x5"
        elif (length_feet+1 <= 6):
            website_size = "4x6"
        elif (length_feet+1 <= 7):
            website_size = "5x7"
        elif (length_feet+1 <= 8):
            website_size = "5x8"
        elif (length_feet+1 <= 9):
            website_size = "6x9"            
        else:
            website_size = "runner"

    elif (width_feet+1 <= 4):
        if (length_feet+1 <= 6):
            website_size = "4x6"
        elif (length_feet+1 <= 7):
            website_size = "5x7"
        elif (length_feet+1 <= 8):
            website_size = "5x8"
        elif (length_feet+1 <= 9):
            website_size = "6x9"
        elif (length_feet+1 <= 10):
            website_size = "8x10"
        elif (length_feet+1 < 12):
            website_size = "8x12"
        else:
            website_size = "runner"
            
    elif (width_feet+1 <= 5):
        if (length_feet+1 <= 7):
            website_size = "5x7" 
        elif (length_feet+1 <= 8):
            website_size = "5x8"
        elif (length_feet+1 <= 9):
            website_size = "6x9"
        elif (length_feet+1 <= 10):
            website_size = "8x10"
        elif (length_feet+1 <= 12):
            website_size = "8x12"
        elif (length_feet+1 <= 14):
            website_size = "10x14"
        elif (length_feet+1 < 15):
            website_size = "10x14+"
        else:
            website_size = "runner"  
        
    elif (width_feet+1 <= 6):
        if (length_feet+1 <= 8):
            website_size = "6x8"
        elif (length_feet+1 <= 9):
            website_size = "6x9"
        elif (length_feet+1 <= 10):
            website_size = "8x10"
        elif (length_feet+1 <= 12):
            website_size = "8x12"
        elif (length_feet+1 <= 14):
            website_size = "10x14"
        elif (length_feet+1 < 18):
            website_size = "10x14+"
        else:
            website_size = "runner"
        
    elif (width_feet+1 <= 8):
        if (length_feet+1 <= 9):
            website_size = "8x9"
        elif (length_feet+1 <= 10):
            website_size = "8x10"
        elif (length_feet+1 <= 12):
            website_size = "8x12"
        elif (length_feet+1 <= 14):
            website_size = "10x14"
        elif (length_feet+1 < 24):
            website_size = "10x14+"
        else:
            website_size = "runner" 
        
    elif (width_feet <= 9):
        if (length <= 12):
            website_size = "9x12"
        elif (length <= 14):
            website_size = "10x14"
        elif (length < 27):
            website_size = "10x14+"  
        else:
            website_size = "runner"
        
    elif (width_feet+1 <=10):
        if (length_feet+1 <= 14):
            website_size = "10x14"
        elif (length_feet+1 < 30):
            website_size = "10x14+"
        else:
            website_size = "runner" 
        
    else:
        website_size = "10x14+"
        
    return website_size
#Family of Size Functions End

def Weight(toPrint):
    width_ft = (FindSize(toPrint)['width_feet'])
    width_in = (FindSize(toPrint)['width_inch'])
    total_width = (float(width_ft)*12+float(width_in))

    length_ft = (FindSize(toPrint)['length_feet'])
    length_in = (FindSize(toPrint)['length_inch'])
    total_length = (float(length_ft)*12+float(length_in))
    
    total_weight = float(total_width)*float(total_length)/288 #Converts to Feet then /2
    return total_weight
def BinaryConversion(toPrint):
    if toPrint == ['1']:
        response = 'yes'
    else:
        response = ''
    return response
def CrossMerch(toPrint):
    if FindBrandIcon(toPrint,brands)[3] != None:
        return 'Carpet & Rugs'
    else:
        return ''
    

def Output(toPrint):
    
    care_string = "To maintain the condition and extend the life of your rug, vacuum regularly and try our organic cleaning solutions. For hard-to-remove stains professional care is recommended, contact ABC Rug &amp; Carpet Cleaning Service at 212.929.1886"
    
    print (
    FindSKU(toPrint)[0]+'\t'+							#Master SKU
    FindSKU(toPrint)[0]+'\t'+							#SKU
    FindBrandIcon(toPrint,brands)[0].capitalize()+'\t'+	#Brand
    FindBrandIcon(toPrint,brands)[0].capitalize()+' '+str(FindCountry(toPrint,countries)[0][1])+' '+str(FindMaterial(toPrint,materials)[0])+' Rug - '+DisplaySize(toPrint)+'\t'+
    FindBrandIcon(toPrint,brands)[0].capitalize()+' <br/>'+str(FindCountry(toPrint,countries)[0][1])+' '+str(FindMaterial(toPrint,materials)[0])+' Rug <br/>'+DisplaySize(toPrint)+'\t'+
    ''+'\t'+											#Overview
    FindBrandIcon(toPrint,brands)[0].capitalize()+'\t'+	#Slide 1
    ''+'\t'+											#Slide 2
    ''+'\t'+											#Details
    care_string+'\t'+									#Care
    'Carpet & Rugs'+'\t'+								#1st Nav
    FindBrandIcon(toPrint,brands)[2]+'\t'+				#Cat
    ''+'\t'+											#Subcat
    CrossMerch(toPrint)+'\t'+							#Cross Merch
    FindBrandIcon(toPrint,brands)[3]+'\t'+				#CM Cat
    ''+'\t'+											#CM Subcat
    FindBrandIcon(toPrint,brands)[0].capitalize()+'\t'+	#Brand Page
    ''+'\t'+											#Retail
    ''+'\t'+											#Color
    str(FindMaterial(toPrint,materials)[1])+'\t'+		#Materials
    SizeFilter(toPrint)+'\t'+							#Size
    ''+'\t'+											#Back Order
    str(Weight(toPrint))+'\t'+							#Weight
    ''+'\t'+                                          	#Clothing
    ''+'\t'+                                         	#Ship Group
    ''+'\t'+                                        	#Group
    ''+'\t'+                                        	#Small
    ''+'\t'+											#goodwill
    str(BinaryConversion(SortIcons(FindBrandIcon(sample,brands)[1][7])))+'\t'+	#goodthread
    ''+'\t'+																	#organic
    ''+'\t'+    																#pure
    str(BinaryConversion(SortIcons(FindBrandIcon(sample,brands)[1][3])))+'\t'+	#goodcolor
    ''+'\t'+    																#lifecycle
    ''+'\t'+    																#energyconscious
    str(BinaryConversion(SortIcons(FindBrandIcon(sample,brands)[1][1])))+'\t'+	#community/coop
    str(BinaryConversion(SortIcons(FindBrandIcon(sample,brands)[1][2])))+'\t'+	#fair&square
    ''+'\t'+    																#crueltyfree
    ''+'\t'+    																#localeconomy
    str(BinaryConversion(SortIcons(FindBrandIcon(sample,brands)[1][4])))+'\t'+	#handmade
    ''+'\t'+    																#certified
    str(BinaryConversion(SortIcons(FindBrandIcon(sample,brands)[1][5])))+'\t'+	#indigenous
    str(BinaryConversion(SortIcons(FindBrandIcon(sample,brands)[1][0])))+'\t'+	#exclusive
    ''+'\t'+    																#iconcount
    str(BinaryConversion(SortIcons(FindBrandIcon(sample,brands)[1][7])))+'\t'	#recycled
        )
    
sample = "1234567_nuvibrant_india_cotton_wool_6-9x12-9_1000_500.jpg"

#print (SortIcons(FindBrandIcon(sample,brands)[1][7]))
#print FindSKU(sample)
#print FindMaterial(sample,materials)
print (FindBrandIcon(sample,brands)[0])
#print SortIcons(FindBrandIcon(sample,brands)[1][0])

Output(sample)
    