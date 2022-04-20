'Locate Hash images for displaying on the website.'
import base64,io,zlib
from PIL import Image
from randomizer.Patching.Patcher import ROM
def get_hash_images():
	'Get and return a list of hash images for the website UI.';Z='rgba32';K='big';H='rgba16';G='name';F='h';E='index';D='table';C='format';A='w';a=[{G:'bongos',C:H,D:25,E:5548,A:40,F:40},{G:'crown',C:H,D:25,E:5893,A:44,F:44},{G:'dk_coin',C:H,D:7,E:500,A:48,F:44},{G:'fairy',C:Z,D:25,E:5869,A:32,F:32},{G:'guitar',C:H,D:25,E:5547,A:40,F:40},{G:'nin_coin',C:H,D:25,E:5912,A:44,F:44},{G:'orange',C:H,D:7,E:309,A:32,F:32},{G:'rainbow_coin',C:H,D:25,E:5963,A:48,F:44},{G:'rw_coin',C:H,D:25,E:5905,A:44,F:44},{G:'saxaphone',C:H,D:25,E:5549,A:40,F:40}];L=1055824;V=[]
	for B in a:
		ROM().seek(L+B[D]*4);W=L+int.from_bytes(ROM().readBytes(4),K);ROM().seek(W+B[E]*4);X=L+int.from_bytes(ROM().readBytes(4),K);ROM().seek(W+(B[E]+1)*4);b=L+int.from_bytes(ROM().readBytes(4),K);Y=b-X;ROM().seek(X)
		if B[D]==25:S=zlib.decompress(ROM().readBytes(Y),15+32)
		else:S=ROM().readBytes(Y)
		M=Image.new(mode='RGBA',size=(B[A],B[F]));c=M.load();d=B[A]*B[F]
		for N in range(d):
			if B[C]==H:J=N*2;T=J+2;I=int.from_bytes(S[J:T],K);O=I>>11&31;P=I>>6&31;Q=I>>1&31;R=I&1;O=int(O/31*255);P=int(P/31*255);Q=int(Q/31*255);R=R*255
			elif B[C]==Z:J=N*4;T=J+4;I=int.from_bytes(S[J:T],K);O=I>>24&255;P=I>>16&255;Q=I>>8&255;R=I&255
			e=N%B[A];f=int(N/B[A]);c[(e,f)]=O,P,Q,R
		U=io.BytesIO();M=M.transpose(Image.FLIP_LEFT_RIGHT);M.save(U,format='PNG');U.seek(0);g=U.read();h=base64.b64encode(g);i=h.decode('ascii');V.append(i)
	return V