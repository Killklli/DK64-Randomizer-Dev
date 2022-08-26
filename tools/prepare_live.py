'Convert files to their minified types.'
_A=True
import glob,os,shutil,subprocess
from pathlib import Path
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
def get_files(path,extension,recursive=False):
	'Generate filepaths for each file into path with the target extension.';C='/*.';B=extension
	if not recursive:
		for A in glob.iglob(path+C+B):yield A
	else:
		for (D,E,F) in os.walk(path):
			for A in glob.iglob(D+C+B):yield A
def find_list_resources(tag,attribute,soup):
	'Find resources based off of their tag and attributes.';list=[]
	for A in soup.findAll(tag):
		try:list.append(A[attribute])
		except KeyError:pass
	return list
for f in [*get_files(os.getcwd(),'html.jinja2',recursive=_A),*get_files(os.getcwd(),'html',recursive=_A)]:
	with open(f,'r')as reader:
		html=reader.read();soup=BeautifulSoup(html,features='html.parser');image_src=find_list_resources('img','src',soup);script_src=find_list_resources('script','src',soup);css_link=find_list_resources('link','href',soup)
		for link in [*(css_link),*(script_src),*(image_src)]:
			if'http://'in link or'https://'in link:
				file_name='/web_cache'+urlparse(link).path+urlparse(link).query;Path(os.getcwd()+os.path.dirname(file_name)).mkdir(parents=_A,exist_ok=_A);req=requests.get(link,allow_redirects=False);open(f".{file_name}",'wb').write(req.content);html=html.replace(link,f".{file_name}")
				with open(f,'w')as writer:writer.write(html)
subprocess.run(['pyminify','-i','.'])
subprocess.run(['python3','setup.py','bdist_wheel'])
shutil.copyfile('dist/dk64rando-1.0.0-py3-none-any.whl','static/py_libraries/dk64rando-1.0.0-py3-none-any.whl')