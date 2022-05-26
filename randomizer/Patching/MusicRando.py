'Randomize Music passed from Misc options.'
_D='compressed_size'
_C='entries'
_B='pointing_to'
_A='index'
import gzip,json,random
from ast import And
import js,randomizer.Lists.Exceptions as Ex
from randomizer.Enums.SongType import SongType
from randomizer.Lists.Songs import Song,SongGroup,song_data
from randomizer.Patching.Patcher import ROM
from randomizer.Settings import Settings
from randomizer.Spoiler import Spoiler
def randomize_music(spoiler):
	'Randomize music passed from the misc music settings.\n\n    Args:\n        settings (Settings): Settings object from the windows form.\n    ';U='uploaded';M='music_events';K='music_fanfares';H='default';G='randomized';F='music_bgm';E=spoiler;Y=E.settings
	if js.document.getElementById('random_music').checked:js.document.getElementById(F).value=G;js.document.getElementById(K).value=G;js.document.getElementById(M).value=G
	if js.document.getElementById(F).value!=H or js.document.getElementById(M).value!=H or js.document.getElementById(K).value!=H:V=33476640;ROM().seek(V+287);ROM().write(1)
	if js.document.getElementById(F).value!=H:
		if js.document.getElementById(F).value==G:
			B=[]
			for N in range(12):B.append([])
			for A in song_data:
				if A.type==SongType.BGM:B[A.channel-1].append(js.pointer_addresses[0][_C][song_data.index(A)])
			for N in range(12):I=B[N].copy();random.shuffle(I);shuffle_music(E,B[N].copy(),I)
		elif js.document.getElementById(F).value=='chaos':
			L=js.pointer_addresses[0][_C][song_data.index(next((A for A in song_data if A.name=='DK Rap'),None))];B=[]
			for A in song_data:
				if A.type==SongType.BGM:B.append(js.pointer_addresses[0][_C][song_data.index(A)])
			ROM().seek(L[_B]);W=ROM().readBytes(L[_D]);R=js.pointer_addresses[26][_C][0]
			for A in B:ROM().seek(A[_B]);ROM().writeBytes(W);ROM().seek(R[_B]+4*B.index(A));X=ROM().readBytes(4);ROM().seek(R[_B]+4*B.index(L));ROM().writeBytes(X);ROM().seek(33550336+A[_A]*2);ROM().writeMultipleBytes(song_data[L[_A]].memory,2)
		elif js.document.getElementById(F).value==U:
			B=[]
			for A in song_data:
				if A.type==SongType.BGM:B.append(js.pointer_addresses[0][_C][song_data.index(A)])
			S=list(js.cosmetics.bgm);random.shuffle(S);D=[]
			for O in S:
				def J():
					A=random.choice(B)
					if len(D)>=len(B):return
					if A not in D:ROM().seek(A[_B]);ROM().writeBytes(gzip.compress(bytes(O),compresslevel=9));D.append(A)
					else:J()
				J()
			C=B.copy();random.shuffle(C);shuffle_music(E,B.copy(),C)
	if js.document.getElementById(K).value!=H:
		if js.document.getElementById(K).value==G:
			P=[]
			for A in song_data:
				if A.type==SongType.Fanfare:P.append(js.pointer_addresses[0][_C][song_data.index(A)])
			I=P.copy();random.shuffle(I);shuffle_music(E,P.copy(),I)
		elif js.document.getElementById(K).value==U:
			B=[]
			for A in song_data:
				if A.type==SongType.Fanfare:B.append(js.pointer_addresses[0][_C][song_data.index(A)])
			T=list(js.cosmetics.fanfares);random.shuffle(T);D=[]
			for O in T:
				def J():
					A=random.choice(B)
					if len(D)>=len(B):return
					if A not in D:ROM().seek(A[_B]);ROM().writeBytes(gzip.compress(bytes(O),compresslevel=9));D.append(A)
					else:J()
				J()
			C=B.copy();random.shuffle(C);shuffle_music(E,B.copy(),C)
	if js.document.getElementById(M).value!=H:
		if js.document.getElementById(M).value==G:
			Q=[]
			for A in song_data:
				if A.type==SongType.Event:Q.append(js.pointer_addresses[0][_C][song_data.index(A)])
			C=Q.copy();random.shuffle(C);shuffle_music(E,Q.copy(),C)
def ShuffleMusicWithSizeCheck(spoiler,song_list):
	'Facilitate shuffling of music.';L=song_list;E=spoiler;C='uncompressed_size';J=0
	while True:
		try:
			M=L.copy();K=L.copy();random.shuffle(K);N=[];O=[];G={};H={}
			while len(M)>0:
				F=M.pop(0);A=song_data[F[_A]];I=None
				for D in K:
					I=song_data[D[_A]]
					if A.group is not None and A.type==SongType.BGM:
						B=SongGroup(A.group).name
						if B not in G:G[B]=0
						if B not in H:H[B]=0
						if SongGroup(A.group)==SongGroup.Self:
							if D[C]>F[C]:continue
						elif H[B]+D[C]>G[B]+F[C]:continue
						G[B]+=F[C];H[B]+=D[C]
					elif A.type==SongType.Fanfare:
						if D[C]>F[C]*1.5:continue
					K.remove(D);N.append(F);O.append(D)
					if A.type==SongType.BGM:E.music_bgm_data[A.name]=I.name
					elif A.type==SongType.Fanfare:E.music_fanfare_data[A.name]=I.name
					elif A.type==SongType.Event:E.music_event_data[A.name]=I.name
					break
				else:raise Ex.MusicPlacementExceededMapThreshold
			print(G);print(H);shuffle_music(N,O);return
		except Ex.MusicPlacementExceededMapThreshold:
			if J==20:print('Music rando failed, out of retries.');raise Ex.MusicAttemptCountExceeded
			J+=1;print('Music rando failed. Retrying. Tries: '+str(J))
			if A.type==SongType.BGM:E.music_bgm_data={}
			elif A.type==SongType.Fanfare:E.music_fanfare_data={}
			elif A.type==SongType.Event:E.music_event_data={}
def shuffle_music(spoiler,pool_to_shuffle,shuffled_list):
	'Shuffle the music pool based on the OG list and the shuffled list.\n\n    Args:\n        pool_to_shuffle (list): Original pool to shuffle.\n        shuffled_list (list): Shuffled order list.\n    ';E=pool_to_shuffle;D=spoiler;G=js.pointer_addresses[26][_C][0];H={};I={}
	for A in E:ROM().seek(A[_B]);J=ROM().readBytes(A[_D]);H[A[_A]]=J;ROM().seek(G[_B]+4*A[_A]);K=ROM().readBytes(4);I[A[_A]]=K
	for A in E:
		F=shuffled_list[E.index(A)];L=H[F[_A]];ROM().seek(A[_B]);ROM().writeBytes(L);M=I[F[_A]];ROM().seek(G[_B]+4*A[_A]);ROM().writeBytes(M);B=A[_A];C=F[_A];N=song_data[C].memory;ROM().seek(33550336+2*B);ROM().writeMultipleBytes(N,2)
		if song_data[B].type==SongType.BGM:D.music_bgm_data[song_data[B].name]=song_data[C].name
		elif song_data[B].type==SongType.Fanfare:D.music_fanfare_data[song_data[B].name]=song_data[C].name
		elif song_data[B].type==SongType.Event:D.music_event_data[song_data[B].name]=song_data[C].name