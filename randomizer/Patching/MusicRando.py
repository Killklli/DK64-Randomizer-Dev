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
	'Randomize music passed from the misc music settings.\n\n    Args:\n        settings (Settings): Settings object from the windows form.\n    ';S='uploaded';O='randomized';G='default';F=spoiler;C=F.settings
	if C.music_bgm!=G or C.music_events!=G or C.music_fanfares!=G:T=33476640;ROM().seek(T+287);ROM().write(1)
	if C.music_bgm!=G:
		if C.music_bgm==O:
			B=[]
			for K in range(12):B.append([])
			for A in song_data:
				if A.type==SongType.BGM:B[A.channel-1].append(js.pointer_addresses[0][_C][song_data.index(A)])
			for K in range(12):H=B[K].copy();random.shuffle(H);shuffle_music(F,B[K],H)
		elif C.music_bgm=='chaos':
			J=js.pointer_addresses[0][_C][song_data.index(next((A for A in song_data if A.name=='DK Rap'),None))];B=[]
			for A in song_data:
				if A.type==SongType.BGM:B.append(js.pointer_addresses[0][_C][song_data.index(A)])
			ROM().seek(J[_B]);U=ROM().readBytes(J[_D]);P=js.pointer_addresses[26][_C][0]
			for A in B:ROM().seek(A[_B]);ROM().writeBytes(U);ROM().seek(P[_B]+4*B.index(A));V=ROM().readBytes(4);ROM().seek(P[_B]+4*B.index(J));ROM().writeBytes(V);ROM().seek(33550336+A[_A]*2);ROM().writeMultipleBytes(song_data[J[_A]].memory,2)
		elif C.music_bgm==S:
			B=[]
			for A in song_data:
				if A.type==SongType.BGM:B.append(js.pointer_addresses[0][_C][song_data.index(A)])
			Q=list(js.cosmetics.bgm);random.shuffle(Q);E=[]
			for L in Q:
				def I():
					A=random.choice(B)
					if len(E)>=len(B):return
					if A not in E:ROM().seek(A[_B]);ROM().writeBytes(gzip.compress(bytes(L),compresslevel=9));E.append(A)
					else:I()
				I()
			D=B.copy();random.shuffle(D);shuffle_music(F,B,D)
	if C.music_fanfares!=G:
		if C.music_fanfares==O:
			M=[]
			for A in song_data:
				if A.type==SongType.Fanfare:M.append(js.pointer_addresses[0][_C][song_data.index(A)])
			H=M.copy();random.shuffle(H);shuffle_music(F,M,H)
		elif C.music_fanfares==S:
			B=[]
			for A in song_data:
				if A.type==SongType.Fanfare:B.append(js.pointer_addresses[0][_C][song_data.index(A)])
			R=list(js.cosmetics.fanfares);random.shuffle(R);E=[]
			for L in R:
				def I():
					A=random.choice(B)
					if len(E)>=len(B):return
					if A not in E:ROM().seek(A[_B]);ROM().writeBytes(gzip.compress(bytes(L),compresslevel=9));E.append(A)
					else:I()
				I()
			D=B.copy();random.shuffle(D);shuffle_music(F,B,D)
	if C.music_events!=G:
		if C.music_events==O:
			N=[]
			for A in song_data:
				if A.type==SongType.Event:N.append(js.pointer_addresses[0][_C][song_data.index(A)])
			D=N.copy();random.shuffle(D);shuffle_music(F,N,D)
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
			else:
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