'Create complex images from in-game assets.'
_I='assets/Non-Code/displays/'
_H='assets/Non-Code/hash/'
_G='56789.png'
_F='01234.png'
_E='RGBA'
_D='image_list'
_C='image'
_B='crop'
_A='num'
from PIL import Image
import PIL,os
print('Composing complex images')
number_crop=[{_C:_F,_D:[{_A:0,_B:(0,0,20,24)},{_A:1,_B:(20,0,30,24)},{_A:2,_B:(30,0,45,24)},{_A:3,_B:(45,0,58,24)},{_A:4,_B:(58,0,76,24)}]},{_C:_G,_D:[{_A:5,_B:(0,0,14,24)},{_A:6,_B:(14,0,29,24)},{_A:7,_B:(29,0,43,24)},{_A:8,_B:(43,0,58,24)},{_A:9,_B:(58,0,76,24)}]}]
kongs=['dk','diddy','lanky','tiny','chunky']
hash_dir=_H
if not os.path.exists(hash_dir):os.mkdir(hash_dir)
for file_info in number_crop:
	for num_info in file_info[_D]:
		key_num=num_info[_A]
		if key_num>=1 and key_num<=8:
			base_dir=_H
			if not os.path.exists(base_dir):os.mkdir(base_dir)
			file_dir=f"{base_dir}{file_info[_C]}";key_dir=f"{base_dir}boss_key.png";num_im=Image.open(file_dir);key_im=Image.open(key_dir);key_im=key_im.rotate(45,PIL.Image.NEAREST,expand=1);num_im=num_im.crop(num_info[_B]);Image.Image.paste(key_im,num_im,(40,10));bbox=key_im.getbbox();key_im=key_im.crop(bbox);key_im=key_im.resize((32,32));key_im.save(f"assets/Non-Code/file_screen/key{key_num}.png")
kong_res=32,32
for kong in kongs:
	base_dir=_I
	if not os.path.exists(base_dir):os.mkdir(base_dir)
	im=Image.new(mode=_E,size=(64,64))
	for x in range(2):
		im1=Image.open(f"{hash_dir}{kong}_face_{x}.png");x_p=32*x
		if kong=='dk'or kong=='tiny':x_p=32-x_p
		Image.Image.paste(im,im1,(x_p,0))
	im=im.resize(kong_res);im.save(f"{base_dir}{kong}_face.png")
im=Image.new(mode=_E,size=(64,64))
shared_x_move=[4,16,30,10,26]
shared_y_move=[0,0,0,23,23]
kong_z_order=[0,1,2,3,4]
disp_dir=_I
for x in range(5):kong_index=kong_z_order[x];im1=Image.open(f"{disp_dir}{kongs[kong_index]}_face.png");im.paste(im1,(shared_x_move[kong_index],shared_y_move[kong_index]),im1)
bbox=im.getbbox()
im=im.crop(bbox)
im=im.resize(kong_res)
im.save(f"{disp_dir}shared.png")
im=Image.new(mode=_E,size=kong_res)
im.save(f"{disp_dir}none.png")
rmve=[_F,_G,'boss_key.png']
for kong in kongs:
	for x in range(2):rmve.append(f"{kong}_face_{x}.png")
for x in rmve:
	if os.path.exists(f"assets/Non-Code/hash/{x}"):os.remove(f"assets/Non-Code/hash/{x}")