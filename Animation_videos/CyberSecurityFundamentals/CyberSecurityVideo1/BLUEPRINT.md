# Video Blueprint — Cyber Attack X FAANG

## Video 01

**Working Title:** What Happens When Big Tech Gets Security Wrong?
**Series:** Cyber Attack X FAANG
**Video Type:** Cybersecurity Fundamentals / Cinematic Technical Story
**Status:** Blueprint Draft — Ready for Scene Definition

---

## 1. Video Objective

Introduce the fundamentals of cybersecurity through a **fictional Big-Tech security incident** rather than through dictionary-style definitions.

The viewer should understand:

* Why security becomes critical at Big-Tech scale.
* What the CIA Triad means in practical engineering terms.
* The difference between:

  * Threat
  * Threat Vector
  * Vulnerability
  * Attack
  * Impact
  * Risk
* How these concepts connect together during a real security incident.
* Why security is not a single feature but a **layered system of defenses**.

The video should feel like a **security investigation** unfolding inside a massive technology company.

---

## 2. Core Story Idea

A fictional Big-Tech company experiences a mysterious production incident in the middle of the night.

At first, engineers only see symptoms:

* Traffic suddenly increases.
* Latency starts rising.
* Database CPU approaches critical levels.
* Some requests appear abnormal.
* Users begin experiencing failures.

The investigation gradually moves backward:

**Impact → Attack → Vulnerability → Threat Vector → Threat**

While investigating, the video introduces the CIA Triad:

**Confidentiality → Integrity → Availability**

The viewer eventually understands that security is about protecting the system across all three dimensions.

The final reveal:

> Big-Tech security is not one firewall or one authentication mechanism.
> It is a layered system designed to prevent, detect, contain and recover from attacks.

---

## 3. Viewer Promise

By the end of the video, the viewer should be able to look at a security incident and ask:

> **What are we protecting?**
> **Who could harm it?**
> **How could they reach it?**
> **What weakness could they exploit?**
> **What did they actually do?**
> **What was the impact?**
> **How much risk does that create?**

This framework becomes the foundation for the rest of the series.

---

## 4. Target Audience

Primary:

* Software engineers
* Backend engineers
* SDEs preparing for interviews
* System-design learners
* Developers interested in cybersecurity
* Engineers curious about how FAANG-scale systems think about security

Secondary:

* CS students
* Engineering aspirants
* Tech enthusiasts

The explanation should remain understandable to someone who knows basic software architecture, while still containing enough technical detail to interest experienced engineers.

---

## 5. Storytelling Style

### Primary Style

**Cinematic + Technical + Investigative**

The video should feel closer to a technology thriller than a cybersecurity lecture.

Avoid:

* Long dictionary definitions
* Static PowerPoint-style slides
* Listing security terms one after another
* Excessive bullet points
* Classroom-style teaching

Prefer:

* Production dashboards
* Architecture diagrams
* Data/request particles
* Zoom-ins into services
* Animated API requests
* System state changes
* Suspicious traffic
* Database activity
* Security layers
* Visual reveals

---

## 6. Narrative Structure

### Act 1 — Something Is Wrong

Introduce a large-scale production system.

Then suddenly:

**02:13 AM**

Something starts going wrong.

The viewer sees symptoms before being told what caused them.

---

### Act 2 — What Are We Protecting?

Move from the incident into the architecture.

Explain that a Big-Tech system isn't just servers.

It contains:

* Users
* APIs
* Services
* Databases
* Payments
* Identity systems
* Internal infrastructure
* Sensitive information

Then introduce the three things security must protect:

**Confidentiality**

**Integrity**

**Availability**

---

### Act 3 — How Does an Attack Happen?

Move from the protected system to the attacker.

Introduce:

**Threat**

↓

**Threat Vector**

↓

**Vulnerability**

↓

**Attack**

The concepts should emerge naturally as the investigation progresses.

---

### Act 4 — How Bad Is It?

Connect the attack to:

**Impact**

and ultimately:

**Risk**

Show that not every vulnerability represents the same level of risk.

An exposed low-value internal service is different from an internet-facing payment system.

---

### Act 5 — How Big Tech Defends Itself

Reveal the layered security architecture.

Example:

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
Application Services
   ↓
Database
   ↓
Encryption
   ↓
Audit Logs
   ↓
