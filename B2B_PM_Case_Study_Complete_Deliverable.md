# B2B Product Requirement Document (PRD) — Subcontractor Operations Platform
## Eliminating the £50M Field Operations Blind Spot for National Fiber Broadband Rollouts

> **Document Type:** Executive Product Requirement Document (Google Doc / PRD Format)  
> **Author:** Komal Agarwal  
> **Status:** Final / Approved  
> **Date:** November 2026  
> **Operational Scope:** ~6,000 jobs/week | ~200 independent subcontractor firms | £50M+ annual outsourced field spend  
> **Interactive Links:** [Live Prototype (`wireframes.html`)](./wireframes.html) | [Slide Deck (`presentation_deck.html`)](./presentation_deck.html) | [PowerPoint (`presentation_deck.pptx`)](./presentation_deck.pptx)

---

## Executive Summary & Key Metrics

A national fiber broadband operator delivers **~6,000 jobs per week**, relying on **~200 independent subcontractor firms** for 70% of field capacity (residential FTTH installs, customer premise drops, and fault repairs). 

Today, this £50M+ annual operation runs through an operational black box: requests travel over ad-hoc WhatsApp chats and unmonitored inboxes. Variations appear on invoices 45 days later, triggering commercial disputes, delayed payments, and technician defection to rival telecom networks.

| Key Metric | Baseline Reality Today | Platform Target | Strategic Impact |
|---|---|---|---|
| **Field Volume** | 6,000 jobs / week | 6,000 jobs / week | 70% delivered by 200 partner firms |
| **Payment Velocity** | 45–60 days | 7–14 days | -70% payment lag; stops vendor defection |
| **Dispute Resolution** | 45+ days post-invoice | < 1.4 days (Same-day) | 4-hour decision SLA on field requests |
| **Field Interaction** | 8–10 mins (App crashes) | < 120 seconds | 4 taps, 0 typing, 100% offline-ready |
| **Net Operator ROI** | £1.8M dispute leakage | £1,071,200 net savings | **2.86x ROI** (Payback in < 5 months) |

> **The Core Shift:** Replace unverified end-of-month commercial warfare with a **real-time, offline-first shared source of truth** linking the technician's van directly to the operator's console and self-billing payment milestones.

---

## 1. Stakeholder Personas & The Incentive Compact

```
+-------------------------------------------------------+-------------------------------------------------------+
| OPERATOR PERSPECTIVE (Priya Sharma & David Vance)     | SUBCONTRACTOR PERSPECTIVE (Imran, Meera & Ravi)       |
+-------------------------------------------------------+-------------------------------------------------------+
| • Priya Sharma (Regional Ops Manager - 1,500 jobs/wk) | • Imran Khan (Firm Owner - 25 vans, £150k monthly payroll)
| • David Vance (Vendor Commercial Manager - 200 firms) | • Meera (Dispatcher - 70 daily jobs via WhatsApp/Excel)
|                                                       | • Ravi Patel (Field Technician - 6 yrs piece-rate tech)
+-------------------------------------------------------+-------------------------------------------------------+
| Core Motivation:                                      | Core Motivation:                                      |
| High throughput, first-time fix rate, cost control    | Cash flow predictability, weekly payroll stability,   |
| against rate cards, defensible audit trails.          | protection against arbitrary deductions, zero app pain.|
+-------------------------------------------------------+-------------------------------------------------------+
| Current Pain Today:                                   | Current Pain Today:                                   |
| • Rate variations arrive as £95 surprises 4 wks late. | • Subcontractor net margin is 6%; arbitrary invoice   |
| • Unclear if 'access failure' was real or late tech.  |   clawbacks wipe out monthly profit.                  |
| • 2 full days monthly spent stitching CSV scorecards. | • Mobile app crashes in basements and loses photos.   |
+-------------------------------------------------------+-------------------------------------------------------+
| ❌ REJECTION TRIGGER:                                 | ❌ REJECTION TRIGGER:                                 |
| "If it requires manual data re-entry or doesn't tie   | "If you charge our 6% margin a SaaS fee, or if the    |
| directly to our dispatch pipeline, supervisors will   | app adds >2 minutes per job, we will shift our vans   |
| ignore it completely."                                | to your competitor's network."                       |
+-------------------------------------------------------+-------------------------------------------------------+
```

### The Three-Part Incentive Compact
1. **Rate Variations:** Operator gets geotagged photo proof on-site  ←→  Subcontractor gets a binding 4-hour decision turnaround.
2. **SLA Clock Pauses:** Operator prevents false access claims  ←→  Subcontractor auto-attaches GPS & timestamps to prove presence.
3. **Platform Monetization:** Operator funds platform via leakage savings (£1.20/job)  ←→  Core platform is **100% FREE** to subcontractors.

---

## 2. Product Solution & UX Specifications

