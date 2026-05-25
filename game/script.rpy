## script.rpy — Beneath the Neon
## Master narrative engine. All scene labels, dialogue, choices, and flow control.
## Revised per Section 14 of Galagame_Finalised.pdf.
## Characters: Morikawa Reiji (reiji) and Ren (ren).

## ======================================================================
## GLOBAL START
## ======================================================================

label start:
    scene bg_black
    with Dissolve(1.0)

    pause 1.5

    n "A low electronic hum."

    pause 0.8

    n "Then, slowly, the city wakes into color."

    jump prologue_surface


## ======================================================================
## PROLOGUE: SURFACE OF TOKYO (Section 14 — Revised)
## ======================================================================

label prologue_surface:
    scene bg train_in
    with Dissolve(2.0)

    play music "audio/background.mp3" fadein 3.0 volume 0.6

    pause 1.0

    n "At first, there is only light."

    n "Neon crawls across the glass skin of Tokyo like a second bloodstream. Tower after tower rises into the wet night, each one cleaner, brighter, and taller than the last."

    n "Blue advertisements dissolve into pink. Pink becomes gold. Gold becomes the logo of another company promising comfort, health, memory, desire, sleep."

    n "Above the streets, automated trains cut through the skyline without a sound. Their windows reflect holographic koi swimming through the air between office towers."

    n "Below them, traffic moves in perfect lanes, guided by corporate navigation systems that adjust every second to prevent delay."

    pause 0.5

    n "The city does not pause."

    n "It calculates."

    n "It improves."

    n "It sells."

    pause 0.8

    n "A woman on a billboard smiles with impossible calm."

    advert "Your happiness, measured. Your wellness, monitored. Your future, optimized."

    n "The smile repeats across a thousand screens."

    n "On the news towers, the same headlines rotate every thirty seconds."

    news "Tokyo Corridor productivity rises for the seventh consecutive quarter."

    news "Consumer confidence reaches a five-year high."

    news "Corporate housing satisfaction remains stable."

    news "Unauthorized population reduction campaign declared successful."

    n "The headlines are clean."

    n "The fonts are clean."

    n "Even the rain seems clean as it falls through the neon."

    pause 0.5

    n "From a distance, Tokyo looks like proof that history can be repaired by enough light."

    pause 1.0

    scene bg train_in
    with Dissolve(1.5)

    n "Inside Train Line 7, no one speaks."

    n "The train slides above the commercial district, passing office towers, capsule hotels, entertainment malls, private clinics, and vertical gardens sealed behind climate-controlled glass."

    n "Every passenger faces forward. Every wristband blinks softly. Every eye avoids every other eye."

    show reiji face_l
    with Dissolve(0.5)

    n "Morikawa Reiji sits near the window."

    n "His company badge rests against his coat, warm from the scanner at the platform gate. His wrist display glows with a pending notification — the deployment report for the new neural calibration framework."

    pause 0.5

    n "He reads it without reading it. The words have become shapes. Approve. Confirm. Acknowledge. The same three buttons he has pressed every day for six years."

    show badge
    with Dissolve(0.3)

    n "His thumb moves on instinct. The report is approved before the train reaches the next station."

    system "Deployment report approved. Framework version 9.4.1 scheduled for rollout. Thank you for your prompt review, Engineer Morikawa."

    n "Reiji does not feel prompt. He feels hollowed out, like a component that has been running too long without replacement."

    system "Identity confirmed. Employment status: active. Transit privilege: approved. Wellness risk: moderate."

    n "Reiji does not look at the message for long."

    n "Outside, another advertisement expands across the side of a building."

    advert "Sleep better. Work clearer. Feel human again."

    n "Reiji watches the words disappear behind rain."

    $ dual_line("Reiji", "Almost home.", "Home was a word the system used because \"assigned residential unit\" tested poorly in employee satisfaction surveys.")

    n "The train enters a tunnel of reflected light."

    n "For a few seconds, the window becomes a mirror."

    n "Reiji sees his own face layered over the city: tired eyes, pressed collar, company haircut, the expression of someone who has learned to look functional before learning to feel anything."

    n "His schedule scrolls automatically across his wrist display."

    system "Tomorrow: 07:30 wake cycle. 08:10 transit. 09:00 neural-interface calibration review. 12:00 nutrition break. 12:20 productivity sync. 18:40 wellness recommendation: social exposure."

    n "Reiji closes the display."

    n "The train slows."

    n "Below, on a service platform between two transit lines, three corporate security officers surround a man without shoes."

    show police
    with Dissolve(0.3)
    show drone
    with Dissolve(0.3)

    n "The man holds a plastic bag against his chest. Something metallic spills from it onto the concrete: broken circuits, old access tags, cracked lenses, a child's toy with one glowing eye."

    n "One officer speaks into his shoulder mic."

    n "Another points toward the lower stairwell."

    n "The man shakes his head. The motion is small but desperate — the kind of refusal that comes when you have nothing left but the word no."

    n "The train continues moving before Reiji can see what happens next."

    hide police
    with Dissolve(0.3)
    hide drone
    with Dissolve(0.3)

    n "Reiji looks away."

    $ noise += 1

    n "His wristband chimes softly, logging the elevated heart rate as a minor wellness flag. The system will recommend meditation later."

    n "It will not recommend thinking about the man."

    news "Urban sanitation operation improves public mobility in lower transit sectors."

    n "No one in the train reacts."

    n "Reiji wonders whether everyone saw it."

    n "Then he wonders whether it matters."

    pause 0.8

    n "A child across the aisle is watching a cartoon through retinal projection. Her pupils flicker with artificial stars."

    n "Her mother sits beside her, asleep with her mouth slightly open, still wearing an office headset. Every few seconds, the headset whispers into her ear."

    headset "Rest cycle detected. Micro-recovery in progress. Thank you for your contribution."

    n "The train arrives at Shinjuku Corporate Exchange."

    scene bg subway_in
    with Dissolve(1.0)

    show reiji face_l
    with Dissolve(0.3)

    n "The doors open."

    n "A wall of sound enters the carriage: station chimes, shoe steps, synthetic announcements, distant music, vending machine jingles, security drones, rainwater dripping from coats onto polished floor."

    announce "Welcome to Shinjuku Corporate Exchange. Please keep your badge visible. Unregistered persons are not permitted beyond the yellow zone."

    n "Reiji steps out with the crowd."

    scene bg street
    with Dissolve(1.0)

    show reiji face_l
    with Dissolve(0.3)

    n "No one pushes."

    n "No one slows."

    n "Everyone moves as if the station has already decided where their bodies should go."

    n "Above the platform, another billboard blooms to life."

    n "A group of young office workers laugh around a glowing table in a bar. Their faces are flushed, beautiful, effortless."

    advert "NEON PUB — after work, become yourself again."

    n "Reiji stops walking for half a second."

    n "The crowd bends around him without noticing."

    n "His wrist display lights up again."

    system "Wellness recommendation available: controlled social environment within 0.8 km. Suggested venue: Neon Pub. Estimated improvement in emotional variance: 12 percent."

    n "Reiji almost laughs."

    n "It comes out as a breath."

    $ dual_line("Reiji", "Sure.", "He did not want a drink. He wanted evidence that he had not become a machine that occasionally required alcohol.")

    hide reiji face_l
    with Dissolve(0.5)

    jump neon_pub


## ======================================================================
## ACT I: NEON PUB (Section 14 — Revised)
## Reiji goes INSIDE the pub. Drink choice. Then alley. Drone encounter.
## ======================================================================

label neon_pub:
    scene bg club_out
    with Dissolve(1.5)

    show reiji face_l
    with Dissolve(0.5)

    pause 0.5

    n "Reiji follows the station signs upward."

    n "The escalator carries him toward the commercial level. The walls become brighter with every floor. Concrete disappears behind chrome. Security gates disappear behind decorative glass."

    n "The air begins to smell less like rain and more like citrus disinfectant."

    n "At the top, Tokyo opens again."

    pause 0.5

    n "Neon Pub sits beneath an elevated highway, surrounded by holographic banners and steam from street vents."

    n "Corporate workers line up outside, laughing too loudly. A pair of smugglers argue near a vending machine. A woman in a silver jacket sells illegal memory patches from inside an umbrella."

    n "A security drone passes overhead, ignores them, and continues toward the lower stairwell."

    n "Music pulses from the pub entrance — deep synth bass, layered over a vocal track too processed to sound human anymore."

    n "For a moment, the whole street looks alive."

    pause 0.5

    scene bg club_in
    with Dissolve(1.0)

    show reiji face_l
    with Dissolve(0.3)

    n "Reiji pushes through the door."

    n "The interior of Neon Pub is a cathedral of artificial light. Holographic advertisements drift between booths like bioluminescent fish. The bar glows cyan along its entire length. Every surface reflects something that isn't there."

    n "The music is louder inside. It fills the space between thoughts."

    n "Corporate workers cluster in groups, performing relaxation with the same efficiency they bring to their desks. They laugh on schedule. They drink on schedule. They check their wristbands when they think no one is looking."

    pause 0.5

    n "Reiji finds a seat at the bar. The stool is uncomfortable in a way that was probably designed by someone who had never sat down."

    show dealer
    with Dissolve(0.3)

    n "The bartender — a broad-shouldered man with a chrome implant running along his jaw — slides toward him without appearing to move his feet."

    bartender "What'll it be?"

    n "The question lands heavier than it should. Reiji stares at the menu hologram flickering above the bar. The drinks have names like promises."

    menu:
        "Order the Neon Classic.":
            $ drink_order = "neon_classic"
            $ masking += 1
            jump pub_drink_choice

        "Order the Calm Static.":
            $ drink_order = "calm_static"
            $ trust += 1
            jump pub_drink_choice

        "Just water.":
            $ drink_order = "water"
            $ noise += 1
            jump pub_drink_choice