Monitoring / Detection
```

The viewer should understand:

> Security is a system, not a single component.

---

### Act 6 — The Next Investigation

End with a rapid visual preview of actual attacks:

* SQL Injection
* XSS
* CSRF
* DDoS
* Credential Attacks
* MITM
* Malware

Do **not** deeply explain these attacks in Video 1.

They become future episodes of **Cyber Attack X FAANG**.

---

# 7. Core Concepts Covered

## CIA Triad

### Confidentiality

Only authorized people/systems should be able to access information.

Technical examples:

* Unauthorized API response
* Cross-user data exposure
* Database access
* Leaked credentials

---

### Integrity

Data and system state should not be modified improperly.

Technical examples:

* Changing an order
* Modifying payment information
* Altering database records
* Manipulating a request

---

### Availability

Authorized users should be able to access the system when required.

Technical examples:

* Request floods
* Resource exhaustion
* Service overload
* Database saturation
* Infrastructure failure

---

## Threat

A potential source of harm.

The video should distinguish:

**Threat ≠ Attack**

A threat represents the possibility/source of harm.

---

## Threat Vector

The route or mechanism through which a threat can reach the system.

Examples:

* Web application
* API
* Employee device
* Exposed service
* Network connection
* Compromised credential

---

## Vulnerability

A weakness that can be exploited.

Examples:

* Missing authorization check
* Unsafe input handling
* Weak authentication
* Misconfiguration
* Exposed internal service
* Insecure application logic

---

## Attack

The actual malicious action performed against the system.

Conceptually:

```text
Threat
   ↓
Threat Vector
   ↓
Vulnerability
   ↓
Attack
   ↓
Impact
```

---

## Impact

What happens when the attack succeeds.

Possible consequences:

* Data exposure
* Data modification
* Service outage
* Financial loss
* Account compromise
* Operational disruption

---

## Risk

Risk represents the potential business/system consequence of a threat exploiting a vulnerability.

Simple mental model:

```text
Risk ≈ Likelihood × Impact
```

The video should emphasize that security teams prioritize risks rather than treating every weakness as equally dangerous.

---

# 8. Technical Depth

The video should contain real engineering concepts without becoming a deep implementation tutorial.

Technical examples may include:

### Authentication

```text
Client
  ↓
Authentication
  ↓
"Who are you?"
```

### Authorization

```text
Authenticated User
        ↓
Authorization
        ↓
"Are you allowed to do this?"
```

### API Security

```text
Client
  ↓
API Gateway
  ↓
Authentication
  ↓
Authorization
  ↓
Service
  ↓
Database
```

### Request Flow

Use animated requests moving through the architecture to visually demonstrate how an attacker can interact with a system.

---

# 9. Scene-Level Story Direction

The video will eventually be broken into approximately 13 cinematic scenes.

### Scene 01 — The Night Something Goes Wrong

Production alert.

Traffic spikes.

Error rate rises.

Database approaches saturation.

**Purpose:** Hook the viewer.

---

### Scene 02 — The Big-Tech Architecture

Zoom out and reveal the massive distributed system.

**Purpose:** Establish scale.

---

### Scene 03 — What Are We Protecting?

Introduce data and the three security dimensions.

**Purpose:** Set up CIA.

---

### Scene 04 — Confidentiality Breach

One user's request unexpectedly exposes another user's information.

**Purpose:** Demonstrate confidentiality through an incident.

---

### Scene 05 — Integrity Breach

A transaction/order/payment value is manipulated.

**Purpose:** Demonstrate integrity.

---

### Scene 06 — Availability Attack

Traffic overwhelms the system.

**Purpose:** Demonstrate availability.

---

### Scene 07 — Who Is Doing This?

Pull outside the architecture.

An unknown actor is introduced.

**Concept:** Threat.

---

### Scene 08 — How Do They Get In?

Highlight possible entry points.

**Concept:** Threat Vector.

---

### Scene 09 — Finding the Weakness

Zoom into a vulnerable component.

**Concept:** Vulnerability.

---

### Scene 10 — Vulnerability Becomes an Attack

Show a malicious request exploiting the weakness.

**Concept:** Attack.

Specific attacks are intentionally not deeply explained yet.

---

### Scene 11 — So How Bad Is It?

Connect:

```text
Threat
   +
Threat Vector
   +
Vulnerability
   +
Attack
   ↓
Impact
   ↓
Risk
```

**Purpose:** Connect the vocabulary into one framework.

---

### Scene 12 — Big-Tech Security Is Layers

Reveal the layered security architecture.

**Purpose:** Explain why large companies invest heavily in security.

---

### Scene 13 — The Investigation Continues

Rapid visual preview:

```text
SQL Injection
XSS
CSRF
DDoS
Credential Attacks
MITM
Malware
```

End with:

**CYBER ATTACK X FAANG**

Then tease the next investigation.

---

# 10. Visual Direction

## Overall Visual Language

* Dark cinematic environment
* High-tech infrastructure
* Realistic distributed-system visualization
* Glowing request/data particles
* Minimal UI clutter
* Strong contrast
* Smooth camera movement
* Frequent zoom-ins and zoom-outs
* Architecture diagrams integrated into the environment
* Dynamic counters and system metrics
* Suspenseful transitions

---

## Animation Philosophy

Avoid simply showing diagrams.

Instead:

**Make the architecture move.**

For example:

```text
User Request
     ↓
API Gateway
     ↓
Service
     ↓
