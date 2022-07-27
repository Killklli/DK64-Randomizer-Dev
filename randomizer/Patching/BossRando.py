'Apply Boss Locations.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_bosses(spoiler):'Apply Boss locations based on boss_maps from spoiler.';A=spoiler;B=A.settings.rom_data;C=151;ROM().seek(B+C);ROM().writeBytes(bytearray(A.settings.boss_kongs));ROM().writeBytes(bytearray(A.settings.boss_maps));D=288;ROM().seek(B+D);ROM().writeBytes(bytearray(A.settings.kutout_kongs))