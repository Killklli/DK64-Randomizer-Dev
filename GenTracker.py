'File which generates a basic HTML tracker table for your seed.'
import js,json
def generateTracker(spoilerJson):
	'Use the tracker template and spoiler data to generate a basic tracker.';P='Shuffled Exits';O='</table>\n';N='</tr>\n';M='" class="spoiler">';L=')"/></td>\n';K='<tr>\n';J='<table>\n';I='Locations';F='</td>\n';E='">';C=js.getFile('./TrackerTemplate.html');D=json.loads(spoilerJson);G='<!--Start Generated Content-->';H=C.index(G)+len(G);A='\n';A+='<h4>Seed: '+D['Settings']['seed']+'</h4>\n'
	if I in D:
		A+='<h3>Locations</h3>\n';A+=J;B=0
		for (Q,R) in D[I].items():A+=K;A+='<td id="loc_'+str(B)+E+Q+F;A+='<td class="check-cell"><input id="itemCheck_'+str(B)+'" type="checkbox" onclick="showRow(\'item\', '+str(B)+L;A+='<td id="item_'+str(B)+M+R+F;A+=N;B+=1
		A+=O;A+='<input type="hidden" id="locCount" value="'+str(B)+E
	else:A+='<input type="hidden" id="locCount" value="0">'
	if P in D:
		A+='<h3>Exits</h3>\n';A+=J;B=0
		for (S,T) in D[P].items():A+=K;A+='<td id="front_'+str(B)+E+S+F;A+='<td class="check-cell"><input id="backCheck_'+str(B)+'" type="checkbox" onclick="showRow(\'back\', '+str(B)+L;A+='<td id="back_'+str(B)+M+T+F;A+=N;B+=1
		A+=O;A+='<input type="hidden" id="exitCount" value="'+str(B)+E
	else:A+='<input type="hidden" id="exitCount" value="0">'
	C=C[:H]+A+C[H:];return C