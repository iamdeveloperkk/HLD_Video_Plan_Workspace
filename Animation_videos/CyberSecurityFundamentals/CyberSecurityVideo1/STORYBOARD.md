# STORYBOARD.md

# Cyber Attack X FAANG — Video 01

## What Happens When Big Tech Gets Security Wrong?

**Series:** Cyber Attack X FAANG
**Episode:** 01
**Format:** Cinematic Technical Explainer
**Visual Style:** Dark cinematic cyber-tech / Big-Tech infrastructure
**Narration:** Creator voice
**Status:** Scene Storyboard — Ready for Visual Asset Generation

---

# 1. Storyboard Objective

This storyboard defines exactly what the viewer should see throughout the video.

The video should **not feel like a cybersecurity lecture**.

The story should unfold visually as an investigation:

```text
Something Goes Wrong
        ↓
How Big Is This System?
        ↓
What Are We Protecting?
        ↓
Confidentiality
        ↓
Integrity
        ↓
Availability
        ↓
Who Is Doing This?
        ↓
How Did They Reach Us?
        ↓
Where Is The Weakness?
        ↓
How Did It Become An Attack?
        ↓
What Is The Impact?
        ↓
How Much Risk?
        ↓
How Does Big Tech Defend Itself?
```

---

# 2. Global Visual Rules

## Color Language

Primary environment:

* Dark blue / black
* Cool blue system UI
* White technical labels
* Red for malicious traffic / failures / alerts
* Green for healthy systems
* Amber for warning states

Red should be reserved primarily for:

* Attack traffic
* Critical failures
* Security alerts
* Compromised components
* High-risk states

---

## Animation Language

Prefer:

* Moving request particles
* Flowing network traffic
* Camera pushes
* Camera pulls
* Architecture reveals
* Graph animation
* Data movement
* System state changes
* UI updates
* Zooming into technical components

Avoid:

* Static diagrams for long periods
* Excessive text
* PowerPoint-style transitions
* Random futuristic decoration
* Unnecessary code screens

---

## Technical Visual Principle

Whenever possible:

> **Show the system behaving rather than showing a definition.**

Example:

Instead of displaying:

```text
Availability = System remains accessible
```

show:

```text
1K requests/sec
       ↓
100K
       ↓
1M
       ↓
Queue grows
       ↓
Latency increases
       ↓
Requests fail
       ↓
SERVICE UNAVAILABLE
```

The creator's narration explains what the viewer is seeing.

---

# 3. Scene Overview

| Scene | Title                           | Primary Purpose             |
| ----- | ------------------------------- | --------------------------- |
| 01    | The Night Something Goes Wrong  | Hook                        |
| 02    | The Big-Tech Architecture       | Establish scale             |
| 03    | What Are We Protecting?         | Introduce CIA               |
| 04    | Confidentiality Breach          | Demonstrate confidentiality |
| 05    | Integrity Breach                | Demonstrate integrity       |
| 06    | Availability Attack             | Demonstrate availability    |
| 07    | Who Is Doing This?              | Introduce threat            |
| 08    | How Do They Get In?             | Introduce threat vector     |
| 09    | Finding the Weakness            | Introduce vulnerability     |
| 10    | Vulnerability Becomes an Attack | Introduce attack            |
| 11    | So How Bad Is It?               | Impact + risk               |
| 12    | Big-Tech Security Is Layers     | Defense                     |
| 13    | The Investigation Continues     | Series hook                 |

---

# SCENE 01 — THE NIGHT SOMETHING GOES WRONG

**Purpose:** Hook the viewer with a mysterious production incident.

**Estimated duration:** 25–35 seconds

---

## Shot 01 — NEXA Headquarters

**Visual**

Nighttime exterior of fictional Big-Tech company **NEXA**.

Large modern technology campus.

Most offices are dark.

A few floors remain illuminated.

**Camera**

Slow cinematic dolly toward the building.

**Animation**

* City lights subtly move.
* A few windows flicker.
* Cars move in the distance.
* Light rain / atmospheric particles optional.

**On-screen text**