label pub_drink_choice:
    hide dealer
    with Dissolve(0.3)

    if drink_order == "neon_classic":
        $ dual_line("Reiji", "Neon Classic.", "He ordered the thing that sounded most like what a person would order. A person who relaxed. A person who existed outside the system's recommendations.")
        n "The bartender nods. The drink arrives in a glass that glows faintly blue from the bottom. It tastes like artificial citrus and something else — something that numbs the back of the throat."
        n "Reiji drinks it faster than he intended."

    elif drink_order == "calm_static":
        $ dual_line("Reiji", "Calm Static. Please.", "He added 'please' to remind himself he was still human. Machines didn't say please. Not yet.")
        n "The bartender raises an eyebrow — a flicker of something almost like approval — and pours a pale lavender liquid into a frosted glass. It tastes like lavender too, or the synthetic memory of lavender."
        n "Reiji holds the glass without drinking. The cold against his palm is grounding."

    else:
        $ dual_line("Reiji", "Just water.", "He couldn't bring himself to perform relaxation tonight. The system wanted 12 percent improvement. He wanted silence.")
        n "The bartender's expression doesn't change. He fills a glass from a tap and sets it down. No judgment. No interest. Water is the easiest drink to serve."
        n "Reiji stares at the glass. Even water tastes processed here."

    pause 0.8

    n "The pub hums around him. A group in the corner erupts in laughter at something a holographic host just said. A couple near the window argue in whispers too low to decode. Someone's wristband chimes a hydration reminder."

    n "Reiji finishes his drink. The glass is empty before he remembers deciding to empty it."

    pause 0.5

    n "The walls feel closer now. The music feels louder. The laughter from the corner booth sounds less like joy and more like warning."

    n "He needs air."

    scene bg club_out
    with Dissolve(1.0)

    n "The alley behind Neon Pub is a different world."

    n "The neon doesn't reach here. What light exists is secondhand — reflections off wet concrete, the faint amber glow of a broken street lamp, the red blink of a drone passing somewhere above."

    n "There are people here, half-hidden behind stacked delivery crates, picking through discarded electronics from the pub."

    n "Broken drink cartridges. Cracked neural adapters. Burnt-out access chips. Anything with a trace of metal, memory, or resale value."

    pause 0.5

    show ren face_l
    with Dissolve(0.5)

    n "One of them looks up."

    n "A young man. Thin jacket. Wet hair plastered to his forehead. Eyes too bright for someone standing in a pile of trash."

    n "He grins. The grin is a weapon, a shield, and a question all at once."

    n "Reiji has never seen him before, but the recognition is immediate — not of a face, but of a type. The type the system warns you about. The type that survives in the gaps between regulations."

    n "Ren."

    n "Their eyes meet for less than a second."

    n "Ren raises two fingers in a casual salute, as if they are old friends, as if being seen is not dangerous."

    $ dual_line("Ren", "Nice night for garbage, huh?", "Always open with a joke. If they laugh, you're a person. If they don't, you're a problem.")

    n "Reiji doesn't laugh. But he doesn't look away either."

    $ dual_line("Reiji", "I was just getting some air.", "It sounded defensive. He hadn't meant it to. But the alley made everything feel like an explanation.")

    n "Ren's grin widens. He holds up a burnt-out access chip between two fingers, examining it like a jeweler with a suspect diamond."

    $ dual_line("Ren", "Air's free. The stuff inside costs three times what it should. You're the smart one.", "He's corporate. Coat. Badge. Wristband. The whole package. Don't stare at the badge.")

    pause 0.5

    n "Before Reiji can respond, the red blink from above becomes a white beam."

    show drone
    with Dissolve(0.3)

    n "A security drone descends from the upper transit lane, its rotors a low mechanical whisper. It hovers at the alley entrance, scanning."

    drone "IDENTITY VERIFICATION. ALL PERSONS IN RESTRICTED ZONE: DISPLAY REGISTRATION."

    n "Ren freezes. The grin stays on his face, but his eyes go flat — the look of someone calculating distances, exits, how fast he can run on wet concrete."

    n "The drone's scanner sweeps the alley. Red lines trace across stacked crates. Across Ren's chest. Across the access chip still pinched between his fingers."

    drone "UNREGISTERED INDIVIDUAL DETECTED. STAND BY FOR SECURITY DISPATCH."

    n "Reiji speaks before his brain can intervene."

    $ dual_line("Reiji", "He's with me. Temporary disposal contractor. Authorized for site cleanup.", "The lie assembled itself from corporate vocabulary like a pre-fabricated module. He had written dozens of contractor justifications. He had never used one on a person before.")

    n "The drone's lens refocuses. It scans Reiji's badge — the plastic rectangle glowing green through his coat. The scanner reads it from two meters away."

    show badge
    with Dissolve(0.2)

    drone "CORPORATE ID CONFIRMED. ENGINEER MORIKAWA REIJI. EMPLOYMENT STATUS: ACTIVE. CONTRACTOR: CONDITIONALLY VERIFIED. LOGGING INCIDENT."

    n "The drone hovers for three more seconds. Then it ascends, its light sweeping toward the next alley, the next unregistered body, the next problem that is someone else's to solve."

    hide drone
    with Dissolve(0.3)

    pause 0.8

    n "Ren exhales. It's a long, slow breath that sounds like it's been held for years."

    $ dual_line("Ren", "...Temporary disposal contractor. That's a new one.", "He saved you. Why did he save you? People don't do that. Not tower people. Not badge people. What does he want?")

    $ dual_line("Reiji", "It was the first thing that sounded official.", "It was the first thing that sounded like he wasn't letting another human being get dragged to a processing center. He didn't say that part.")

    n "Ren studies him for a long moment. The grin fades into something less performative. Something almost unguarded."

    ren "You should get back inside. Your drink's probably getting warm."

    n "Reiji looks toward the pub. The warm light still spills across the wet concrete. The music still pulses. Inside, everything is clean and measured and pretending."

    n "Out here, the rain is cold and the garbage is real and a stranger is looking at him like he's the first person to tell a lie on his behalf."

    $ dual_line("Reiji", "Take care of yourself.", "He meant: I won't forget this. He didn't know why. He didn't know what it would cost.")

    n "Ren's grin returns, but softer now. Less armor. More acknowledgment."

    $ dual_line("Ren", "Always do.", "He never did. But tonight, someone had lied to a drone for him. That was more than anyone had done in months.")

    hide ren face_l
    with Dissolve(0.5)

    n "Reiji walks back toward the pub entrance. Behind him, the alley settles back into darkness."

    n "The billboard woman smiles again."

    advert "Your happiness, measured."

    n "The rain keeps falling."

    n "The city keeps shining."

    n "And somewhere in the alley, a young man with wet hair watches a corporate engineer walk away and wonders if what just happened was real."

    pause 1.0

    jump subway_checkpoint


## ======================================================================
## ACT II: SUBWAY CHECKPOINT (Section 14 — Revised)
## Badge gone. Ren has it. Three-way choice. Host Liability Agreement.
## Elevator ride to apartment.
## ======================================================================

