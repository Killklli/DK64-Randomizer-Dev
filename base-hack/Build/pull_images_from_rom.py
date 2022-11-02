'Pull hash images from ROM.'
_G='assets/Non-Code/hash'
_F='peanut'
_E='rgba32'
_D='big'
_C=False
_B='rgba16'
_A=True
import os,zlib
from PIL import Image
class ImageData:
	'Class to store information regarding images.'
	def __init__(A,name,format,table,index,width,height,resize,flip):'Initialize with given data.';A.name=name;A.format=format;A.table=table;A.index=index;A.width=width;A.height=height;A.resize=resize;A.flip=flip
crate_frame_l=7
crate_frame_r=9
images=[ImageData('bongos',_B,25,5548,40,40,_A,_A),ImageData('crown',_B,25,5893,44,44,_A,_A),ImageData('dkcoin',_B,7,500,48,44,_A,_A),ImageData('fairy',_E,25,5869,32,32,_A,_A),ImageData('guitar',_B,25,5547,40,40,_A,_A),ImageData('triangle',_B,25,5550,40,40,_A,_A),ImageData('trombone',_B,25,5551,40,40,_A,_A),ImageData(_F,_B,7,424,32,32,_A,_A),ImageData(_F,_B,7,424,32,32,_A,_A),ImageData('feather',_B,7,642,32,32,_A,_A),ImageData('grape',_B,7,650,32,32,_A,_A),ImageData('pineapple',_B,7,666,32,48,_A,_A),ImageData('coconut',_B,7,675,40,51,_A,_A),ImageData('nin_coin',_B,25,5912,44,44,_A,_A),ImageData('orange',_B,7,309,32,32,_A,_A),ImageData('rainbow_coin',_B,25,5963,48,44,_A,_A),ImageData('rw_coin',_B,25,5905,44,44,_A,_A),ImageData('sax',_B,25,5549,40,40,_A,_A),ImageData('boss_key',_B,25,5877,44,44,_C,_A),ImageData('01234',_B,14,15,76,24,_C,_C),ImageData('56789',_B,14,16,76,24,_C,_C),ImageData('WXYL',_B,14,12,76,24,_C,_C),ImageData('specialchars',_B,14,30,64,32,_C,_C),ImageData('red_qmark_0',_B,7,508,32,64,_C,_C),ImageData('red_qmark_1',_B,7,509,32,64,_C,_C),ImageData('dk_tie_palette',_B,25,3686,32,32,_C,_C),ImageData('tiny_palette',_B,25,3689,32,32,_C,_C),ImageData('homing_crate_0',_B,7,185,32,64,_C,_A),ImageData('homing_crate_1',_B,7,200,32,64,_C,_A),ImageData('standard_crate_0',_B,7,392,32,64,_C,_A),ImageData('standard_crate_1',_B,7,407,32,64,_C,_A),ImageData('num_1_unlit',_B,7,510,32,32,_C,_C),ImageData('num_1_lit',_B,7,511,32,32,_C,_C),ImageData('num_6_unlit',_B,7,520,32,32,_C,_C),ImageData('num_6_lit',_B,7,521,32,32,_C,_C),ImageData('num_7_unlit',_B,7,522,32,32,_C,_C),ImageData('num_7_lit',_B,7,523,32,32,_C,_C),ImageData('num_9_unlit',_B,7,526,32,32,_C,_C),ImageData('num_9_lit',_B,7,527,32,32,_C,_C),ImageData('film',_B,7,439,48,42,_C,_A),ImageData('melon',_B,7,544,48,42,_C,_A),ImageData('headphones',_B,7,979,40,40,_C,_A),ImageData('special_coin_side',_B,25,5901,44,44,_C,_A),ImageData('gb',_B,25,5468,44,44,_C,_A),ImageData('medal',_B,25,5484,44,44,_C,_A),ImageData('dk_bp',_B,25,5628,48,42,_C,_A),ImageData('lanky_bp',_B,25,5523,48,42,_C,_A),ImageData('key',_B,25,5877,44,44,_C,_A),ImageData('crown_shop',_B,25,5893,44,44,_C,_A)]
kong_tex=['chunky','tiny','lanky','diddy','dk']
tex_idx=627
for kong in kong_tex:
	for x in range(2):images.append(ImageData(f"{kong}_face_{x}",_B,25,tex_idx+x,32,64,_C,_A))
	tex_idx+=2
ptr_offset=1055824
if not os.path.exists(_G):os.mkdir(_G)
print('Extracting Images from ROM')
with open('rom/dk64.z64','rb')as fh:
	for x in images:
		fh.seek(ptr_offset+x.table*4);ptr_table=ptr_offset+int.from_bytes(fh.read(4),_D);fh.seek(ptr_table+x.index*4);img_start=ptr_offset+int.from_bytes(fh.read(4),_D);fh.seek(ptr_table+(x.index+1)*4);img_end=ptr_offset+int.from_bytes(fh.read(4),_D);img_size=img_end-img_start;fh.seek(img_start)
		if x.table==7:dec=fh.read(img_size)
		else:dec=zlib.decompress(fh.read(img_size),15+32)
		img_name=f"assets/Non-Code/hash/{x.name}.png"
		if os.path.exists(img_name):os.remove(img_name)
		with open(img_name,'wb')as fg:fg.seek(0)
		im=Image.new(mode='RGBA',size=(x.width,x.height));pix=im.load();pix_count=x.width*x.height
		for pixel in range(pix_count):
			if x.format==_B:start=pixel*2;end=start+2;pixel_data=int.from_bytes(dec[start:end],_D);red=pixel_data>>11&31;green=pixel_data>>6&31;blue=pixel_data>>1&31;alpha=pixel_data&1;red=int(red/31*255);green=int(green/31*255);blue=int(blue/31*255);alpha=alpha*255
			elif x.format==_E:start=pixel*4;end=start+4;pixel_data=int.from_bytes(dec[start:end],_D);red=pixel_data>>24&255;green=pixel_data>>16&255;blue=pixel_data>>8&255;alpha=pixel_data&255
			pix_x=pixel%x.width;pix_y=int(pixel/x.width);pix[(pix_x,pix_y)]=red,green,blue,alpha
		if x.flip:im=im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
		if x.resize:im=im.resize((32,32))
		im.save(img_name)