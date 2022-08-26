'Create complex images from in-game assets.'
_I='56789.png'
_H='01234.png'
_G='image_list'
_F='image'
_E='assets/Non-Code/displays/'
_D='assets/Non-Code/hash/'
_C='RGBA'
_B='crop'
_A='num'
import os,PIL
from PIL import Image
pre='../'
cwd=os.getcwd()
cwd_split=cwd.split('\\')
last_part=cwd_split[-1]
pre=''
if last_part.upper()=='BUILD':pre='../'
def getDir(directory):'Convert directory into the right format based on where the script is run.';return f"{pre}{directory}"
print('Composing complex images')
number_crop=[{_F:_H,_G:[{_A:0,_B:(0,0,20,24)},{_A:1,_B:(20,0,30,24)},{_A:2,_B:(30,0,45,24)},{_A:3,_B:(45,0,58,24)},{_A:4,_B:(58,0,76,24)}]},{_F:_I,_G:[{_A:5,_B:(0,0,14,24)},{_A:6,_B:(14,0,29,24)},{_A:7,_B:(29,0,43,24)},{_A:8,_B:(43,0,58,24)},{_A:9,_B:(58,0,76,24)}]}]
kongs=['dk','diddy','lanky','tiny','chunky']
hash_dir=getDir(_D)
if not os.path.exists(hash_dir):os.mkdir(hash_dir)
for file_info in number_crop:
	for num_info in file_info[_G]:
		key_num=num_info[_A]
		if key_num>=1 and key_num<=8:
			base_dir=getDir(_D)
			if not os.path.exists(base_dir):os.mkdir(base_dir)
			file_dir=f"{base_dir}{file_info[_F]}";key_dir=f"{base_dir}boss_key.png";num_im=Image.open(file_dir);key_im=Image.open(key_dir);key_im=key_im.rotate(45,PIL.Image.Resampling.NEAREST,expand=1);num_im=num_im.crop(num_info[_B]);Image.Image.paste(key_im,num_im,(40,10));bbox=key_im.getbbox();key_im=key_im.crop(bbox);key_im=key_im.resize((32,32));key_im.save(f"{getDir('assets/Non-Code/file_screen/key')}{key_num}.png")
kong_res=32,32
for kong in kongs:
	base_dir=getDir(_E)
	if not os.path.exists(base_dir):os.mkdir(base_dir)
	im=Image.new(mode=_C,size=(64,64))
	for x in range(2):
		im1=Image.open(f"{hash_dir}{kong}_face_{x}.png");x_p=32*x
		if kong in('dk','tiny'):x_p=32-x_p
		Image.Image.paste(im,im1,(x_p,0))
	im=im.resize(kong_res);im.save(f"{base_dir}{kong}_face.png")
im=Image.new(mode=_C,size=(64,64))
shared_x_move=[4,16,30,10,26]
shared_y_move=[0,0,0,23,23]
kong_z_order=[0,1,2,3,4]
disp_dir=getDir(_E)
for x in range(5):kong_index=kong_z_order[x];im1=Image.open(f"{disp_dir}{kongs[kong_index]}_face.png");im.paste(im1,(shared_x_move[kong_index],shared_y_move[kong_index]),im1)
bbox=im.getbbox()
im=im.crop(bbox)
im=im.resize(kong_res)
im.save(f"{disp_dir}shared.png")
im=Image.new(mode=_C,size=kong_res)
im.save(f"{disp_dir}none.png")
im=Image.new(mode=_C,size=(44,44))
im.save(f"{disp_dir}empty44.png")
im=Image.new(mode=_C,size=(32,64))
im.save(f"{disp_dir}empty3264.png")
im=Image.open(f"{disp_dir}soldout_bismuth.png")
im_height=26
im=im.resize((32,im_height))
im1=Image.new(mode=_C,size=(32,32))
Image.Image.paste(im1,im,(0,int((32-im_height)/2)))
im1.save(f"{disp_dir}soldout32.png")
im=Image.open(f"{hash_dir}specialchars.png")
im=im.crop((30,0,55,32))
bbox=im.getbbox()
im=im.crop(bbox)
imw,imh=im.size
if imh==0:imh=1
imhb=22
scale=imhb/imh
imw=int(imw*scale)
im=im.resize((imw,imhb))
im1=Image.open(f"{hash_dir}WXYL.png")
im2=Image.new(mode=_C,size=(32,32))
Image.Image.paste(im1,im2,(61,0))
Image.Image.paste(im1,im,(65,1))
im1.save(f"{disp_dir}wxys.png")
for idx in range(2):
	im=Image.open(f"{hash_dir}red_qmark_{idx}.png");im_hsv=im.convert('HSV');H,S,V=im_hsv.split();H=H.point(lambda p:p+40 if p<10 else p);im_hsv=Image.merge('HSV',(H,S,V));im_rgb=im_hsv.convert(_C);pix_alpha=im.load();imw,imh=im.size;pix_hsv=im_rgb.load();im_new=Image.new(mode=_C,size=(imw,imh));pix_new=im_new.load()
	for x in range(imw):
		for y in range(imh):r,g,b,a=im.getpixel((x,y));r2,g2,b2,a2=im_rgb.getpixel((x,y));pix_new[(x,y)]=r2,g2,b2,a
	im_new.save(f"{disp_dir}yellow_qmark_{idx}.png")
crate_names=['standard_crate','homing_crate']
for crate in crate_names:
	base_dir=getDir(_E)
	if not os.path.exists(base_dir):os.mkdir(base_dir)
	im=Image.new(mode=_C,size=(64,64));crate_r_offset=0
	for x in range(2):
		im1=Image.open(f"{hash_dir}{crate}_{x}.png");x_p=32*x;y_p=0
		if x==1:y_p=crate_r_offset
		Image.Image.paste(im,im1,(x_p,y_p))
	im=im.resize(kong_res);im.save(f"{base_dir}{crate}.png")
lit=['num_6_lit','num_1_lit']
unlit=['num_6_unlit','num_1_unlit']
num_types=[lit,unlit]
base_dir=getDir(_E)
hash_dir=getDir(_D)
for num_type in num_types:
	number=num_type[0];line_num=num_type[1]
	if not os.path.exists(base_dir):os.mkdir(base_dir)
	line_im=Image.open(f"{hash_dir}{line_num}.png");line=line_im.crop((13,5,16,18));line_90=line.rotate(90,PIL.Image.Resampling.NEAREST,expand=1);num_im=Image.open(f"{hash_dir}{number}.png");line_y=2;num_im.paste(line_90,(5,line_y),line_90);num_im.paste(line_90,(12,line_y),line_90);num_im.save(f"{base_dir}{number}.png")
lit=['num_9_lit','num_7_lit']
unlit=['num_9_unlit','num_7_unlit']
num_types=[lit,unlit]
for num_type in num_types:number=num_type[0];line_num=num_type[1];line_im=Image.open(f"{hash_dir}{line_num}.png");line=line_im.crop((10,23,22,26));num_im=Image.open(f"{hash_dir}{number}.png");line_y=1;num_im.paste(line,(7,line_y),line);num_im.paste(line,(14,line_y),line);num_im.save(f"{base_dir}{number}.png")
rmve=[_H,_I,'boss_key.png','WXYL.png','specialchars.png','red_qmark_0.png','red_qmark_1.png']
for kong in kongs:
	for x in range(2):rmve.append(f"{kong}_face_{x}.png")
for x in rmve:
	if os.path.exists(f"{getDir(_D)}{x}"):os.remove(f"{getDir(_D)}{x}")