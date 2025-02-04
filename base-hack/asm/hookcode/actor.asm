damageMultiplerCode:
    BGEZ 	a3, damageMultiplerCode_Finish
    LB 		t9, 0x2FD (v0)
    SUBU 	t2, r0, a3
    SLTI 	t2, t2, 12
    BEQZ 	t2, damageMultiplerCode_Finish
    NOP
    LUI 	t2, hi(DamageMultiplier)
    LBU 	t2, lo(DamageMultiplier) (t2)
    MULTU 	a3, t2
    MFLO 	a3

    damageMultiplerCode_Finish:
        J 		0x806C9A84
        ADDU 	t0, t9, a3

tagPreventCode:
    LUI 		a1, hi(preventTagSpawn)
    LBU 		a1, lo(preventTagSpawn) (a1)
    BEQZ 		a1, tagPreventCode_Vanilla
    NOP
    LH 			a1, 0x0 (s1)
    ADDIU 		a1, a1, 0x10
    ADDIU 		t8, r0, 98
    BEQ 		a1, t8, tagPreventCode_Prevent
    NOP
    ADDIU 		t8, r0, 136
    BEQ 		a1, t8, tagPreventCode_Prevent
    NOP
    ADDIU 		t8, r0, 137
    BEQ 		a1, t8, tagPreventCode_Prevent
    NOP

    tagPreventCode_Vanilla:
        LH 		a1, 0x0 (s1)
        J 		0x8068953C
        SUBU 	t3, t3, r0

    tagPreventCode_Prevent:
        J 		0x8068968C
        NOP

destroyAllBarrelsCode:
    LW 			t6, 0x0 (s1)
    SB 			v0, 0x131 (t6)
    LUI 		a0, hi(Gamemode)
    LBU 		a0, lo(Gamemode) (a0)
    ADDIU 		t0, r0, 3
    BEQ 		a0, t0, destroyAllBarrelsCode_Finish
    NOP
    LUI 		a0, hi(bonusAutocomplete)
    LBU 		a0, lo(bonusAutocomplete) (a0)
    ANDI 		t0, a0, 1
    BEQZ 		t0, destroyAllBarrelsCode_Helm
    NOP
    LW 			t0, 0x58 (t6)
    ADDIU 		v0, r0, 0x1C
    BNE 		t0, v0, destroyAllBarrelsCode_Helm
    NOP
    ADDIU 		t0, r0, 0xC
    SB 			t0, 0x154 (t6)
    SB 			r0, 0x155 (t6)
    ADDIU 		t0, r0, 3
    SB 			t0, 0x185 (t6)

    destroyAllBarrelsCode_Helm:
    ANDI 		t0, a0, 2
    BEQZ  		t0, destroyAllBarrelsCode_Finish
    NOP
    LW 			t0, 0x58 (t6)
    ADDIU 		v0, r0, 0x6B
    BNE 		t0, v0, destroyAllBarrelsCode_Finish
    NOP
    ADDIU 		t0, r0, 0xC
    SB 			t0, 0x154 (t6)
    SB 			r0, 0x155 (t6)
    ADDIU 		t0, r0, 3
    SB 			t0, 0x185 (t6)

    destroyAllBarrelsCode_Finish:
    J 			0x80680D18
    NOP

