//functions
extern void setFlag(int flagIndex, int value, char flagType);
extern int checkFlag(int flagIndex, char flagType);
extern int getFlagIndex(int startFlag, int level, int kong);
extern void* dk_malloc(int size);
extern void dk_free(void* mallocPtr);
extern void playSound(short soundIndex, int unk0, int unk1, int unk2, int unk3, int unk4);
extern void initiateTransition(int map, int exit);
extern void initiateTransition_0(int map, int exit, int unk0, int unk1);
extern void WarpToParent(void);
extern void ExitFromBonus(void);
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
extern int SaveToGlobal();
extern int SaveToUnk();
extern int DetectGameOver();
extern int DetectAdventure();
extern void displaySprite(void* control_pointer, void* sprite, int x, int y, int scale, int gif_updatefrequency, int movement_style);
extern int* getOtherSpritePointer();
extern void alterSize(void* object, int size);
extern void unkSizeFunction(void* object);
extern void spawnRocketbarrel(void* object, int unk);
extern void* getObjectArrayAddr(void* init_address, int common_object_size, int index);
extern void playSong(int songIndex, int volume);
extern void playLevelMusic(void);
extern void loadExtraHooks();
extern void playCutscene(void* actor, int cutscene_index, int cutscene_type);
extern void setHUDItemAsInfinite(int item_index, int player_index, char isInfinite);
extern void resetCoconutHUD(void);
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
extern int __osEepromProbe(void* unk0);
extern void copyFunc(int rom_offset, int size, void* write_location);
extern void* getMapData(data_indexes data_idx, int _index, char compressbyte0, char compressbyte1);
extern void loadSetup(void* setup_file, int unk0, int unk1);
extern int getParentDataIndex(int map);
extern void WarpToDKTV(void);
extern void initHelmTimer(void);
extern void LoadGameOver(void);
extern int getActorSpawnerIDFromTiedActor(void* actor);
extern void deleteActorContainer(void* actor);
extern void renderActor(void* actor, int unk0);
extern void initCharSpawnerActor(void);
extern void cutsceneKongGenericCode(void);
extern void DisplayTextFlagCheck(short text_file, char text_index, short flag);
extern void handleCutsceneKong(void* actor, int index);
extern void alterCutsceneKongProperties(void);
extern void unkCutsceneKongFunction(int unk0, int unk1, void* actor, int unk2, int unk3);
extern void spawnCutsceneKongText(int text_index, int text_file, int unk0);
extern void unkCutsceneKongFunction_0(int unk0, int unk1);
extern void changeActorColor(int red, int green, int blue, int alpha);
extern void unkCutsceneKongFunction_1(int unk0);
extern float getAnimationTimer(void* actor);
extern int getPadGravity(void* actor);
extern void BananaMedalGet(void);
extern void CrownGet(void);

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
extern void unkObjFunction7(int id, int unk0, int unk1);
extern int unkObjFunction8(int id, int unk0);
extern int touchingModel2Object(int id);
extern int GetKongUnlockedFlag(int actor_type, int kong_index);
extern void setNextTransitionType(int type);
extern int isPlayerInRangeOfObject(int distance);
extern int getPlayerObjectDistance(void);
extern void spawnWrinkly(behaviour_data* behaviour, int index, int door_kong_index, int unk0);
extern int isWrinklySpawned(void);
extern void setAction(int action, void* actor, int player_index);
extern void exitPortalPath(behaviour_data* behaviour, int index, int unk0, int unk1);
extern int getInteractionOfContactActor(int contact_actor);
extern void enterPortal(void* player);
extern void drawBossDoorNumber(behaviour_data* behaviour, int index, int unk0, int unk1);

