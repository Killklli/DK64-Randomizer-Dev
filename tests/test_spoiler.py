'Temp file used for testing new logic system.'
_C='forward'
_B='algorithm'
_A=True
import random
from copy import deepcopy
import pytest
from randomizer.Fill import Generate_Spoiler
from randomizer.Lists import Exceptions
from randomizer.Settings import Settings
from randomizer.Spoiler import Spoiler
@pytest.fixture
def generate_settings():B=False;A={};A['seed']=random.randint(0,100000000);A['blocker_0']=0;A['blocker_1']=0;A['blocker_2']=0;A['blocker_3']=0;A['blocker_4']=0;A['blocker_5']=0;A['blocker_6']=0;A['blocker_7']=100;A['troff_0']=100;A['troff_1']=100;A['troff_2']=100;A['troff_3']=100;A['troff_4']=100;A['troff_5']=100;A['troff_6']=100;A['unlock_all_moves']=B;A['kasplat_rando']=B;A['unlock_all_kongs']=B;A['crown_door_open']=B;A['coin_door_open']=B;A['unlock_fairy_shockwave']=B;A['krool_phase_count']=4;A['download_patch_file']=_A;A['music_bgm']=_A;A['music_fanfares']=_A;A['music_events']=_A;A['generate_spoilerlog']=_A;A['fast_start_beginning_of_game']=B;A['helm_setting']='default';A['quality_of_life']=_A;A['enable_tag_anywhere']=B;A['random_krool_phase_order']=_A;return A
def test_forward(generate_settings):B=generate_settings;B[_B]=_C;A=Settings(B);A.shuffle_loading_zones='all';A.decoupled_loading_zones=_A;C=Spoiler(A);Generate_Spoiler(C);C.toJson()
def test_shuffles(generate_settings):
	B=generate_settings;B[_B]=_C;D=Settings(B);A=deepcopy(D);A.training_barrels=_A;A.unlock_all_moves=_A;A.unlock_all_kongs=_A;A.unlock_fairy_shockwave=_A;A.shuffle_items='moves';A.shuffle_loading_zones='all';A.decoupled_loading_zones=_A;C=Spoiler(A)
	try:Generate_Spoiler(C);C.toJson()
	except Exception:pass
def test_assumed(generate_settings):
	A=generate_settings;A[_B]='assumed';C=Settings(A);B=Spoiler(C)
	try:Generate_Spoiler(B);B.toJson()
	except Exception:pass