## characters.rpy — Beneath the Neon
## Character definitions, display names, side images, and fallback asset mappings.
## All image assets use Solid() color placeholders so the game compiles
## without external asset files.

## ---------- CHARACTER DEFINITIONS ----------

## Narrator — used for scene description, atmospheric text, and transitions
define n = Character(None, what_color="#c0d0f0", what_size=28, what_italic=True)

## Reiji — Morikawa Reiji, The Corporate Engineer
## Introverted, technical, emotionally restrained, masking fatigue behind rational language
define reiji = Character("Reiji", who_color="#44ccff", what_color="#cceeff", what_size=28)

## Ren — The Drifter
## Extroverted, energetic, socially adaptive, uses humor defensively
define ren = Character("Ren", who_color="#ff8844", what_color="#ffddcc", what_size=28)

## System — Automated corporate interface messages, wrist display notifications
define system = Character("SYSTEM", who_color="#00ff88", what_color="#88ffcc",
                          what_size=24, what_font="DejaVuSans.ttf")

## News — State propaganda broadcasts and ticker headlines
define news = Character("NEWS", who_color="#ff4444", what_color="#ffaaaa",
                        what_size=24)

## Advertisement — Corporate billboard and ad copy
define advert = Character("ADVERTISEMENT", who_color="#ff44ff", what_color="#ffaaff",
                          what_size=24, what_italic=True)

## Announcement — Public transit / station announcements
define announce = Character("ANNOUNCEMENT", who_color="#ffcc44", what_color="#ffeeaa",
                            what_size=24)

## Headset — The micro-recovery headset voice
define headset = Character("HEADSET", who_color="#88aacc", what_color="#aaccee",
                           what_size=22, what_italic=True)

## ---------- NEW MINOR CHARACTERS (Section 14) ----------

## Drone Audio — Security drone vocal output
define drone = Character("DRONE AUDIO", who_color="#aadd44", what_color="#ccff88",
                          what_size=22, what_font="DejaVuSans.ttf")

## Bartender — Neon Pub bartender
define bartender = Character("BARTENDER", who_color="#ff9966", what_color="#ffcc99",
                              what_size=26)

## Coworker — Reiji's office colleague
define coworker = Character("COWORKER", who_color="#6699cc", what_color="#aaccee",
                             what_size=26)

## Supervisor — Reiji's corporate supervisor
define supervisor = Character("SUPERVISOR", who_color="#cc6666", what_color="#ffaaaa",
                               what_size=26)

## Market Auntie — Lower market stall vendor
define market_auntie = Character("MARKET AUNTIE", who_color="#ffaa44", what_color="#ffddaa",
                                  what_size=26)

## Checkpoint Display — Automated checkpoint scanner display
define checkpoint = Character("CHECKPOINT DISPLAY", who_color="#44dddd", what_color="#aaffff",
                               what_size=22, what_font="DejaVuSans.ttf")


## ---------- IMAGE DECLARATIONS ----------
## Real image assets mapped per Galagame_Finalised.pdf scene structure.
## Case-sensitive extensions must be preserved exactly for cross-platform compatibility.

## --- Sprite Positioning Transforms ---
## Left: frames the cyan spoken-dialogue card (xalign 0.05)
## Right: frames the magenta internal-thought card (xalign 0.95)

transform sprite_left:
    xalign 0.15
    yalign 0.9

transform sprite_left_a:
    xalign 0.03
    yalign 0.9

transform sprite_left_b:
    xalign 0.30
    yalign 0.9

transform sprite_right:
    xalign 0.85
    yalign 0.9


## --- Background Scaling Transform ---

transform bg_fill:
    xalign 0.5
    yalign 0.5
    xysize (1920, 1080)


## --- Backgrounds ---

image bg train_in = At("images/train_in.png", bg_fill)
image bg subway_in = At("images/subway_in.png", bg_fill)
image bg subway_out = At("images/subway_out.png", bg_fill)
image bg street = At("images/street.png", bg_fill)
image bg club_out = At("images/club_out.png", bg_fill)
image bg club_in = At("images/club_in.png", bg_fill)
image bg apartment_out = At("images/apartment_out.png", bg_fill)
image bg apartment_in = At("images/apartment_in.png", bg_fill)
image bg apartment_in_day = At("images/apartment_in_day.png", bg_fill)
image bg city_map = At("images/city_map.png", bg_fill)
image bg blackMarket = At("images/blackMarket.png", bg_fill)
image bg riverbank = At("images/riverbank.png", bg_fill)
image bg workingArea = At("images/workingArea.jpg", bg_fill)
image bg_black = "#000000"


## --- Character Sprites ---

image reiji face_l = At("images/charA_faceL.PNG", sprite_left)
image reiji face_r = At("images/charA_faceR.jpg", sprite_right)
image ren face_l = At("images/charB_faceL.png", sprite_right)
image ren face_r = At("images/charB_faceR.png", sprite_right)
image ren face_3char = At("images/charB_faceR.png", sprite_left_b)
image reiji no_badge = At("images/charA_noBadge.PNG", sprite_left)


## --- Items & Props ---

transform badge_pos:
    xalign 0.95
    yalign 0.05
    zoom 0.25

image badge = At("images/badge.PNG", badge_pos)
image police = At("images/police.PNG", sprite_right)

transform drone_pos:
    xalign 0.5
    yalign 0.15
    zoom 0.35

image drone = At("images/drone.PNG", drone_pos)
image dealer = At("images/dealer.PNG", sprite_right)