label subway_checkpoint:
    scene bg subway_out
    with Dissolve(1.5)

    show reiji face_l
    with Dissolve(0.5)

    pause 0.5

    n "Reiji leaves Neon Pub behind. The rain has thickened — fat drops that hit the concrete like small accusations. His coat is wet before he reaches the station entrance."

    n "The subway platform is crowded with the usual late-night traffic: exhausted workers, intoxicated students, street vendors packing up unsold goods."

    n "The station chime rings. An announcement loops overhead."

    announce "Identity verification in progress. Please have your badge ready. Unregistered individuals will be detained."

    scene bg subway_in
    with Dissolve(0.8)

    show reiji face_l
    with Dissolve(0.3)

    n "Reiji approaches the checkpoint. The gates glow green in sequence as passengers swipe through — badge, beep, pass, repeat. The rhythm of compliant humanity."

    n "He reaches for his coat pocket."

    n "It is empty."

    pause 0.8

    n "His badge is gone."

    show badge
    with Dissolve(0.3)

    n "He checks every pocket. Twice. Then a third time, as if the plastic rectangle might have materialized from sheer professional obligation."

    n "Nothing."

    system "Warning: ID not detected. Transit access suspended. Please report to nearest verification kiosk."

    n "Reiji's hand tightens around nothing."

    n "The crowd pushes past him. A woman's shoulder knocks against his arm. No one apologizes. No one notices."

    n "Panic is a luxury. Reiji has forgotten how to afford it. Instead, his mind runs through possibilities with cold, technical precision: lost on the train, dropped in the alley, stolen. Stolen makes the most sense. The alley. The drone. The stranger with the grin."

    pause 0.5

    show ren face_3char
    with Dissolve(0.5)

    n "And then Ren is standing in front of him."

    n "The same thin jacket. The same wet hair. The same grin — though now it carries something sharper. Something deliberate."

    n "He is holding Reiji's badge between two fingers, turning it over like a curiosity. Like a key he hasn't decided whether to use."

    pause 0.3

    $ line = renpy.random.choice(subway_ren_jokes)
    ren "[line]"

    n "Reiji stares at the badge. Then at Ren."

    n "Three corporate security officers are working their way down the platform. Their shoulder lights sweep across the crowd in cold white arcs. BODYSCAN stenciled across their chest plates."

    show police
    with Dissolve(0.3)

    n "Ren notices them too. The grin doesn't fade, but something behind it tightens. His fingers close around the badge."

    n "The security checkpoint is two hundred meters away. Without that badge, Reiji cannot pass. Without that badge, Ren cannot exist — not in the system's eyes, not anywhere the scanners reach."

    checkpoint "ALL PASSENGERS: IDENTITY VERIFICATION ACTIVE. UNREGISTERED INDIVIDUALS MUST REPORT TO PROCESSING. GUEST PASSES ACCEPTED WITH REGISTERED HOST."

    pause 0.5

    n "Ren's eyes flick to the checkpoint display. Then to the security officers. Then to Reiji."

    $ dual_line("Ren", "They're getting closer.", "He had run this calculation before. Distance to exit. Time to scan. Probability of getting caught. The numbers were never good.")

    n "Reiji looks at his badge in Ren's hand. He looks at the security officers. He looks at Ren's face — the grin still there, but the eyes beneath it are not grinning."

    n "This is the moment. The surface splits."

    pause 0.5

    menu:
        "Help him. Get him through the checkpoint.":
            $ trust += 1
            $ projection -= 1
            $ liability += 1
            $ help_ren_choice = True
            jump help_ren

        "Ask for the truth first. Why did he take it?":
            $ masking += 1
            $ demand_id_choice = True
            jump demand_truth

        "Keep walking. Turn back at the last second.":
            $ trust -= 1
            $ noise += 1
            $ liability += 2
            $ ignore_ren_choice = True
            jump walk_away_turn_back


## ======================================================================
## BRANCH 1: HELP HIM THROUGH THE CHECKPOINT
## ======================================================================

label help_ren:
    scene bg subway_in

    show reiji face_l
    with Dissolve(0.3)
    show ren face_l
    with Dissolve(0.3)

    n "Reiji makes a choice before his mind can veto it."

    n "He steps closer to Ren, close enough that the security lights might read them as a single shape instead of two separate problems."

    $ dual_line("Reiji", "Stay close. Walk like you belong here. Don't run.", "He had no idea if this would work. He had no idea why he was doing it. The why would have to wait.")

    n "Ren's eyes flicker. For a fraction of a second, the grin cracks into something unguarded — surprise, maybe, or the memory of surprise."

    $ dual_line("Ren", "You're serious.", "No one is ever serious. Not about him. Not when security is thirty seconds away.")

    n "Reiji doesn't answer. He just starts walking toward the checkpoint."

    n "Ren falls in beside him, hands in his pockets, shoulders loose in a performance of ease that must have taken years to perfect."

    n "The security officers scan faces as the line moves forward. Badges glow green. Bodies pass through. The system hums its quiet approval."

    n "Reiji reaches the checkpoint first. Ren presses the badge into his palm — a brief transfer, fingers brushing, the plastic warm from someone else's hand. Reiji swipes. The scanner blinks green."

    system "Identity confirmed. Transit privilege: approved."

    n "Then Ren steps forward."

    n "The officer's gaze lingers a second too long. His hand drifts toward his belt — not a weapon, but a scanner. The kind that reads more than badges."

    n "Reiji speaks before the question can form."

    $ dual_line("Reiji", "He's with me. Guest pass. I'll file the liability form.", "The lie came out smooth. Too smooth. He wondered how long he had been practicing it without knowing.")

    n "The officer looks at Reiji's badge. At his corporate coat. At the exhaustion in his eyes that reads, correctly, as compliance. Then at Ren — thin jacket, wrong posture, the look of someone who doesn't belong on this side of the yellow line."

    n "The scanner beeps."

    system "Transit privilege: approved. Guest access: temporary. Host liability: accepted. Duration: 24 hours."

    n "Ren passes through."

    n "On the other side, they do not look at each other."

    n "But Ren's hand, for just a moment, rests on Reiji's shoulder — a brief pressure, light as rain, gone before either of them can name it."

    $ dual_line("Ren", "...Thanks.", "Don't say more. Don't make it weird. But don't forget it, either. People who lie to security for you are not common currency.")

    n "Reiji nods. Just once."

    $ dual_line("Reiji", "The liability form takes twelve hours to process. You have until tomorrow night.", "He had read the fine print years ago, never thinking he would use it. The system prepared him for everything except the things that mattered.")

    n "Ren's grin returns, but it's different now. Less performance. More recognition."

    $ dual_line("Ren", "Guess I owe you one, Engineer Morikawa.", "He remembered the name from the drone's scan. He was good with names. He had to be. Names were currency when you had nothing else.")

    $ trust += 1

    jump elevator_ride


## ======================================================================
## BRANCH 2: ASK FOR THE TRUTH FIRST
## ======================================================================

label demand_truth:
    scene bg subway_in

    show reiji face_l
    with Dissolve(0.3)
    show ren face_l
    with Dissolve(0.3)

    n "Reiji's training overrides his instinct. Information first. Action second. Everything in its proper order."

    $ dual_line("Reiji", "Why did you take it?", "His voice came out harder than he intended. It always did when he was uncertain. And right now, he was drowning in uncertainty.")

    n "Ren's grin sharpens. It becomes a blade held sideways — still a smile, but only just."

    $ dual_line("Ren", "Why does anyone take anything? It was there. You weren't looking.", "That wasn't the real answer. The real answer was: because a badge like this is worth three months of food on the lower markets. Because he was hungry. Because he was always hungry. But he would die before saying that to a tower man.")

    n "Reiji studies him. The thin jacket. The hands that haven't stopped moving. The eyes that track the security officers like a cat tracking dogs."

    $ dual_line("Reiji", "You could have sold it. You didn't.", "He was reasoning out loud. It was what engineers did. Break the problem into components. The component in front of him didn't fit any of his existing schematics.")

    n "Ren's grin falters — just a flicker, a crack in the armor."

    $ dual_line("Ren", "Maybe I'm a bad businessman.", "Maybe he saw you in the alley and thought: that one looks like he's already carrying enough. Maybe he didn't know why either.")

    pause 0.5

    n "The security officers are closer now. One of them glances toward the two men standing too long in the middle of the platform."

    n "Reiji makes a decision. Not an engineer's decision. Not a calculation. Something older and less logical."

    $ dual_line("Reiji", "The checkpoint has guest pass protocols. I can sponsor you for 24 hours. After that... we figure something out.", "He used 'we.' He noticed it the moment it left his mouth. He didn't take it back.")

    n "Ren stares at him. The grin is gone entirely now. What remains is something younger and more fragile."

    ren "You barely know me."

    $ dual_line("Reiji", "I know you gave the badge back.", "That was enough. He didn't say: it's more than most people would do. He didn't say: I've been invisible too. But the words hung in the air between them anyway.")

    pause 0.5

    n "Ren nods. Once. It is the smallest movement Reiji has ever seen carry so much weight."

    $ trust += 1
    $ liability += 1

    jump host_liability_agreement


## ======================================================================
## BRANCH 3: KEEP WALKING — THEN TURN BACK
## ======================================================================

