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
	'Randomize music passed from the misc music settings.\n\n    Args:\n        settings (Settings): Settings object from the windows form.\n    ';T='uploaded';S='music_fanfares';R='music_bgm';G='default';D='randomized';A=spoiler;X=A.settings
	if js.document.getElementById('override_cosmetics').checked:
		if js.document.getElementById('random_music').checked:A.settings.music_bgm=D;A.settings.music_fanfares=D;A.settings.music_events=D
		else:A.settings.music_bgm=js.document.getElementById(R).value;A.settings.music_fanfares=js.document.getElementById(S).value;A.settings.music_events=js.document.getElementById('music_events').value
	elif A.settings.random_music:A.settings.music_bgm=D;A.settings.music_fanfares=D;A.settings.music_events=D
	if A.settings.music_bgm!=G or A.settings.music_events!=G or A.settings.music_fanfares!=G:U=A.settings.rom_data;ROM().seek(U+302);ROM().write(1)
	if A.settings.music_bgm!=G:
		if A.settings.music_bgm==D:
			C=[]
			for K in range(12):C.append([])
			for B in song_data:
				if B.type==SongType.BGM:C[B.channel-1].append(js.pointer_addresses[0][_C][song_data.index(B)])
			for K in range(12):H=C[K].copy();random.shuffle(H);shuffle_music(A,C[K].copy(),H)
		elif A.settings.music_bgm=='chaos':
			J=js.pointer_addresses[0][_C][song_data.index(next((A for A in song_data if A.name=='DK Rap'),None))];C=[]
			for B in song_data:
				if B.type==SongType.BGM:C.append(js.pointer_addresses[0][_C][song_data.index(B)])
			ROM().seek(J[_B]);V=ROM().readBytes(J[_D]);O=js.pointer_addresses[26][_C][0]
			for B in C:ROM().seek(B[_B]);ROM().writeBytes(V);ROM().seek(O[_B]+4*C.index(B));W=ROM().readBytes(4);ROM().seek(O[_B]+4*C.index(J));ROM().writeBytes(W);ROM().seek(33550336+B[_A]*2);ROM().writeMultipleBytes(song_data[J[_A]].memory,2)
		elif js.document.getElementById(R).value==T:
			C=[]
			for B in song_data:
				if B.type==SongType.BGM:C.append(js.pointer_addresses[0][_C][song_data.index(B)])
			P=list(js.cosmetics.bgm);random.shuffle(P);F=[]
			for L in P:
				def I():
					A=random.choice(C)
					if len(F)>=len(C):return
					if A not in F:ROM().seek(A[_B]);ROM().writeBytes(gzip.compress(bytes(L),compresslevel=9));F.append(A)
					else:I()
				I()
			E=C.copy();random.shuffle(E);shuffle_music(A,C.copy(),E)
	if A.settings.music_fanfares!=G:
		if A.settings.music_fanfares==D:
			M=[]
			for B in song_data:
				if B.type==SongType.Fanfare:M.append(js.pointer_addresses[0][_C][song_data.index(B)])
			H=M.copy();random.shuffle(H);shuffle_music(A,M.copy(),H)
		elif js.document.getElementById(S).value==T:
			C=[]
			for B in song_data:
				if B.type==SongType.Fanfare:C.append(js.pointer_addresses[0][_C][song_data.index(B)])
			Q=list(js.cosmetics.fanfares);random.shuffle(Q);F=[]
			for L in Q:
				def I():
					A=random.choice(C)
					if len(F)>=len(C):return
					if A not in F:ROM().seek(A[_B]);ROM().writeBytes(gzip.compress(bytes(L),compresslevel=9));F.append(A)
					else:I()
				I()
			E=C.copy();random.shuffle(E);shuffle_music(A,C.copy(),E)
	if A.settings.music_events!=G:
		if A.settings.music_events==D:
			N=[]
			for B in song_data:
				if B.type==SongType.Event:N.append(js.pointer_addresses[0][_C][song_data.index(B)])
			E=N.copy();random.shuffle(E);shuffle_music(A,N.copy(),E)
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