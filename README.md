<p align="center">
  <img src="game/images/cover.jpg" alt="Where the Rainbow Ends — Cover Art" width="600"/>
</p>

# Where the Rainbow Ends

<p align="center">
  <em>A cyberpunk visual novel about two people trapped by the same city in different ways.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/engine-Ren'Py-ff69b4?style=flat-square" alt="Ren'Py"/>
  <img src="https://img.shields.io/badge/genre-visual_novel-00cc99?style=flat-square" alt="Visual Novel"/>
  <img src="https://img.shields.io/badge/setting-cyberpunk_Tokyo-9b59b6?style=flat-square" alt="Cyberpunk Tokyo"/>
  <img src="https://img.shields.io/badge/resolution-1920×1080-3498db?style=flat-square" alt="1920x1080"/>
</p>

---

## Overview

Tokyo hums with efficiency. Its towers gleam, its transit runs on time, its citizens smile in corporate headshots. But beneath the neon, something is unraveling.

**Where the Rainbow Ends** is a cyberpunk visual novel set in a futuristic Tokyo that appears prosperous, efficient, and technologically advanced, but hides inequality, surveillance, and emotional exhaustion beneath its neon surface. Players follow **Morikawa Reiji**, a corporate engineer, as he meets **Ren**, a lower-class drifter, and gradually discovers how both of them are trapped by the same city in different ways.

The project explores the problem of dehumanization in systems that look successful from the outside — a city where every wristband tracks wellness, every billboard promises happiness, and every headline reports record productivity, while unregistered citizens are "reduced" in sanitation campaigns and corporate workers press the same three buttons for six years without feeling anything.

## Demo

Download **demo.mp4** in the repository.

## Core Innovation: Split-Screen Dialogue System

The game's signature mechanic is a **split-screen dialogue system** that shows both what characters say aloud and what they truly think — side by side, simultaneously.

```
┌──────────────────────────────┐  ┌──────────────────────────────┐
│  Reiji says:                 │  │  Reiji thinks:               │
│  "Almost home."              │  │  Home was a word the system  │
│                              │  │  used because "assigned      │
│                              │  │  residential unit" tested    │
│                              │  │  poorly in employee surveys. │
└──────────────────────────────┘  └──────────────────────────────┘
```

This mechanic turns the hackathon theme "Beneath the Surface" into the game's central interaction. Every key emotional beat uses `dual_line()` to expose the distance between performed compliance and genuine feeling — the surface the city demands, and the truth it suppresses.

## Story and Act Structure

The narrative unfolds across a prologue and five acts, following Reiji and Ren from a chance encounter to a defining moment of choice.

### Prologue: Surface of Tokyo

The city introduces itself through propaganda — billboards promising optimized happiness, news tickers celebrating productivity, corporate announcements welcoming compliant citizens. Reiji rides the train home, pressing "Approve" on deployment reports without reading them, his wristband logging moderate wellness risk. He witnesses security officers surround a shoeless man on a service platform, then watches the train carry him past before he can see what happens.

### Act I: Neon Pub

Reiji follows a system wellness recommendation to a corporate bar where workers perform relaxation with the same efficiency they bring to their desks. A drink choice (Neon Classic / Calm Static / Just Water) shapes his initial characterization. Stepping into the alley for air, he encounters **Ren** — a drifter picking through discarded electronics. Their first exchange is interrupted by a security drone demanding identity verification. Reiji lies to the drone, claiming Ren is a temporary disposal contractor. The lie works. Something shifts.

### Act II: Subway Checkpoint

Reiji discovers his corporate badge is missing. Ren has it — turning it over like a curiosity, like a key he hasn't decided whether to use. Three security officers sweep the platform. A checkpoint display warns that unregistered individuals must report to processing. This is the story's **first major branch point**:

- **Help him through** — Reiji sponsors Ren through the checkpoint as a registered guest
- **Demand the truth first** — Reiji asks why Ren took the badge, then sponsors him anyway
- **Walk away, then turn back** — Reiji's corporate mask takes over, but he stops himself and returns

Regardless of the branch, Reiji signs a **Host Liability Agreement** — assuming full legal responsibility for Ren within all yellow-zone sectors for 24 hours. This agreement later becomes the mechanism through which the system tracks Ren's movements.

### Act III: Apartment Conversation

In Reiji's 34th-floor corporate unit, the two men slowly lower their defenses. Ren fixes Reiji's broken holo-koi projector — a gift from Reiji's late mother, flickering for two years, ignored like everything else that felt too heavy to fix. The koi begins swimming smoothly. The metaphor is deliberate.

The conversation explores four topics through randomized dialogue pools:
- **Work** — corporate routine vs. survival labor
- **Identity** — what a badge proves vs. what a face can't
- **Sleep** — climate-controlled insomnia vs. cold concrete and security sweeps
- **The window that doesn't open** — centralized climate regulation as a metaphor for controlled existence

A timer counts down: 21 hours of guest access remaining. Reiji offers Ren the floor for the night. Neither sleeps. Neither is entirely alone.

### Act IV: One Month Montage