extern int* initDisplayList(int* dl);
extern int getTextStyleHeight(int style);
extern int* displayText(int* dl, int style, int x, int y, void* text_pointer, char unk0);
extern int* displayImage(int* dl, int texture_index, int unk3, codecs codec_index, int width, int height, int x, int y, float xScale, float yScale, int unk11, float unk12);
extern void getScreenPosition(float x, float y, float z, float* x_store, float* y_store, int unk8, float scale, char player_index);
extern int* textDraw(int* dl, int style, int x, int y, char* str);
extern void* getPtr14Texture(int texture);
extern void renderImage_Internal(void* dl, void* texture, int unk0, int width, int height, int unk1, int unk1_copy, int unk2, int unk2_copy, float width_f, float height_f, float x_center, float y_center, int unk3);

extern void cancelPausedCutscene(void);
extern void pauseCutscene(void);
extern void getTextPointer_0(void* actor, int text_file, int text_index);

extern int hasTurnedInEnoughCBs(void);
extern int getWorld(int map, int lobby_is_isles);
extern void displayImageOnObject(int obj_id, int position, int image_index, int unk4);
extern void drawNumberObject(int model, int unk2, int image_index, int unk4);
extern int isLobby(int map);
extern float determineXRatioMovement(unsigned int unk);
extern int countFlagArray(int starting_flag, int count, int flagType);
extern int canHitSwitch(void);
extern void setSomeTimer(int model2_type);
extern int indexOfNextObj(int id);
extern int playSFXFromObject(int object_index, short sfx, char unk0, char unk1, char unk2, char unk3, float unk4);

extern void unkMultiplayerWarpFunction(void* actor, int player_index);
extern void renderScreenTransition(int transition_type);

extern void setWaterHeight(int chunk, float height, float unk2);
extern void loadObjectForScripting(void* unk0, int unk1);
extern void updateObjectScript(void* behaviour_pointer);
extern void executeBehaviourScript(void* behaviour_pointer, int unk0);
extern void* loadCounterFontTexture(int texture_base, void* write_location, int position, int texture_offset, int width);
extern void delayedObjectModel2Change(int map, int model2_id, int state);
extern void cycleRNG(void);
extern void voidWarp(void);
extern void setToeTexture(void* actor, int data);
extern void applyFootDamage(void* actor, int unk0, int unk1, int unk2);
extern void modifyCharSpawnerAttributes(int unk0, int unk1, int unk2);
extern void modifyObjectState(int object_id, int dest_state);
extern void spawnPianoKremling(int kremling_index, int unk0);
extern void setAcceptablePianoKey(int id, int key, int unk0);
extern int checkContactSublocation(void* behaviour_pointer, int id, int key, int unk0);
extern void PlayCutsceneFromModelTwoScript(void* behavior_pointer, int cutscene, int unk0, int unk1);
extern void handleGuardDetection(float offset, float radius);
extern int guardShouldMove(void);
extern void guardUnkFunction(int unk0);
extern void generalActorHandle(int control_state, int x, int z, int unk0, float unk1);
extern void handleGuardDefaultAnimation(void);
extern void setActorSpeed(void* actor, int speed);
extern void playActorAnimation(void* actor, int animation);
extern void actorUnkFunction(void);
extern int getRNGLower31(void);
extern void setActorAnimation(int animation);
extern void actorUnkFunction_0(int control_state, int unk0);
extern void spawnSparkles(float x, float y, float z, int size);
extern void spawnEnemyDrops_Vanilla(void* actor);
extern void spawnActorWithFlag(int object, int x_f, int y_f, int z_f, int unk0, int cutscene, int flag, int unk1);
extern void spawnObjectAtActor(int object, int flag);
extern void* isActorLoaded(int actor_type);
extern void beaverControlSwitchCase(int unk0, int unk1, int unk2);
extern void BonusBarrelCode(void);
extern void DisplayExplosionSprite(void);
extern void displayWarpSparkles(behaviour_data* behaviour, int index, int unk0, int unk1);
extern void setObjectScriptState(int id, int state, int offset);

extern float getXRatioMovement(int dk64u_angle);
extern float getZRatioMovement(int dk64u_angle);
extern void updateActorProjectileInfo(void* actor, int unk0);
extern void spawnProjectile(short object, short subtype, int speed, float x, float y, float z, float unk0, void* actor);
extern void controlStateControl(int unk0);
extern void save(void);
extern void getObjectPosition(int index, int unk0, int unk1, void* x, void* y, void* z);

