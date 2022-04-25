//functions
extern void setFlag(int flagIndex, int value, char flagType);
extern int checkFlag(int flagIndex, char flagType);
extern void* dk_malloc(int size);
extern void dk_free(void* mallocPtr);
extern void playSound(short soundIndex, int unk0, int unk1, int unk2, int unk3, int unk4);
extern void initiateTransition(int map, int exit);
extern void initiateTransition_0(int map, int exit, int unk0, int unk1);
extern int* getFlagBlockAddress(char flagType);
extern int isAddressActor(void* address);
extern int getTimestamp();
extern void dmaFileTransfer(int romStart, int romEnd, int ramStart);
extern void deleteActor(void* actor);
extern int spawnActor(int actorID, int actorBehaviour);
extern void spawnTextOverlay(int style, int x, int y, char* string, int timer1, int timer2, unsigned char effect, unsigned char speed);
extern float dk_sqrt(float __x);
extern float dk_cos(float __x);
extern float dk_sin(float __x);
extern void dk_strFormat(char* destination, char* source, ...);
extern void dk_multiply(double val1, double val2, int unk1, int unk2);
extern double convertTimestamp(double unk0, double unk1, unsigned int unk2, unsigned int unk3);
extern void resetMap();
extern void prepKongColoring();
extern void callFunc(int* addr);
extern int getTimestampDiff(unsigned int major, unsigned int minor);
extern void patchHook(unsigned int hook_rdram_location, int offset_in_hook_list, char hook_byte_size);
extern void* dk_memcpy(void* _dest, void* _src, int size);
extern void getTimestampDiffInTicks(unsigned int major, unsigned int minor);
extern int timestampDiffToMilliseconds(unsigned int major, unsigned int minor);
extern void timestampAdd(int* timestamp1, int* timestamp2);
extern void SaveToGlobal();
extern int DetectGameOver();
extern int DetectAdventure();
extern void displaySprite(void* control_pointer, void* sprite, int x, int y, int scale, int gif_updatefrequency, int movement_style);
extern int* getOtherSpritePointer();
extern void alterSize(void* object, int size);
extern void unkSizeFunction(void* object);
extern void spawnRocketbarrel(void* object, int unk);
extern void* getObjectArrayAddr(void* init_address, int common_object_size, int index);
extern void playSong(int songIndex);
extern void loadExtraHooks();
extern void playCutscene(void* actor, int cutscene_index, int cutscene_type);
extern void setHUDItemAsInfinite(int item_index, int player_index, char isInfinite);
extern void osWritebackDCacheAll();
extern void copyFromROM(int rom_start, void* write_location, void* file_size_location, int unk1, int unk2, int unk3, int unk4);
extern int getActorSpawnerID(void* actor);
extern void textOverlayCode(void);
extern void spawnTransferredActor(void);
extern void resolveMovementBox(void* spawner);
extern void wipeMemory(void* location, int size);
extern void setArcadeTextXY(int x, int y);
extern void spawnArcadeText(void* write_location, void* text_pointer);
extern void setArcadeTextColor(int red, int green, int blue, int alpha);
extern int arcadeGetObjIndexOfType(int obj_type);
extern int arcadeGetNextVacantSlot(void);
extern void setArcadeSong(int songIndex);
extern void hideHUD(void);
extern void tagKong(int kong_actor_index);
extern void clearGun(void* player);
extern void playAnimation(void* player, int anim_index);
extern void clearTagSlide(void* player);
extern void initiateTransitionFade(int map, int cutscene, int gamemode);
extern void __osInvalICache(void* write_location, int size);
extern void __osInvalDCache(void* write_location, int size);
extern void __osWritebackDCache(void* write_location, int size);
extern void __osCreateMesgQueue(void* queue, void* message, int unk);
extern void __osRecvMesg(void* queue, void* message, int os_state);
extern void __osEPiStartDMA(void* unk, void* iomessage, int os_state);
extern void __osPiRawReadIo(int a0, void* a1);
extern int __osDisableInt();
extern void __osRestoreInt(int mask);
extern void copyFunc(int rom_offset, int size, void* write_location);
extern void* getMapData(data_indexes data_idx, int _index, char compressbyte0, char compressbyte1);
extern void loadSetup(void* setup_file, int unk0, int unk1);
extern int getParentDataIndex(int map);
extern void WarpToDKTV(void);
extern int getActorSpawnerIDFromTiedActor(void* actor);
extern void deleteActorContainer(void* actor);
extern void renderActor(void* actor, int unk0);

extern void wipeStoredSetup(void* setup);
extern void complex_free(void* ptr);
extern void createCollision(int type, void* player, collision_types subtype, int map, int exit, int x, int y, int z);
extern void setScriptRunState(void* behaviour_pointer, int destination_state, int unk0);

