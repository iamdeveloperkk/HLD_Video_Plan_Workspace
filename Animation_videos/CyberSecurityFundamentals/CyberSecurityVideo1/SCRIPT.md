# SCRIPT.md

# Cyber Attack X FAANG — Video 01

## What Happens When Big Tech Gets Security Wrong?

**Series:** Cyber Attack X FAANG
**Episode:** 01
**Narration:** Creator voice
**Style:** Cinematic / Investigative / Technical
**Status:** Draft — Narration aligned to storyboard

---

# SCENE 01 — THE NIGHT SOMETHING GOES WRONG

### Shot 01–04

It's 2:13 in the morning.

While most people are sleeping, thousands of engineers, services and machines are quietly doing what they do every night.

Keeping a massive technology platform alive.

Everything looks normal.

120,000 API requests every second.

31 milliseconds of latency.

Less than one tenth of one percent of requests failing.

Nothing unusual.

At least...

not yet.

---

### Shot 05–07

Then something changes.

120,000 requests per second...

becomes 340,000.

Then 520,000.

And suddenly...

890,000 requests every second.

Latency starts climbing.

31 milliseconds...

120...

420...

and then over a second.

The database is now sitting at 96% CPU.

And then...

the alert nobody wants to see appears.

**Production service degradation detected.**

---

### Shot 08–11

But here's the interesting part.

This isn't one server.

This isn't one application.

This is a system serving millions of users across the world.

And now...

something is attacking it.

But what exactly is happening?

And more importantly...

how can something like this even happen to a system this big?

To understand that...

we need to zoom out.

---

# SCENE 02 — THE BIG-TECH ARCHITECTURE

### Shot 01–02

Imagine you're using a Big-Tech application.

You open the app.

You click a button.

Behind that single click...

a lot more happens than you see.

Your request travels through the internet...

reaches the company's edge infrastructure...

and eventually enters the application.

---

### Shot 03–05

It might pass through a CDN.

Then a Web Application Firewall.

Then an API Gateway.

And from there...

it could be routed to one of hundreds of services.

One service might handle your profile.

Another might handle orders.

Another payments.

Another recommendations.

And eventually...

some of those services need to read or write data.

So they communicate with databases, caches and storage systems.

---

### Shot 06

And this is where things become interesting.

At Big-Tech scale...

we aren't protecting a server.

We're protecting an ecosystem.

Millions of users.

Thousands of services.

Multiple regions.

Petabytes of data.

And countless requests moving through the system every second.

So the first question security teams need to ask is...

**What exactly are we protecting?**

---

# SCENE 03 — WHAT ARE WE PROTECTING?

### Shot 01

Think about the data inside a technology company.

Customer information.

Orders.

Payments.

Messages.

Credentials.

Business data.

Internal systems.

Some of this information can be extremely sensitive.

But protecting data isn't simply about putting it behind a password.

There are three fundamental properties we care about.

---

### Shot 02

**Confidentiality.**

**Integrity.**

**Availability.**

Together...

they form one of the most fundamental security models:

the CIA Triad.

---

### Shot 03 — Confidentiality

Confidentiality asks:

**Who is allowed to see this information?**

If I request my order history...

I should see my orders.

Not yours.

If another customer can somehow retrieve my private information...

we have a confidentiality problem.

---

### Shot 04 — Integrity

Integrity asks a different question.

**Can someone change the information when they shouldn't be able to?**

Imagine placing an order for one thousand rupees.

The system stores:

one thousand.

But somewhere along the way...

that value becomes one hundred thousand.

The data may still be available.

It may even be confidential.

But it isn't trustworthy anymore.

That's an integrity problem.

---

### Shot 05–06 — Availability

And then there's availability.

Can legitimate users actually use the system when they need it?

Because imagine a perfectly secured application...

where nobody can access the data...

because the entire service is down.

From a user's perspective...

security hasn't exactly succeeded.

So confidentiality protects what should remain private.

Integrity protects what should remain correct.

And availability protects the ability to use the system.

But now...

let's see what happens when each one fails.

---

# SCENE 04 — CONFIDENTIALITY BREACH