### Surface 1: Field Tech Mobile App (Android 11+, Offline-First)
- **6-Step Fast Onboarding (<3 Minutes):** SMS invite deep link → Auto-reads OTP (binds phone to firm) → Transparent camera & location permissions → 12MB offline pack download → 45s skippable micro-tour → Ready for Job 1.
- **Offline as Default State:** Built on local encrypted SQLite store. Every tap commits in 0ms without network spinners. Monotonic sequence IDs and GPS UTC stamps prevent duplicate actions.
- **<120-Second Field Budget:** 4-tap complete closeout workflow, 48px+ touch targets for gloved fingers, zero mandatory free-text entry, and a live SLA countdown clock.
- **Guided 3-Photo Closeout:**
  1. *Optical Power Meter (OPM):* On-device OCR reads and verifies numeric reading (-18.2 dBm) within safe optical attenuation limits.
  2. *Fusion Splice Tray:* Visual check for neat fiber routing and heat shrink protection.
  3. *Premise Entry CSP Box:* Verifies weatherproof grommet and exterior demarcation.
- **1-Tap Scope Mismatch Drawer:** Submits rate variation or SLA pause with automatically bound 10-minute stationary GPS and UTC timestamp.

### Surface 2: Operator Web Console (Next.js / Tailwind)
- **Firm Performance Scorecard:** Benchmarks 200 firms in real-time on SLA Hit Rate (%), First-Time Fix (% 30-day rework-free), and Dispute Rate (%). Eliminates 2 days/month of manual analyst work.
- **Strict 4-Hour Decision SLA:** Visual countdown on paused jobs. Changes from slate to amber (2h) to red (3.5h). *Default Rule:* If the operator stalls past 4 hours, the claim automatically credits in the subcontractor's favor.
- **Side-by-Side Adjudication Queue:** Dispatched contract scope, claimed variation diff (+£45), and raw high-res geotagged photos displayed adjacent to each other.
- **1-Click Action Bar:** Approve (£45), Counter-Offer / Modify, Request More Info, or Reject with mandatory audit reason codes (`EVID-INSUFFICIENT`, `OUT-OF-SCOPE-PERMIT`).

---

## 3. System Architecture & AI Governance

### Degraded Modes Fallback Matrix
| System Endpoint | Mechanism | Data Payload | Degraded Mode (System Unavailable) |
|---|---|---|---|
| **Operator WFM** (Siebel / Netcracker) | PULL / Webhook | Work orders, SLA clock, scope code. | **Circuit Breaker:** Serve cached jobs from Redis/Postgres; buffer updates in Kafka. |
| **Operator GIS** (ESRI / Smallworld) | PULL / REST | DP locations, duct availability, fiber pairs. | **Static Snapshot:** Pre-cached dispatch snapshot used; flags pending check. |
| **Operator Billing** (SAP S/4HANA) | PUSH / Webhook | Completion tokens, self-billing remittance. | **PostgreSQL Outbox:** Resilient transactional outbox retries with idempotency keys. |
| **Weather Feed** (Tomorrow.io) | PULL / Hourly | Winds >35mph, thunderstorm alerts. | **Permissive Fallback:** Auto-allows manual tech pause; flags for spot review. |

> **Enterprise Reality Check:** On Day 1, we ingest via scheduled **SFTP flat-file CSV batch drops** and export self-billing CSVs. Zero dependency on real-time synchronous SOAP/REST APIs for pilot go-live.

### AI Workflow Boundaries: Scope Triage
- **What AI Decides (Model):** OCR reads -18.2 dBm on OPM display; validates trench depth >300mm; detects duplicate/reused photos via perceptual hashing; maps condition to contract rate code (`RC-CIV-04`); generates confidence score (0–100%).
- **What Human Decides (Vendor Manager):** Reviews pre-populated diff card in <30s; executes 100% of binding financial approval clicks; handles ambiguous edge cases; signs audit-trail event for ERP ledger.
- **Where AI is Strictly Forbidden:**
  1. *NO Automated Clawbacks:* Machine financial deductions destroy supplier trust and trigger lawsuits.
  2. *NO Algorithmic De-ranking:* Banning vendors via black-box scoring breaches labor norms.
  3. *NO Auto-Rejection:* Low confidence routes to human queue, never auto-rejected.

---

## 4. Business Model, Unit Economics & 2.86x ROI

### The Subcontractor Margin Law
Subcontractor firms operate on paper-thin **5% to 8% net profit margins**. A 2% SaaS fee charged to them wipes out 25% to 40% of their net profit, inducing immediate defection. **The platform is 100% FREE to subcontractors.**

### Commercial Structure
- **Operator Enterprise SaaS:** £1.20 per completed job (funded by Operator) = **£374,400 ARR** across 312,000 jobs/year.
- **Optional FinTech Fast-Pay:** Standard Net-45 settlement is always free. Optional 48-hour settlement at 1.5% dynamic discount factoring funded by banking partner.

