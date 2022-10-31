'Write new end sequence text credits.'
_I='ERROR: Too many cards'
_H='longheader'
_G='ascii'
_F='bottom'
_E='right'
_D='header'
_C='left'
_B='top'
_A='normal'
import os,sys,requests as rs
is_v2_release=False
csv_url='https://docs.google.com/spreadsheets/d/e/2PACX-1vTjqxasaI40I2zf3RG9_7Vv-H1grc2JMhy_C08SZkW9MFApNaZ8ARnUDRfA0QrgCi874s9efWxhy6mW/pub?gid=1075755893&single=true&output=csv'
basher_names=[]
if is_v2_release:
	try:
		res=rs.get(url=csv_url);txt=res.content.decode(_G);bigbugbashers=txt.split('\r\n')[1:];basher_names=[]
		for b in bigbugbashers:
			if len(b.split(',')[1])>0:basher_names.append(b.split(',')[1])
	except rs.exceptions.HTTPError as err:raise SystemExit(err)
header_length=120
names_length=160
general_buffer=154
end_buffer=204
class CreditItem:
	'Credit Squish Item.'
	def __init__(A,squish_from,subtype,text):
		'Initialize with given data.';B=subtype;A.squish_from=squish_from;A.duration=names_length;A.cooldown=general_buffer
		if B==_D:A.duration=header_length
		elif B==_H:A.duration=names_length*2
		A.text=text
main_devs=[CreditItem(_B,_D,['Randomizer Developers']),CreditItem(_C,_A,['2dos','AlmostSeagull','Ballaam']),CreditItem(_E,_A,['Bismuth','Cfox','KillKlli']),CreditItem(_C,_A,['Lrauq','ShadowShine57','Znernicus'])]
assistant_devs=[CreditItem(_B,_D,['Assistant Developers']),CreditItem(_E,_A,['GloriousLiar','Mittenz']),CreditItem(_C,_A,['Naramgamjan','OnlySpaghettiCode','Rain'])]
beta_testers=[CreditItem(_B,_D,['Beta Testers']),CreditItem(_C,_A,['Adam Whitmore','Auphonium','CandyBoots','ChelseyXLynn','ChristianVega64']),CreditItem(_E,_A,['Connor75','CornCobx0','Fuzzyness','KaptainKohl','KiwiKiller67']),CreditItem(_C,_A,['Nukkuler','Obiyo','Revven','Riley']),CreditItem(_F,_A,['SirSmackStrikesBack','UsedPizza','VidyaJames','Wex','Zorulda'])]
bbb_contest=[CreditItem(_B,_D,['Big Bug Bashers']),CreditItem(_E,_A,basher_names)]
additional_thanks=[CreditItem(_B,_D,['Additional Thanks']),CreditItem(_C,_A,['Game Developers',' ','Rareware Ltd','Nintendo']),CreditItem(_F,_A,['Crankys Lab Developer','Isotarge']),CreditItem(_E,_A,['SpikeVegeta','KeiperDontCare'])]
links=[CreditItem(_B,_H,['You have been playing','DK64 Randomizer','dk64randomizer.com']),CreditItem(_F,_H,['Discord',' ','discord.dk64randomizer.com'])]
end_sequence_cards=[]
end_sequence_cards.extend(main_devs)
end_sequence_cards.extend(assistant_devs)
if not is_v2_release:end_sequence_cards.extend(beta_testers)
if len(basher_names)>0 and is_v2_release:end_sequence_cards.extend(bbb_contest)
end_sequence_cards.extend(additional_thanks)
end_sequence_cards.extend(links)
def createTextFile(directory):
	'Create the text file associated with end sequence.';A=directory
	if not os.path.exists(A):os.mkdir(A)
	if len(end_sequence_cards)>21:print(_I);sys.exit()
	with open(f"{A}/credits.bin",'wb')as B:
		for C in end_sequence_cards:
			for D in C.text:E=D.upper()+'\n';B.write(E.encode(_G))
		F='*\n';B.write(F.encode(_G))
def createSquishFile(directory):
	'Create the squish data associated with end sequence.';C='big'
	if len(end_sequence_cards)>21:print(_I);sys.exit()
	D=[_B,_C,_F,_E]
	with open(f"{directory}/squish.bin",'wb')as A:
		for B in end_sequence_cards:
			E=0
			if B.squish_from in D:E=D.index(B.squish_from)
			A.write(B.duration.to_bytes(2,C));A.write(B.cooldown.to_bytes(2,C));A.write(E.to_bytes(1,C));A.write(len(B.text).to_bytes(1,C))
		F=[]
		for G in range(6):F.append(255)
		A.write(bytearray(F))