Database
```

should be represented by an animated request particle physically traveling through the system.

When something goes wrong:

* Traffic particles multiply.
* Queues grow.
* Latency counters increase.
* Services turn unhealthy.
* Database activity accelerates.
* Requests begin failing.

The viewer should understand the system visually before hearing the explanation.

---

# 11. Audio Direction

Narration will be recorded by the creator.

No AI voice should be required.

Audio should contain:

* Creator narration
* Subtle cinematic background music
* Server/terminal ambience
* Alert sounds
* Request/packet-style sound effects
* Low-frequency tension during investigation
* Strong transition sounds for reveals

Narration will be written **after the scene animations/visuals are finalized**, so the explanation can precisely match what is happening on screen.

---

# 12. Important Storytelling Constraint

This is **not**:

> "Here are six cybersecurity definitions."

It is:

> "A massive technology company has a security problem. Let's investigate how something like this can happen."

The concepts are discovered during the investigation.

---

# 13. Security Accuracy Rules

### Fictionalize the company

Use a fictional Big-Tech company rather than claiming that a specific real company experienced the fictional incident.

The visual scale can be inspired by companies such as Amazon/Google/Meta/Netflix, but the incident itself should remain fictional.

---

### Do not oversimplify XSS

When XSS is teased or later explained, do not imply that XSS automatically compromises backend APIs.

The later explanation should account for:

* Browser context
* Same-origin policy
* Cookies
* Authentication
* CORS
* CSP
* Application design

---

### Avoid Phishing in Video 1

Phishing is intentionally excluded from this episode.

It may be covered as a separate future attack episode.

---

# 14. What This Video Should NOT Cover Deeply

Do not turn Video 1 into detailed tutorials for:

* SQL Injection
* XSS
* CSRF
* DDoS
* Credential Attacks
* MITM
* Malware
* Phishing

These are future episodes.

Video 1 should establish the **security mental model** required to understand those attacks.

---

# 15. Episode 2 Relationship

Video 1 asks:

> **Why does security matter?**

Video 2 asks:

> **How can attackers actually break a system this big?**

Video 1:

```text
System
  ↓
What are we protecting?
  ↓
CIA
  ↓
Threat
  ↓
Threat Vector
  ↓
Vulnerability
  ↓
Attack
  ↓
Impact
  ↓
Risk
  ↓
Defense
```

Video 2:

```text
Attack Scenario
      ↓
What happened?
      ↓
How did attacker reach it?
      ↓
What vulnerability existed?
      ↓
How was it exploited?
      ↓
What did it affect?
      ↓
How do we defend it?
```

This creates a natural transition from **security fundamentals → real attack mechanics**.

---

# 16. Production Workflow

The video will be produced in phases.

### Phase 1 — Blueprint

**This document**

Status: Defined.

---

### Phase 2 — Scene Definition

For every scene define:

* Scene purpose
* Exact visual
* Camera movement
* Objects/elements
* Animation behavior
* On-screen text
* Approximate duration
* Transition to next scene

---

### Phase 3 — Visual Generation

Generate/assemble the visual assets and animated scene concepts.

Priority:

**Visual clarity > decorative complexity**

---

### Phase 4 — Narration

Once scenes are finalized, write the creator's narration scene-by-scene.

Narration should explain exactly what the viewer is seeing.

---

### Phase 5 — Editing

Combine:

```text
Creator Voice
+
Animated Scenes
+
Sound Design
+
Music
+
Transitions
```

---

### Phase 6 — Thumbnail & Publishing

Create:

* Thumbnail
* Title
* Description
* Chapters
* Tags/keywords
* Short-form clips

---

# 17. Success Criteria

The video is successful if the viewer finishes it understanding:

1. Why security matters at Big-Tech scale.
2. What confidentiality, integrity and availability mean.
3. What a threat is.
4. What a threat vector is.
5. What a vulnerability is.
6. What an attack is.
7. What impact and risk mean.
8. How these concepts connect.
9. Why large systems require multiple security layers.
10. Why specific attacks such as SQL Injection, XSS and DDoS deserve deeper investigation.

Most importantly, the viewer should think:

> **"I finally understand how security teams look at an attack."**

---

# 18. Final Emotional Arc

The viewer should experience:

**Curiosity**

↓

**Something is wrong**

↓

**How big is this system?**

↓

**What are we protecting?**

↓

**Oh — confidentiality, integrity, availability**

↓

**But how did the attacker reach it?**

↓

**Threat → Vector → Vulnerability → Attack**

↓

**How bad could this become?**

↓

**Risk**

↓

**Oh… that's why Big Tech has security everywhere.**

↓

**But how do these actual attacks work?**

↓

**Next episode.**

---

## Blueprint Status

**READY FOR SCENE DEFINITION**

Next production phase:

**Define Scene 01 → Scene 13 in exact visual/animation detail before generating the visual assets.**
