__author__ = 'Andy Wong'

#Brands and their Icons

_1921=['yes','','','','yes','','yes','']
aquasilk=['yes','','yes','yes','yes','yes','','']
ashbury=['yes','','yes','','yes','','yes','yes']
aura=['yes','','yes','yes','yes','yes','','']
bara_bara=['yes','','','yes','yes','yes','yes','']
boucherouite=['yes','','','','yes','yes','yes','']
cable_aran=['yes','','','','','','','yes']
cascade=['yes','','','','yes','','','']
chimera=['yes','','','yes','yes','','','']
cinque_terre=['yes','','yes','','yes','','','']
color_reform=['yes','','','','yes','','yes','']
color_reform_patchwork=['yes','','','','yes','','yes','']
color_reform_silk =['yes','','','','yes','','yes','']
color_reform_spectrum=['yes','','','','yes','','','']
dama=['yes','','','','yes','','yes','']
DLB=['yes','','','','yes','','yes','']
ethos=['yes','','yes','yes','yes','yes','','']
fresco=['yes','','','','yes','','yes','']
kinetic=['yes','','yes','','yes','','','']
manzara=['yes','','yes','yes','yes','yes','yes','']
masana=['yes','yes','yes','','yes','yes','','yes']
maza=['yes','','','','yes','','','']
nabati=['yes','','','yes','yes','yes','','']
nandi=['yes','yes','yes','','yes','yes','yes','']
nu_vibrant=['yes','','yes','','yes','','','']
orion=['yes','','','','yes','','','']
ovas=['yes','','','','yes','','','']
petra=['yes','','','','yes','','','']
prism=['yes','','yes','','yes','','','']
rio=['yes','','yes','','yes','','yes','']
samode=['yes','','','','yes','','','']
samoke=['yes','','','','yes','','','']
sunclipse=['yes','','yes','yes','yes','','','']
terra=['yes','','','','yes','','','']
tesselation=['yes','','','','yes','','','']
thera=['yes','','','','yes','','','']
tulu=['yes','','','yes','yes','yes','yes','yes']
umbra=['yes','','','','yes','','','']

def Icons(brand):
    print  (""+'\t'+		#clothing
           ""+'\t'+			#ship group
           ""+'\t'+			#group
           ""+'\t'+			#small
           ""+'\t'+			#good wood
           brand[7]+'\t'+	#good thread
           ""+'\t'+			#organic
           ""+'\t'+			#pure
           brand[3]+'\t'+	#good color
           ""+'\t'+			#life cycle
           ""+'\t'+			#energy conscious
           brand[1]+'\t'+	#community/coop
           brand[2]+'\t'+	#fair & square
           ""+'\t'+			#cruelty free
           ""+'\t'+			#local economy
           brand[4]+'\t'+	#handmade
           ""+'\t'+			#certified
           brand[5]+'\t'+	#indigenous
           brand[0]+'\t'+	#exclusively ABC
           ""+'\t'+			#icon count
           brand[6]+'\t'	#recycled
           )