label walk_away_turn_back:
    scene bg subway_in

    show reiji face_l
    with Dissolve(0.3)
    show ren face_l
    with Dissolve(0.3)

    n "Reiji's body moves before his conscience can catch up."

    n "He walks past Ren as if he is made of the same rain-streaked glass as the station windows. His face does not change. His posture does not shift. The corporate mask clicks into place with the precision of a machine part."

    $ dual_line("Reiji", "I don't know what you're talking about.", "The sentence was clean. Surgical. It removed Ren from his reality in eight words.")

    n "Ren's grin freezes mid-performance. It stays frozen for half a second too long."

    $ dual_line("Ren", "Right. Wrong guy. My mistake.", "He knew this would happen. It always happened. Still, the stomach drops the same way every time. He pressed the badge into Reiji's palm anyway — a reflex, or maybe an accusation. His fingers were cold.")

    n "Reiji takes the badge. The plastic is warm where Ren held it."

    n "He swipes through the turnstile. Green light. Access granted. Everything in order."

    n "He walks ten steps. Twenty steps. The platform stretches ahead of him in clean, predictable lines."

    n "His wristband shows his heart rate. Elevated. The system flags it for review."

    pause 0.8

    n "He stops."

    n "His feet stop before his brain authorizes the command."

    n "He turns around."

    n "Ren is still standing where he left him — at the edge of the yellow zone, hands in his pockets, shoulders set like someone who has been left behind enough times to expect it."

    $ dual_line("Reiji", "Wait.", "The word came out louder than he intended. Several people looked. He didn't care. He hadn't cared about anything in years, and now he was shouting 'wait' at a stranger on a subway platform.")

    n "Ren looks up. The grin tries to return. It doesn't make it."

    n "Reiji walks back. Each step feels heavier than the last — not because of the distance, but because of what the distance means."

    $ dual_line("Reiji", "I have a guest pass. I can sponsor you for 24 hours.", "He didn't explain why he had walked away. He didn't explain why he came back. Some things couldn't be explained. They could only be done.")

    n "Ren's expression shifts through three emotions faster than Reiji can name them: disbelief, suspicion, something that might be hope if hope weren't so dangerous."

    $ dual_line("Ren", "You walked away.", "He said it like evidence. Like a fact entered into a record that couldn't be changed.")

    $ dual_line("Reiji", "I know. I came back.", "He didn't say: I've never come back for anything before. He didn't say: you're the first person who made me want to.")

    pause 0.8

    n "The security officers are scanning the far end of the platform. They haven't noticed yet. But they will."

    n "Ren looks at Reiji. At the badge. At the checkpoint gate glowing green and patient and indifferent."

    $ dual_line("Ren", "Okay. 24 hours.", "He didn't trust it. Trust was a luxury for people who had never had it broken. But he was tired. And the man in front of him had turned back. That was something. That was almost enough.")

    $ trust += 1
    $ liability += 2

    jump host_liability_agreement


## ======================================================================
## HOST LIABILITY AGREEMENT
## ======================================================================

label host_liability_agreement:
    scene bg subway_in
    with Dissolve(0.5)

    show reiji face_l
    with Dissolve(0.3)
    show ren face_l
    with Dissolve(0.3)
    show badge
    with Dissolve(0.3)

    n "The checkpoint kiosk glows cold blue. A screen extends toward Reiji's wristband, pulling data from a chip embedded in his coat sleeve."

    checkpoint "HOST LIABILITY AGREEMENT ACTIVATED. SPONSOR: MORIKAWA REIJI. EMPLOYEE ID: 7-4-1-9-2-2-8. GUEST: UNREGISTERED. DURATION: 24 HOURS. BY ACCEPTING, THE HOST ASSUMES FULL LEGAL RESPONSIBILITY FOR THE GUEST'S ACTIONS WITHIN ALL YELLOW-ZONE AND ABOVE SECTORS."

    n "Reiji reads the text three times. Each time, the words are the same. Each time, they mean the same thing."

    n "He has never sponsored anyone before. Most people haven't. Most people don't need to. The system is designed so that everyone who belongs is already registered, and everyone who isn't registered doesn't belong."

    checkpoint "WARNING: VIOLATIONS BY UNREGISTERED GUEST WILL BE PERMANENTLY LOGGED TO HOST EMPLOYMENT RECORD. REPEATED SPONSORSHIP OF UNREGISTERED INDIVIDUALS MAY TRIGGER SECURITY REVIEW."

    n "Ren stands beside him, reading the screen over his shoulder. His expression is unreadable."

    $ dual_line("Ren", "That's a lot of warnings for one button.", "He wanted to tell him not to do it. The words were right there. But so was the security officer at the end of the platform. And so was the cold. And so was the memory of the last time someone had looked at him like he mattered.")

    $ dual_line("Reiji", "I've read worse terms of service.", "He pressed the button before he could think about what his supervisor would say. What the system would log. What 24 hours of liability actually meant.")

    system "HOST LIABILITY AGREEMENT ACCEPTED. GUEST ACCESS: APPROVED. DURATION: 24 HOURS. WELCOME, UNREGISTERED GUEST. PLEASE REMAIN WITH YOUR SPONSOR AT ALL TIMES."

    $ signed_liability = True

    n "The checkpoint gate slides open."

    n "Ren steps through. The motion is small — one foot, then the other — but his expression makes it look like crossing a border into another country."

    n "In a way, it is."

    pause 0.5

    n "The gate closes behind them. The green light fades. The system logs the transaction and moves on to the next body, the next badge, the next calculation."

    jump elevator_ride


## ======================================================================
## ELEVATOR RIDE TO APARTMENT
## ======================================================================

label elevator_ride:
    scene bg apartment_out
    with Dissolve(1.0)

    show reiji face_l
    with Dissolve(0.5)
    show ren face_l
    with Dissolve(0.5)

    pause 0.5

    n "The elevator is silver and silent. Corporate-grade. The kind that doesn't play music because music implies leisure, and leisure is not efficient."

    n "Reiji presses the button for the 34th floor. The doors close with a sound like a breath held."

    n "Ren leans against the back wall. He doesn't touch the rail. He doesn't touch anything. His hands stay in his pockets, his eyes track the floor numbers as they climb."

    pause 0.5

    $ dual_line("Ren", "Thirty-four floors. Must be nice, being that high up.", "He meant: the higher you are, the further from the flooded tunnels. From the gangs. From the cold. He didn't say that. It would sound like jealousy. It was partly jealousy.")

    $ dual_line("Reiji", "It's a standard corporate unit. Kitchenette. Single window.", "He was describing the apartment like a specification sheet. It was easier than admitting that he had never had a guest before. That no one had ever stood in his building's elevator and commented on the number of floors.")

    n "Ren nods. The numbers climb: 18, 19, 20."

    n "The silence between them is not comfortable. But it's not hostile either. It's the silence of two people who have already said more than they meant to and are waiting to see what happens next."

    pause 0.5

    $ dual_line("Ren", "I've never been in a residential elevator before.", "He said it like a confession. Like admitting a lack that he had learned to hide behind jokes and grins. The words echoed in the silver box.")

    n "Reiji doesn't know what to say to that. He has never thought about elevators as something you could have never been in. Elevators just were. Like wristbands. Like schedules. Like the system itself."

    $ dual_line("Reiji", "It goes up. That's about all it does.", "He meant it as reassurance. It came out as understatement. Everything he said came out as understatement.")

    n "Ren laughs — a short, surprised sound that seems to startle him as much as it startles Reiji."

    ren "Yeah. I figured that part out."

    n "Floor 34. The doors open."

    scene bg apartment_in
    with Dissolve(1.0)

    show reiji face_l
    with Dissolve(0.5)
    show ren face_l
    with Dissolve(0.5)

    n "Reiji's apartment is a single room. Kitchenette against one wall. A narrow window that looks out onto another building's air vents. The ceiling light buzzes faintly, a yellow hum that never quite goes away."

    n "Rain streaks the window in diagonal lines. Thunder rolls somewhere over the commercial district."

    n "Ren steps inside. He looks at the room the way someone looks at a museum exhibit: curious, distant, aware he does not belong."

    n "Reiji hangs his wet coat on a hook. The routine is automatic. Coat. Badge on the counter. Wristband on the charger. Sit. Exist."

    pause 0.8

    n "The silence stretches."

    jump apartment_conversation


## ======================================================================
## ACT III: APARTMENT CONVERSATION (Section 14 — Revised)
## Nuanced conversation. Koi projector. Window/bed. Timer running out.
## ======================================================================

