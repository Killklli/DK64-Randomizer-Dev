'Logic file for Hideout Helm.'
_A=True
from randomizer.Enums.Events import Events
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.LogicClasses import Event,LocationLogic,Region,TransitionFront
LogicRegions={Regions.HideoutHelmStart:Region('Hideout Helm Start',Levels.HideoutHelm,_A,None,[],[],[TransitionFront(Regions.HideoutHelmLobby,lambda l:_A),TransitionFront(Regions.HideoutHelmMain,lambda l:l.settings.fast_start_hideout_helm or l.handstand and l.lanky and l.pineapple and l.chunky and l.mini and l.istiny)]),Regions.HideoutHelmMain:Region('Hideout Helm Main',Levels.HideoutHelm,_A,-1,[LocationLogic(Locations.HelmBattleArena,lambda l:l.jetpack and l.diddy),LocationLogic(Locations.HelmDonkey1,lambda l:(l.settings.fast_start_hideout_helm or l.bongos)and l.isdonkey,_A),LocationLogic(Locations.HelmDonkey2,lambda l:(l.settings.fast_start_hideout_helm or l.bongos)and l.isdonkey,_A),LocationLogic(Locations.HelmDonkeyMedal,lambda l:Events.HelmDonkeyDone in l.Events),LocationLogic(Locations.HelmChunky1,lambda l:(l.settings.fast_start_hideout_helm or l.triangle)and l.ischunky,_A),LocationLogic(Locations.HelmChunky2,lambda l:(l.settings.fast_start_hideout_helm or l.triangle)and l.ischunky,_A),LocationLogic(Locations.HelmChunkyMedal,lambda l:Events.HelmChunkyDone in l.Events),LocationLogic(Locations.HelmTiny1,lambda l:(l.settings.fast_start_hideout_helm or l.saxophone)and l.istiny,_A),LocationLogic(Locations.HelmTiny2,lambda l:(l.settings.fast_start_hideout_helm or l.saxophone)and l.istiny,_A),LocationLogic(Locations.HelmTinyMedal,lambda l:Events.HelmTinyDone in l.Events),LocationLogic(Locations.HelmLanky1,lambda l:(l.settings.fast_start_hideout_helm or l.trombone)and l.islanky,_A),LocationLogic(Locations.HelmLanky2,lambda l:(l.settings.fast_start_hideout_helm or l.trombone)and l.islanky,_A),LocationLogic(Locations.HelmLankyMedal,lambda l:Events.HelmLankyDone in l.Events),LocationLogic(Locations.HelmDiddy1,lambda l:(l.settings.fast_start_hideout_helm or l.guitar)and l.isdiddy,_A),LocationLogic(Locations.HelmDiddy2,lambda l:(l.settings.fast_start_hideout_helm or l.guitar)and l.isdiddy,_A),LocationLogic(Locations.HelmDiddyMedal,lambda l:Events.HelmDiddyDone in l.Events),LocationLogic(Locations.HelmBananaFairy1,lambda l:l.camera and Events.HelmKeyAccess in l.Events),LocationLogic(Locations.HelmBananaFairy2,lambda l:l.camera and Events.HelmKeyAccess in l.Events),LocationLogic(Locations.HelmKey,lambda l:Events.HelmKeyAccess in l.Events)],[Event(Events.HelmDoorsOpened,lambda l:l.grab and l.donkey and l.jetpack and l.diddy and l.punch and l.chunky),Event(Events.HelmDonkeyDone,lambda l:(Events.HelmDoorsOpened in l.Events or l.settings.fast_start_hideout_helm)and l.HelmDonkey1 and l.HelmDonkey2),Event(Events.HelmChunkyDone,lambda l:(Events.HelmDonkeyDone in l.Events or l.settings.fast_start_hideout_helm)and l.HelmChunky1 and l.HelmChunky2),Event(Events.HelmTinyDone,lambda l:(Events.HelmChunkyDone in l.Events or l.settings.fast_start_hideout_helm)and l.HelmTiny1 and l.HelmTiny2),Event(Events.HelmLankyDone,lambda l:(Events.HelmTinyDone in l.Events or l.settings.fast_start_hideout_helm)and l.HelmLanky1 and l.HelmLanky2),Event(Events.HelmDiddyDone,lambda l:(Events.HelmLankyDone in l.Events or l.settings.fast_start_hideout_helm)and l.HelmDiddy1 and l.HelmDiddy2),Event(Events.HelmKeyAccess,lambda l:(Events.HelmDonkeyDone in l.Events and Events.HelmChunkyDone in l.Events and Events.HelmTinyDone in l.Events and Events.HelmLankyDone in l.Events and Events.HelmDiddyDone in l.Events)and(l.settings.crown_door_open or l.BattleCrowns>=4)and(l.settings.coin_door_open or l.nintendoCoin and l.rarewareCoin))],[])}