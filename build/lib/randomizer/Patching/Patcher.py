'Patcher class and Functions for modifying ROM files.'
import js
class ROM:
	'Patcher for ROM files loaded via Rompatcherjs.'
	def __init__(A,file=None):
		'Patch functions for the ROM loaded within Rompatcherjs.\n\n        This is mostly a hint file, you could directly call the javascript functions,\n        but to keep this a bit more logical for team members we just import it and treat\n        this like a bytesIO object.\n\n        Args:\n            file ([type], optional): [description]. Defaults to None.\n        '
		if file is None:A.rom=js.patchedRom
		else:A.rom=file
	def write(A,val):'Write value to current position.\n\n        Starts at 0x0 as the inital position without seeking.\n\n        Args:\n            val (int): Int value to write.\n        ';A.rom.writeU8(val)
	def writeBytes(A,byte_data):'Write an array a bytes to the current position.\n\n        Starts at 0x0 as the inital position without seeking.\n\n        Args:\n            byte_data (bytes): Bytes object to write to current position.\n        ';A.rom.writeBytes(bytes(byte_data))
	def writeString(A,string,length):'Write a string to the current position.\n\n        Starts at 0x0 as the inital position without seeking.\n\n        Args:\n            string (str): String to write.\n            length (int): Length in bytes to write.\n        ';A.rom.writeString(string,length)
	def writeMultipleBytes(G,value,size):
		'Write multiple bytes of a size to the current position.\n\n        Starts at 0x0 as the inital position without seeking.\n\n        Args:\n            value (int): Value to write.\n            size (int): Size of the bytes to write.\n        ';B=[];A=value
		for D in range(size):B.append(0)
		E=True;C=size-1
		while E:
			F=A%256;B[C]=F;A=int((A-F)/256)
			if C==0 or A==0:E=False
			C-=1
		for D in B:G.write(D)
	def isEOF(A):'Get if we are currently at the end of the ROM.\n\n        Returns:\n            bool: True or False if we are at the end of the file.\n        ';return bool(A.rom.isEOF())
	def save(A,file_name):'Save the patched file to a downloadable file.\n\n        You need to pass the whole file and extension.\n        eg save("dk64-randomizer-12345.z64")\n\n        Args:\n            file_id (str): Name of file to save as.\n        ';A.rom.fileName=file_name;A.rom.save()
	def slice(A,offset,length):'Slice the rom at a position.\n\n        Args:\n            offset (int): Starting location to offset.\n            length (int): Length to retain.\n\n        Returns:\n            javascriptPatch: RompatcherJS MarcFile for patching.\n        ';return A.rom.slice(offset,length)
	def seek(A,val):'Seek to position in current file.\n\n        Args:\n            val (int): Position to seek to.\n        ';A.rom.seek(val)
	def read(A):'Read at the current Position.\n\n        Starts at 0x0 as the inital position without seeking.\n\n        Returns:\n            int: Value read.\n        ';return int(A.rom.readU8())
	def readString(A,len):'Read data as a string.\n\n        Starts at 0x0 as the inital position without seeking.\n\n        Args:\n            len (int): Length to read.\n\n        Returns:\n            string: Data read in rom.\n        ';return str(A.rom.readString(len))
	def readBytes(A,len):'Read bytes from current position.\n\n        Starts at 0x0 as the inital position without seeking.\n\n        Args:\n            len (int): Length to read.\n\n        Returns:\n            bytes: List of bytes read from current position.\n        ';return bytes(A.rom.readBytes(len))
	def fixChecksum(A):'Fix the checksum of the current file.';js.fixChecksum(A.rom)
	def fixSecurityValue(A):'Set the security code and update the rom checksum.';A.seek(12628);A.write(0);A.fixChecksum()