label apartment_conversation:
    scene bg apartment_in
    with Dissolve(0.5)

    show reiji face_l
    with Dissolve(0.5)
    show ren face_l
    with Dissolve(0.5)

    stop music fadeout 3.0

    pause 0.5

    n "Ren stands near the door, dripping onto the floor. He hasn't moved since he entered."

    n "Reiji notices the drip but doesn't mention it. The floor is synthetic. It will dry."

    n "Then Ren laughs — a short, startled sound."

    $ dual_line("Ren", "It's so quiet in here.", "He meant: I can hear myself thinking. I don't know if I like it. Down below, there's always noise — trains, drones, arguments, music. Silence is a luxury. Silence is terrifying.")

    n "Reiji looks around the room as if seeing it for the first time."

    $ dual_line("Reiji", "It's insulated. Corporate standard.", "He had never noticed the quiet until someone else pointed it out. Now it felt like a symptom. Like the apartment itself was trying not to be heard.")

    n "Ren moves to the window. He doesn't touch anything. His hands stay in his pockets. But his eyes sweep the room the way Reiji's diagnostic tools sweep circuit boards — cataloging, assessing, reading what's broken."

    pause 0.5

    n "His gaze stops at Reiji's desk."

    n "On the corner of the desk, half-hidden behind a stack of calibration reports, sits a small holographic projector. It is shaped like a river stone, smooth and dark, with a hairline crack along one edge. It flickers weakly — the ghost of a koi fish swimming in corrupted circles."

    $ dual_line("Ren", "What's that?", "He knew what it was. Everyone knew what holo-projectors were. But asking was safer than commenting on the flicker. The flicker meant something was broken. Broken things were his specialty.")

    $ dual_line("Reiji", "Holo-koi. It was a gift. From... someone. A long time ago.", "He didn't say: my mother. He didn't say: she died three years later. He didn't say: I've kept it on my desk through three apartments and two promotions, and I don't know why, because every time I look at it I feel something I can't calibrate.")

    n "Ren steps closer to the desk. He leans down, examining the crack with the intensity of someone who has spent years fixing things that everyone else threw away."

    $ dual_line("Ren", "The projector lens is misaligned. And the power coupling is loose. That's why it flickers.", "He didn't add: I've fixed a hundred of these. Rich people throw them out when the warranty expires. Poor people fix them. The world's repair manual is written by people who can't afford replacements.")

    n "Reiji blinks."

    $ dual_line("Reiji", "You can fix it?", "He heard the hope in his own voice. It sounded foreign. It sounded like someone else.")

    n "Ren doesn't answer with words. He picks up the projector, turns it over in his hands, and presses his thumb against the seam along the bottom edge. There's a soft click."

    n "The flickering stops."

    n "The koi swims. Smooth. Whole. Its orange scales cast tiny reflections across the ceiling."

    pause 0.8

    $ koi_fixed = True

    show reiji no_badge
    with Dissolve(0.5)

    $ dual_line("Ren", "Just needed pressure in the right place.", "He meant more than the projector. He didn't know if Reiji understood that. He hoped he did.")

    n "Reiji stares at the koi. It has been flickering for two years. He had learned to ignore it, the way he had learned to ignore the ceiling hum and the wristband chimes and the ache behind his eyes that never quite went away."

    $ dual_line("Reiji", "Thank you.", "The words were insufficient. He said them anyway. He was beginning to understand that insufficient words were better than silence.")

    n "Ren sets the projector back on the desk. The koi keeps swimming."

    pause 1.0

    n "The rain intensifies. The window rattles faintly in its frame."

    n "For a while, neither of them speaks. The city hums outside — distant trains, distant sirens, the constant low-frequency pulse of a million machines running in synchronization."

    n "And then, slowly, they begin to talk."

    pause 1.0

    ## ---------- TOPIC 1: WORK ----------

    n "The first silence breaks around the subject of work."

    $ work_pair_reiji = renpy.random.choice(reiji_work_lines)
    $ dual_line("Reiji", work_pair_reiji[0], work_pair_reiji[1])

    $ work_pair_ren = renpy.random.choice(ren_work_lines)
    $ dual_line("Ren", work_pair_ren[0], work_pair_ren[1])

    n "Reiji stares at his wrist. The display is dark now, charging, but he can still feel the ghost of tomorrow's schedule pressing against his skin."

    $ dual_line("Reiji", "Every day is the same. The system tells me where to go. I go there.", "He had stopped deciding things. Decisions were errors. The algorithm corrected errors.")

    $ dual_line("Ren", "At least you know where you'll be tomorrow.", "He didn't mean it as an accusation. It still landed like one.")

    n "The rain fills the pause."

    n "Ren turns from the window. His reflection stays behind, a ghost on the glass."

    $ dual_line("Ren", "You ever think about leaving? Just... not showing up?", "He had thought about it every day for as long as he could remember. But leaving meant disappearing. And disappearing, for someone like him, was permanent.")

    $ dual_line("Reiji", "Where would I go?", "He meant: the system would find me. Or worse, it wouldn't, and I would discover I was never really there to begin with — just a badge and a schedule and a set of approved emotional responses.")

    $ dual_line("Ren", "Anywhere. Nowhere. The lower districts don't keep lists.", "He meant: I have never been on a list. I don't know if that's freedom or erasure. Maybe both. Maybe neither.")

    $ topics_explored += 1

    pause 0.8

    ## ---------- TOPIC 2: IDENTITY ----------

    n "The conversation shifts. Work bleeds into something deeper."

    $ identity_pair_reiji = renpy.random.choice(reiji_identity_lines)
    $ dual_line("Reiji", identity_pair_reiji[0], identity_pair_reiji[1])

    $ identity_pair_ren = renpy.random.choice(ren_identity_lines)
    $ dual_line("Ren", identity_pair_ren[0], identity_pair_ren[1])

    n "Reiji looks at his badge sitting on the counter. A small rectangle of plastic. His face. His name. His employee number. Everything the system needs to know."

    $ dual_line("Reiji", "Without this, I don't exist here.", "He had never said it out loud. The words felt dangerous, as if the walls were listening. They probably were.")

    n "Ren picks up the badge. He turns it over in his hands the same way he did at the station — like a curiosity. Like a question."

    $ dual_line("Ren", "Without this, you'd exist somewhere else.", "He almost added: like me. He didn't. It would have been a lie anyway — he existed differently, not better. Different was not the same as free.")

    n "Reiji watches Ren hold the badge. The plastic looks smaller in Ren's hands. Lighter. As if the weight Reiji feels is something he added himself."

    $ dual_line("Ren", "You know what my ID is?", "He asked it lightly. Too lightly. The way people ask questions they already know the answer to.")

    n "Ren taps his temple."

    $ dual_line("Ren", "My face. My voice. If security doesn't like either one, I run.", "He smiled when he said it. The smile was not happy. The smile was a survival mechanism that had calcified into a personality.")

    $ dual_line("Ren", "That's the whole system.", "It wasn't the whole system. But it was the part of the system that mattered to people like him. The part that decided who got to exist and who got to be erased.")

    n "Reiji looks at the badge in Ren's hand. For a moment, he doesn't recognize his own face in the photo. The man in the picture looks younger. Less tired. Like someone who still believed the wristband's wellness recommendations might work."

    $ topics_explored += 1

    pause 0.8

    ## ---------- TOPIC 3: SLEEP ----------

    n "The hour is late. The rain has not stopped. Somewhere in the building, a neighbor's wristband chimes a sleep reminder through the wall."

    $ sleep_pair_reiji = renpy.random.choice(reiji_sleep_lines)
    $ dual_line("Reiji", sleep_pair_reiji[0], sleep_pair_reiji[1])

    $ sleep_pair_ren = renpy.random.choice(ren_sleep_lines)
    $ dual_line("Ren", sleep_pair_ren[0], sleep_pair_ren[1])

    n "Reiji's wristband glows softly on its charger. The display shows a sleep-readiness score. It does not show the hours he spends staring at the ceiling, running tomorrow's tasks in a loop."

    $ dual_line("Reiji", "I don't remember the last time I woke up feeling rested.", "He remembered. It was six years ago. Before the promotion. Before the wristband. Before the system learned his name and decided it owned his hours.")

    n "Ren leans against the wall. His posture has shifted. The performance energy is draining out of him, replaced by something heavier. Something that looks like exhaustion but feels like trust."

    show ren face_r
    with Dissolve(0.5)

    $ dual_line("Ren", "You ever sleep somewhere and wake up not knowing where you are?", "He asked it like a casual question. It wasn't casual. It was his every morning. Concrete. Cold. The vertigo of having no fixed point in the universe.")

    n "Reiji shakes his head."

    $ dual_line("Ren", "That's my every morning. Cold. Disoriented. Checking if your stuff is still there.", "He didn't say: checking if you're still there. But the thought leaked through. It always leaked through, no matter how tight he held the grin.")

    n "The rain beats against the window."

    n "Reiji looks at his bed. Single mattress. Clean sheets. Climate-controlled. The system tracks his REM cycles and adjusts the temperature automatically."

    n "He has never felt more ashamed of comfort."

    pause 0.5

    n "Ren notices the look. He follows Reiji's gaze to the bed, then to the window, then back."

    $ dual_line("Ren", "That window. It doesn't open, does it?", "He already knew the answer. Corporate apartments never had windows that opened. Opening implied choice. Choice was a variable the system preferred to control.")

    $ dual_line("Reiji", "No. None of them do. Climate regulation is centralized.", "He had never questioned it. A window that didn't open was normal. Like a schedule he didn't write. Like a wristband he couldn't remove.")

    $ dual_line("Ren", "Must be weird. Looking at the sky and never feeling the wind.", "He meant: that's what your whole life is. Looking at things you can't touch. He didn't say it. The koi was still swimming. The room was still quiet. Some things you let people figure out on their own.")

    show ren face_l
    with Dissolve(0.5)

    pause 0.8

    n "Reiji's wristband glows again. The display shows the time: 02:47 AM. Below it, in smaller text: Guest access: 21 hours remaining."

    n "The timer."

    n "Ren sees it too."

    $ dual_line("Ren", "Twenty-one hours.", "He said it like a countdown. Like a sentence. Time was always running out. That was the one thing he and Reiji had in common, even if neither of them knew it yet.")

    $ dual_line("Reiji", "You could stay. Tonight. The floor is... I have an extra blanket.", "The offer came out before his brain could intercept it. It was the most honest thing he had said all night. The most honest thing he had said in years.")

    n "Ren stares at him."

    n "The grin tries to return. It doesn't make it all the way. What reaches his face is something smaller. Sadder. More real."

    $ dual_line("Ren", "Yeah. Okay. Just tonight.", "He had said 'just tonight' to twelve different couches and six different shelters. It had never been just tonight. But he wanted this one to be. That was new. That was terrifying.")

    $ topics_explored += 1
    $ trust += 1

    scene bg_black
    with Dissolve(2.0)

    n "The light goes out."

    n "The rain keeps falling."

    n "The koi keeps swimming — a small orange light moving in endless circles on the ceiling."

    n "Two people, who should never have met, breathe in the same dark room."

    n "Neither of them sleeps. But for the first time in a long time, neither of them is entirely alone."

    pause 1.0

    n "The wristband logs the sleep anomaly. The system notes the guest access. The data flows upward into servers that never forget."

    n "Twenty-one hours."

    pause 0.5

    jump one_month_montage


