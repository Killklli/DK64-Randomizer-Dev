'Generate list of all permutations for Kong Rando with a given ruleset.'
_H=False
_G='factory'
_F='icetemple'
_E='llama'
_D='japes'
_C='starting'
_B='puzz'
_A='lock'
import math
traps=[_D,_E,_F,_G]
trap_names=['Jungle Japes','Llama Temple','Tiny Temple','Frantic Factory']
roles=[_A,_B]
role_names=['Locked','Puzzle']
def numToBase(n,b,d):
	'Convert number n to base b with number of digits d.'
	if n==0:A=[0]
	else:
		A=[]
		while n:A.append(int(n%b));n//=b
	if len(A)<d:
		B=d-len(A)
		for C in range(B):A.append(0)
	return A[::-1]
random_ruleset={_C:[0,1,2,3,4],_D:{_A:[0,1,2,3,4],_B:[0,1,2,3,4]},_E:{_A:[0,1,2,3,4],_B:[0,2,3]},_F:{_A:[0,2,3,4],_B:[1]},_G:{_A:[0,1,2,3,4],_B:[2,3]}}
random_ruleset_free_llama_temple={_C:[0,1,2,3,4],_D:{_A:[0,1,2,3,4],_B:[0,1,2,3,4]},_E:{_A:[0,1,2,3,4],_B:[0,1,2,3,4]},_F:{_A:[0,2,3,4],_B:[1]},_G:{_A:[0,1,2,3,4],_B:[2,3]}}
vanilla_ruleset={_C:[0,1,2,3,4],_D:{_A:[0,1,2,3,4],_B:[0,1,2,3,4]},_E:{_A:[1,2,3,4],_B:[0]},_F:{_A:[0,2,3,4],_B:[1]},_G:{_A:[0,1,3,4],_B:[2]}}
expanded_random={_C:[0,1,2,3,4],_D:{_A:[0,1,2,3,4],_B:[0,1,2,3,4]},_E:{_A:[0,1,2,3,4],_B:[0,1,2,3,4]},_F:{_A:[0,1,2,3,4],_B:[1,4]},_G:{_A:[0,1,2,3,4],_B:[0,1,2,3,4]}}
ruleset=expanded_random
total_perm=0
checks=0
fail_by_invalid_lock=0
fail_by_unreachable_kongs=0
fail_by_nonmatching_ruleset=0
total_verif=0
unreach_kongs_total=[0,0,0,0,0,0]
balance={_C:[0,0,0,0,0],_D:{_A:[0,0,0,0,0],_B:[0,0,0,0,0]},_E:{_A:[0,0,0,0,0],_B:[0,0,0,0,0]},_F:{_A:[0,0,0,0,0],_B:[0,0,0,0,0]},_G:{_A:[0,0,0,0,0],_B:[0,0,0,0,0]}}
def verifyBeatable(info):
	'Verify assortment is beatable, and filter non-beatable seeds.';A=info;global fail_by_unreachable_kongs;global fail_by_invalid_lock;global fail_by_nonmatching_ruleset;C=[];C.append(A[_C]);C.append(A[_D][_A]);C.append(A[_E][_A]);C.append(A[_F][_A]);C.append(A[_G][_A])
	for H in range(5):
		if H not in C:fail_by_invalid_lock+=1;return _H
	if A[_C]not in ruleset[_C]:return _H
	for B in traps:
		for E in roles:
			if A[B][E]not in ruleset[B][E]:fail_by_nonmatching_ruleset+=1;return _H
	F=[];D=[A[_C]]
	for G in range(5):
		for B in traps:
			if A[B][_B]in D and B not in F:F.append(B);D.append(A[B][_A])
	for G in range(5):
		if G not in D:fail_by_unreachable_kongs+=1;unreach_kongs_total[len(D)]+=1;return _H
	return True
def printPerm(lst,name):
	'Print permutations.';B=[0,0,0,0,0]
	for C in range(5):
		if total_perm==0:A=0
		else:A=lst[C]*100/total_perm
		A=math.floor(A*100);A/=100;B[C]=str(A)+'%'
	print(f"{name}: {str(B)}")
for permutation in range(int(math.pow(5,5))):
	kong_unlocks=numToBase(permutation,5,5);cont=True
	for x in range(5):
		if x not in kong_unlocks:cont=_H
	if cont:
		checks+=1
		for sub_perm in range(int(math.pow(5,4))):
			kong_puzzle=numToBase(sub_perm,5,4);base5=[]
			for x in range(9):base5.append(0)
			base5[0]=kong_unlocks[0]
			for x in range(4):base5[1+2*x]=kong_unlocks[x+1];base5[2+2*x]=kong_puzzle[x]
			info={_C:base5[0]};index=1
			for trap in traps:info[trap]={_A:base5[index],_B:base5[index+1]};index+=2
			total_verif+=1;passes=verifyBeatable(info)
			if passes:
				balance[_C][info[_C]]+=1
				for trap in traps:
					for role in roles:balance[trap][role][info[trap][role]]+=1
				total_perm+=1
print(f"Total Verifications: {total_verif}")
print(f"Fail (Invalid Lock): {fail_by_invalid_lock}")
print(f"Fail (Unreachable Kongs): {fail_by_unreachable_kongs}")
print(f"Fail (Ruleset): {fail_by_nonmatching_ruleset}")
print('Unreachable Kongs Count:')
for x in range(6):print(f"\t{5-x} Kongs: {unreach_kongs_total[x]}")
print(f"Total Permutations: {total_perm}")
printPerm(balance[_C],'Starting Kong')
for x in range(4):
	trap=traps[x];trap_name=trap_names[x]
	for y in range(2):role=roles[y];role_name=role_names[y];printPerm(balance[trap][role],f"{trap_name} - {role_name}")