destroyAllBarrelsCodeNew:
    LUI         a3, hi(CurrentActorPointer_0)
    LW          a3, lo(CurrentActorPointer_0) (a3)
    LUI         v0, hi(Gamemode)
    LBU         v0, lo(Gamemode) (v0)
    ADDIU       a2, r0, 3
    BEQ         v0, a2, destroyAllBarrelsCodeNew_Finish
    NOP
    LUI         v0, hi(bonusAutocomplete)
    LBU         v0, lo(bonusAutocomplete) (v0)
    ANDI        a2, v0, 1
    BEQZ        a2, destroyAllBarrelsCode_Helm
    NOP
    LW          a2, 0x58 (a3)
    ADDIU       a1, r0, 0x1C
    BNE         a1, a2, destroyAllBarrelsCodeNew_Helm
    NOP
    ADDIU       a1, r0, 0xC
    SB          a1, 0x154 (a3)
    SB          r0, 0x155 (a3)
    ADDIU       a1, r0, 3
    SB          a1, 0x185 (a3)

    destroyAllBarrelsCodeNew_Helm:
        ANDI    a2, v0, 2
        BEQZ    a2, destroyAllBarrelsCodeNew_Finish
        NOP
        LW      a2, 0x58 (a3)
        ADDIU   a1, r0, 0x6B
        BNE     a1, a2, destroyAllBarrelsCodeNew_Finish
        NOP
        ADDIU       a1, r0, 0xC
        SB          a1, 0x154 (a3)
        SB          r0, 0x155 (a3)
        ADDIU       a1, r0, 3
        SB          a1, 0x185 (a3)

    destroyAllBarrelsCodeNew_Finish:
        LUI     v0, 0x8080
        J       0x80681228
        ADDIU   v0, v0, 0xBB70

GuardAutoclear:
    // Check Overlay
    LUI 		a1, 0x8080
    LW 			a1, 0xBB64 (a1)
    ANDI 		a0, a1, 0x4000
    BNEZ 		a0, GuardAutoclear_IsSnoop
    NOP
    SRA 		a1, a1, 16
    ANDI 		a0, a1, 0x10
    BNEZ		a0, GuardAutoclear_IsSnoop
    NOP

    GuardAutoclear_NotSnoop:
        JAL 	guardCatch // Void Warp
        NOP
        B 		GuardAutoclear_Finish
        NOP

    GuardAutoclear_IsSnoop:
        ADDIU 	a0, r0, 0x43
        JAL 	0x806EB0C0
        LW 		a1, 0x0 (s0)

    GuardAutoclear_Finish:
        J 		0x806AE564
        NOP

GuardDeathHandle:
    JAL 	newGuardCode
    NOP
    LUI 	v1, 0x8080
    LW 		s0, 0xBB40 (v1)
    J 		0x806AF754
    NOP

AutowalkFix:
    // Free Variables
    // at, t2, a0, t7, t8
    LUI 	a0, hi(TransitionSpeed)
    LHU 	a0, lo(TransitionSpeed) (a0)
    ANDI 	a0, a0, 0x8000 // Get sign
    BEQZ 	a0, AutowalkFix_Vanilla // No transition exit
    NOP
    LUI 	t7, hi(DestMap)
    LW 		t7, lo(DestMap) (t7)
    LUI 	t8, hi(DestExit)
    LW 		t8, lo(DestExit) (t8)
    ADDIU 	t2, r0, 0x22
    BNE 	t7, t2, AutowalkFix_NotAztecDoor
    ADDIU 	a0, r0, 3
    BEQ 	t8, a0, AutowalkFix_Finish
    LUI 	at, 0x44F2

    AutowalkFix_NotAztecDoor:
        ADDIU 	t2, r0, 0x1A
        BNE 	t7, t2, AutowalkFix_NotCrusher
        ADDIU 	a0, r0, 8
        LUI 	at, 0x4536
        BEQ 	t8, a0, AutowalkFix_Finish
        ADDIU 	at, at, 0x4000

    AutowalkFix_NotCrusher:
        ADDIU 	t2, r0, 0x57
        BNE 	t7, t2, AutowalkFix_NotCastle
        ADDIU 	a0, r0, 15
        LUI 	at, 0x452F
        BEQ 	t8, a0, AutowalkFix_Finish // Castle Tree
        ADDIU 	at, at, 0x9000
        ADDIU 	a0, r0, 11
        LUI 	at, 0x4552
        BEQ 	t8, a0, AutowalkFix_Finish // Castle Ballroom
        ADDIU 	at, at, 0x4000
        ADDIU 	a0, r0, 21
        LUI 	at, 0x45FD
        BEQ 	t8, a0, AutowalkFix_Finish // Castle Entry (Cancel Autowalk)
        ADDIU 	at, at, 0x2000

    AutowalkFix_NotCastle:
        ADDIU 	t2, r0, 0x70
        BNE  	t7, t2, AutowalkFix_Vanilla
        ADDIU 	a0, r0, 1
        BEQ 	t8, a0, AutowalkFix_Finish
        LUI 	at, 0x4361

    AutowalkFix_Vanilla:
        LUI 	at, 0x42C8

    AutowalkFix_Finish:
        J 		0x806F3E7C
        OR 		t2, r0, r0