## ======================================================================
## ACT IV: ONE MONTH MONTAGE (Section 14 — Revised)
## Rapid scene-switching. Reiji corporate routine vs Ren lower market.
## Sequence 8: Reiji discovers system tracked Ren's movements.
## ======================================================================

label one_month_montage:
    scene bg apartment_in_day
    with Dissolve(1.5)

    pause 0.5

    n "One month."

    n "The city does not pause. It never pauses."

    pause 0.8

    ## --- Sequence 1: Reiji's Morning ---

    scene bg apartment_in_day
    with Dissolve(0.5)

    show reiji no_badge
    with Dissolve(0.3)

    n "Reiji wakes."

    n "The wristband chimes. The schedule scrolls. The shower runs at exactly the temperature the system recommends for optimal morning alertness."

    n "The blanket Ren used is folded on the chair. Reiji has not moved it. He tells himself it is because he is tidy."

    pause 0.3

    ## --- Sequence 2: Ren's Morning ---

    scene bg blackMarket
    with Dissolve(0.5)

    show ren face_l at sprite_left
    with Dissolve(0.3)

    n "Ren wakes somewhere different."

    n "A market stall. An underpass. A subway platform. The location changes but the cold is the same. He folds the cardboard he slept on and tucks it behind a vent where no one will find it."

    n "The guest pass expired twenty-nine days ago. He is invisible again."

    pause 0.3

    ## --- Sequence 3: Reiji's Commute ---

    scene bg subway_out
    with Dissolve(0.5)

    show reiji face_l
    with Dissolve(0.3)
    show police
    with Dissolve(0.3)

    n "Reiji commutes."

    n "The train is always on time. The advertisements change. The passengers do not."

    n "He finds himself looking at the service platforms between stations. The places where people without shoes hold plastic bags. He never sees the same person twice. He is not sure if that is comforting or damning."

    pause 0.3

    ## --- Sequence 4: Ren's Hustle ---

    scene bg blackMarket
    with Dissolve(0.5)

    show ren face_l at sprite_left
    with Dissolve(0.3)
    show dealer
    with Dissolve(0.3)
    show drone
    with Dissolve(0.3)

    n "Ren trades."

    $ line = renpy.random.choice(market_auntie_lines)
    market_auntie "[line]"

    n "Ren grins at the market auntie — the same grin he used on Reiji in the alley. It works less well here. She has seen every variation. She has seen every drifter who thought a smile was currency."

    n "He walks away with half of what he asked for. It's more than he expected."

    pause 0.3

    ## --- Sequence 5: Reiji's Office ---

    scene bg workingArea
    with Dissolve(0.5)

    show reiji face_l
    with Dissolve(0.3)

    n "Reiji works."

    $ dual_line("Reiji", "The calibration numbers are within tolerance.", "Tolerance was a word the company used to mean 'good enough.' Reiji had been 'good enough' for six years. He was beginning to wonder what the threshold was for 'not good enough.' What happened when you crossed it. Whether anyone would notice.")

    $ line = renpy.random.choice(coworker_lines)
    coworker "[line]"

    n "Reiji nods without processing the words. The coworker doesn't notice. No one ever notices."

    pause 0.3

    ## --- Sequence 6: Ren's Evasion ---

    scene bg blackMarket
    with Dissolve(0.5)

    show ren face_l at sprite_left
    with Dissolve(0.3)
    show drone
    with Dissolve(0.3)

    n "Ren moves."

    n "Security sweeps the lower platform at 2 AM. Ren knows the schedule now. He is gone by 1:45. He leaves nothing behind because there is nothing to leave."

    n "The underpass is cold. The concrete sweats. Somewhere above, a train passes — the same train Reiji might be on, headed home, wristband glowing, schedule scrolling. Neither of them knows."

    pause 0.3

    ## --- Sequence 7: Reiji's Cafeteria ---

    scene bg workingArea
    with Dissolve(0.5)

    show reiji face_l
    with Dissolve(0.3)

    n "Reiji eats."

    n "Neural-interface calibration review. Productivity sync. Nutrition break at exactly 12:00. The cafeteria serves the same meal every Tuesday. The same synthetic protein. The same vitamin-enriched broth. The same fluorescent lighting that makes everyone look slightly dead."

    system "Nutrition break: 12:00–12:20. Next appointment: productivity sync with Supervisor Tanaka."

    n "Reiji looks at his tray. He is not hungry. He is never hungry at 12:00. But the schedule says eat, so he eats."

    pause 0.3

    ## --- Sequence 8: THE DISCOVERY ---

    scene bg workingArea
    with Dissolve(0.8)

    show reiji face_l
    with Dissolve(0.3)

    pause 0.5

    n "It is 3:47 PM on a Thursday when Reiji discovers the truth."

    n "He is running a routine security audit — one of the hundred peripheral tasks the system assigns to fill the gaps between real work. Cross-referencing access logs. Flagging anomalies."

    n "His wristband pings. A submenu opens. GUEST ACCESS HISTORY, it says. A routine entry, buried under layers of transit data."

    n "He almost dismisses it. Almost."

    n "Then he sees the map."

    show bg city_map
    with Dissolve(0.5)

    pause 0.8

    n "The system has been tracking Ren."

    n "Not Ren by name — Ren has no name in the system. But the guest pass Reiji sponsored thirty days ago has a digital signature. And that signature has been mapped. Every checkpoint. Every scanner that caught the edge of his silhouette. Every drone that logged an unregistered body in the twenty-four hours the pass was active."

    n "The system didn't stop tracking when the pass expired."

    n "It followed the gaps. It mapped the places where Ren wasn't supposed to be. It correlated his movements with a dozen other unregistered persons, building a network map of invisible people by tracing the spaces they left behind."

    system "GUEST ACCESS PATTERN ANALYSIS: SUBJECT [[UNREGISTERED]] HAS BEEN FLAGGED FOR MOVEMENT CORRELATION. ASSOCIATED NODES: 17 UNREGISTERED INDIVIDUALS. RECOMMENDATION: FORWARD TO SECURITY COMPLIANCE DIVISION."

    n "Reiji stares at the screen."

    $ noticed_tracking = True

    $ dual_line("Reiji", "...", "The system had used his act of kindness as a surveillance node. His signature. His liability. His one moment of humanity — converted into data points on seventeen people who had never consented to be mapped.")

    n "He reads the recommendation again. Forward to Security Compliance Division."

    n "Security Compliance Division. The same division that runs the 'urban sanitation' campaigns. The same division that clears platforms between transit lines."

    n "His hand moves to the screen. There is a button. FORWARD REPORT. It blinks green. The system's preferred color. The color of compliance."

    n "He does not press it."

    pause 0.8

    n "Instead, he scrolls to the bottom of the report. There is another option, buried in a submenu marked ADMINISTRATIVE OVERRIDE."

    system "OVERRIDE OPTIONS: [1] FORWARD TO COMPLIANCE. [2] MARK AS ROUTINE — NO ACTION. [3] DELETE ACCESS LOG."

    n "Reiji selects Option 3."

    system "WARNING: DELETION OF GUEST ACCESS LOGS REQUIRES SUPERVISOR AUTHORIZATION. THIS ACTION WILL BE LOGGED TO YOUR EMPLOYMENT RECORD."

    n "He hesitates for exactly three seconds. Then he types his override code."

    system "ACCESS LOG DELETED. THIS ACTION HAS BEEN RECORDED."

    $ noise += 2

    n "Reiji closes the terminal. His hands are shaking. The wristband logs elevated heart rate. The system recommends meditation."

    n "He stands up from his desk."

    n "For the first time in six years, he leaves the office before the schedule tells him to."

    scene bg subway_out
    with Dissolve(1.0)

    show reiji face_l
    with Dissolve(0.3)

    n "He doesn't go home. He doesn't go to Neon Pub. He walks without direction, the rain finding him again, the city sliding past in streaks of neon and chrome."

    n "He walks until his feet ache and his coat is soaked through and the wristband has given up recommending anything."

    pause 0.8

    ## --- Sequence 9: Divergence Headlines ---

    scene bg street
    with Dissolve(1.0)

    n "The news ticker cycles through its headlines. The words change. The meaning does not."

    news "Tokyo Corridor Productivity Reaches New High."

    news "Public Satisfaction Remains Stable."

    news "Urban Sanitation Campaign Successful."

    news "Unauthorized Population Reduced."

    news "Consumer Confidence Rising."

    pause 0.8

    n "Reiji and Ren live in the same city. Breathe the same air. Walk the same rain-slicked streets."

    n "But they move in different worlds, separated by a membrane of light and data."

    n "Reiji's world is measured. Tracked. Optimized."

    n "Ren's world is improvised. Fleeting. Unrecorded — or so Ren believes. Or so Reiji believed, until today."

    n "The surface shines. Beneath it, something is cracking."

    pause 0.8

    n "One month. Twenty-nine days since the guest pass expired. Twenty-nine days since Reiji last saw Ren's face."

    n "Twenty-nine days since he learned that caring about another person was an exploit the system could weaponize."

    n "And then, on the thirtieth night, the rain is heavier than it has ever been."

    scene bg_black
    with Dissolve(2.0)

    n "And Reiji receives a message from a number he does not recognize."

    system "Unknown sender. Message: come to the river. i need someone who sees me."

    n "Reiji reads it three times."

    n "He puts on his coat."

    n "He does not check the weather. He does not check the transit schedule. He does not wait for the system to recommend a course of action."

    n "For the first time in six years, Morikawa Reiji makes a decision that belongs to no one but himself."

    jump riverbank


