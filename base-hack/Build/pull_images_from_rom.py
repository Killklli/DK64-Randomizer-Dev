'Pull hash images from ROM.'
_N='assets/Non-Code/hash'
_M='rgba32'
_L='big'
_K=False
_J='rgba16'
_I='flip'
_H='resize'
_G='name'
_F='h'
_E='index'
_D='table'
_C='format'
_B=True
_A='w'
import os,zlib
from PIL import Image
images=[{_G:'bongos',_C:_J,_D:25,_E:5548,_A:40,_F:40,_H:_B,_I:_B},{_G:'crown',_C:_J,_D:25,_E:5893,_A:44,_F:44,_H:_B,_I:_B},{_G:'dkcoin',_C:_J,_D:7,_E:500,_A:48,_F:44,_H:_B,_I:_B},{_G:'fairy',_C:_M,_D:25,_E:5869,_A:32,_F:32,_H:_B,_I:_B},{_G:'guitar',_C:_J,_D:25,_E:5547,_A:40,_F:40,_H:_B,_I:_B},{_G:'nin_coin',_C:_J,_D:25,_E:5912,_A:44,_F:44,_H:_B,_I:_B},{_G:'orange',_C:_J,_D:7,_E:309,_A:32,_F:32,_H:_B,_I:_B},{_G:'rainbow_coin',_C:_J,_D:25,_E:5963,_A:48,_F:44,_H:_B,_I:_B},{_G:'rw_coin',_C:_J,_D:25,_E:5905,_A:44,_F:44,_H:_B,_I:_B},{_G:'sax',_C:_J,_D:25,_E:5549,_A:40,_F:40,_H:_B,_I:_B},{_G:'boss_key',_C:_J,_D:25,_E:5877,_A:44,_F:44,_H:_K,_I:_B},{_G:'01234',_C:_J,_D:14,_E:15,_A:76,_F:24,_H:_K,_I:_K},{_G:'56789',_C:_J,_D:14,_E:16,_A:76,_F:24,_H:_K,_I:_K},{_G:'WXYL',_C:_J,_D:14,_E:12,_A:76,_F:24,_H:_K,_I:_K},{_G:'specialchars',_C:_J,_D:14,_E:30,_A:64,_F:32,_H:_K,_I:_K},{_G:'red_qmark_0',_C:_J,_D:7,_E:508,_A:32,_F:64,_H:_K,_I:_K},{_G:'red_qmark_1',_C:_J,_D:7,_E:509,_A:32,_F:64,_H:_K,_I:_K}]
kong_tex=['chunky','tiny','lanky','diddy','dk']
tex_idx=627
for kong in kong_tex:
	for x in range(2):images.append({_G:f"{kong}_face_{x}",_C:_J,_D:25,_E:tex_idx+x,_A:32,_F:64,_H:_K,_I:_B})
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
		im=Image.new(mode='RGBA',size=(x[_A],x[_F]));pix=im.load();pix_count=x[_A]*x[_F]
		for pixel in range(pix_count):
			if x[_C]==_J:start=pixel*2;end=start+2;pixel_data=int.from_bytes(dec[start:end],_L);red=pixel_data>>11&31;green=pixel_data>>6&31;blue=pixel_data>>1&31;alpha=pixel_data&1;red=int(red/31*255);green=int(green/31*255);blue=int(blue/31*255);alpha=alpha*255
			elif x[_C]==_M:start=pixel*4;end=start+4;pixel_data=int.from_bytes(dec[start:end],_L);red=pixel_data>>24&255;green=pixel_data>>16&255;blue=pixel_data>>8&255;alpha=pixel_data&255
			pix_x=pixel%x[_A];pix_y=int(pixel/x[_A]);pix[(pix_x,pix_y)]=red,green,blue,alpha
		if x[_I]:im=im.transpose(Image.FLIP_TOP_BOTTOM)
		if x[_H]:im=im.resize((32,32))
		im.save(img_name)