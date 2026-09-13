# ANIMATIONPROMPTS_VIDEO_02.md

# Cyber Attack X FAANG — Video 02

## How Can Attackers Break a System This Big?

**Purpose:** Animation-generation prompts for Video 2 only  
**Series:** Cyber Attack X FAANG  
**Episode:** 02  
**Format:** Attack Simulation / Technical Investigation  
**Visual Style:** Same NEXA universe as Video 1  
**Narration:** Creator voice  
**Status:** Animation prompt draft

---

# 1. Episode Objective

Video 2 moves from:

> **Why does security matter?**

to:

> **How can an attacker actually exploit a system?**

The viewer should see attack mechanics rather than simply hear attack names.

---

# 2. Episode Structure

Every attack follows the same investigation framework:

```text
INCIDENT
   ↓
HOW DID ATTACKER REACH IT?
   ↓
THREAT VECTOR
   ↓
VULNERABILITY
   ↓
ATTACK
   ↓
IMPACT
   ↓
DEFENSE
```

This structure connects directly to Video 1.

---

# 3. Attacks Covered

Primary attacks:

1. SQL Injection
2. XSS
3. CSRF
4. DDoS
5. Credential Attacks
6. MITM
7. Malware

Phishing is intentionally excluded from this episode.

---

# 4. Global Visual Continuity

Use the same fictional company:

**NEXA**

Use the same:

- Architecture
- Dark-blue environment
- Server design
- API visualization
- Request particles
- Monitoring UI
- Security operations center
- Global infrastructure

Do not redesign the universe between episodes.

---

# 5. Opening — The Investigation Begins

## Shot 01 — Previous Incident

```text
Cinematic flashback to the NEXA production incident from the previous episode, dark operations center, red alerts, overloaded infrastructure, rapidly moving request particles, dramatic camera push toward the failing system.
```

---

## Shot 02 — Question

Black screen.

Post-production:

```text
We know something went wrong.

But how?
```

---

## Shot 03 — Attack Surface

```text
Cinematic wide shot of NEXA's complete internet-facing architecture, web applications, APIs, authentication systems, databases and services visible as interconnected infrastructure, millions of requests moving through the system.
```

---

# 6. ATTACK 01 — SQL INJECTION

## Shot 01 — Incident

```text
Cinematic close-up of a web application login or search interface connected to a backend API and database, normal user input initially flowing through the system, realistic enterprise application environment.
```

---

## Shot 02 — Normal Query

```text
Cinematic visualization of a backend application receiving user input and constructing a database query, request travels from web application to application server and then database, clean organized flow.
```

---

## Shot 03 — Vulnerability

```text
Extreme close-up of an application passing untrusted user input into a database query without safely separating data from query logic, subtle red vulnerability indicator, realistic application-security visualization.
```

---

## Shot 04 — Malicious Input

```text
Cinematic visualization of crafted malicious input entering a vulnerable application and altering the intended database query logic, abstract representation rather than copyable exploit payload, red request particle crossing the application boundary.
```

---

## Shot 05 — Database Effect

```text
Cinematic visualization of a database unexpectedly returning records outside the intended query scope after malicious input reaches the query layer, multiple data records becoming exposed, realistic database visualization.
```

---

## Shot 06 — Impact

```text
Cinematic visualization of sensitive records being exposed from a database after an application-layer attack, red security warning spreading through the data layer, camera pulling back to show affected service.
```

---

## Shot 07 — Defense

```text
Cinematic visualization of secure parameterized database queries separating user input from query logic, malicious input treated as data rather than executable query structure, attack attempt blocked before reaching sensitive database operations.
```

Post:

```text
PARAMETERIZED QUERIES
INPUT VALIDATION
LEAST PRIVILEGE
```

---

# 7. ATTACK 02 — XSS

## Shot 01 — Web Application

```text
Cinematic visualization of a modern web application displaying user-generated content, browser rendering the page normally, realistic browser and backend interaction.
```

---

## Shot 02 — Malicious Content

```text
Cinematic visualization of malicious script content being stored or reflected through a vulnerable web application and reaching a victim browser, red warning indicator, realistic web security environment.
```

---

## Shot 03 — Browser Execution

```text
Cinematic close-up of a victim browser rendering unexpected script behavior inside its application context, malicious script visually highlighted, realistic browser environment, dark cyber-thriller lighting.
```

---

## Shot 04 — Browser Context

```text
Cinematic visualization of a browser session containing authenticated application state while unexpected script executes within the affected web context, secure browser boundary visible, realistic web security visualization.
```

---

## Shot 05 — Impact

```text
Cinematic visualization of unauthorized browser actions occurring within an affected web application session, sensitive page content being accessed or an unintended action being initiated, red warning indicators.
```

---

## Shot 06 — Defense

```text
Cinematic visualization of a web application security stack blocking malicious script content using output encoding, content security policy and safe input handling, malicious script stopped before executing in the browser.
```

Post:

```text
OUTPUT ENCODING
CSP
SAFE INPUT HANDLING
```

---

# 8. XSS ACCURACY RULE

Do NOT show:

```text
XSS → directly hacks backend API
```

Instead show:

```text
Malicious Script
       ↓
Victim Browser
       ↓
Affected Web Context
       ↓
Unauthorized Browser Actions
```

The narration should explain that the actual impact depends on:

- Browser security model
- Same-origin policy
- Cookies
- Authentication design
- CORS
- CSP
- Application architecture

---

# 9. ATTACK 03 — CSRF

## Shot 01 — Authenticated Browser

```text
Cinematic visualization of a user logged into a legitimate web application, authenticated browser session active, normal secure application state.
```

---

## Shot 02 — Forged Request

```text
Cinematic visualization of an attacker-controlled web context causing a victim browser to initiate an unintended request toward a legitimate application, forged request represented as a red path.
```

---

## Shot 03 — Server Receives Request

```text
Cinematic visualization of a legitimate server receiving an unwanted state-changing request that appears to originate from an authenticated browser session, realistic API flow.
```

---

## Shot 04 — State Change

```text
Cinematic visualization of an unintended transaction or account state change caused by a forged request, database record changing unexpectedly, red warning pulse.
```

---

## Shot 05 — Defense

```text
Cinematic visualization of a web application validating CSRF protection before accepting a state-changing request, forged request rejected while legitimate request continues.
```

Post:

```text
CSRF TOKEN
SAME-SITE COOKIES
ORIGIN CHECKS
```

---

# 10. ATTACK 04 — DDoS

## Shot 01 — Normal Traffic

```text
Cinematic visualization of a healthy global API receiving organized user traffic, stable request flow across multiple regions, calm system indicators.
```

---

## Shot 02 — Distributed Sources

```text
Cinematic global visualization showing enormous numbers of compromised or automated sources distributed across multiple geographic regions, all beginning to send traffic toward the same target infrastructure.
```

---

## Shot 03 — Traffic Flood

```text
High-intensity cinematic visualization of millions of distributed request particles converging on NEXA infrastructure, multiple network paths merging into a massive traffic flood, realistic distributed-system architecture.
```

---

## Shot 04 — Edge Saturation

```text
Cinematic visualization of network and edge infrastructure becoming saturated by enormous traffic volume, queues and capacity indicators rising, legitimate requests becoming mixed with attack traffic.
```

---

## Shot 05 — Service Degradation

```text
Cinematic visualization of API latency rapidly increasing, queues filling, servers approaching resource limits and legitimate requests failing, realistic backend behavior.
```

---

## Shot 06 — Defense

```text
Cinematic visualization of DDoS mitigation absorbing and filtering massive malicious traffic before it reaches core services, distributed traffic scrubbing and rate controls protecting the application, legitimate traffic continuing.
```

Post:

```text
RATE LIMITING
TRAFFIC FILTERING
DDoS MITIGATION
CAPACITY PLANNING
```

---

# 11. ATTACK 05 — CREDENTIAL ATTACKS

## Shot 01 — Login

```text
Cinematic close-up of a modern enterprise authentication system receiving normal login requests, secure identity infrastructure, blue healthy indicators.
```

---

## Shot 02 — Repeated Attempts

```text
Cinematic visualization of a rapidly increasing stream of abnormal authentication attempts against a login service, repeated requests represented abstractly without displaying real credentials, red warning indicators.
```

---

## Shot 03 — Pattern Detection

```text
Cinematic visualization of an authentication monitoring system detecting abnormal login patterns across multiple accounts and locations, security analytics dashboard highlighting suspicious behavior.
```

---

## Shot 04 — Account Risk

```text
Cinematic visualization of an account becoming at risk after repeated suspicious authentication attempts, identity system highlighting the account and initiating protective controls.
```

---

## Shot 05 — Defense

```text
Cinematic visualization of multi-factor authentication, rate limiting, account lockout controls and anomaly detection preventing unauthorized account access, suspicious requests stopped while legitimate user continues.
```

Post:

```text
MFA
RATE LIMITING
ANOMALY DETECTION
ACCOUNT PROTECTION
```

---

# 12. ATTACK 06 — MITM

## Shot 01 — Legitimate Connection

```text
Cinematic visualization of two legitimate systems communicating across a secure network connection, blue encrypted data path traveling between them, realistic network infrastructure.
```

---

## Shot 02 — Intermediary

```text
Cinematic visualization of an unauthorized intermediary appearing between two communicating systems, attempting to intercept traffic, secure blue connection disrupted by a red interception path, realistic network-security visualization.
```

---

## Shot 03 — Intercepted Traffic

```text
Cinematic visualization of network traffic being redirected through an unauthorized intermediary, packets visually passing through the interception point, dark cyber-thriller environment.
```

---

## Shot 04 — Protection

```text
Cinematic visualization of authenticated encrypted communication preventing an unauthorized intermediary from reading or modifying protected traffic, secure connection restored, attacker unable to interpret protected data.
```

Post:

```text
TLS
CERTIFICATE VALIDATION
AUTHENTICATED ENCRYPTION
```

---

# 13. ATTACK 07 — MALWARE

## Shot 01 — Entry

```text
Cinematic visualization of a malicious software payload entering an enterprise computing environment through an initially compromised endpoint, subtle red digital object crossing into the network, realistic enterprise infrastructure.
```