```text
02:13 AM
```

**Audio**

Low ambient hum.

Very subtle tension begins.

---

## Shot 02 — Time Reveal

**Visual**

Digital clock:

```text
02:13:07 AM
```

**Camera**

Slow push toward the clock.

**Animation**

Seconds tick forward.

**Transition**

Hard cut into the operations center.

---

## Shot 03 — Global Operations Center

**Visual**

Large NEXA operations center.

Multiple engineers.

Wall-sized global map.

Multiple monitoring screens.

**Camera**

Slow horizontal pan across the room.

**Animation**

* Screens update.
* World map pulses.
* Engineers interact with dashboards.
* Data moves across screens.

**Narration role**

Establish that this is a massive global system operating continuously.

---

## Shot 04 — Everything Looks Normal

Close-up of monitoring dashboard.

```text
API REQUESTS      120K / sec
LATENCY           31 ms
ERROR RATE        0.08%
DB CPU             61%
```

Graph is stable.

Green/healthy indicators.

**Camera**

Slow push toward metrics.

---

## Shot 05 — Traffic Spike

API request graph begins climbing.

```text
120K → 180K → 340K / sec
```

**Animation**

* Request particles increase.
* Graph begins rising.
* Dashboard updates in real time.

**Camera**

Move closer to graph.

---

## Shot 06 — Rapid Escalation

Metrics accelerate.

```text
API REQUESTS      890K / sec
LATENCY           1.2 sec
ERROR RATE        47.3%
DB CPU             96%
```

**Animation**

* Graph rapidly climbs.
* Request particles flood the screen.
* Warning indicators appear.
* Screens begin flashing.

**Camera**

Fast push toward dashboard.

---

## Shot 07 — Production Alert

Full-screen alert:

```text
⚠ PRODUCTION ALERT

SERVICE DEGRADATION
DETECTED
```

**Animation**

* Red alert pulse.
* UI flicker.
* Screen shake very subtly.

**Audio**

Sharp alert sound.

---

## Shot 08 — Pull Back

Camera rapidly pulls away from dashboard.

The dashboard becomes one component inside a huge distributed architecture.

Red traffic enters the system.

---

## Shot 09 — Global Impact

Show Earth at night.

Millions of connection lines.

Red traffic begins spreading across regions.

**On-screen text**

```text
Millions of users.
One platform.
Everything connected.
```

---

## Shot 10 — Engineer Reaction

Close-up behind an engineer.

Monitor reflection visible.

Screen:

```text
Something's wrong...
```

Engineer pauses.

---

## Shot 11 — End Beat

Black screen.

Text appears slowly:

```text
At 2:13 AM,

something started attacking
the system.
```

**Transition**

Cut directly into Scene 02.

---

# SCENE 02 — THE BIG-TECH ARCHITECTURE

**Purpose:** Make the viewer understand the scale of the system.

**Estimated duration:** 30–45 seconds

---

## Shot 01 — Zoom Out From NEXA

Start with one server.

Camera pulls backward.

Reveal:

```text
Server
 ↓
Cluster
 ↓
Service
 ↓
Region
 ↓
Global System
```

---

## Shot 02 — User Traffic

Show thousands of users connecting.

Request particles travel toward the platform.

```text
USERS
 ↓
INTERNET
```

---

## Shot 03 — Edge Layer

Reveal:

```text
CDN
 ↓
WAF
 ↓
API GATEWAY
```

Traffic passes through each layer.

---

## Shot 04 — Services

Camera follows a request into:

```text
SERVICE A
SERVICE B
SERVICE C
SERVICE D
```

Requests branch into different paths.

---

## Shot 05 — Data Layer

Zoom into:

```text
DATABASE
CACHE
OBJECT STORAGE
```

Show data moving between components.

---

## Shot 06 — Full Architecture

Pull back and reveal the complete system:

```text
Users
 ↓
CDN
 ↓
WAF
 ↓
API Gateway
 ↓
Services
 ↓
Data Layer
```

**Narration role**

Explain that security at this scale means protecting an interconnected ecosystem rather than a single server.