Rapid scene-switching contrasts Reiji's corporate routine against Ren's lower-market survival. The guest pass expired twenty-nine days ago. Ren is invisible again.

The act's turning point comes when Reiji, running a routine security audit, discovers the system has been tracking Ren's movements — and correlated them with **seventeen other unregistered individuals**, building a network map of invisible people by tracing the spaces they leave behind. His one act of kindness was converted into a surveillance node.

Reiji deletes the access log, accepting a permanent mark on his employment record. He walks out of the office before the schedule tells him to — for the first time in six years.

### Act V: Rainy Riverbank

Ren sends a message from an unknown number: *"come to the river. i need someone who sees me."*

Reiji finds him standing on the wrong side of a guardrail, toes touching the edge where concrete drops into black water. During their conversation, Reiji's wristband delivers a system interrupt — the deleted access log has been regenerated from backup. Three options appear. He selects Option 3: permanently delete all data, accepting the consequences.

The **final choice** determines which of three endings plays:

| Choice | Ending | Tone |
|--------|--------|------|
| "Come back with me." | **Quiet Survival** | Two people learn to exist together. Not a rescue. Something quieter. The koi keeps swimming. |
| "I'm sorry." | **Reflection** | They part at the intersection between towers and lower districts. Both carry each other in ways neither fully understands. |
| Say nothing. | **The City Continues** | Silence stretches too long. Ren walks away. The headlines keep cycling. No anomalies detected. |

## Character Design

### Morikawa Reiji — The Corporate Engineer

Reiji has spent six years pressing the same three buttons: Approve. Confirm. Acknowledge. His company badge proves he exists. His wristband tracks his sleep cycles, his heart rate, his emotional variance. The system knows his employment status. It does not know him.

- **Personality**: Introverted, technical, emotionally restrained. Masks fatigue behind rational language — describes loneliness as "a suboptimal emotional configuration" and social exposure as something that "improves emotional variance by twelve percent."
- **Internal voice**: Clinical self-diagnosis that reveals more than it conceals. Files feelings away like completed reports. Has not made a genuine decision in six years.
- **Arc**: From compliance to choice. Learns that caring about another person is an exploit the system can weaponize — and does it anyway.

### Ren — The Drifter

Ren has never been on a list. No ID. No record. No debt. No credit. He exists wherever he's standing — and when he moves, he stops existing there too. His ID is his face and his voice. If security doesn't like either, he runs.

- **Personality**: Extroverted, energetic, socially adaptive. Uses humor as both weapon and shield — always opens with a joke because "if they laugh, you're a person. If they don't, you're a problem."
- **Internal voice**: Survival calculus masked as performance. Constantly reading threats, exits, whether someone is about to become dangerous. Has normalized the edge — made standing on the wrong side of guardrails a landmark, a reference point.
- **Arc**: From performance to presence. Learns that someone turning back, someone showing up, someone choosing him over the system — might be real. Has never received a genuine apology before. Doesn't know what to do with one.

### Supporting Cast

| Character | Role | Narrative Function |
|-----------|------|-------------------|
| **SYSTEM** | Automated corporate interface | The voice of optimization — logs everything, recommends nothing that matters |
| **NEWS** | State propaganda broadcasts | Cycles sanitized headlines ("Unauthorized Population Reduced") — the city's official story |
| **ADVERTISEMENT** | Corporate billboard copy | Promises comfort, health, memory, desire, sleep — products the city sells but cannot deliver |
| **ANNOUNCEMENT** | Transit station announcements | Reminds citizens to keep badges visible, to stay within yellow zones |
| **HEADSET** | Micro-recovery headset voice | Whispers into sleeping workers' ears: "Thank you for your contribution" |
| **DRONE** | Security drone vocal output | Scans. Verifies. Logs. Reports unregistered bodies for dispatch |
| **BARTENDER** | Neon Pub server | Chrome jaw implant. Slides toward customers without appearing to move |
| **COWORKER** | Reiji's office colleague | Speaks in corporate fragments — meetings, patches, scores — never connects |
| **SUPERVISOR** | Reiji's corporate superior | Embodies the compliance structure Reiji is quietly breaking from |
| **MARKET AUNTIE** | Lower market stall vendor | Has seen every drifter who thought a smile was currency |
| **CHECKPOINT DISPLAY** | Automated checkpoint scanner | Gatekeeper between registered and unregistered existence |

## Key Features

### Emotional Tracking System

Six hidden variables form the game's emotional backbone, tracked across every choice and influencing dialogue variants, internal thought pools, ending tone, and visual effects:

| Variable | Tracks | Effect |
|----------|--------|--------|
| `trust` | Intimacy and honesty between Reiji and Ren | Influences vulnerability of dialogue, determines ending availability |
| `masking` | Reiji's reliance on rationalization to hide exhaustion | Shapes Reiji's internal monologue patterns |
| `noise` | Environmental pressure — surveillance, fatigue, systemic friction | Triggers visual glitch overlay at ≥3, influences ending tone |
| `projection` | Mutual misconceptions of each other's status | Affects whether characters see each other as people or symbols |
| `liability` | Ren's exposure risk to corporate security | Escalates narrative tension in Acts II–V |

