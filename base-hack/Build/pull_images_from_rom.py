'Pull hash images from ROM.'
_N='assets/Non-Code/hash'
_M='rgba32'
_L='big'
_K=False
_J='rgba16'
_I='flip'
_H='resize'
_G='name'
_F=True
_E='h'
_D='index'
_C='table'
_B='format'
_A='w'
import os,zlib
from PIL import Image
images=[{_G:'bongos',_B:_J,_C:25,_D:5548,_A:40,_E:40,_H:_F,_I:_F},{_G:'crown',_B:_J,_C:25,_D:5893,_A:44,_E:44,_H:_F,_I:_F},{_G:'dkcoin',_B:_J,_C:7,_D:500,_A:48,_E:44,_H:_F,_I:_F},{_G:'fairy',_B:_M,_C:25,_D:5869,_A:32,_E:32,_H:_F,_I:_F},{_G:'guitar',_B:_J,_C:25,_D:5547,_A:40,_E:40,_H:_F,_I:_F},{_G:'nin_coin',_B:_J,_C:25,_D:5912,_A:44,_E:44,_H:_F,_I:_F},{_G:'orange',_B:_J,_C:7,_D:309,_A:32,_E:32,_H:_F,_I:_F},{_G:'rainbow_coin',_B:_J,_C:25,_D:5963,_A:48,_E:44,_H:_F,_I:_F},{_G:'rw_coin',_B:_J,_C:25,_D:5905,_A:44,_E:44,_H:_F,_I:_F},{_G:'sax',_B:_J,_C:25,_D:5549,_A:40,_E:40,_H:_F,_I:_F},{_G:'boss_key',_B:_J,_C:25,_D:5877,_A:44,_E:44,_H:_K,_I:_F},{_G:'01234',_B:_J,_C:14,_D:15,_A:76,_E:24,_H:_K,_I:_K},{_G:'56789',_B:_J,_C:14,_D:16,_A:76,_E:24,_H:_K,_I:_K},{_G:'WXYL',_B:_J,_C:14,_D:12,_A:76,_E:24,_H:_K,_I:_K},{_G:'specialchars',_B:_J,_C:14,_D:30,_A:64,_E:32,_H:_K,_I:_K},{_G:'red_qmark_0',_B:_J,_C:7,_D:508,_A:32,_E:64,_H:_K,_I:_K},{_G:'red_qmark_1',_B:_J,_C:7,_D:509,_A:32,_E:64,_H:_K,_I:_K},{_G:'dk_tie_palette',_B:_J,_C:25,_D:3686,_A:32,_E:32,_H:_K,_I:_K},{_G:'tiny_palette',_B:_J,_C:25,_D:3689,_A:32,_E:32,_H:_K,_I:_K}]
kong_tex=['chunky','tiny','lanky','diddy','dk']
tex_idx=627
for kong in kong_tex:
	for x in range(2):images.append({_G:f"{kong}_face_{x}",_B:_J,_C:25,_D:tex_idx+x,_A:32,_E:64,_H:_K,_I:_F})
	tex_idx+=2
ptr_offset=1055824
if not os.path.exists(_N):os.mkdir(_N)
print('Extracting Images from ROM')
with open('rom/dk64.z64','rb')as fh:
	for x in images:
		fh.seek(ptr_offset+x[_C]*4);ptr_table=ptr_offset+int.from_bytes(fh.read(4),_L);fh.seek(ptr_table+x[_D]*4);img_start=ptr_offset+int.from_bytes(fh.read(4),_L);fh.seek(ptr_table+(x[_D]+1)*4);img_end=ptr_offset+int.from_bytes(fh.read(4),_L);img_size=img_end-img_start;fh.seek(img_start)
		if x[_C]==7:dec=fh.read(img_size)
		else:dec=zlib.decompress(fh.read(img_size),15+32)
		img_name=f"assets/Non-Code/hash/{x[_G]}.png"
		if os.path.exists(img_name):os.remove(img_name)
		with open(img_name,'wb')as fg:fg.seek(0)
		im=Image.new(mode='RGBA',size=(x[_A],x[_E]));pix=im.load();pix_count=x[_A]*x[_E]
		for pixel in range(pix_count):
			if x[_B]==_J:start=pixel*2;end=start+2;pixel_data=int.from_bytes(dec[start:end],_L);red=pixel_data>>11&31;green=pixel_data>>6&31;blue=pixel_data>>1&31;alpha=pixel_data&1;red=int(red/31*255);green=int(green/31*255);blue=int(blue/31*255);alpha=alpha*255
			elif x[_B]==_M:start=pixel*4;end=start+4;pixel_data=int.from_bytes(dec[start:end],_L);red=pixel_data>>24&255;green=pixel_data>>16&255;blue=pixel_data>>8&255;alpha=pixel_data&255
			pix_x=pixel%x[_A];pix_y=int(pixel/x[_A]);pix[(pix_x,pix_y)]=red,green,blue,alpha
		if x[_I]:im=im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
		if x[_H]:im=im.resize((32,32))
		im.save(img_name)