CannonForceCode:
    LUI 		a0, hi(CurrentMap)
    LW 			a0, lo(CurrentMap) (a0)
    ADDIU 		v0, r0, 0x22
    BEQ 		a0, v0, CannonForceCode_IsIsles
    NOP
    J 			0x8067B694
    NOP

    CannonForceCode_CheckFlag:
        JAL 	0x8067B450
        OR 		a0, s0, r0
        J 		0x8067B68C
        NOP

    CannonForceCode_IsIsles:
        LUI 	a0, hi(LobbiesOpen)
        LBU		a0, lo(LobbiesOpen) (a0)
        BEQZ 	a0, CannonForceCode_CheckFlag
        NOP
        J 		0x8067B6CC
        NOP

DKCollectableFix:
    LHU 		v0, 0x4A (s0)
    ADDIU 		t8, r0, 0xD // CB Single
    BEQ 		v0, t8, DKCollectableFix_IsCollectable
    NOP
    ADDIU 		t8, r0, 0x2B // CB Bunch
    BEQ 		v0, t8, DKCollectableFix_IsCollectable
    NOP
    ADDIU 		t8, r0, 0x1D // Coin
    BEQ 		v0, t8, DKCollectableFix_IsCollectable
    NOP
    SRA 		t8, a0, 0x10
    J 			0x806324CC
    OR 			a0, t8, r0

    DKCollectableFix_IsCollectable:
        J 		0x806324CC
        ADDIU 	a0, r0, 385

KeyCompressionCode:
    SRA 		s5, t7, 0x10
    ADDIU 		t5, r0, 1
    SB 			t5, 0x154 (t4)
    J 			0x806BD330
    SH 			t5, 0x146 (t4)

VineCode:
    // | 0x00800000
    // & 0xFBFF7FFF
    ADDIU       at, r0, 70
    SH          at, 0x128 (s0) // Make transparent
    ADDIU       at, r0, 0xFF
    SB          at, 0x16A (s0) // R
    SB          r0, 0x16B (s0) // G
    SB          r0, 0x16C (s0) // B
    LUI         at, 0x80
    OR          t7, v0, at // Enable RGB Mask
    LUI         at, 0xFBFF
    ORI         at, at, 0x7FFF
    J           0x80698414
    AND         t7, t7, at // Enable Opacity filter

VineShowCode:
    // | 0x04008004
    // & 0xFF7FFFFF
    LUI         at, 0x400
    ORI         at, at, 0x8004
    OR          v0, v0, at
    LUI         at, 0xFF7F
    ORI         at, at, 0xFFFF
    J           0x80698428
    AND         t8, v0, at

SpriteFix:
    SB      r0, 0x0 (t0)
    LUI     t1, hi(CurrentActorPointer_0)
    LW      t1, lo(CurrentActorPointer_0) (t1)
    LW      t1, 0x58 (t1)
    ADDIU   t3, r0, 0x36 // Race Coin
    BEQ     t1, t3, SpriteFix_Finish
    ADDIU   t9, r0, 0
    ADDIU   t9, r0, 1

    SpriteFix_Finish:
        J       0x806A6710
        SB      t9, 0x1 (t0)