## ======================================================================
## ACT V: RAINY RIVERBANK (Section 14 — Revised)
## System interrupt: "NO RECORD". Final choice. Three endings.
## ======================================================================

label riverbank:
    scene bg riverbank
    with Dissolve(2.0)

    show reiji face_l
    with Dissolve(0.5)

    play music "audio/theme.mp3" fadein 4.0 volume 0.8

    pause 1.0

    n "The riverbank is a concrete scar between industrial districts."

    n "Floodwalls rise on either side. Rusted guardrails line the pedestrian path. The water below is black and fast and does not reflect the city lights."

    n "It swallows them."

    n "The rain is relentless. It hammers the concrete. It hammers the corrugated roofs of distant warehouses. It hammers Reiji's shoulders as he walks along the path, searching."

    pause 0.8

    show ren face_l
    with Dissolve(0.5)

    n "He finds Ren standing on the other side of the guardrail."

    n "Not leaning against it. Standing beyond it. The toes of his shoes touching the edge of the concrete where it drops into black water."

    n "Ren's jacket is soaked through. His hair is plastered to his forehead. His eyes are fixed on the water below."

    n "He does not turn when Reiji approaches."

    pause 0.5

    $ dual_line("Reiji", "Ren.", "His voice came out steadier than he felt. The name hung in the rain like something fragile. It was the first time he had said it out loud.")

    n "Ren's shoulders tense. Then they don't. The tension leaves him as if it was never there, as if he has been holding it so long he forgot what release felt like."

    $ dual_line("Ren", "You came.", "He didn't believe anyone would. He sent the message anyway — a coin tossed into a well. The splash surprised him. The surprise hurt more than the silence would have.")

    n "Reiji steps closer. Not too close. Close enough that Ren could reach him if he turned around."

    $ dual_line("Reiji", "You asked me to.", "He meant: I didn't have to think about it. That scared him more than the guardrail. More than the water. More than the report he deleted two days ago.")

    n "Ren finally turns. His face is raw. The grin is gone. What remains is younger and older at the same time — the face of someone who has been holding himself together with improvisation and caffeine and the memory of a stranger's kindness."

    $ dual_line("Ren", "Do you know how many nights I've stood here?", "He asked it calmly. Too calmly. The calm of someone who has normalized the edge. Made it a landmark. A reference point. A place to go when the city got too loud.")

    n "Reiji doesn't answer. He knows the question isn't finished."

    $ dual_line("Ren", "Too many. And every time, I talk myself out of it. Stupid, right?", "He wanted Reiji to say it was stupid. He wanted Reiji to give him a reason that wasn't his own exhausted voice. He wanted proof that someone would notice if he stopped talking himself out of it.")

    n "The rain beats down."

    n "Reiji moves to the guardrail. He doesn't cross it. He stands on the safe side, but his hands wrap around the cold, wet metal, and he faces the water with Ren."

    $ dual_line("Reiji", "It's not stupid.", "He had never stood on the wrong side of a guardrail. But he had stood in a bathroom at 3 AM, staring at his own reflection, wondering who was staring back. He knew the shape of the feeling, if not its weight. The shape was enough.")

    pause 0.8

    n "Ren looks at him — really looks — for what might be the first time."

    n "Not at the corporate coat. Not at the badge. Not at the system that props Reiji up like a paper figure in a display window."

    n "At Reiji."

    $ dual_line("Ren", "You're not what I thought you were.", "He had thought: tower man, badge man, system man. He had not thought: person who deletes reports. Person who turns back. Person who comes to a riverbank in the rain because someone asked. He was sorry. He didn't say it. The apology was there, beneath the words, like everything else beneath the neon.")

    $ dual_line("Reiji", "Neither are you.", "He had thought: drifter, performer, problem. He had not thought: person who fixes holo-projectors. Person who folds blankets. Person who has been standing on the wrong side of guardrails for years and keeps climbing back. He was sorry. He didn't say it either. The apology was there, beneath the surface, where all the real things lived.")

    pause 1.0

    n "His wristband vibrates."

    show badge
    with Dissolve(0.5)

    n "Once. Twice. A pattern that means system interrupt."

    n "The display glows through his wet sleeve."

    system "SYSTEM INTERRUPT: ENGINEER MORIKAWA REIJI. UNAUTHORIZED ACCESS LOG DELETION FLAGGED FOR REVIEW. GUEST ACCESS PATTERN RE-GENERATED FROM BACKUP. FORWARD TO SECURITY COMPLIANCE DIVISION: PENDING."

    n "Reiji stares at the words."

    n "The system found the backup. Of course it did. Systems always have backups. That's what makes them systems."

    system "OPTIONS: [1] CONFIRM FORWARD TO COMPLIANCE. [2] MARK FOR REVIEW — 48 HOUR DELAY. [3] NO RECORD — PERMANENTLY DELETE ALL GUEST ACCESS DATA. WARNING: OPTION 3 REQUIRES EXECUTIVE OVERRIDE AND WILL BE PERMANENTLY LOGGED TO EMPLOYMENT RECORD."

    pause 0.5

    n "Ren sees the glow. He can't read the text, but he reads Reiji's face. The face tells him enough."

    $ dual_line("Ren", "What is it?", "He already knew. Something bad. Something about him. Everything was always about him, even when it wasn't.")

    n "Reiji doesn't answer. His thumb hovers over the display."

    n "Three options. Three futures."

    n "He thinks about the man on the service platform. He thinks about the child with retinal projections. He thinks about the koi swimming in circles on his ceiling. He thinks about seventeen names he will never know, mapped by a system that sees people as data points."

    n "He selects Option 3."

    system "EXECUTIVE OVERRIDE ACCEPTED. ALL GUEST ACCESS DATA: PERMANENTLY DELETED. NO RECORD RETAINED. THIS ACTION HAS BEEN LOGGED TO EMPLOYMENT RECORD: MORIKAWA REIJI."

    $ noise += 2

    n "The screen goes dark."

    show reiji no_badge
    with Dissolve(0.5)

    n "Somewhere in a server farm beneath the commercial district, seventeen names dissolve into static. Seventeen maps become noise. Seventeen invisible people become invisible again."

    n "Reiji looks up at Ren."

    $ dual_line("Reiji", "It's nothing. Just a system notification.", "The lie was the biggest he had ever told. It was also the truest thing he had ever done. He had erased data to protect a person. He had broken the system to save a stranger. The stranger wasn't a stranger anymore.")

    n "Ren doesn't believe him. But he doesn't push. He has learned, over years of survival, that some truths are too heavy to hand over all at once."

    pause 0.8

    n "The guardrail is cold."

    n "The water is black."

    n "But the space between them has shrunk to something almost human."

    pause 1.0

    n "Ren climbs back over the guardrail."

    n "His feet land on the safe side of the concrete. He stands there, shivering, water dripping from his chin, hands shoved deep into soaked pockets."

    $ dual_line("Ren", "I don't know what happens now.", "He never knew. That was the problem. That was always the problem. But tonight, someone had come. Someone had seen him. Someone had chosen him over the system. He didn't know what that meant. But it meant something.")

    n "Reiji looks at the water. Then at Ren. Then at the city glowing in the distance — a million lights, a million lies, a million people performing wellness for an algorithm that doesn't care."

    n "The rain begins to slow."

    n "The moment crystallizes."

    pause 0.5

    n "This is the final choice. The one that cannot be undone. The one that determines which version of this story gets told."

    menu:
        "\"Come back with me.\"":
            $ ending_push = "come_back"
            $ trust += 2
            jump ending_quiet_survival

        "\"I'm sorry.\"":
            $ ending_push = "sorry"
            $ masking += 2
            jump ending_reflection

        "Say nothing. Just stand beside him.":
            $ ending_push = "silence"
            $ noise += 2
            jump ending_city_continues


## ======================================================================
## ENDING A: QUIET SURVIVAL (High Trust — "Come back with me.")
## ======================================================================