extern void unkObjFunction0(int id, int unk0, int unk1);
extern void unkObjFunction1(int id, int unk0, int unk1);
extern void unkObjFunction2(int id, int unk0, int unk1);
extern int unkObjFunction3(int unk0, int unk1, int unk2, int unk3, int unk4, int unk5, int unk6);
extern void unkObjFunction4(int behav_38, int unk0);
extern void unkObjFunction5(int behav_38, int unk0);
extern void unkObjFunction6(int behav_38, int unk0);
extern int touchingModel2Object(int id);
extern int GetKongUnlockedFlag(int actor_type, int kong_index);
extern void setNextTransitionType(int type);

extern int* initDisplayList(int* dl);
extern int getTextStyleHeight(int style);
extern int* displayText(int* dl, int style, int x, int y, void* text_pointer, char unk0);
extern int* displayImage(int* dl, int texture_index, int unk3, codecs codec_index, int width, int height, int x, int y, float xScale, float yScale, int unk11, float unk12);
extern void getScreenPosition(float x, float y, float z, float* x_store, float* y_store, int unk8, float scale, char player_index);
extern int* textDraw(int* dl, int style, int x, int y, char* str);

extern void cancelPausedCutscene(void);
extern void pauseCutscene(void);

extern int hasTurnedInEnoughCBs(void);
extern int getWorld(int map, int unk2);
extern void displayImageOnObject(int obj_id, int position, int image_index, int unk4);
extern void drawNumberObject(int model, int unk2, int image_index, int unk4);
extern int isLobby(int map);
extern float determineXRatioMovement(unsigned int unk);
extern int countFlagArray(int starting_flag, int count, int flagType);
extern int canHitSwitch(void);
extern void setSomeTimer(int model2_type);
extern int indexOfNextObj(int id);

extern void setWaterHeight(int chunk, float height, float unk2);
extern void loadObjectForScripting(void* unk0, int unk1);
extern void updateObjectScript(void* behaviour_pointer);
extern void executeBehaviourScript(void* behaviour_pointer, int unk0);
extern void* loadCounterFontTexture(int texture_base, void* write_location, int position, int texture_offset, int width);
extern void delayedObjectModel2Change(int map, int model2_id, int state);
extern void cycleRNG(void);

//vanilla data
extern float TransitionSpeed;
extern char CutsceneWillPlay;
extern char KRoolRound;
extern KongBase MovesBase[6];
extern int PlayerOneColor;
extern char Mode;
extern char TBVoidByte;
extern int CurrentMap;
extern int DestMap;
extern int DestExit;
extern char StorySkip;
extern char HelmTimerShown;
extern char TempFlagBlock[0x10];
extern submapInfo SubmapData[0x12];
extern char HelmTimerPaused;
extern int LagBoost;
extern int FrameLag;
extern int FrameReal;
extern int RNG;
extern char BetaNinRWSkip;
extern char LogosDestMap;
extern char LogosDestMode;
extern char Gamemode;
extern int* ObjectModel2Pointer;
extern int ObjectModel2Timer;
extern int ObjectModel2Count;
extern int ObjectModel2Count_Dupe;
extern short CutsceneIndex;
extern char CutsceneActive;
extern short CutsceneTimer;
extern cutsceneType* CutsceneTypePointer;
extern short PreviousCameraState;
extern short CurrentCameraState;
extern short CameraStateChangeTimer;
extern unsigned short CutsceneStateBitfield;
extern AutowalkData* AutowalkPointer;
extern char IsAutowalking;
extern WarpInfo PositionWarpInfo;
extern short PositionWarpBitfield;
extern float PositionFloatWarps[3];
extern unsigned short PositionFacingAngle;
extern char ChimpyCam;
extern char ScreenRatio;
extern int* CurrentActorPointer;
extern char LoadedActorCount;
extern loadedActorArr LoadedActorArray[64];
extern SpawnerMasterInfo SpawnerMasterData;
extern unsigned char MenuSkyTopRGB[3];
extern unsigned char MenuSkyRGB[3];
extern int* ActorArray[];
extern short ActorCount;
extern short ButtonsEnabledBitfield;
extern char JoystickEnabledX;
extern char JoystickEnabledY;
extern char MapState;
extern Controller ControllerInput;
extern Controller NewlyPressedControllerInput;
extern Controller PreviouslyPressedButtons;
extern playerData* Player;
extern SwapObjectData* SwapObject;
extern char Character;
extern cameraData* Camera;
extern char ISGActive;
extern unsigned int ISGTimestampMajor;
extern unsigned int ISGTimestampMinor;
extern char ISGPreviousFadeout;
extern unsigned int CurrentTimestampMajor;
extern unsigned int CurrentTimestampMinor;
extern ISGFadeoutData ISGFadeoutArray[];
extern InventoryBase CollectableBase;
extern char ModelTwoTouchCount;
extern short ModelTwoTouchArray[4];
extern char TransitionProgress;
extern Controller BackgroundHeldInput;
extern unsigned int PauseTimestampMajor;
extern unsigned int PauseTimestampMinor;
extern unsigned int HelmStartTimestampMajor;
extern unsigned int HelmStartTimestampMinor;
extern int HelmStartTime;
extern short p1PressedButtons;
extern short p1HeldButtons;
extern char player_count;
extern int* sprite_table[0xAF];
extern char sprite_translucency;
extern int* bbbandit_array[4];
extern char StoredDamage;
extern void* ActorSpawnerPointer;
extern char DebugInfoOn;
extern char CutsceneFadeActive;
extern short CutsceneFadeIndex;
extern heap* heap_pointer;
extern char stickX_magnitude;
extern char stickY_magnitude;
extern float phasewalk_stickmagnitude;
extern fairyInfo fairy_data;
extern short transferredActorType;
extern charSpawnerData characterSpawnerActors[0x71];
extern unsigned char levelIndexMapping[216];
extern char stickX_interpretted;
extern char stickY_interpretted;
extern char preventSongPlaying;
extern int parentDataCount;
extern parentMaps parentData[17];
extern void* SetupFilePointer;
extern int* focusedParentDataSetup[17];
extern hudData* HUD;
extern text_struct textData[6];
extern float LZFadeoutProgress;
extern int* mapFloorPointer;
extern int mapFloorBlockCount;
extern int displayListCount;
extern char TransitionType;
extern char DKTVKong;

