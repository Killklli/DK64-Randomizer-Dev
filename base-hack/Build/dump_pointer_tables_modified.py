'Dump the pointer tables of our modified rom.'
_A='rom/pointer_tables_modified.log'
from recompute_pointer_table import dumpPointerTableDetails,dumpPointerTableDetailsLegacy,parsePointerTables
ROMName='./rom/dk64-randomizer-base-dev.z64'
with open(ROMName,'rb')as fh:parsePointerTables(fh);dumpPointerTableDetails(_A,fh);dumpPointerTableDetailsLegacy(_A,fh)