label ending_quiet_survival:
    scene bg riverbank
    with Dissolve(1.0)

    show reiji no_badge
    with Dissolve(0.5)
    show ren face_l
    with Dissolve(0.5)
    show badge
    with Dissolve(0.3)

    pause 0.5

    $ dual_line("Reiji", "Come back with me.", "He didn't specify where. The apartment. The surface. The life he had been living before a stranger in an alley taught him that kindness was a thing you could do instead of a thing you could measure. 'With me' was the part that mattered. 'With me' was the part that was new.")

    n "Ren doesn't move for a long moment."

    n "The rain drips from his chin. His eyes are red-rimmed — from rain or tears or exhaustion, it doesn't matter. What matters is the way he looks at Reiji. Like Reiji is a door that wasn't supposed to open. Like he is afraid to walk through it. Like he is more afraid not to."

    $ dual_line("Ren", "You mean that.", "It wasn't a question. It was a realization. A slow, careful realization, the kind you make when you've been wrong about people so many times that being right feels like a trap.")

    $ dual_line("Reiji", "I mean it.", "He did. He had never meant anything more. He had approved deployment reports and signed liability forms and pressed compliance buttons for six years, and none of it had meant anything. This meant everything.")

    pause 0.8

    n "They do not save each other."

    n "That is not how this story works. There are no heroes here. No rescue arcs. No single conversation that fixes a lifetime of erosion."

    n "But something shifts."

    scene bg apartment_in
    with Dissolve(2.0)

    n "Ren starts showing up at Reiji's apartment. Not every night. Not on a schedule. But regularly enough that Reiji starts buying extra food without thinking about it."

    n "Reiji starts leaving work at the scheduled time instead of the optimized time. The wristband notices. The system sends wellness recommendations. Reiji dismisses them. Then he dismisses them again. Eventually, the system stops sending them."

    n "One night, Ren asks Reiji to show him what neural-interface calibration actually means. Reiji tries to explain. Ren doesn't understand half of it. But he listens all the way through, and when Reiji is done, Ren says: 'So you make dreams work. That's not nothing.'"

    n "One morning, Reiji sleeps past his alarm. The wristband reports a 'sleep anomaly.' Reiji turns it off and makes coffee for two."

    n "They do not fix the city. They cannot. The towers still rise. The billboards still smile. The trains still run on time."

    n "But sometimes, in a cramped apartment above the endless motion, two people sit in silence and do not feel alone."

    n "The koi keeps swimming."

    n "And beneath the neon, that is enough."

    pause 2.0

    n "The headlines keep cycling."

    n "The city keeps shining."

    n "But somewhere, in a room too small for the system to care about, two people have stopped performing."

    n "And that, perhaps, is a kind of survival."

    n "Not the kind the system measures."

    n "The kind that matters."

    pause 1.0

    jump credits


## ======================================================================
## ENDING B: REFLECTION (Mixed — "I'm sorry.")
## ======================================================================

label ending_reflection:
    scene bg riverbank
    with Dissolve(1.0)

    show reiji no_badge
    with Dissolve(0.5)
    show ren face_l
    with Dissolve(0.5)

    pause 0.5

    $ dual_line("Reiji", "I'm sorry.", "He didn't know what he was apologizing for. The system. The city. The six years he spent pressing buttons while people disappeared on service platforms. The fact that he couldn't fix any of it. The fact that 'sorry' was too small a word for the weight of what he meant.")

    n "Ren hears the word. He has heard it before — from social workers, from security officers, from strangers who dropped coins into his palm without making eye contact. Sorry was the cheapest currency in the city."

    n "But this time, it sounds different."

    n "This time, it sounds like someone who means it."

    $ dual_line("Ren", "You don't have to be sorry. You showed up.", "He meant: that's more than anyone else did. He meant: I don't know what to do with an apology that's real. I've never received one before.")

    pause 0.8

    n "Ren climbs back over the guardrail. But something in him stays on the other side."

    n "They walk away from the river together. The rain has stopped. The streets are wet and quiet and empty."

    scene bg subway_out
    with Dissolve(1.5)

    n "At the intersection where their paths diverge — Reiji toward the towers, Ren toward the lower districts — they stop."

    n "Neither knows what to say."

    n "The conversation at the riverbank opened something. But opening is not the same as healing. Healing takes time. Healing takes trust. Healing takes more than one night."

    $ dual_line("Reiji", "Will I see you again?", "He was afraid of the answer. Both answers. Yes meant more risk. No meant more silence. He wasn't ready for either. He asked anyway.")

    $ dual_line("Ren", "Probably. The city's not that big.", "It was that big. It was infinite. But he wanted to mean it. He wanted to believe that two people who met in an alley could find each other again in a city designed to keep them apart.")

    n "They part."

    scene bg street
    with Dissolve(1.5)

    n "The days that follow are the same as the days that came before. Reiji works. Ren survives. The city spins."

    n "But something lingers — a residue of the night at the riverbank. An awareness that the surface is not the whole story."

    n "Reiji catches himself looking at the service platforms when his train passes. He never sees Ren. But he looks. Every single time, he looks."

    n "Ren catches himself standing a little further from the edge of the platform. He doesn't know why. He doesn't question it. Some changes don't announce themselves. They just arrive."

    n "The city continues. The headlines rotate. The billboards smile."

    n "But beneath the surface, two people carry each other in ways neither fully understands."

    n "It is not a happy ending."

    n "It is an honest one."

    n "And sometimes, honesty is the only thing the system cannot measure."

    pause 1.0

    jump credits


## ======================================================================
## ENDING C: CITY CONTINUES (High Noise / Low Trust — "Say nothing.")
## ======================================================================

label ending_city_continues:
    scene bg riverbank
    with Dissolve(1.0)

    show reiji no_badge
    with Dissolve(0.5)
    show ren face_l
    with Dissolve(0.5)
    show badge
    with Dissolve(0.3)
    show drone
    with Dissolve(0.3)

    pause 0.5

    n "Reiji says nothing."

    n "He doesn't have the words. He has never had the words. Six years of technical language — calibration, optimization, compliance — and none of it prepared him for this. For a person on the edge of a river. For a question that has no menu of approved responses."

    n "He stands beside Ren. Their shoulders are close enough to touch. They don't touch."

    n "The silence stretches. The rain fills it. The city hums beneath it."

    $ dual_line("Ren", "Yeah. That's what I thought.", "He had hoped for words. He had prepared for silence. Silence was the default. Silence was what people gave you when they didn't know what to do with you. He was used to silence. That didn't make it hurt less.")

    n "Ren climbs back over the guardrail on his own."

    n "The motion is practiced. Efficient. He has done this before. He will do it again."

    n "He stands on the safe side of the concrete, but his eyes stay on the water. As if the water is still an option. As if it will always be an option."

    pause 0.8

    n "Reiji wants to say something. Anything. His throat is a locked door. The key is somewhere in his chest, buried under six years of compliance training and emotional deferral and the slow erosion of his own voice."

    n "By the time he finds it, Ren is already walking away."

    scene bg riverbank
    with Dissolve(1.0)

    n "The riverbank is empty."

    n "Reiji stands alone at the guardrail. Ren has slipped away during a silence that stretched too long."

    n "The rain has stopped. The city hums in the distance."

    n "Reiji does not know if Ren climbed back over the guardrail or stayed on the other side. He does not know which answer he is hoping for."

    n "He waits for an hour."

    n "The water keeps moving. It does not care."

    pause 0.8

    scene bg apartment_in
    with Dissolve(1.5)

    n "Reiji returns to his apartment. The blanket Ren used is still folded on the chair. Reiji looks at it for a long time."

    n "The wristband chimes. Sleep reminder. Tomorrow's schedule scrolls automatically: 07:30 wake cycle, 08:10 transit, 09:00 neural-interface calibration review."

    n "The system does not notice that anything is different."

    n "Reiji lies down. The ceiling is the same. The hum is the same. The numbers will be adequate. The numbers are always adequate."

    n "The koi keeps swimming. It has been swimming for years. It will keep swimming for years more."

    n "But something has shifted — a crack in the surface, too small for the system to measure, too deep to ignore."

    n "He closes his eyes."

    n "And the city carries on, indifferent and bright and utterly unaffected."

    pause 0.8

    scene bg street
    with Dissolve(1.5)

    news "Tokyo Corridor productivity rises for the eighth consecutive quarter."

    news "Consumer confidence stable across all demographics."

    news "All systems operating within acceptable parameters."

    news "No anomalies detected."

    pause 1.0

    n "The headlines are clean."

    n "The fonts are clean."

    n "Even the silence seems clean."

    n "From a distance, Tokyo looks like proof that history can be repaired by enough light."

    scene bg_black
    with Dissolve(3.0)

    n "And beneath the neon, the water keeps moving."

    pause 2.0

    jump credits


## ======================================================================
## CREDITS
## ======================================================================

label credits:
    scene bg_black
    with Dissolve(2.0)

    pause 1.0

    n "Where the Rainbow Ends"

    n "A cyberpunk visual novel about the human cost hidden beneath a city of light."

    pause 1.0

    n "A city can look successful while the people inside it are quietly breaking."

    pause 1.5

    n "This project reveals the social and emotional decay hidden beneath the surface of a prosperous cyberpunk city."

    pause 1.0

    n "The split-screen dialogue system shows both what characters say and what they truly think, turning the theme 'Beneath the Surface' into the game's central mechanic."

    pause 1.5

    n "Thank you for playing."

    pause 1.0

    n "The city does not pause."

    n "But sometimes, we should."

    pause 2.0

    ## Return to main menu
    return