---

# SCENE 03 — WHAT ARE WE PROTECTING?

**Purpose:** Introduce the CIA Triad.

**Estimated duration:** 30–40 seconds

---

## Shot 01 — Data Zoom

Camera enters the data layer.

Show:

* Customer profiles
* Orders
* Payments
* Messages
* Credentials
* Internal data

---

## Shot 02 — Three Dimensions

Three large visual pillars appear:

```text
CONFIDENTIALITY
INTEGRITY
AVAILABILITY
```

---

## Shot 03 — Confidentiality

Data is inside a secure container.

Unauthorized user approaches.

Access denied.

---

## Shot 04 — Integrity

Show transaction:

```text
₹1,000
```

Then malicious modification:

```text
₹100,000
```

---

## Shot 05 — Availability

Show healthy service.

Then request volume increases.

Service begins struggling.

---

## Shot 06 — CIA Together

Three dimensions appear around the system:

```text
        CONFIDENTIALITY
              |
              |
INTEGRITY — SYSTEM — AVAILABILITY
```

**Narration role**

Explain that security is not only about preventing data leaks.

---

# SCENE 04 — CONFIDENTIALITY BREACH

**Purpose:** Make confidentiality concrete through an API incident.

**Estimated duration:** 30–40 seconds

---

## Shot 01 — User A

Show authenticated User A.

```text
USER A
```

User requests:

```text
GET /api/orders
```

---

## Shot 02 — API Flow

```text
USER A
 ↓
API
 ↓
ORDER SERVICE
 ↓
DATABASE
```

---

## Shot 03 — Unexpected Response

API response contains another user's information.

```text
USER B
NAME
EMAIL
ORDERS
```

---

## Shot 04 — Highlight

Red warning:

```text
UNAUTHORIZED DATA
```

---

## Shot 05 — Zoom Into Authorization

Show:

```text
Authentication
     ↓
"Who are you?"

Authorization
     ↓
"Are you allowed?"
```

Highlight missing/incorrect authorization.

---

## Shot 06 — Confidentiality Reveal

Data becomes locked again.

Text:

```text
CONFIDENTIALITY
```

**Narration role**

Explain confidentiality using the incident rather than a dictionary definition.

---

# SCENE 05 — INTEGRITY BREACH

**Purpose:** Demonstrate unauthorized modification.

**Estimated duration:** 30–40 seconds

---

## Shot 01 — Original Order

Customer places order.

```text
ORDER
₹1,000
```

---

## Shot 02 — Normal Request

```text
CLIENT
 ↓
API
 ↓
PAYMENT SERVICE
 ↓
DATABASE
```

---

## Shot 03 — Manipulated Request

Request changes:

```text
amount=1000
```

to:

```text
amount=100000
```

---

## Shot 04 — Database State

Database updates unexpectedly.

---

## Shot 05 — Processed Order

Show:

```text
ORIGINAL
₹1,000

PROCESSED
₹100,000
```

---

## Shot 06 — Integrity Reveal

Red system-state mutation.

Text:

```text
INTEGRITY COMPROMISED
```

**Narration role**

Explain that integrity means preventing unauthorized changes to data/system state.

---

# SCENE 06 — AVAILABILITY ATTACK

**Purpose:** Demonstrate resource exhaustion and availability failure.

**Estimated duration:** 35–45 seconds

---

## Shot 01 — Healthy API

```text
REQUESTS       1K/sec
LATENCY        30 ms
ERROR RATE     0%
```

Everything healthy.

---

## Shot 02 — Incoming Traffic

Multiple request particles enter.

Then hundreds.

Then thousands.

---

## Shot 03 — Traffic Flood

```text
1K → 100K → 1M requests/sec
```

**Animation**

Request particles visually flood the API.

---

## Shot 04 — Resource Exhaustion

Show:

```text
CPU
████████████ 96%

QUEUE
████████████ 99%
```

---

## Shot 05 — Latency

```text
30 ms
 ↓
800 ms
 ↓
5 sec
```

---

## Shot 06 — Failure

```text
SERVICE UNAVAILABLE
```

