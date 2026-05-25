## dialogue_variants.rpy — Beneath the Neon
## Pools of dialogue variation strings for replay value.
## Each list contains multiple phrasings of the same narrative beat,
## selected randomly at runtime.

## ---------- SUBWAY: REN'S DEFENSIVE JOKES ----------
## Ren uses sharp humor when crossing security checkpoints.

default subway_ren_jokes = [
    "You tower people drop expensive things like they're cigarette ash.",
    "Relax. I only borrowed your entire legal identity.",
    "Funny. This card opens more doors than your face does.",
    "Don't worry, I didn't sell it. Yet.",
    "You looked like you needed someone to hold onto something for you.",
    "Calm down. Your badge is safer with me than it was with you."
]

## ---------- REIJI'S INTERNAL DEFLECTIONS ----------
## Reiji rationalizes exhaustion through technical language.

default reiji_deflections = [
    "This is a suboptimal emotional configuration.",
    "The system flagged moderate wellness risk. He should listen to the system.",
    "He categorized the feeling as 'ambient loneliness' and filed it away.",
    "Statistically, social exposure improves emotional variance by twelve percent.",
    "The algorithm recommended this. He was just following the recommendation.",
    "Fatigue was a variable. He could optimize for it later."
]

## ---------- REN'S INTERNAL DEFLECTIONS ----------
## Ren masks vulnerability behind performance.

default ren_deflections = [
    "Keep smiling. If he gets angry, run.",
    "Don't sound jealous. Make it a joke.",
    "He's looking at you like you're already a problem. Be funny.",
    "The trick is to talk before they can categorize you.",
    "Never let them see you need anything. That's the rule.",
    "Smile wider. People trust people who smile."
]

## ---------- REIJI'S APARTMENT RESPONSES: WORK ----------
## Reiji's spoken + thought pairs about corporate work during the apartment scene.

default reiji_work_lines = [
    ("It's stable. Benefits. Routine.", "Stable meant predictable. Predictable meant hollow."),
    ("They value my output.", "Output was the only thing they measured. He knew that."),
    ("I calibrate neural interfaces.", "He calibrated machines so the company could sell better dreams."),
    ("The work is technical. Clean.", "Clean meant sterile. Sterile meant nothing grew there.")
]

## ---------- REN'S APARTMENT RESPONSES: WORK ----------
## Ren's spoken + thought pairs about survival labor during the apartment scene.

default ren_work_lines = [
    ("Whatever pays. Today it was hauling scrap.", "Don't say 'whatever.' It makes you sound like you don't care."),
    ("I find things. Fix things. Move things.", "The things no one else wants. The things no one else touches."),
    ("There's always something to do if you don't say no.", "Say no and you disappear from every list that matters."),
    ("It's not a career. It's... motion.", "Motion was the only thing keeping him from sinking.")
]

## ---------- REIJI'S APARTMENT RESPONSES: IDENTITY ----------
## Reiji's spoken + thought pairs about identity and validation.

default reiji_identity_lines = [
    ("My badge proves I exist.", "Without it, he would be as invisible as the man on the platform."),
    ("The system knows who I am.", "The system knew his employment status. It did not know him."),
    ("I'm a valid citizen. Registered. Tracked.", "Valid was a word for 'compliant.' He had stopped pretending otherwise.")
]

## ---------- REN'S APARTMENT RESPONSES: IDENTITY ----------
## Ren's spoken + thought pairs about identity and non-existence.

default ren_identity_lines = [
    ("I don't have a number. Not the kind that matters.", "He had never been counted. He had never been missed."),
    ("No ID. No record. No debt. No credit.", "Freedom sounded better when you weren't shivering in it."),
    ("I exist wherever I'm standing.", "And when he moved, he stopped existing there, too.")
]

## ---------- REIJI'S APARTMENT RESPONSES: SLEEP ----------
## Reiji's spoken + thought pairs about sleep and insomnia.

default reiji_sleep_lines = [
    ("I sleep. Technically. The hours pass.", "His body lay still. His mind ran diagnostics."),
    ("The wristband tracks my rest cycles.", "The wristband reported numbers. Numbers were not rest."),
    ("The ads say 'Sleep better.' I've tried.", "He had tried five brands of sleep aid. They all worked, according to the data.")
]

## ---------- REN'S APARTMENT RESPONSES: SLEEP ----------
## Ren's spoken + thought pairs about sleep and insecurity.

default ren_sleep_lines = [
    ("You sleep light when security does sweeps.", "Every hour, a new sound. Every sound, a new threat."),
    ("Subway stations are warm. Mostly.", "Warm until 2 AM. Then the vents switch and the cold comes up from below."),
    ("I close my eyes. That counts, right?", "It didn't count. He knew it didn't count.")
]

## ---------- NEWS TICKER MESSAGES ----------
## State propaganda strings that cycle during the montage.

default ticker_messages = [
    "Tokyo Corridor Productivity Reaches New High.",
    "Public Satisfaction Remains Stable.",
    "Urban Sanitation Campaign Successful.",
    "Unauthorized Population Reduced.",
    "Consumer Confidence Rising.",
    "Corporate Housing Satisfaction at 94.2%.",
    "Neural-Interface Adoption Rate Exceeds Projections.",
    "Transit Efficiency Improved 3.1% This Quarter.",
    "Wellness Monitoring Program Shows Positive Outcomes.",
    "Security Compliance Rates Stable Across All Sectors."
]

## ---------- AMBIENT OBSERVATIONS ----------
## Short narrative fragments used during scene transitions.

default ambient_observations = [
    "The city does not pause. It calculates. It improves. It sells.",
    "Somewhere, a billboard changes its message. No one looks up.",
    "The rain continues falling. It has been falling for forty years.",
    "A drone passes overhead. It does not stop. It has nothing to stop for.",
    "The neon reflects in puddles. The puddles reflect nothing back.",
    "Another train arrives. Another train departs. No one on board speaks."
]

## ---------- ACT II: CHECKPOINT DISPLAY MESSAGES ----------

default checkpoint_messages = [
    "ID VERIFICATION ACTIVE. UNREGISTERED INDIVIDUALS: REPORT TO PROCESSING.",
    "SCANNING. ALL GUEST PASSES MUST BE ACCOMPANIED BY REGISTERED HOST.",
    "WARNING: UNAUTHORIZED ACCESS IS A CIVIL VIOLATION. PENALTIES APPLY.",
    "BIOMETRIC SCAN IN PROGRESS. PLEASE REMAIN STILL."
]

## ---------- ACT IV: OFFICE DIALOGUE FRAGMENTS ----------

default coworker_lines = [
    "Productivity sync got moved to 11:30. System says it's more efficient.",
    "Did you see the sanitation report? Numbers are up again.",
    "The new neural calibration patch dropped. Everyone's scores went up.",
    "Lunch? Oh, you're at 12:00. I'm at 12:20. Maybe next quarter."
]

## ---------- ACT IV: MARKET AUNTIE LINES ----------

default market_auntie_lines = [
    "Fresh scrap! Better than what you found yesterday!",
    "You again? No credit, no trade. I told you last time.",
    "Those adapters are burnt. I'll give you half.",
    "Security came through an hour ago. You should move."
]