extern int crystalsUnlocked(int kong);
extern void setMovesForAllKongs(shop_paad* paad, int is_bitfield);
extern void setMoveProgressive(shop_paad* paad, int kong);
extern void setMoveBitfield(shop_paad* paad, int kong);
extern void refillHealth(int player_index);
extern void changeCollectableCount(int item, int player_index, int change);
extern void save(void);
extern void* getSpawnerTiedActor(short target_trigger, short props_change);

extern void _guScaleF(void* mtx, int x, int y, int z);
extern void _guTranslateF(void* mtx, int x, int y, int z);
extern void _guMtxCatF(void* mtx, void* unk0, void* unk1);
extern void _guMtxF2L(void* mtx, void* unk0);
extern void* getTextPointer(int file, int text_index, int unk0);
extern void addDLToOverlay(int code, void* actor, int delay);
extern int groundContactCheck(void);
extern void groundContactSet(void);
extern int getRefillCount(int item, int player);
extern int doAllKongsHaveMove(shop_paad* paad, int unk0);
extern void getSequentialPurchase(shop_paad* paad, KongBase* movedata);
extern int ReadFile(int data, int kong, int level, int file);
extern int* printText(int* dl, short x, short y, float scale, char* str);

extern void assessFlagMapping(int map, int id);
extern void coinCBCollectHandle(int player, int obj, int is_homing);
extern void displayItemOnHUD(int item, int unk0, int unk1);
extern int getCollectableOffset(int item, int obj, int homing);
extern void GoldenBananaCode(void);

extern void unkSpriteRenderFunc(int unk0);
extern void unkSpriteRenderFunc_0(void);
extern void loadSpriteFunction(int func);
extern void displaySpriteAtXYZ(void* sprite, int scale, float x, float y, float z);
extern void* getHUDSprite(int item);
extern void updateMenuController(void* actor, void* paad, int unk0);
extern void lockInput(int unk0);
extern void fileStart(int file);
extern int isFileEmpty(int file);
extern void initMenuBackground(void* paad, int unk0);
extern int calculateFilePercentage(void);
extern void displayMenuSprite(void* paad, void* sprite_address, int x, int y, float scale, int unk0, int unk1);
extern void loadFile(int file, int restock_inventory);
extern void loadEndSeq(int mode);
extern void checkGlobalProgress(int flag);
extern void updateCutscene(void);
extern void loadDKTVData(void);
extern void clearActorList(void);
extern void updateModelScales(void* actor, int size);
extern void WipeFile(int file, int will_save);
extern void WipeImageCache(void);
extern void calculateScreenPosition(float x, float y, float z, float* x_store, float* y_store, int unk0, float unk1, int unk2);
extern int getNewSaveTime(void);
extern void unkBonusFunction(actorData* actor);
extern void internalKasplatCode(int has_bp);

extern void spriteActorGenericCode(float unk0);
extern void assignGIFToActor(void* paad, void* sprite, int scale_f);
extern int loadSetupNew(int map);
extern int getParentIndex(int map);

extern void wipeTextureSlot(void* location);
extern void copyImage(void* location, void* image, int width);
extern void blink(void* actor, int unk0, int unk1);
extern void applyImageToActor(void* actor, int unk0, int unk1);
extern void writeImageSlotToActor(void* actor, int unk0, int unk1, void* location);

//vanilla data
extern float TransitionSpeed;
extern char CutsceneWillPlay;
extern char KRoolRound;
extern KongBase MovesBase[6];
extern int PlayerOneColor;
extern char** PauseTextPointer;
extern char** LevelNamesPointer;
extern char Mode;
extern char TBVoidByte;
extern int CurrentMap;
extern short PreviousMap;
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
extern skybox_blend_struct SkyboxBlends[8];
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
extern short HelmMinigameFlags[10];
extern short p1PressedButtons;
extern short p1HeldButtons;
extern char player_count;
extern int* sprite_table[0xAF];
extern char sprite_translucency;
extern int* bbbandit_array[4];
extern char StoredDamage;
extern actorSpawnerData* ActorSpawnerPointer;
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
extern cutsceneType CutsceneBanks[2];
extern int EEPROMType;

