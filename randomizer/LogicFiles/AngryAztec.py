'Logic file for Angry Aztec.'
_C=None
_B=False
_A=True
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MinigameType import MinigameType
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.LogicClasses import Event,LocationLogic,Region,TransitionFront
LogicRegions={Regions.AngryAztecStart:Region('Angry Aztec Start',Levels.AngryAztec,_A,_C,[LocationLogic(Locations.AztecDonkeyMedal,lambda l:l.ColoredBananas[Levels.AngryAztec][Kongs.donkey]>=75),LocationLogic(Locations.AztecDiddyMedal,lambda l:l.ColoredBananas[Levels.AngryAztec][Kongs.diddy]>=75),LocationLogic(Locations.AztecLankyMedal,lambda l:l.ColoredBananas[Levels.AngryAztec][Kongs.lanky]>=75),LocationLogic(Locations.AztecTinyMedal,lambda l:l.ColoredBananas[Levels.AngryAztec][Kongs.tiny]>=75),LocationLogic(Locations.AztecChunkyMedal,lambda l:l.ColoredBananas[Levels.AngryAztec][Kongs.chunky]>=75),LocationLogic(Locations.AztecDonkeyFreeLlama,lambda l:Events.LlamaFreed in l.Events and l.donkey),LocationLogic(Locations.AztecChunkyVases,lambda l:l.pineapple and l.chunky),LocationLogic(Locations.AztecKasplatSandyBridge,lambda l:not l.settings.kasplat_location_rando and l.coconut and(l.strongKong and l.isdonkey or l.settings.damage_amount=='default')),LocationLogic(Locations.AztecKasplatOnTinyTemple,lambda l:not l.settings.kasplat_location_rando and l.jetpack)],[Event(Events.AztecEntered,lambda l:_A)],[TransitionFront(Regions.AngryAztecLobby,lambda l:_A,Transitions.AztecToIsles),TransitionFront(Regions.TempleStart,lambda l:l.peanut and l.isdiddy or l.grape and l.islanky or l.feather and l.istiny or l.pineapple and l.ischunky),TransitionFront(Regions.AngryAztecMain,lambda l:l.settings.open_levels or l.guitar and l.diddy),TransitionFront(Regions.CandyAztec,lambda l:_A),TransitionFront(Regions.AztecBossLobby,lambda l:_A)]),Regions.TempleStart:Region('Temple Start',Levels.AngryAztec,_B,-1,[LocationLogic(Locations.AztecTinyKlaptrapRoom,lambda l:l.mini and l.istiny),LocationLogic(Locations.AztecChunkyKlaptrapRoom,lambda l:l.triangle and l.ischunky)],[],[TransitionFront(Regions.AngryAztecStart,lambda l:_A),TransitionFront(Regions.TempleUnderwater,lambda l:_A)]),Regions.TempleUnderwater:Region('Temple Underwater',Levels.AngryAztec,_B,-1,[LocationLogic(Locations.TinyKong,lambda l:l.CanFreeTiny()),LocationLogic(Locations.AztecDiddyFreeTiny,lambda l:l.CanFreeTiny()),LocationLogic(Locations.AztecLankyVulture,lambda l:l.Slam and l.grape and l.islanky),LocationLogic(Locations.AztecBattleArena,lambda l:l.Slam and l.grape and l.islanky)],[],[TransitionFront(Regions.TempleStart,lambda l:_A)]),Regions.AngryAztecMain:Region('Angry Aztec Main',Levels.AngryAztec,_A,_C,[LocationLogic(Locations.AztecDiddyRamGongs,lambda l:l.charge and l.jetpack and l.diddy),LocationLogic(Locations.AztecDiddyVultureRace,lambda l:l.jetpack and l.diddy),LocationLogic(Locations.AztecChunkyCagedBarrel,lambda l:l.hunkyChunky and l.ischunky,MinigameType.BonusBarrel),LocationLogic(Locations.AztecKasplatNearLab,lambda l:not l.settings.kasplat_location_rando)],[Event(Events.FedTotem,lambda l:l.settings.high_req or l.jetpack and l.peanut and l.Slam and l.diddy)],[TransitionFront(Regions.AngryAztecStart,lambda l:_A),TransitionFront(Regions.DonkeyTemple,lambda l:Events.FedTotem in l.Events and l.coconut and l.isdonkey,Transitions.AztecMainToDonkey),TransitionFront(Regions.DiddyTemple,lambda l:Events.FedTotem in l.Events and l.peanut and l.isdiddy,Transitions.AztecMainToDiddy),TransitionFront(Regions.LankyTemple,lambda l:Events.FedTotem in l.Events and l.grape and l.islanky,Transitions.AztecMainToLanky),TransitionFront(Regions.TinyTemple,lambda l:Events.FedTotem in l.Events and l.feather and l.istiny,Transitions.AztecMainToTiny),TransitionFront(Regions.ChunkyTemple,lambda l:Events.FedTotem in l.Events and l.pineapple and l.ischunky,Transitions.AztecMainToChunky),TransitionFront(Regions.AztecTinyRace,lambda l:l.charge and l.jetpack and l.diddy and l.mini and l.saxophone and l.istiny,Transitions.AztecMainToRace),TransitionFront(Regions.LlamaTemple,lambda l:l.coconut and l.isdonkey or l.grape and l.islanky or l.feather and l.istiny),TransitionFront(Regions.AztecBaboonBlast,lambda l:l.blast and l.isdonkey),TransitionFront(Regions.CrankyAztec,lambda l:_A),TransitionFront(Regions.Snide,lambda l:_A),TransitionFront(Regions.FunkyAztec,lambda l:_A),TransitionFront(Regions.AztecDonkeyQuicksandCave,lambda l:Events.AztecDonkeySwitch in l.Events and l.strongKong and l.donkey)]),Regions.AztecDonkeyQuicksandCave:Region('Aztec Donkey Sand Tunnel',Levels.AngryAztec,_B,-1,[LocationLogic(Locations.AztecDonkeyQuicksandCave,lambda l:l.isdonkey,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.AngryAztecMain,lambda l:l.isdonkey and l.strongKong)]),Regions.AztecBaboonBlast:Region('Aztec Baboon Blast',Levels.AngryAztec,_B,_C,[],[Event(Events.LlamaFreed,lambda l:l.isdonkey)],[TransitionFront(Regions.AngryAztecMain,lambda l:_A)]),Regions.DonkeyTemple:Region('Donkey Temple',Levels.AngryAztec,_B,TransitionFront(Regions.AngryAztecStart,lambda l:l.coconut and l.isdonkey),[LocationLogic(Locations.AztecDonkey5DoorTemple,lambda l:l.coconut and l.isdonkey)],[],[TransitionFront(Regions.AngryAztecMain,lambda l:_A,Transitions.AztecDonkeyToMain)]),Regions.DiddyTemple:Region('Diddy Temple',Levels.AngryAztec,_B,TransitionFront(Regions.AngryAztecStart,lambda l:l.peanut and l.isdiddy),[LocationLogic(Locations.AztecDiddy5DoorTemple,lambda l:l.peanut and l.isdiddy)],[],[TransitionFront(Regions.AngryAztecMain,lambda l:_A,Transitions.AztecDiddyToMain)]),Regions.LankyTemple:Region('Lanky Temple',Levels.AngryAztec,_B,TransitionFront(Regions.AngryAztecStart,lambda l:l.grape and l.islanky),[LocationLogic(Locations.AztecLanky5DoorTemple,lambda l:l.grape and l.islanky,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.AngryAztecMain,lambda l:_A,Transitions.AztecLankyToMain)]),Regions.TinyTemple:Region('Tiny Temple',Levels.AngryAztec,_B,TransitionFront(Regions.AngryAztecStart,lambda l:l.feather and l.istiny),[LocationLogic(Locations.AztecTiny5DoorTemple,lambda l:l.feather and l.istiny),LocationLogic(Locations.AztecBananaFairyTinyTemple,lambda l:l.camera and l.feather and l.mini and l.istiny)],[],[TransitionFront(Regions.AngryAztecMain,lambda l:_A,Transitions.AztecTinyToMain)]),Regions.ChunkyTemple:Region('Chunky Temple',Levels.AngryAztec,_B,TransitionFront(Regions.AngryAztecStart,lambda l:l.pineapple and l.ischunky),[LocationLogic(Locations.AztecChunky5DoorTemple,lambda l:l.pineapple and l.ischunky,MinigameType.BonusBarrel),LocationLogic(Locations.AztecKasplatChunky5DT,lambda l:not l.settings.kasplat_location_rando and l.pineapple and l.ischunky)],[],[TransitionFront(Regions.AngryAztecMain,lambda l:_A,Transitions.AztecChunkyToMain)]),Regions.AztecTinyRace:Region('Aztec Tiny Race',Levels.AngryAztec,_B,_C,[LocationLogic(Locations.AztecTinyBeetleRace,lambda l:l.istiny)],[],[TransitionFront(Regions.AngryAztecMain,lambda l:_A,Transitions.AztecRaceToMain)],Transitions.AztecMainToRace),Regions.LlamaTemple:Region('Llama Temple',Levels.AngryAztec,_A,-1,[LocationLogic(Locations.LankyKong,lambda l:l.CanFreeLanky()),LocationLogic(Locations.AztecDonkeyFreeLanky,lambda l:l.CanFreeLanky()),LocationLogic(Locations.AztecLankyLlamaTempleBarrel,lambda l:l.trombone and l.islanky,MinigameType.BonusBarrel),LocationLogic(Locations.AztecLankyMatchingGame,lambda l:l.grape and l.Slam and l.lanky),LocationLogic(Locations.AztecBananaFairyLlamaTemple,lambda l:l.camera)],[Event(Events.AztecDonkeySwitch,lambda l:l.Slam and l.donkey),Event(Events.AztecLlamaSpit,lambda l:l.bongos and l.donkey)],[TransitionFront(Regions.AngryAztecMain,lambda l:_A),TransitionFront(Regions.LlamaTempleBack,lambda l:l.mini and l.tiny)]),Regions.LlamaTempleBack:Region('Llama Temple Back',Levels.AngryAztec,_B,-1,[LocationLogic(Locations.AztecTinyLlamaTemple,lambda l:l.Slam and l.twirl and l.istiny),LocationLogic(Locations.AztecKasplatLlamaTemple,lambda l:not l.settings.kasplat_location_rando)],[],[TransitionFront(Regions.LlamaTemple,lambda l:_A)]),Regions.AztecBossLobby:Region('Aztec Boss Lobby',Levels.AngryAztec,_A,_C,[],[],[TransitionFront(Regions.AztecBoss,lambda l:l.IsBossReachable(Levels.AngryAztec))]),Regions.AztecBoss:Region('Aztec Boss',Levels.AngryAztec,_B,_C,[LocationLogic(Locations.AztecKey,lambda l:l.IsBossBeatable(Levels.AngryAztec))],[],[])}