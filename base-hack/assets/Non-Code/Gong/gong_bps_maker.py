'Generate the BPS files from the .bin gong files.'
_A='flips.exe'
import os,shutil,subprocess
shutil.copyfile('..\\..\\..\\build\\flips.exe',_A)
subprocess.Popen([_A,'--create','85722C_ZLib.bin','gong_source.bin','gong_geometry.bps','--bps']).wait()
if os.path.exists(_A):os.remove(_A)
print('File converted')