extern short MapVoid_MinX;
extern short MapVoid_MinZ;
extern short MapVoid_MaxX;
extern short MapVoid_MaxZ;

extern bonus_barrel_info BonusBarrelData[54];

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
extern char FilePercentage; // Unsigned is technically correct, but -124% is more fun
extern int FileGBCount;
extern float FileScreenDLOffset;
extern short CBTurnedInArray[8];
extern short songData[0xB0];
extern unsigned int DKTVData[5];

extern void* ExitPointer;
extern unsigned char ExitCount;

extern charspawner_flagstruct charspawnerflags[0x1F];
extern GBDictItem GBDictionary[113];
extern actorData* CurrentActorPointer_0;
extern short MusicTrackChannels[12];
extern float BoatSpeeds[2];
extern short textParameter;

extern unsigned char collisionType;
extern unsigned char collisionActive;
extern actorData* PlayerPointer_0;
extern SpawnerInfo* currentCharSpawner;
extern short EnemiesKilledCounter;
extern model2_collision_info ModelTwoCollisionArray[42];
extern unsigned char MelonArray[6];
extern int IGT;
extern unsigned int LevelStateBitfield;

extern float menuHeadX[5];
extern float menuHeadY[5];
extern float menuHeadScale[5];
extern collected_item_struct* LatestCollectedObject;
extern image_cache_struct ImageCache[32];

extern short* AnimationTable1;
extern short* AnimationTable2;
extern short* AnimationTable3;
extern SpawnerInfo* TiedCharacterSpawner;
extern kong_model_struct KongModelData[8];
extern tag_model_struct TagModelData[5];
extern short RollingSpeeds[7];
extern int KongTagNames[9];
extern short KrazyKKModels[6];
extern short ChargeVelocities_0[7];
extern short ChargeVelocities_1[7];
extern short ChargeDeceleration[7];
extern char* KongTextNames[8];

extern actor_behaviour_def ActorBehaviourTable[128];
extern float LedgeHangY[7];
extern float LedgeHangY_0[7];

//hack data
extern int TestVariable;
extern char LoadedHooks;
extern varspace Rando;
extern short StoredLag;
extern short ReplacementLobbiesArray[9];
extern short ReplacementLobbyExitsArray[9];
extern unsigned char DamageMultiplier;
extern char LobbiesOpen;
extern char* PauseSlot3TextPointer;
extern char ExpandPauseMenu;
extern unsigned short InitialPauseHeight;
extern short InstanceScriptParams[4];
extern short style128Mtx[0x10];
extern short style6Mtx[0x10];
extern short style2Mtx[0x10];
extern purchase_struct CrankyMoves_New[5][8];
extern purchase_struct CandyMoves_New[5][8];
extern purchase_struct FunkyMoves_New[5][8];
extern purchase_struct TrainingMoves_New[4];
extern purchase_struct BFIMove_New;
extern settingsData StoredSettings;
extern char WarpToIslesEnabled;
extern char permaLossMode;
extern char preventTagSpawn;
extern char bonusAutocomplete;
extern void* StoredCounterTextures[7];
extern char TextHoldOn;
extern unsigned char PauseText;
extern unsigned char ShorterBosses;
extern char ForceStandardAmmo;
extern char KKOPhaseRandoOn;
extern char KKOPhaseOrder[3];
extern unsigned short MultiBunchCount;
extern char QueueHelmTimer;
extern char ToggleAmmoOn;
extern void* WarpData;
extern unsigned char InvertedControls;
extern unsigned char WinCondition;
extern unsigned char ChunkyModel;
extern unsigned char EnemyInView;
extern unsigned char ItemRandoOn;
extern short ItemRando_FLUT[0x320];
extern arbitrary_overlay TextOverlayData;
extern unsigned char KasplatSpawnBitfield;
