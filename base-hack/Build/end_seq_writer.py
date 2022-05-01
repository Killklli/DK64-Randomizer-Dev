'Write new end sequence text credits.'
_J='ERROR: Too many cards'
_I='bottom'
_H='right'
_G='top'
_F='left'
_E='cooldown'
_D='duration'
_C='from'
_B='text'
_A='squish'
header_length=120
names_length=160
general_buffer=154
end_buffer=204
end_sequence_cards=[{_A:{_C:_G,_D:header_length,_E:general_buffer},_B:['Developers']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['2dos','Ballaam']},{_A:{_C:_H,_D:names_length,_E:general_buffer},_B:['Bismuth','Cfox']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['GloriousLiar','KillKlli']},{_A:{_C:_H,_D:names_length,_E:general_buffer},_B:['Mittenz','Naramgamjan']},{_A:{_C:_F,_D:names_length,_E:end_buffer},_B:['Rain','ShadowShine57','Znernicus']},{_A:{_C:_G,_D:header_length,_E:general_buffer},_B:['Beta Testers']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['Auphonium','ChelseyxLynn']},{_A:{_C:_G,_D:names_length,_E:general_buffer},_B:['ChristianVega64','Connor75']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['Fuzzyness','KaptainKohl']},{_A:{_C:_G,_D:names_length,_E:general_buffer},_B:['KiwiKiller67','Nukkular Reaction']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['Obiyo','Revven']},{_A:{_C:_I,_D:names_length,_E:general_buffer},_B:['Riley','SirSmackStrikesBack']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['UsedPizza','VidyaJames']},{_A:{_C:_H,_D:names_length,_E:end_buffer},_B:['Wex','Zorulda']},{_A:{_C:_G,_D:header_length,_E:general_buffer},_B:['Additional Thanks']},{_A:{_C:_F,_D:names_length,_E:general_buffer},_B:['Game Developers',' ','Rareware Ltd','Nintendo']},{_A:{_C:_I,_D:names_length,_E:general_buffer},_B:['Crankys Lab Developer','Isotarge']},{_A:{_C:_G,_D:names_length*2,_E:general_buffer},_B:['You have been playing','DK64 Randomizer','dk64randomizer.com']},{_A:{_C:_I,_D:names_length*2,_E:general_buffer},_B:['Discord',' ','discord.dk64randomizer.com']}]
def createTextFile(directory):
	'Create the text file associated with end sequence.';B='ascii'
	if len(end_sequence_cards)>21:print(_J);exit()
	with open(f"{directory}/credits.bin",'wb')as A:
		for C in end_sequence_cards:
			for D in C[_B]:E=D.upper()+'\n';A.write(E.encode(B))
		F='*\n';A.write(F.encode(B))
def createSquishFile(directory):
	'Create the squish data associated with end sequence.';C='big'
	if len(end_sequence_cards)>21:print(_J);exit()
	D=[_G,_F,_I,_H]
	with open(f"{directory}/squish.bin",'wb')as A:
		for B in end_sequence_cards:
			E=0
			if B[_A][_C]in D:E=D.index(B[_A][_C])
			A.write(B[_A][_D].to_bytes(2,C));A.write(B[_A][_E].to_bytes(2,C));A.write(E.to_bytes(1,C));A.write(len(B[_B]).to_bytes(1,C))
		F=[]
		for G in range(6):F.append(255)
		A.write(bytearray(F))