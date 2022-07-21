'Pull hash images from ROM.'
_N='assets/Non-Code/hash'
_M='rgba32'
_L='big'
_K=True
_J='rgba16'
_I='flip'
_H='resize'
_G='name'
_F='h'
_E='index'
_D='table'
_C='format'
_B='w'
_A=False
import os,zlib
from PIL import Image
crate_frame_l=7
crate_frame_r=9
images=[{_G:'bongos',_C:_J,_D:25,_E:5548,_B:40,_F:40,_H:_K,_I:_K},{_G:'crown',_C:_J,_D:25,_E:5893,_B:44,_F:44,_H:_K,_I:_K},{_G:'dkcoin',_C:_J,_D:7,_E:500,_B:48,_F:44,_H:_K,_I:_K},{_G:'fairy',_C:_M,_D:25,_E:5869,_B:32,_F:32,_H:_K,_I:_K},{_G:'guitar',_C:_J,_D:25,_E:5547,_B:40,_F:40,_H:_K,_I:_K},{_G:'nin_coin',_C:_J,_D:25,_E:5912,_B:44,_F:44,_H:_K,_I:_K},{_G:'orange',_C:_J,_D:7,_E:309,_B:32,_F:32,_H:_K,_I:_K},{_G:'rainbow_coin',_C:_J,_D:25,_E:5963,_B:48,_F:44,_H:_K,_I:_K},{_G:'rw_coin',_C:_J,_D:25,_E:5905,_B:44,_F:44,_H:_K,_I:_K},{_G:'sax',_C:_J,_D:25,_E:5549,_B:40,_F:40,_H:_K,_I:_K},{_G:'boss_key',_C:_J,_D:25,_E:5877,_B:44,_F:44,_H:_A,_I:_K},{_G:'01234',_C:_J,_D:14,_E:15,_B:76,_F:24,_H:_A,_I:_A},{_G:'56789',_C:_J,_D:14,_E:16,_B:76,_F:24,_H:_A,_I:_A},{_G:'WXYL',_C:_J,_D:14,_E:12,_B:76,_F:24,_H:_A,_I:_A},{_G:'specialchars',_C:_J,_D:14,_E:30,_B:64,_F:32,_H:_A,_I:_A},{_G:'red_qmark_0',_C:_J,_D:7,_E:508,_B:32,_F:64,_H:_A,_I:_A},{_G:'red_qmark_1',_C:_J,_D:7,_E:509,_B:32,_F:64,_H:_A,_I:_A},{_G:'dk_tie_palette',_C:_J,_D:25,_E:3686,_B:32,_F:32,_H:_A,_I:_A},{_G:'tiny_palette',_C:_J,_D:25,_E:3689,_B:32,_F:32,_H:_A,_I:_A},{_G:'homing_crate_0',_C:_J,_D:7,_E:176+crate_frame_r,_B:32,_F:64,_H:_A,_I:_K},{_G:'homing_crate_1',_C:_J,_D:7,_E:193+crate_frame_l,_B:32,_F:64,_H:_A,_I:_K},{_G:'standard_crate_0',_C:_J,_D:7,_E:383+crate_frame_r,_B:32,_F:64,_H:_A,_I:_K},{_G:'standard_crate_1',_C:_J,_D:7,_E:400+crate_frame_l,_B:32,_F:64,_H:_A,_I:_K},{_G:'num_1_unlit',_C:_J,_D:7,_E:510,_B:32,_F:32,_H:_A,_I:_A},{_G:'num_1_lit',_C:_J,_D:7,_E:511,_B:32,_F:32,_H:_A,_I:_A},{_G:'num_6_unlit',_C:_J,_D:7,_E:520,_B:32,_F:32,_H:_A,_I:_A},{_G:'num_6_lit',_C:_J,_D:7,_E:521,_B:32,_F:32,_H:_A,_I:_A},{_G:'num_7_unlit',_C:_J,_D:7,_E:522,_B:32,_F:32,_H:_A,_I:_A},{_G:'num_7_lit',_C:_J,_D:7,_E:523,_B:32,_F:32,_H:_A,_I:_A},{_G:'num_9_unlit',_C:_J,_D:7,_E:526,_B:32,_F:32,_H:_A,_I:_A},{_G:'num_9_lit',_C:_J,_D:7,_E:527,_B:32,_F:32,_H:_A,_I:_A}]
kong_tex=['chunky','tiny','lanky','diddy','dk']
tex_idx=627
for kong in kong_tex:
	for x in range(2):images.append({_G:f"{kong}_face_{x}",_C:_J,_D:25,_E:tex_idx+x,_B:32,_F:64,_H:_A,_I:_K})
	tex_idx+=2
ptr_offset=1055824
if not os.path.exists(_N):os.mkdir(_N)
print('Extracting Images from ROM')
with open('rom/dk64.z64','rb')as fh:
	for x in images:
		fh.seek(ptr_offset+x[_D]*4);ptr_table=ptr_offset+int.from_bytes(fh.read(4),_L);fh.seek(ptr_table+x[_E]*4);img_start=ptr_offset+int.from_bytes(fh.read(4),_L);fh.seek(ptr_table+(x[_E]+1)*4);img_end=ptr_offset+int.from_bytes(fh.read(4),_L);img_size=img_end-img_start;fh.seek(img_start)
		if x[_D]==7:dec=fh.read(img_size)
		else:dec=zlib.decompress(fh.read(img_size),15+32)
		img_name=f"assets/Non-Code/hash/{x[_G]}.png"
		if os.path.exists(img_name):os.remove(img_name)
		with open(img_name,'wb')as fg:fg.seek(0)
		im=Image.new(mode='RGBA',size=(x[_B],x[_F]));pix=im.load();pix_count=x[_B]*x[_F]
		for pixel in range(pix_count):
			if x[_C]==_J:start=pixel*2;end=start+2;pixel_data=int.from_bytes(dec[start:end],_L);red=pixel_data>>11&31;green=pixel_data>>6&31;blue=pixel_data>>1&31;alpha=pixel_data&1;red=int(red/31*255);green=int(green/31*255);blue=int(blue/31*255);alpha=alpha*255
			elif x[_C]==_M:start=pixel*4;end=start+4;pixel_data=int.from_bytes(dec[start:end],_L);red=pixel_data>>24&255;green=pixel_data>>16&255;blue=pixel_data>>8&255;alpha=pixel_data&255
			pix_x=pixel%x[_B];pix_y=int(pixel/x[_B]);pix[(pix_x,pix_y)]=red,green,blue,alpha
		if x[_I]:im=im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
		if x[_H]:im=im.resize((32,32))
		im.save(img_name)