### Shot 01–02

Let's start with something simple.

User A logs in.

The system knows who User A is.

User A requests:

`GET /api/orders`

The request travels through the API...

reaches the order service...

and the service queries the database.

So far...

everything looks normal.

---

### Shot 03–04

But then the response comes back.

And something is wrong.

User A requested their orders...

but the response contains information belonging to User B.

Name.

Email.

Order history.

Private information.

---

### Shot 05

Now notice something important.

Authentication may have worked perfectly.

The system knew who User A was.

But authentication answers:

**Who are you?**

It doesn't automatically answer:

**What are you allowed to access?**

That's authorization.

And if authorization is implemented incorrectly...

an authenticated user can still access something they shouldn't.

---

### Shot 06

That's a confidentiality failure.

The information wasn't supposed to be visible...

but it became visible.

And that distinction between authentication and authorization...

is incredibly important in real systems.

Because knowing who someone is...

is not the same thing as deciding what they're allowed to do.

---

# SCENE 05 — INTEGRITY BREACH

### Shot 01–02

Now let's look at another possibility.

A customer creates an order worth one thousand rupees.

The request flows normally.

Client...

API...

payment service...

database.

Everything appears fine.

---

### Shot 03–05

But imagine someone manages to manipulate the request.

The application expected:

`amount = 1000`

But somehow...

the system processes:

`amount = 100000`

The database now contains a value that should never have been there.

The system accepted a state change...

that it should have rejected.

---

### Shot 06

This is an integrity problem.

Because the question isn't:

**Can we access the data?**

The question is:

**Can we trust the data?**

If an attacker can modify prices...

orders...

permissions...

or financial records...

the integrity of the system is compromised.

And depending on the system...

that can become much more serious than a simple incorrect value.

---

# SCENE 06 — AVAILABILITY ATTACK

### Shot 01

Now let's look at the third part.

Availability.

Our API is healthy.

One thousand requests per second.

Thirty milliseconds of latency.

Almost no errors.

Everything is working.

---

### Shot 02–03

Then requests start arriving.

And arriving.

And arriving.

One thousand requests...

one hundred thousand...

one million requests every second.

The system has finite resources.

CPU.

Memory.

Connections.

Queues.

Database capacity.

Eventually...

something has to give.

---

### Shot 04–05

CPU climbs.

Queues fill up.

Latency goes from milliseconds...

to hundreds of milliseconds...

then seconds.

Users click...

and wait.

Then wait some more.

And eventually...

requests start failing.

---

### Shot 06–07

The service becomes unavailable.

This is an availability failure.

And notice something interesting.

The attacker didn't necessarily need to steal any data.

They didn't necessarily need to modify the database.

They simply prevented legitimate users from using the system.

This is one reason attacks against availability can be so powerful.

---

# SCENE 07 — WHO IS DOING THIS?

### Shot 01–03

So now we know what can go wrong.

Confidentiality.

Integrity.

Availability.

But our original question still remains.

Someone...

or something...

is causing this.

Who?

A malicious attacker?

A botnet?

A compromised account?

An insider?

Some other threat actor?

We don't know yet.

---

### Shot 04–05

And this brings us to our next concept.

**Threat.**

A threat is a potential source of harm.

But here's an important distinction.

A threat is not the attack itself.

Think of it like this.

The threat is the possibility that someone or something could cause damage.

The attack is what actually happens.

So if a malicious actor wants to target our system...

that's the threat.

But we still need to understand...

how they can actually reach us.

---

# SCENE 08 — HOW DO THEY GET IN?

### Shot 01–03

Because a threat sitting somewhere on the internet...

doesn't automatically have access to our infrastructure.

There has to be a path.

Maybe it's the web application.

Maybe it's an API.

Maybe it's a mobile application.

Maybe it's an exposed service.

Maybe it's a compromised employee device.

Maybe it's a stolen credential.

Maybe it's a third-party integration.

There can be many paths into a system.

---

### Shot 04–05

That path...

is what we call a **threat vector**.

Or, in many security discussions...

an attack vector.

It's the route or mechanism through which a threat can reach the system.

So now our investigation looks like this:

A threat...

has a vector...

through which it can reach our system.

But reaching the system isn't enough.

The attacker still needs something to exploit.

And that's where things get interesting.

---

# SCENE 09 — FINDING THE WEAKNESS

### Shot 01–02

Let's follow that request.

The attacker reaches an API.

The API sends data into the application.

The application processes that input...

and eventually communicates with the database.

On the surface...

everything looks normal.

---

### Shot 03–04

But security engineers start looking closer.

What happens if the input isn't what the developer expected?

What if the application trusts something it shouldn't?

What if an authorization check is missing?

What if input validation is weak?

What if a configuration exposes something that should have remained internal?

These are weaknesses.

---

### Shot 05–06

And when a weakness can be exploited by an attacker...

we call it a **vulnerability**.

That's an important distinction.

A vulnerability isn't necessarily an attack.

It's the weakness that creates the opportunity.

And now our chain is getting clearer.

We have a threat.

We have a way to reach the system.

And we've found a weakness.

The next question is...

what happens when someone actually uses it?

---

# SCENE 10 — VULNERABILITY BECOMES AN ATTACK

### Shot 01–03

The attacker sends a malicious request.

It enters through the exposed path.

It reaches the vulnerable component.

And instead of behaving the way the developer intended...

the system responds in a way the attacker can exploit.

---

### Shot 04–05

The system moves from:

**Healthy**

to...

**Compromised.**

Data could be exposed.

Data could be modified.

A service could be disrupted.

Accounts could potentially be compromised.

The exact outcome depends on the vulnerability...

the attack...

and the system around it.

---

### Shot 06

And that's the distinction we need to remember.

A vulnerability is the weakness.

An attack is the malicious action that exploits that weakness.

So now we have:

**Threat.**

**Threat Vector.**

**Vulnerability.**

**Attack.**

But we're still missing one very important question.

**How bad is it?**

---

# SCENE 11 — SO HOW BAD IS IT?

### Shot 01

Let's put everything together.

A threat...

finds a threat vector...

reaches a vulnerability...

and performs an attack.

But the story doesn't end there.

We need to understand the consequence.

That's the **impact**.

---

### Shot 02–03

Suppose the vulnerable component is an internal tool used by a small team.

Maybe the impact is limited.

Now compare that with an internet-facing payment service...

used by millions of customers.

The same type of weakness...

can have a completely different consequence.

---

### Shot 04

Maybe customer data is exposed.

Maybe financial transactions are manipulated.

Maybe accounts are compromised.

Maybe an entire service goes offline.

Maybe the company loses money.

Maybe customers lose trust.

Impact can extend far beyond the technical system.

---

### Shot 05–06

And that's where we get to **risk**.

A simple way to think about it is:

**Risk is related to likelihood and impact.**

A weakness that is extremely difficult to exploit...

and would cause almost no damage...

is very different from an easily exploitable weakness...

sitting directly in front of a payment system.

Security teams therefore don't just ask:

**"Do we have vulnerabilities?"**

They ask:

**"Which vulnerabilities represent the greatest risk?"**

And that's one of the reasons security at Big-Tech scale is so complicated.

Because there are thousands of things that could potentially go wrong.

So how do you defend a system this large?

---

# SCENE 12 — BIG-TECH SECURITY IS LAYERS

### Shot 01–03

The answer isn't one firewall.

It isn't one security tool.

And it isn't one team sitting in a security operations center.

Security is layered.

A request may first encounter the CDN.

Then a Web Application Firewall.

Then an API Gateway.

Each layer can provide a different type of protection.

---

### Shot 04–06

Then comes identity.

Authentication asks:

**Who are you?**

Authorization asks:

**Are you allowed to do this?**

Because even if someone reaches the API...

they shouldn't automatically be able to access everything behind it.

---

### Shot 07

Then there's rate limiting.

If someone suddenly sends an enormous number of requests...

the system can limit how much traffic a particular client is allowed to generate.

This helps protect availability and system resources.

---

### Shot 08–09

Behind that...

services still need their own protections.

Databases need access controls.

Sensitive information may need encryption.

Secrets need to be protected.

