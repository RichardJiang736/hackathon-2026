## variables.rpy — Beneath the Neon
## Hidden system variables tracking narrative state and character psychology.
##
## These variables form the core emotional tracking system.
## They influence dialogue variants, internal thought pools, ending tone,
## and optional UI glitch effects when noise is high.

## trust — Tracks intimacy and honesty between Reiji and Ren.
## Higher trust means more vulnerability, lower means guarded distance.
default trust = 0

## projection — Tracks mutual misconceptions of each other's status.
## When high, characters see each other as symbols rather than people.
default projection = 0

## noise — Tracks environmental pressure: surveillance, fatigue, systemic friction.
## High noise triggers ticker glitches and colder narrative framing.
default noise = 0

## masking — Tracks Reiji's reliance on rationalization to hide exhaustion.
## High masking means Reiji buries feelings under technical language.
default masking = 0

## liability — Tracks Ren's exposure risk (introduced in Act II choices).
## Higher liability means Ren is in more danger from corporate security.
default liability = 0

## ending_push — Tracks which emotional direction the final choice tilts toward.
## Set during Act V riverbank scene. Values: "come_back", "sorry", "silence"
default ending_push = ""

## Additional tracking for ending determination
default help_ren_choice = False
default demand_id_choice = False
default ignore_ren_choice = False

## Tracks which conversation topics were fully explored
default topics_explored = 0

## Tracks if Reiji chose to sign the Host Liability Agreement
default signed_liability = False

## Tracks if Reiji noticed the system mapping Ren's movements
default noticed_tracking = False

## Tracks the drink order in Act I
default drink_order = ""

## Tracks if the koi projector was fixed
default koi_fixed = False
