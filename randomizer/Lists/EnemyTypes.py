'List of enemies with in-game index.'
_B=True
_A=False
from enum import IntEnum
from os import kill
class Enemies(IntEnum):'List of Enemies with in-game index.';BeaverBlue=0;GiantClam=1;Krash=2;Book=3;ZingerCharger=5;Klobber=6;Snide=7;ArmyDillo=8;Klump=9;Cranky=11;Funky=12;Candy=13;Beetle=14;Mermaid=15;Kaboom=16;VultureTemple=17;Squawks=18;CutsceneDK=19;CutsceneDiddy=20;CutsceneLanky=21;CutsceneTiny=22;CutsceneChunky=23;TandSPadlock=24;Llama=25;MadJack=26;KlaptrapGreen=27;ZingerLime=28;VultureRace=29;KlaptrapPurple=30;KlaptrapRed=31;GetOut=32;BeaverGold=33;FireColumn=35;TNTMinecart0=36;TNTMinecart1=37;Pufftoss=38;SeasickCannon=39;KRoolFoot=40;Fireball=42;MushroomMan=44;Troff=46;BadHitDetectionMan=48;Ruler=51;ToyBox=52;Squawks1=53;Seal=54;Scoff=55;RoboKremling=56;Dogadon=57;Kremling=59;SpotlightFish=60;KasplatDK=61;KasplatDiddy=62;KasplatLanky=63;KasplatTiny=64;KasplatChunky=65;MechFish=66;Seal1=67;Fairy=68;SquawksSpotlight=69;Rabbit=72;Owl=73;NintendoLogo=74;FireBreath=75;MinigameController=76;BattleCrownController=77;ToyCar=78;TNTMinecart2=79;CutsceneObject=80;Guard=81;RarewareLogo=82;ZingerRobo=83;Krossbones=84;Shuri=85;Gimpfish=86;MrDice0=87;SirDomino=88;MrDice1=89;Rabbit1=90;FireballGlasses=92;KLumsy=93;SpiderBoss=94;SpiderSmall=95;Squawks2=96;KRoolDK=97;SkeletonHead=98;Bat=99;EvilTomato=100;Ghost=101;Pufftup=102;Kosha=103;EnemyCar=105;KRoolDiddy=106;KRoolLanky=107;KRoolTiny=108;KRoolChunky=109;Bug=110;FairyQueen=111;IceTomato=112
class EnemyData:
	'Information about the enemy.'
	def __init__(A,*,aggro=1,min_speed=15,max_speed=150,crown_enabled=_B,air=_A,size_cap=0,crown_weight=0,simple=_A,minigame_enabled=_B,killable=_B):
		'Initialize with given parameters.';A.aggro=aggro;A.min_speed=min_speed;A.max_speed=max_speed;A.crown_enabled=crown_enabled;A.air=air;A.size_cap=size_cap;A.crown_weight=crown_weight;A.simple=simple;A.minigame_enabled=minigame_enabled;A.killable=killable
		if air:A.minigame_enabled=_A
EnemyMetaData={Enemies.BeaverBlue:EnemyData(crown_weight=10,simple=_B),Enemies.Book:EnemyData(aggro=6,crown_enabled=_A,air=_B,minigame_enabled=_A),Enemies.ZingerCharger:EnemyData(air=_B,crown_weight=7),Enemies.Klobber:EnemyData(aggro=4,crown_weight=2,killable=_A),Enemies.Klump:EnemyData(crown_weight=1,killable=_A),Enemies.Kaboom:EnemyData(aggro=4,crown_weight=2,killable=_A),Enemies.KlaptrapGreen:EnemyData(crown_weight=8,simple=_B),Enemies.ZingerLime:EnemyData(air=_B,crown_weight=5),Enemies.KlaptrapPurple:EnemyData(crown_weight=2,killable=_A),Enemies.KlaptrapRed:EnemyData(crown_weight=2,killable=_A),Enemies.BeaverGold:EnemyData(crown_weight=10,simple=_B),Enemies.MushroomMan:EnemyData(aggro=4,size_cap=60,crown_weight=10,simple=_B),Enemies.Ruler:EnemyData(crown_weight=10,simple=_B),Enemies.RoboKremling:EnemyData(crown_weight=2,killable=_A),Enemies.Kremling:EnemyData(crown_weight=10,simple=_B),Enemies.KasplatDK:EnemyData(crown_weight=6),Enemies.KasplatDiddy:EnemyData(crown_weight=6),Enemies.KasplatLanky:EnemyData(crown_weight=6),Enemies.KasplatTiny:EnemyData(crown_weight=6),Enemies.KasplatChunky:EnemyData(crown_weight=6),Enemies.ZingerRobo:EnemyData(air=_B,crown_weight=5),Enemies.Krossbones:EnemyData(crown_weight=10,simple=_B),Enemies.Shuri:EnemyData(crown_enabled=_A,minigame_enabled=_A),Enemies.Gimpfish:EnemyData(aggro=1,crown_enabled=_A,minigame_enabled=_A),Enemies.MrDice0:EnemyData(crown_weight=10,simple=_B),Enemies.SirDomino:EnemyData(crown_weight=10,simple=_B),Enemies.MrDice1:EnemyData(crown_weight=10,simple=_B),Enemies.FireballGlasses:EnemyData(aggro=35,min_speed=100,max_speed=255,crown_weight=10,killable=_A),Enemies.SpiderSmall:EnemyData(crown_weight=7),Enemies.Bat:EnemyData(air=_B,crown_weight=5,minigame_enabled=_A),Enemies.EvilTomato:EnemyData(aggro=4,crown_enabled=_A,minigame_enabled=_A),Enemies.Ghost:EnemyData(crown_weight=10,simple=_B),Enemies.Pufftup:EnemyData(crown_enabled=_A,size_cap=40,minigame_enabled=_A),Enemies.Kosha:EnemyData(crown_weight=1,killable=_A),Enemies.GetOut:EnemyData(aggro=6,crown_weight=1,minigame_enabled=_A),Enemies.Guard:EnemyData(aggro=1,crown_enabled=_A,minigame_enabled=_A)}