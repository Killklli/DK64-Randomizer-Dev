'File which generates a basic HTML tracker table for your seed.'
import json,js
def generateTracker(spoilerJson):
	'Use the tracker template and spoiler data to generate a basic tracker.';V='Shuffled Level Order';U='Shuffled Exits';T='</table>\n';S='</tr>\n';R='" class="spoiler">';Q=')"/></td>\n';P='<tr>\n';O='<table>\n';N='Other';M='Shops';L='Kongs';I='</td>\n';H='">';D='Items';E=js.getFile('./TrackerTemplate.html');C=json.loads(spoilerJson);J='<!--Start Generated Content-->';K=E.index(J)+len(J);A='\n';A+='<h4>Seed: '+C['Settings']['Seed']+'</h4>\n'
	if D in C:
		F={}
		if L in C[D]:F.update(C[D][L])
		if M in C[D]:F.update(C[D][M])
		if N in C[D]:F.update(C[D][N])
		A+='<h3>Locations</h3>\n';A+=O;B=0
		for (W,X) in F.items():A+=P;A+='<td id="loc_'+str(B)+H+str(W)+I;A+='<td class="check-cell"><input id="itemCheck_'+str(B)+'" type="checkbox" onclick="showRow(\'item\', '+str(B)+Q;A+='<td id="item_'+str(B)+R+str(X)+I;A+=S;B+=1
		A+=T;A+='<input type="hidden" id="locCount" value="'+str(B)+H
	else:A+='<input type="hidden" id="locCount" value="0">'
	G={}
	if U in C:G.update(C[U])
	if V in C:G.update(C[V])
	if len(G)>0:
		A+='<h3>Exits</h3>\n';A+=O;B=0
		for (Y,Z) in G.items():A+=P;A+='<td id="front_'+str(B)+H+str(Y)+I;A+='<td class="check-cell"><input id="backCheck_'+str(B)+'" type="checkbox" onclick="showRow(\'back\', '+str(B)+Q;A+='<td id="back_'+str(B)+R+str(Z)+I;A+=S;B+=1
		A+=T;A+='<input type="hidden" id="exitCount" value="'+str(B)+H
	else:A+='<input type="hidden" id="exitCount" value="0">'
	E=E[:K]+A+E[K:];return E