These variables are never shown to the player. They operate beneath the surface — a design choice that mirrors the game's theme.

### Dialogue Variation Pools

Key narrative beats draw from randomized pools (6+ variants each) to increase replay value while preserving narrative coherence:

- **Ren's defensive jokes** at the checkpoint — sharp humor masking fear
- **Reiji's internal deflections** — technical language rationalizing emotional states
- **Apartment conversation responses** — randomized pairs for work, identity, and sleep topics
- **News ticker messages** — propaganda headlines that cycle throughout

### Persistent News Ticker

A scrolling overlay continuously runs state propaganda headlines across the bottom of the screen: *"Tokyo Corridor Productivity Reaches New High. Public Satisfaction Remains Stable. Unauthorized Population Reduced."* The ticker is registered as a persistent overlay screen — it runs automatically, no manual show/hide needed, and its presence throughout the game reinforces the gap between the city's official story and the reality the player is experiencing.

### Character Positioning System

Characters are precisely positioned using sprite transforms to reinforce the split-screen dialogue mechanic:

- **Left-aligned sprites** (`sprite_left`, `sprite_left_a`, `sprite_left_b`): Frame Reiji against the cyan spoken-dialogue card
- **Right-aligned sprites** (`sprite_right`): Frame Ren against the magenta internal-thought card
- **Dynamic repositioning**: Characters shift between transforms during key emotional beats — Ren moves from `sprite_right` to `sprite_left` during the apartment scene when his defenses lower
- **Props and overlays**: Badge, drone, and police sprites appear contextually with their own position transforms

### Music and Audio Design

Two original music tracks serve distinct narrative functions:

- **`background.mp3`** — Plays during the Prologue (train ride through Tokyo), establishing the city's ambient mood. Fades out during Act III when the apartment conversation begins — the silence amplifying the intimacy.
- **`theme.mp3`** — Plays during Act V (riverbank), marking the emotional climax. Fades in at higher volume (0.8), signaling that this scene is different from everything before it.

The strategic use of silence during the apartment conversation (Act III) is a deliberate design choice — Ren comments on the quiet, and the player experiences it with him.

### Multiple Endings

Three distinct endings are determined by the player's final choice at the riverbank, shaped by every variable accumulated across the narrative:

1. **Quiet Survival** — High trust. Two people learn to exist together in a room too small for the system to care about.
2. **Reflection** — Mixed. They part carrying each other in ways neither fully understands. Not happy. Honest.
3. **The City Continues** — High noise, low trust. Silence wins. The headlines keep cycling. No anomalies detected.

### World-Building Through System Voices

Rather than relying on narrator exposition, the game builds its world through five distinct "system" character voices — each representing a different layer of the city's institutional surface. Corporate announcements, news propaganda, advertisements, and transit warnings interweave to create a world where the city is always speaking, always measuring, always selling — and never listening.

## How to Play

1. Download and install the application [here](https://drive.google.com/drive/folders/1sgDBV73fYzE96zzLbnizfG47LgLW-w_s?usp=sharing)
2. Unzip and run the application. **Enjoy!**

## Technical Architecture

```
game/
├── script.rpy                 # Master narrative engine — 1,868 lines, all acts, scenes, branches, endings
├── screens.rpy                # Custom UI — dual_dialogue screen, news_ticker overlay, noise_glitch, dual_line()
├── characters.rpy             # 12 character definitions + sprite transforms + image declarations
├── dialogue_variants.rpy      # 10+ randomized dialogue pools (6 variants each) + ticker messages
├── variables.rpy              # Emotional tracking system — 6 hidden variables + ending flags
├── gui.rpy                    # GUI configuration — 1920×1080, cyberpunk color palette
├── options.rpy                # Engine configuration
├── images/                    # Hand-crafted backgrounds and character portraits
└── audio/                     # background.mp3, theme.mp3
```

### Key Technical Implementations

**`dual_line(speaker, spoken, thought)`** — Python function in `screens.rpy` that calls the `dual_dialogue` screen as a modal overlay. The screen renders side-by-side frames: cyan-tinted spoken dialogue on the left, magenta-tinted internal thought on the right. Dismissed with a single click. This function is called inline from script blocks throughout the entire narrative.

**`news_ticker()`** — Persistent overlay screen registered in `config.overlay_screens`. Joins `ticker_messages` with pipe separators and scrolls them horizontally using a `scrolling_ticker` transform (40-second linear animation, repeating). Zero manual show/hide management.

**`noise_glitch()`** — Conditional overlay that renders randomized pixel artifacts when `noise >= 3`. Direct visual feedback from the emotional tracking system.

**Sprite transforms** — Seven positioning transforms (`sprite_left`, `sprite_left_a`, `sprite_left_b`, `sprite_right`, `bg_fill`, `badge_pos`, `drone_pos`) enable precise character and prop placement supporting the split-screen layout.

## Credits

Built with [Ren'Py](https://www.renpy.org/).

## Influences

*Taxi Driver*, *The Batman*, *Joker*, Radiohead, Nirvana

---

<p align="center">
  <em>Hackathon 2026</em>
</p>
