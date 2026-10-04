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
    'diegeticUnificationRig', 'diegeticMilestoneRig', 'diegeticDawnRig'
]

missing = [i for i in required_ids if f'id="{i}"' not in html]
if missing:
    print('MISSING:', missing)
    exit(1)
else:
    print(f'SUCCESS: ALL {len(required_ids)} required DOM element IDs verified in preview.html!')
