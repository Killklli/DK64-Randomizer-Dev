'Select CB Location selection.'
_C='balloons'
_B='cb'
_A='logic'
from randomizer.LogicClasses import Collectible
from .Enums.Collectibles import Collectibles
import randomizer.Lists.CBLocations.JungleJapesCBLocations,randomizer.Lists.CBLocations.AngryAztecCBLocations,randomizer.Lists.CBLocations.FranticFactoryCBLocations,randomizer.Lists.CBLocations.GloomyGalleonCBLocations,randomizer.Lists.CBLocations.FungiForestCBLocations,randomizer.Lists.CBLocations.CrystalCavesCBLocations,randomizer.Lists.CBLocations.CreepyCastleCBLocations,randomizer.CollectibleLogicFiles.JungleJapes,randomizer.CollectibleLogicFiles.AngryAztec,randomizer.CollectibleLogicFiles.FranticFactory,randomizer.CollectibleLogicFiles.GloomyGalleon,randomizer.CollectibleLogicFiles.FungiForest,randomizer.CollectibleLogicFiles.CrystalCaves,randomizer.CollectibleLogicFiles.CreepyCastle
from randomizer.Enums.Levels import Levels
from randomizer.Spoiler import Spoiler
from randomizer.Enums.Kongs import Kongs
import random
max_balloons=105
max_singles=780
max_bunches=790-max_balloons*2-round(max_singles/5)
level_data={Levels.JungleJapes:{_B:randomizer.Lists.CBLocations.JungleJapesCBLocations.ColoredBananaGroupList,_C:randomizer.Lists.CBLocations.JungleJapesCBLocations.BalloonList,_A:randomizer.CollectibleLogicFiles.JungleJapes.LogicRegions},Levels.AngryAztec:{_B:randomizer.Lists.CBLocations.AngryAztecCBLocations.ColoredBananaGroupList,_C:randomizer.Lists.CBLocations.AngryAztecCBLocations.BalloonList,_A:randomizer.CollectibleLogicFiles.AngryAztec.LogicRegions},Levels.FranticFactory:{_B:randomizer.Lists.CBLocations.FranticFactoryCBLocations.ColoredBananaGroupList,_C:randomizer.Lists.CBLocations.FranticFactoryCBLocations.BalloonList,_A:randomizer.CollectibleLogicFiles.FranticFactory.LogicRegions},Levels.GloomyGalleon:{_B:randomizer.Lists.CBLocations.GloomyGalleonCBLocations.ColoredBananaGroupList,_C:randomizer.Lists.CBLocations.GloomyGalleonCBLocations.BalloonList,_A:randomizer.CollectibleLogicFiles.GloomyGalleon.LogicRegions},Levels.FungiForest:{_B:randomizer.Lists.CBLocations.FungiForestCBLocations.ColoredBananaGroupList,_C:randomizer.Lists.CBLocations.FungiForestCBLocations.BalloonList,_A:randomizer.CollectibleLogicFiles.FungiForest.LogicRegions},Levels.CrystalCaves:{_B:randomizer.Lists.CBLocations.CrystalCavesCBLocations.ColoredBananaGroupList,_C:randomizer.Lists.CBLocations.CrystalCavesCBLocations.BalloonList,_A:randomizer.CollectibleLogicFiles.CrystalCaves.LogicRegions},Levels.CreepyCastle:{_B:randomizer.Lists.CBLocations.CreepyCastleCBLocations.ColoredBananaGroupList,_C:randomizer.Lists.CBLocations.CreepyCastleCBLocations.BalloonList,_A:randomizer.CollectibleLogicFiles.CreepyCastle.LogicRegions}}
def ShuffleCBs(spoiler):
	'Shuffle CBs selected from location files.';r='map';q='type';p='level';o='kong';n='name';e=None;f=0;K=0;L=0;g=[]
	for (F,B) in enumerate(level_data):
		for s in level_data[B][_A]:
			for h in level_data[B][_A][s]:
				if h.type in[Collectibles.balloon,Collectibles.bunch,Collectibles.banana]:h.enabled=False
		S=[];M=6-F;A={Kongs.donkey:100,Kongs.diddy:100,Kongs.lanky:100,Kongs.tiny:100,Kongs.chunky:100};N=max_balloons-f;i=max(int(N/(7-F))-3,0)
		if M==0:T=N
		else:T=min(int(N/(7-F))+3,int(N/M))
		U=level_data[B][_C].copy();t=min(random.randint(min(i,T),max(i,T)),len(U));random.shuffle(U);V=0
		for H in U:
			if V<t:
				O=H.kongs.copy()
				for E in A:
					if A[E]<10 and E in O:O.remove(E)
				if len(O)>0:D=random.choice(O);A[D]-=10;S.append({'id':H.id,n:H.name,o:D,p:B,q:_C,r:H.map});V+=1;level_data[B][_A][H.region].append(Collectible(Collectibles.balloon,D,H.logic,e,1))
		P=max_bunches-L;Q=max_singles-K;j=max(int(P/(7-F))-5,0);k=max(int(Q/(7-F))-10,0)
		if M==0:W=P;X=min(Q,int((5*(1127-L-K)-sum(A))/4))
		else:W=min(int(P/(7-F))+15,int(P/M));X=min(int(Q/(7-F))+10,int(Q/M))
		l=list(range(1,len(level_data[B][_B])+1));random.shuffle(l);u=random.randint(min(j,W),max(j,W));v=random.randint(min(k,X),max(k,X));Y=0;Z=0
		for w in l:
			R=0;a=0;b=0;m=[A for A in level_data[B][_B]if A.group==w];G=list(A.keys())
			for C in m:
				G=list(set(G)&set(C.kongs.copy()))
				for I in C.locations:R+=I[0];a+=int(I[0]==5);b+=int(I[0]==1)
			for E in A:
				if E in G:
					if A[E]<R or len(G)>1 and A[E]<=10 and A[E]-R>0:G.remove(E)
			if len(G)>0 and v>=Z+b and u>=Y+a:
				D=random.choice(G);A[D]-=R
				if A[D]==0:del A[D]
				for C in m:
					c=0;d=0
					for I in C.locations:c+=int(I[0]==5);d+=int(I[0]==1)
					if c>0:level_data[B][_A][C.region].append(Collectible(Collectibles.bunch,D,C.logic,e,c))
					if d>0:level_data[B][_A][C.region].append(Collectible(Collectibles.banana,D,C.logic,e,d))
					S.append({'group':C.group,n:C.name,o:D,p:B,q:_B,r:C.map,'locations':C.locations})
				Y+=a;Z+=b
			if len(A.keys())==0:break
		f+=V;L+=Y;K+=Z;g.extend(S.copy())
		for J in A:
			if A[J]>0:print(f"WARNING: {A[J]} bananas unassigned for {J.name} in {B.name}")
			elif A[J]<0:print(f"WARNING: {-A[J]} too many bananas assigned for {J.name} in {B.name}")
	if L+K>1127:print(f"WARNING: {L+K} banana objects placed, exceeding cap of 1127")
	spoiler.cb_placements=g