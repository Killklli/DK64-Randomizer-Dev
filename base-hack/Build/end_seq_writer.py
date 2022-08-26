'Write new end sequence text credits.'
_J='ERROR: Too many cards'
_I='bottom'
_H='right'
_G='left'
_F='top'
_E='cooldown'
_D='duration'
_C='from'
_B='text'
_A='squish'
import os,sys
header_length=120
names_length=160
general_buffer=154
end_buffer=204
end_sequence_cards=[{_A:{_C:_F,_D:header_length,_E:general_buffer},_B:['Randomizer Developers']},{_A:{_C:_G,_D:names_length,_E:general_buffer},_B:['2dos','Ballaam','Bismuth']},{_A:{_C:_H,_D:names_length,_E:general_buffer},_B:['Cfox','KillKlli','Lrauq']},{_A:{_C:_G,_D:names_length,_E:general_buffer},_B:['Naramgamjan','ShadowShine57','Znernicus']},{_A:{_C:_F,_D:header_length,_E:general_buffer},_B:['Assistant Developers']},{_A:{_C:_H,_D:names_length,_E:general_buffer},_B:['AlmostSeagull','GloriousLiar']},{_A:{_C:_G,_D:names_length,_E:end_buffer},_B:['Mittenz','OnlySpaghettiCode','Rain']},{_A:{_C:_F,_D:header_length,_E:general_buffer},_B:['Beta Testers']},{_A:{_C:_G,_D:names_length,_E:general_buffer},_B:['Adam Whitmore','Auphonium','CandyBoots']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['ChelseyXLynn','ChristianVega64','Connor75']},{_A:{_C:_G,_D:names_length,_E:general_buffer},_B:['CornCobx0','Fuzzyness','KaptainKohl']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['KiwiKiller67','Nukkuler']},{_A:{_C:_G,_D:names_length,_E:general_buffer},_B:['Obiyo','Revven','Riley']},{_A:{_C:_I,_D:names_length,_E:general_buffer},_B:['SirSmackStrikesBack','UsedPizza','VidyaJames']},{_A:{_C:_H,_D:names_length,_E:end_buffer},_B:['Wex','Zorulda']},{_A:{_C:_F,_D:header_length,_E:general_buffer},_B:['Additional Thanks']},{_A:{_C:_G,_D:names_length,_E:general_buffer},_B:['Game Developers',' ','Rareware Ltd','Nintendo']},{_A:{_C:_I,_D:names_length,_E:general_buffer},_B:['Crankys Lab Developer','Isotarge']},{_A:{_C:_H,_D:names_length,_E:general_buffer},_B:['SpikeVegeta','KeiperDontCare']},{_A:{_C:_F,_D:names_length*2,_E:general_buffer},_B:['You have been playing','DK64 Randomizer','dk64randomizer.com']},{_A:{_C:_I,_D:names_length*2,_E:general_buffer},_B:['Discord',' ','discord.dk64randomizer.com']}]
def createTextFile(directory):
	'Create the text file associated with end sequence.';C='ascii';A=directory
	if not os.path.exists(A):os.mkdir(A)
	if len(end_sequence_cards)>21:print(_J);sys.exit()
	with open(f"{A}/credits.bin",'wb')as B:
		for D in end_sequence_cards:
			for E in D[_B]:F=E.upper()+'\n';B.write(F.encode(C))
		G='*\n';B.write(G.encode(C))
def createSquishFile(directory):
	'Create the squish data associated with end sequence.';C='big'
	if len(end_sequence_cards)>21:print(_J);sys.exit()
	D=[_F,_G,_I,_H]
	with open(f"{directory}/squish.bin",'wb')as A:
		for B in end_sequence_cards:
			E=0
			if B[_A][_C]in D:E=D.index(B[_A][_C])
			A.write(B[_A][_D].to_bytes(2,C));A.write(B[_A][_E].to_bytes(2,C));A.write(E.to_bytes(1,C));A.write(len(B[_B]).to_bytes(1,C))
		F=[]
		for G in range(6):F.append(255)
		A.write(bytearray(F))