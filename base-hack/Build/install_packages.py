'Install packages that are required to build the base hack.'
_A='version'
import subprocess,sys,pkg_resources
installed_packages=pkg_resources.working_set
installed_packages_list=sorted(['%s==%s'%(A.key,A.version)for A in installed_packages])
required_build_packages=['pillow','requests']
current_packages=[]
for pkg in installed_packages_list:pkg_data=pkg.split('==');current_packages.append({'name':pkg_data[0],_A:pkg_data[1]})
print('Checking Packages:')
for req_pkg in required_build_packages:
	installed=False;installed_name='Not Installed'
	for cur_pkg in current_packages:
		if cur_pkg['name'].lower()==req_pkg:installed=True;installed_name=f"Installed ({cur_pkg[_A]})"
	print(f"\t{req_pkg.capitalize()}: {installed_name}")
	if not installed:print(f"\t\tInstalling {req_pkg.capitalize()}");subprocess.check_call([sys.executable,'-m','pip','install',req_pkg],stdout=subprocess.DEVNULL)