---

## Shot 02 — Execution

```text
Cinematic visualization of malicious software executing on a compromised endpoint, abnormal processes appearing and security telemetry changing, realistic operating-system and enterprise-security environment.
```

---

## Shot 03 — Lateral Movement

```text
Cinematic visualization of malicious activity attempting to move from one compromised enterprise system toward connected systems, red network paths spreading through the architecture, realistic cybersecurity visualization.
```

---

## Shot 04 — Detection

```text
Cinematic security monitoring visualization detecting abnormal process behavior and network activity, security alert propagating through a global security operations center.
```

---

## Shot 05 — Containment

```text
Cinematic visualization of a compromised machine being isolated from the enterprise network, network connection severed while the rest of the infrastructure remains operational, realistic incident-response visualization.
```

Post:

```text
DETECT
ISOLATE
CONTAIN
RECOVER
```

---

# 14. Cross-Attack Comparison

## Shot 01 — Seven Attack Paths

```text
Cinematic visualization of seven distinct attack paths converging toward a large technology system, each path representing a different attack category, sophisticated enterprise cybersecurity design.
```

---

## Shot 02 — Different Weaknesses

```text
Cinematic visualization showing different layers of a distributed system being targeted: database, browser, web session, network capacity, identity system, network connection and endpoint, each highlighted sequentially.
```

---

## Shot 03 — Common Pattern

```text
Cinematic visualization connecting all attacks through the same conceptual chain: threat, vector, vulnerability, attack and impact, red paths converging into one unified security model.
```

---

# 15. Final Defense Montage

## Shot 01

```text
Cinematic wide shot of NEXA's complete defense-in-depth architecture operating across global infrastructure, multiple security layers active simultaneously, legitimate traffic flowing smoothly.
```

---

## Shot 02

```text
Cinematic visualization of multiple attacks being detected and blocked at different layers of the architecture, SQL injection stopped at application/database boundary, malicious browser behavior controlled, forged requests rejected, DDoS traffic filtered, suspicious credentials blocked, intercepted traffic protected by encryption and malware contained.
```

---

## Shot 03

```text
Cinematic camera pulling back from the protected infrastructure to reveal the entire global NEXA platform, security telemetry flowing through monitoring systems, protected architecture glowing steadily against a dark global network.
```

---

# 16. Ending

Black screen.

Post-production:

```text
The attacker doesn't need
to break everything.

They only need
one weakness.
```

Pause.

Then:

```text
CYBER ATTACK X FAANG
```

---

# 17. Next Episode Teaser

```text
Cinematic close-up of a single vulnerable component inside an enormous distributed system, camera slowly pushing toward the weakness while the surrounding architecture remains massive and dark, suspenseful cyber-thriller atmosphere.
```

Post:

```text
NEXT

CAN ONE BUG
TAKE DOWN A
BIG-TECH SYSTEM?
```

---

# 18. Animation Rules

Never attempt to generate the complete episode as one AI video.

Use:

```text
Attack
 ↓
Multiple short shots
 ↓
Individual animation
 ↓
Edit
 ↓
Creator narration
 ↓
Sound design
```

Recommended shot length:

```text
Technical explanation: 3–5 sec
Attack reveal: 2–4 sec
Architecture: 4–6 sec
High intensity: 2–4 sec
Final reveal: 3–5 sec
```

---

# 19. Technical Accuracy Rules

## SQL Injection

Show unsafe query construction conceptually.

Do not provide a real exploit payload in generated visuals.

---

## XSS

Show:

```text
Malicious Script
 ↓
Victim Browser
 ↓
Affected Web Context
```

Do not imply direct backend compromise.

---

## CSRF

Show:

```text
Attacker-Controlled Context
 ↓
Victim Browser
 ↓
Forged Request
 ↓
Legitimate Server
```

---

## DDoS

Show distributed traffic overwhelming resources.

Do not imply every high-traffic event is automatically malicious.

---

## Credential Attacks

Show abnormal authentication attempts.

Do not display real credentials.

---

## MITM

Show interception and the importance of authenticated encrypted communication.

---

## Malware

Show infection, execution, detection and containment.

Do not provide operational malware instructions.

---

# 20. Episode Boundary

Video 2 is the **attack mechanics episode**.

Future individual episodes can go deeper into each attack.

Possible future structure:

```text
Episode 03
SQL Injection — How One Input Can Reach Your Database

Episode 04
XSS — When Your Browser Becomes the Attack Surface

Episode 05
CSRF — When Your Browser Sends a Request You Never Intended

Episode 06
DDoS — How Millions of Requests Can Take Down a Service

...
```

---

# 21. Status

```text
BLUEPRINT.md                 ✅
STORYBOARD.md                ⏳
SCRIPT.md                    ⏳
ANIMATIONPROMPTS_VIDEO_02    ✅

VISUAL GENERATION            ⏳
ANIMATION                    ⏳
VOICE RECORDING              ⏳
SOUND DESIGN                ⏳
FINAL EDIT                   ⏳
```

Next:

**Finish Video 2 storyboard and script before generating its final animation assets.**