Requests bounce/fail.

---

## Shot 07 — Availability Reveal

The system becomes inaccessible.

Text:

```text
AVAILABILITY
COMPROMISED
```

**Narration role**

Explain why a system can be secure from a data-access perspective and still fail because users cannot access it.

---

# SCENE 07 — WHO IS DOING THIS?

**Purpose:** Introduce the concept of a threat.

**Estimated duration:** 25–35 seconds

---

## Shot 01 — Pull Away From System

Camera leaves the architecture.

System becomes small.

---

## Shot 02 — Unknown Actor

Dark silhouette appears outside the system.

Do not reveal identity.

---

## Shot 03 — Possible Sources

Briefly show silhouettes/icons:

```text
HACKER
BOTNET
INSIDER
COMPROMISED ACCOUNT
OTHER ACTOR
```

Avoid assigning a specific identity.

---

## Shot 04 — Threat Reveal

Question:

```text
WHO COULD CAUSE HARM?
```

Then:

```text
THREAT
```

---

## Shot 05 — Distinction

Visual:

```text
THREAT ≠ ATTACK
```

Threat represents a potential source of harm.

---

# SCENE 08 — HOW DO THEY GET IN?

**Purpose:** Introduce threat vector.

**Estimated duration:** 30–40 seconds

---

## Shot 01 — Multiple Entry Points

Show system with several possible routes:

```text
WEB APP
API
MOBILE APP
EMPLOYEE DEVICE
THIRD PARTY
```

---

## Shot 02 — Highlight API

One path becomes highlighted.

Red traffic travels toward the API.

---

## Shot 03 — Different Paths

Briefly show multiple possible vectors.

```text
Web
API
Device
Network
Credentials
Third Party
```

---

## Shot 04 — Threat Vector Reveal

Highlighted path becomes:

```text
THREAT VECTOR
```

---

## Shot 05 — Route Visualization

Show:

```text
ATTACKER
   ↓
ENTRY POINT
   ↓
SYSTEM
```

**Narration role**

Explain that a threat needs a way to reach the system.

---

# SCENE 09 — FINDING THE WEAKNESS

**Purpose:** Introduce vulnerability.

**Estimated duration:** 30–40 seconds

---

## Shot 01 — Zoom Into API

Camera follows the malicious path into the application.

---

## Shot 02 — Application Logic

Show:

```text
INPUT
 ↓
APPLICATION
 ↓
DATABASE
```

---

## Shot 03 — Untrusted Input

Highlight:

```text
UNTRUSTED INPUT
```

---

## Shot 04 — Missing Protection

Application accepts unexpected input.

Show a gap in the defensive layer.

---

## Shot 05 — Database Connection

Malicious input reaches the database layer.

---

## Shot 06 — Vulnerability Reveal

Camera freezes on the weak component.

Text:

```text
VULNERABILITY
```

Then:

```text
A weakness that can be exploited.
```

Keep definition brief.

---

# SCENE 10 — VULNERABILITY BECOMES AN ATTACK

**Purpose:** Connect vulnerability to actual malicious action.

**Estimated duration:** 30–45 seconds

---

## Shot 01 — Attacker Request

Show:

```text
ATTACKER
 ↓
MALICIOUS REQUEST
```

---

## Shot 02 — Request Enters System

```text
ATTACKER
 ↓
API
 ↓
APPLICATION
```

---

## Shot 03 — Vulnerable Component

Request reaches the weakness identified in Scene 09.

---

## Shot 04 — Exploitation

System accepts malicious input.

Visual state changes:

```text
HEALTHY
 ↓
COMPROMISED
```

---

## Shot 05 — Impact Begins

Show possible consequences:

```text
DATA EXPOSURE
DATA MODIFICATION
SERVICE OUTAGE
```

Do not deeply explain specific attack techniques.

---

## Shot 06 — Attack Reveal

Text:

```text
VULNERABILITY
       +
MALICIOUS ACTION
       =
ATTACK
```

---

# SCENE 11 — SO HOW BAD IS IT?

**Purpose:** Introduce impact and risk.