### Operator Year-1 Net ROI Waterfall
```
1. Dispute & Rate Leakage Savings:     +£450,000 / Yr   (Disputes drop from 8% to 2% across 312k jobs)
2. First-Time Fix (FTF) Recovery:      +£795,600 / Yr   (FTF lifts 84% -> 87%; 9,360 avoided truck rolls @ £85)
3. Vendor Management Admin Overhead:   +£200,000 / Yr   (4 FTEs redeployed from spreadsheet audits)
------------------------------------------------------
GROSS ANNUAL VALUE CREATED:            +£1,445,600 / Yr
LESS PLATFORM COST (£1.20/job):         (£374,400) / Yr
------------------------------------------------------
NET ANNUAL OPERATOR SAVINGS:           +£1,071,200 / Yr  (2.86x ROI | Payback in < 5 Months)
```

---

## 5. Go-To-Market Rollout & 18-Month Roadmap

### 4-Phase GTM Rollout (Scaling to 200 Firms in 26 Weeks)
1. **Phase 1: Pilot (Weeks 1–6):** 3 friendly Tier-1 firms (~150 techs, 1,000 jobs/wk) in Northern region. Validates offline sync and <2 min budget. *Carrot: Guaranteed Net-7 payment.*
2. **Phase 2: Top 25 (Weeks 7–16):** Onboard top 25 firms delivering 60% of volume. Dedicated train-the-dispatcher workshops; dispatcher portal live.
3. **Phase 3: Long-Tail (Weeks 17–26):** Remaining 175 small outfits (3–15 techs). Self-serve onboarding via SMS deep link and 3-min video guides.
4. **Phase 4: Mandate (Week 27+):** Billing policy update: unverified paper invoices face 60-day audit queues; platform-verified invoices bypass manual audit to pay in 7 days.

### 18-Month Strategic Horizons
- **Horizon 1 (M1–3) — Core Loop:** Offline mobile app, 4-hour operator console, rate card engine, SFTP flat-file batch drops.
- **Horizon 2 (M4–9) — Smart Field Operations:** AI evidence OCR, predictive van stock replenishment via distributor APIs (Rexel, Graybar), automated radar weather delay shield (>35mph wind mass SLA pause).
- **Horizon 3 (M10–18) — Network Ecosystem:** Peer-to-peer van parts exchange between non-competing crews via QR scan, predictive rework prevention, and collective purchasing consortium for van leasing, fuel cards, and fusion splicers.

---

## 6. Live Roleplays: COO Pitch & Scathing Self-Critique

### 3-Minute COO Executive Pitch Script
> *"Good morning. You run 6,000 fiber jobs every week, with 70% delivered by 200 external partner firms. Right now, that £50 million field operation is managed through a complete blind spot between 8:00 AM dispatch and a disputed invoice arriving 45 days later.*  
> 
> *When a technician finds a collapsed duct or a customer no-show, requests travel over WhatsApp and email. The SLA clock keeps running, deductions feel arbitrary, and subcontractors reassign their top certified crews to your direct competitors who pay faster.*  
> 
> *We sit cleanly between your enterprise systems and the van without ripping and replacing your IT. Technicians get an offline-first app that captures geotagged optical power proof in under 90 seconds. Variations become same-day decisions under a strict 4-hour SLA. In return, you guarantee verified payment in 7 to 14 days, securing your labor supply.*  
> 
> *The Economics: £1.20 per completed job equals £374k annual platform cost. In return, you recover £1.07 million in net savings by cutting dispute leakage and avoiding 9,360 second-truck rolls. That is a 2.86x ROI in year one. Let's launch the 6-week pilot in the Northern region."*

### Scathing Self-Critique & Defensive Countermeasures
| Brutal Failure Mode (Critique) | Defensive Countermeasure |
|---|---|
| **1. Evidence Fraud:** Techs snap random closed gates from vans to pause SLA clocks. | **Triple-Vector Telemetry Binding:** Hardware camera EXIF (blocks gallery uploads) + 10-minute continuous stationary GPS within 30m boundary + OPM OCR validation. Statistical outlier clustering flags abuse patterns. |
| **2. Telco IT Integration Graveyard:** Waiting 18 months for legacy SOAP/WFM APIs will kill the pilot. | **Decoupled Asynchronous SFTP Architecture:** Day 1 runs on scheduled flat-file CSV batch drops of jobs and self-billing remittance outputs. Zero synchronous API dependency for launch. |
| **3. Surveillance Backlash:** Techs strike over an 'electronic ankle monitor' tracking their movement. | **Privacy-by-Design:** Zero continuous background GPS tracking; location polled strictly at arrival and closeout taps. Bi-directional transparency: techs track the operator's decision and payment SLA clocks. |
| **4. Vendor Manager Queue Overload:** 200 daily variation requests will break the 4-hour decision SLA. | **Tiered Algorithmic Auto-Clearance:** Micro-variations (<£25 with >95% AI confidence) auto-approve with a 10% spot audit. Active human queue drops from 200/day to fewer than 35 critical decisions per day. |

---
*Authored by Komal Agarwal | B2B PM Case Study Deliverable | November 2026*