And permissions need to follow the principle of least privilege.

---

### Shot 10

And then comes something equally important.

Visibility.

Audit logs.

Monitoring.

Alerts.

Threat detection.

Because preventing every attack is unrealistic.

A mature system also needs to know:

**What happened?**

**When did it happen?**

**What was affected?**

And:

**What should we do next?**

---

### Shot 11–12

So if you look at the entire system...

security becomes a stack of layers.

Internet.

CDN.

WAF.

API Gateway.

Authentication.

Authorization.

Rate limiting.

Services.

Databases.

Encryption.

Logging.

Monitoring.

Threat detection.

Each layer has a job.

And if one layer fails...

another layer may still reduce the damage.

That's what defense in depth is about.

Security isn't one wall.

It's many layers working together.

---

# SCENE 13 — THE INVESTIGATION CONTINUES

### Shot 01–02

But there's a problem.

We've talked about the framework.

We've talked about the architecture.

We've talked about how an attacker can move from a threat...

to a vector...

to a vulnerability...

to an attack.

But we haven't actually looked at the attacks themselves.

---

### Shot 03

Because what happens when that vulnerability is...

SQL Injection?

What happens when malicious JavaScript reaches a victim's browser?

XSS.

What happens when an attacker tricks a browser into sending an unwanted request?

CSRF.

What happens when millions of requests overwhelm your infrastructure?

DDoS.

What happens when credentials are stolen?

Credential attacks.

What happens when communication is intercepted?

Man-in-the-middle.

And what happens when malicious software gets inside the environment?

Malware.

---

### Shot 04–05

Those aren't just names on a security checklist.

They're different ways an attacker can turn a weakness...

into a real-world impact.

And that's what we're going to investigate next.

---

# END

**Cyber Attack X FAANG**

**Real attacks.
Real systems.
Real lessons.**

### NEXT EPISODE

**How Can Attackers Break a System This Big?**

---

# 14. Narration Delivery Notes

## Opening

Slow.

Controlled.

Build curiosity before explaining anything.

Avoid sounding like a tutorial.

---

## Incident Escalation

Increase speaking speed slightly as metrics rise.

Pause immediately before:

> "And then..."

and:

> "something is attacking it."

---

## CIA Section

Slow down again.

Give each concept room to breathe.

The visuals should carry much of the explanation.

---

## Threat → Vector → Vulnerability → Attack

This is the conceptual core of the episode.

Use deliberate pauses between each term.

Example:

> A threat.

**Pause.**

> A way to reach us.

**Pause.**

> A weakness.

**Pause.**

> And finally...

> an attack.

---

## Defense Section

Shift from suspense toward confidence.

The viewer should feel:

> "Now I understand why these systems have so many security layers."

---

## Ending

Speed up during the attack montage.

Then slow down for:

> "Those aren't just names on a security checklist."

End with a strong pause before the next-episode title.

---

# 15. Creator Performance Principle

Do not read the script like a textbook.

The narration should feel like the creator is **walking the viewer through an investigation**.

Use:

* Short pauses
* Emphasis on technical terms
* Changes in speaking speed
* Curiosity in questions
* Slight tension during incident scenes
* Confidence during technical explanations

The animation should provide the visual evidence.

The creator's voice should provide the reasoning.

---

# 16. Script-to-Visual Rule

The narration should never describe something that is not visible for an extended period.

Preferred pattern:

```text
VISUAL EVENT
     ↓
CREATOR EXPLAINS IT
     ↓
VISUAL ZOOMS / REVEALS DETAIL
     ↓
CREATOR EXPLAINS WHY IT MATTERS
```

This keeps the episode visually driven instead of becoming an audio lecture over unrelated animation.

---

# 17. Script Status

```text
BLUEPRINT.md       ✅
STORYBOARD.md      ✅
SCRIPT.md          ✅
VISUAL ASSETS      ⏳
ANIMATION          ⏳
VOICE RECORDING    ⏳
SOUND DESIGN       ⏳
FINAL EDIT         ⏳
```

Next production phase:

**Generate and animate the individual visual shots defined in `STORYBOARD.md`.**
