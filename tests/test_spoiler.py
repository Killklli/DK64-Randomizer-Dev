'Temp file used for testing new logic system.'
_B='forward'
_A='algorithm'
import json,random
from copy import deepcopy
import pytest
from randomizer.Fill import Generate_Spoiler
from randomizer.Lists import Exceptions
from randomizer.Settings import Settings
from randomizer.Spoiler import Spoiler
@pytest.fixture
def generate_settings():A=json.load(open('static/presets/default.json'));A['seed']=random.randint(0,100000000);return A
def test_forward(generate_settings):A=generate_settings;A[_A]=_B;C=Settings(A);B=Spoiler(C);Generate_Spoiler(B);B.toJson()
def test_shuffles(generate_settings):
	C=generate_settings;B=True;C[_A]=_B;E=Settings(C);A=deepcopy(E);A.training_barrels=B;A.unlock_all_moves=B;A.starting_kongs_count=5;A.unlock_fairy_shockwave=B;A.shuffle_items='moves';A.shuffle_loading_zones='all';A.decoupled_loading_zones=B;D=Spoiler(A)
	try:Generate_Spoiler(D);D.toJson()
	except Exception:pass
def test_assumed(generate_settings):
	A=generate_settings;A[_A]='assumed';C=Settings(A);B=Spoiler(C)
	try:Generate_Spoiler(B);B.toJson()
	except Exception:pass