**Estimated duration:** 35–45 seconds

---

## Shot 01 — Complete Chain

Show the complete relationship:

```text
THREAT
   ↓
THREAT VECTOR
   ↓
VULNERABILITY
   ↓
ATTACK
   ↓
IMPACT
```

---

## Shot 02 — Low Impact Example

Show internal low-value service.

```text
LIMITED EXPOSURE
LOW IMPACT
```

---

## Shot 03 — High Impact Example

Transition to payment service.

```text
PAYMENT SYSTEM
MILLIONS OF USERS
```

---

## Shot 04 — High Consequence

Show:

```text
DATA LOSS
FINANCIAL LOSS
SERVICE DISRUPTION
ACCOUNT COMPROMISE
```

---

## Shot 05 — Risk

Visual formula:

```text
RISK ≈ LIKELIHOOD × IMPACT
```

---

## Shot 06 — Risk Comparison

Side-by-side:

```text
Internal Tool
Low Impact
LOWER RISK
```

versus:

```text
Internet-Facing Payment Service
High Impact
HIGHER RISK
```

**Narration role**

Explain why security teams prioritize vulnerabilities based on context and potential impact.

---

# SCENE 12 — BIG-TECH SECURITY IS LAYERS

**Purpose:** Reveal the defense strategy.

**Estimated duration:** 45–60 seconds

---

## Shot 01 — Start With Internet

```text
INTERNET
```

Millions of requests approach.

---

## Shot 02 — CDN

Requests pass through:

```text
CDN
```

---

## Shot 03 — WAF

Then:

```text
WAF
```

Malicious-looking traffic begins getting filtered.

---

## Shot 04 — API Gateway

```text
API GATEWAY
```

Traffic is controlled and routed.

---

## Shot 05 — Authentication

```text
AUTHENTICATION
```

Question:

```text
WHO ARE YOU?
```

---

## Shot 06 — Authorization

```text
AUTHORIZATION
```

Question:

```text
ARE YOU ALLOWED?
```

---

## Shot 07 — Rate Limiting

Request flood begins.

Rate limiter absorbs/rejects excess traffic.

---

## Shot 08 — Services

Legitimate requests continue into services.

---

## Shot 09 — Data Protection

Show:

```text
ENCRYPTION
DATABASE CONTROLS
ACCESS CONTROL
```

---

## Shot 10 — Audit & Monitoring

Show:

```text
AUDIT LOGS
MONITORING
THREAT DETECTION
ALERTING
```

---

## Shot 11 — Complete Defense Stack

Camera pulls back.

Full layered architecture:

```text
Internet
   ↓
CDN
   ↓
WAF
   ↓
API Gateway
   ↓
Authentication
   ↓
Authorization
   ↓
Rate Limiting
   ↓
Services
   ↓
Databases
   ↓
Encryption
   ↓
Audit Logs
   ↓
Monitoring
   ↓
Threat Detection
```

---

## Shot 12 — Final Defense Reveal

All layers light up.

Legitimate traffic remains green.

Malicious traffic gets blocked/redirection.

**On-screen text**

```text
SECURITY IS A SYSTEM.
```

---

# SCENE 13 — THE INVESTIGATION CONTINUES

**Purpose:** Transition into future attack episodes.

**Estimated duration:** 20–30 seconds

---

## Shot 01 — Dark Screen

Silence.

One red cursor blinks.

---

## Shot 02 — Attack Names

Rapid flashes:

```text
SQL INJECTION
```

```text
XSS
```

```text
CSRF
```

```text
DDoS
```

```text
CREDENTIAL ATTACKS
```

```text
MITM
```

```text
MALWARE
```

Each appears for a short duration.

---

## Shot 03 — Attack Visual Montage

Very quick technical visual references:

* SQL query manipulation
* Browser executing malicious script
* Forged request
* Traffic flood
* Credential attempts
* Intercepted connection
* Malicious software spreading

Do not explain them yet.

---

## Shot 04 — Series Identity

Large title:

```text
CYBER ATTACK X FAANG
```

Subtitle:

```text
REAL ATTACKS.
REAL SYSTEMS.
REAL LESSONS.
```

---

## Shot 05 — Next Episode

Final card:

```text
NEXT

How Can Attackers
Break a System This Big?
```

Then:

```text
SQL Injection
XSS
CSRF
DDoS
...
```

---

# 4. Full Visual Flow

The entire episode should visually evolve like this:

```text
                    INCIDENT
                       ↓
               BIG-TECH SYSTEM
                       ↓
                PROTECTED DATA
                       ↓
       ┌───────────────┼───────────────┐
       ↓               ↓               ↓
CONFIDENTIALITY    INTEGRITY      AVAILABILITY
       └───────────────┼───────────────┘
                       ↓
                     THREAT
                       ↓
                THREAT VECTOR
                       ↓
                 VULNERABILITY
                       ↓
                     ATTACK
                       ↓
                    IMPACT
                       ↓
                     RISK
                       ↓
              DEFENSE IN DEPTH
                       ↓
                NEXT INVESTIGATION
```

---

# 5. Animation Generation Strategy

Do not attempt to generate the entire episode as one AI-generated video.

Each scene should be built from multiple short shots.

Recommended structure:

```text
13 Scenes
   ↓
~50–60 individual shots
   ↓
Generate visual/keyframe assets
   ↓
Animate individual shots
   ↓
Edit shots together
   ↓
Creator narration
   ↓
Sound design
   ↓
Final video
```

---

# 6. Shot Generation Rules

For each generated shot:

### Keep

* Same NEXA visual identity
* Same architecture style
* Same UI language
* Same lighting language
* Same technical terminology
* Same visual continuity

### Avoid

* Random new company designs
* Different architectural styles between shots
* Excessive text
* AI-generated unreadable code
* Unnecessary characters
* Generic "hacker movie" clichés

---

# 7. Narration Alignment

Narration is intentionally **not included in this storyboard**.

The creator will narrate after visual shots are finalized.

The narration should follow:

```text
WHAT VIEWER SEES
       ↓
WHAT IT MEANS
       ↓
WHY IT MATTERS
       ↓
TECHNICAL EXAMPLE
       ↓
NEXT VISUAL REVEAL
```

This allows the voiceover to feel naturally synchronized with the animation.

---

# 8. Scene Transition Philosophy

Transitions should tell the story.

Examples:

### Scene 01 → Scene 02

Dashboard zooms out into the architecture.

### Scene 02 → Scene 03

Camera enters the database/data layer.

### Scene 03 → Scene 04

CIA triad zooms into Confidentiality.

### Scene 04 → Scene 05

Data protection transitions into transaction state.

### Scene 05 → Scene 06

Transaction system transitions into resource/traffic system.

### Scene 06 → Scene 07

Camera pulls outside the system to reveal the unknown actor.

### Scene 07 → Scene 08

Unknown actor's path becomes highlighted.

### Scene 08 → Scene 09

Camera follows the path into the vulnerable component.

### Scene 09 → Scene 10

Weakness is exploited.

### Scene 10 → Scene 11

Attack expands into consequences.

### Scene 11 → Scene 12

Risk visualization transforms into defensive layers.

### Scene 12 → Scene 13

Defenses fade into darkness and attack names appear.

---

# 9. Visual Continuity Checklist

Before finalizing any scene, verify:

* [ ] NEXA identity is consistent
* [ ] Architecture remains logically consistent
* [ ] Request flow direction is understandable
* [ ] Healthy vs malicious traffic is visually distinguishable
* [ ] Camera movement has a purpose
* [ ] On-screen text is minimal
* [ ] Technical labels are readable
* [ ] No real company is falsely portrayed as suffering the fictional incident
* [ ] Attack concepts are not prematurely explained
* [ ] Scene connects naturally to the next scene

---

# 10. Current Production Status

```text
BLUEPRINT.md       ✅
STORYBOARD.md      ✅
SCENE DEFINITIONS  ⏳
VISUAL ASSETS      ⏳
ANIMATION          ⏳
NARRATION
```
