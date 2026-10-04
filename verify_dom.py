# -*- coding: utf-8 -*-
with open('preview.html', encoding='utf-8') as f:
    html = f.read()

required_ids = [
    'furnaceHotspot', 'boilerWorkshopModal', 'modalGaugeNeedle', 'modalGaugeValue',
    'modalPressureBar', 'modalStokeCounter', 'modalFurnaceStage', 'modalFurnaceTarget',
    'coalChunk1', 'coalChunk2', 'coalChunk3',
    'dialogueBox', 'dialogueContent',
    'speakerBadge', 'speakerRole', 'btnToggleUI', 'iconEyeOpen', 'iconEyeClosed',
    'inscenePlayerName', 'inscenePlayerAge',
    'diegeticRegisterRig', 'diegeticStudyRig', 'studyCounterBadge',
    'notebookWrittenWords', 'notebookEmptyPrompt',
    'writtenWord1', 'writtenWord2', 'writtenWord3', 'writtenWord4', 'writtenWord5',
    'studyAnhBaInsight', 'btnStudyWord1', 'btnStudyWord5', 'studyCompletionBox', 'btnFinishStudy',
    'diegeticMarseilleRig', 'marseilleCounterBadge', 'marseilleInsightText',
    'marseilleCard1', 'marseilleCard2', 'marseilleCard3',
    'marseilleStatus1', 'marseilleStatus2', 'marseilleStatus3',
    'marseilleQuote1', 'marseilleQuote2', 'marseilleQuote3',
    'marseilleCompletionBox', 'btnFinishMarseille',
    'diegeticUnificationRig', 'diegeticMilestoneRig', 'diegeticDawnRig'
]

for fname in ['preview.html', 'index.html']:
    with open(fname, encoding='utf-8') as f:
        content = f.read()
    missing = [i for i in required_ids if f'id="{i}"' not in content]
    if missing:
        print(f'MISSING in {fname}:', missing)
        exit(1)
    print(f'SUCCESS: ALL {len(required_ids)} required DOM element IDs verified in {fname}!')