extern short screenCenterX;
extern short screenCenterY;
extern float collisionPos[3];
extern char FileIndex;
extern int LockStackCount;
extern char CutsceneBarState;

extern int* TriggerArray;
extern short TriggerSize;
extern cannon* CastleCannonPointer;
extern short TroffNScoffReqArray[8]; // u16 item size
extern unsigned short TroffNScoffTurnedArray[8]; // u16 item size
extern short BLockerDefaultArray[8]; // u16 item size
extern blocker_cheat BLockerCheatArray[8]; // u16 item size, [u8 - GB, u8 - Kong]
extern short CheckmarkKeyArray[8]; // u16 item size
extern short KongFlagArray[4];
extern main_menu_moves_struct MainMenuMoves[8];
extern char DataIsCompressed[32];
extern char KutOutKongArray[5];
extern enemy_drop_struct EnemyDropsTable[27];
extern short scriptLoadedArray[0x46];
extern short scriptsLoaded;
extern unsigned char scriptLoadsAttempted;

extern purchase_struct CrankyMoves[5][7];
extern purchase_struct CandyMoves[5][7];
extern purchase_struct FunkyMoves[5][7];

extern short LobbiesArray[8];
extern short WorldArray[8];
extern short WorldExitArray[8];
extern race_exit_struct RaceExitArray[8];

extern short BossMapArray[8];
extern char BossKongArray[16];

extern char KongUnlockedMenuArray[5];
extern unsigned char FilePercentage;
extern int FileGBCount;
extern float FileScreenDLOffset;
extern short CBTurnedInArray[8];
extern short songData[0xB0];
extern unsigned int DKTVData[5];

extern charspawner_flagstruct charspawnerflags[0x1F];
extern GBDictItem GBDictionary[113];
extern actorData* CurrentActorPointer_0;

//hack data
extern int TestVariable;
extern char LoadedHooks;
extern varspace Rando;
extern short StoredLag;
extern short ReplacementLobbiesArray[9];
extern short ReplacementLobbyExitsArray[9];
extern unsigned char DamageMultiplier;
extern char* PauseSlot3TextPointer;
extern char ExpandPauseMenu;
extern unsigned short InitialPauseHeight;
extern short InstanceScriptParams[4];
extern unsigned int BalancedIGT;
extern short style128Mtx[0x10];
extern short style6Mtx[0x10];
extern short style2Mtx[0x10];
extern purchase_struct CrankyMoves_New[5][7];
extern purchase_struct CandyMoves_New[5][7];
extern purchase_struct FunkyMoves_New[5][7];
extern settingsData StoredSettings;
extern char WarpToIslesEnabled;
extern char SkipDance;
extern char permaLossMode;
extern char preventTagSpawn;
extern char bonusAutocomplete;
extern void* StoredCounterTextures[7];