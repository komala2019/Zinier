import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # blank layout

    # Color Palette
    BG_COLOR = RGBColor(15, 23, 42)         # #0F172A Dark Slate
    CARD_BG = RGBColor(30, 41, 59)          # #1E293B Slate Card
    CARD_BG_ALT = RGBColor(24, 33, 47)      # Slightly darker card
    BORDER_COLOR = RGBColor(51, 65, 85)     # #334155 Slate Border
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_LIGHT = RGBColor(241, 245, 249)    # #F1F5F9
    TEXT_MUTED = RGBColor(148, 163, 184)    # #94A3B8
    BLUE_ACCENT = RGBColor(59, 130, 246)    # #3B82F6
    CYAN_ACCENT = RGBColor(56, 189, 248)    # #38BDF8
    EMERALD_ACCENT = RGBColor(16, 185, 129) # #10B981
    ROSE_ACCENT = RGBColor(244, 63, 94)     # #F43F5E
    AMBER_ACCENT = RGBColor(245, 158, 11)   # #F59E0B

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title, subtitle):
        # Category Pill / Eyebrow
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
        tf = cat_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = category.upper()
        p.font.name = "Arial"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.78), Inches(11.7), Inches(0.6))
        tf2 = title_box.text_frame
        tf2.word_wrap = True
        tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0
        p2 = tf2.paragraphs[0]
        p2.text = title
        p2.font.name = "Arial"
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE

        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.7), Inches(0.4))
        tf3 = sub_box.text_frame
        tf3.word_wrap = True
        tf3.margin_left = tf3.margin_top = tf3.margin_right = tf3.margin_bottom = 0
        p3 = tf3.paragraphs[0]
        p3.text = subtitle
        p3.font.name = "Calibri"
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, bg=CARD_BG, border=BORDER_COLOR):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg
        shape.line.color.rgb = border
        shape.line.width = Pt(1)
        return shape

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: TITLE & EXECUTIVE PROBLEM STATEMENT
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)
    add_header(s1, "Executive Overview | Candidate Case Study Presentation", 
               "The £50M Blind Spot in 6,000 Weekly Fiber Jobs", 
               "Aligning incentives, synchronizing field evidence, and eliminating dispute leakage across 200 subcontractor firms")

    # 3 Stat Cards
    c1 = add_card(s1, Inches(0.8), Inches(2.0), Inches(3.64), Inches(3.2))
    t1 = s1.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(3.24), Inches(2.8))
    tf1 = t1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "~6,000 / Wk"
    p.font.name = "Arial"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf1.add_paragraph()
    p.text = "Massive Field Scale\n"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf1.add_paragraph()
    p.text = "• 70% of installs and repairs delivered by 200 external firms (from 3-person outfits to 400-tech fleets).\n• Interface fragmented across WhatsApp, spreadsheets, and unmonitored email threads.\n• No shared operational truth between van and operator."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_MUTED

    c2 = add_card(s1, Inches(4.84), Inches(2.0), Inches(3.64), Inches(3.2))
    t2 = s1.shapes.add_textbox(Inches(5.04), Inches(2.2), Inches(3.24), Inches(2.8))
    tf2 = t2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "45–60 Days"
    p.font.name = "Arial"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = ROSE_ACCENT
    p = tf2.add_paragraph()
    p.text = "Payment & Dispute Lag\n"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf2.add_paragraph()
    p.text = "• Rate variation requests arrive 4 weeks post-job with no contemporaneous proof.\n• Subcontractors operate on 5–8% net margin; arbitrary deductions threaten cash flow.\n• Technicians reassign scarce certified labor to rival operators who pay faster."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_MUTED

    c3 = add_card(s1, Inches(8.88), Inches(2.0), Inches(3.64), Inches(3.2))
    t3 = s1.shapes.add_textbox(Inches(9.08), Inches(2.2), Inches(3.24), Inches(2.8))
    tf3 = t3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "£1.07M / Yr"
    p.font.name = "Arial"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tf3.add_paragraph()
    p.text = "Net Value Creation (2.86x ROI)\n"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf3.add_paragraph()
    p.text = "• £450k saved by eliminating unverified rate leakage and dispute overhead.\n• £795k recovered by lifting First-Time Fix rate by 3 points (9,360 avoided truck rolls).\n• Subcontractor settlement accelerated from 45 days to 7–14 days."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_MUTED

    # Bottom Summary Banner
    bb = add_card(s1, Inches(0.8), Inches(5.45), Inches(11.72), Inches(1.3), bg=RGBColor(23, 37, 84), border=BLUE_ACCENT)
    tbb = s1.shapes.add_textbox(Inches(1.0), Inches(5.55), Inches(11.32), Inches(1.1))
    tfbb = tbb.text_frame
    tfbb.word_wrap = True
    p = tfbb.paragraphs[0]
    p.text = "THE CORE SHIFT: Replace end-of-month commercial warfare with a real-time, shared source of truth."
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tfbb.add_paragraph()
    p.text = "1. Mobile App (<2 min, offline-first, gloved operation)  |  2. Operator Console (4h Decision SLA, side-by-side evidence)  |  3. Synchronized State Machine (ties field evidence directly to work order, rate card, and self-billing payment milestones)."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(s1, "SPEAKER NOTES:\n- Frame problem around the COO's wallet: £50M+ annual outsourced field budget managed via 1990s spreadsheets and email.\n- Emphasize that we are NOT replacing existing enterprise WFM (Salesforce/Netcracker); we are digitizing the operational interface between the operator and 200 external partner firms.\n- Highlight the 3 core numbers: 6,000 jobs/wk, 45-day payment lag, and £1.07M net year-1 operator value.")

    # =========================================================================
    # SLIDE 2: DISCOVERY & INCENTIVE ALIGNMENT
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Discovery & Alignment | Persona Friction Analysis", 
               "Where the Two Sides Collide: Solving Rejection Triggers", 
               "The platform succeeds only by eliminating the structural reasons each stakeholder would reject it")

    # Column 1: Operator
    c_op = add_card(s2, Inches(0.8), Inches(1.95), Inches(5.7), Inches(3.6))
    top = s2.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.3), Inches(3.3))
    tf_op = top.text_frame
    tf_op.word_wrap = True
    p = tf_op.paragraphs[0]
    p.text = "OPERATOR PERSPECTIVE (Priya & David)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf_op.add_paragraph()
    p.text = "Priya Sharma (Regional Ops) & David Vance (Vendor Commercials)"
    p.font.size = Pt(11)
    p.font.color.rgb = CYAN_ACCENT
    p = tf_op.add_paragraph()
    p.text = "\n• Core Motivation: Regional install velocity, first-time fix rate, margin preservation, strict adherence to contract rate cards."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_LIGHT
    p = tf_op.add_paragraph()
    p.text = "• Current Pain: Rate variations arrive 4 weeks late as £95 disputes; no proof if 'access failure' was legitimate or tech ran late; takes 2 full days monthly to build scorecards."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_LIGHT
    p = tf_op.add_paragraph()
    p.text = "• REJECTION TRIGGER: 'If it requires manual data re-entry or doesn't tie directly to our dispatch and billing systems, my supervisors will ignore it.'"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ROSE_ACCENT

    # Column 2: Subcontractor
    c_sub = add_card(s2, Inches(6.8), Inches(1.95), Inches(5.7), Inches(3.6))
    tsub = s2.shapes.add_textbox(Inches(7.0), Inches(2.1), Inches(5.3), Inches(3.3))
    tf_sub = tsub.text_frame
    tf_sub.word_wrap = True
    p = tf_sub.paragraphs[0]
    p.text = "SUBCONTRACTOR PERSPECTIVE (Imran, Meera & Ravi)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tf_sub.add_paragraph()
    p.text = "Imran Khan (Firm Owner), Meera (Dispatcher), Ravi Patel (Field Tech)"
    p.font.size = Pt(11)
    p.font.color.rgb = CYAN_ACCENT
    p = tf_sub.add_paragraph()
    p.text = "\n• Core Motivation: Cash flow predictability, weekly technician payroll, protection against unfair SLA deductions, zero app friction."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_LIGHT
    p = tf_sub.add_paragraph()
    p.text = "• Current Pain: 6% profit margin wiped out by arbitrary invoice hold-ups; mobile app crashes and loses photos in basements with zero signal."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_LIGHT
    p = tf_sub.add_paragraph()
    p.text = "• REJECTION TRIGGER: 'If you charge my 6% margin a SaaS fee, or if the app adds more than 2 minutes per job, we will shift our vans to your rival.'"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ROSE_ACCENT

    # Bottom Table: How We Resolve the Conflict
    t_res = add_card(s2, Inches(0.8), Inches(5.7), Inches(11.7), Inches(1.25), bg=CARD_BG_ALT)
    tb_res = s2.shapes.add_textbox(Inches(1.0), Inches(5.75), Inches(11.3), Inches(1.15))
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True
    p = tf_res.paragraphs[0]
    p.text = "THE INCENTIVE COMPACT:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT
    p = tf_res.add_paragraph()
    p.text = "1. Rate Variations: Operator gets geotagged photo proof on-site  ←→  Subcontractor gets binding 4-hour decision turnaround.\n2. SLA Enforcement: Operator prevents false access claims  ←→  Subcontractor auto-attaches GPS/timestamp to prove presence.\n3. Monetization: Operator funds platform via leakage savings (£1.20/job)  ←→  Core platform is 100% FREE for subcontractors."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(s2, "SPEAKER NOTES:\n- Highlight that subcontractor firms run on 5-8% net margins. A 2% SaaS fee wipes out 30-40% of their bottom line!\n- Show that you understand the human side: Meera in dispatch juggling WhatsApp, Ravi in a rainy alley with cold hands, David Vance buried under unverified invoice disputes.\n- Emphasize the Incentive Compact: neither side loses.")

    # =========================================================================
    # SLIDE 3: FIELD TECH MOBILE APP & ONBOARDING (ITEM 2.1)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Item 2.1 UX Architecture | Technician Mobile Surface", 
               "Field Tech Mobile App & Zero-Friction Onboarding", 
               "Engineered for dirty hands, heavy safety gloves, low-end Androids, and zero cellular signal")

    # 3 Core Pillars
    w3 = Inches(3.64)
    c31 = add_card(s3, Inches(0.8), Inches(1.95), w3, Inches(2.6))
    tx31 = s3.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(3.24), Inches(2.4))
    tfx31 = tx31.text_frame
    tfx31.word_wrap = True
    p = tfx31.paragraphs[0]
    p.text = "01 | 6-Step Fast Onboarding"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tfx31.add_paragraph()
    p.text = "• Dispatched via SMS invite deep link.\n• Auto-reads 6-digit OTP; binds phone to firm.\n• Plain-English permissions (Camera & GPS).\n• Pre-caches region rate cards & maps (12MB).\n• 45-sec interactive tour (skippable).\n• Ready for first job in < 3 minutes."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    c32 = add_card(s3, Inches(4.84), Inches(1.95), w3, Inches(2.6))
    tx32 = s3.shapes.add_textbox(Inches(5.04), Inches(2.05), Inches(3.24), Inches(2.4))
    tfx32 = tx32.text_frame
    tfx32.word_wrap = True
    p = tfx32.paragraphs[0]
    p.text = "02 | Offline as Default State"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT
    p = tfx32.add_paragraph()
    p.text = "• UI never blocks on network requests.\n• Local encrypted SQLite database.\n• Monotonic client sequence numbers & GPS UTC stamps prevent duplicate actions.\n• Background sync daemon with exponential backoff on reconnect.\n• WebP compression: <200 KB per photo."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    c33 = add_card(s3, Inches(8.88), Inches(1.95), w3, Inches(2.6))
    tx33 = s3.shapes.add_textbox(Inches(9.08), Inches(2.05), Inches(3.24), Inches(2.4))
    tfx33 = tx33.text_frame
    tfx33.word_wrap = True
    p = tfx33.paragraphs[0]
    p.text = "03 | <120-Sec Friction Budget"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tfx33.add_paragraph()
    p.text = "• 4-tap complete workflow.\n• Zero mandatory free-text fields.\n• 48px+ touch targets for gloved fingers.\n• 3 guided camera snaps (OPM dBm OCR, splice tray, premise box).\n• Prominent live SLA countdown timer.\n• 1-tap request drawer auto-attaches GPS."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    # Bottom Screen Flow
    c_flow = add_card(s3, Inches(0.8), Inches(4.75), Inches(11.72), Inches(2.2), bg=CARD_BG_ALT)
    t_flow = s3.shapes.add_textbox(Inches(1.0), Inches(4.85), Inches(11.32), Inches(2.0))
    tff = t_flow.text_frame
    tff.word_wrap = True
    p = tff.paragraphs[0]
    p.text = "CORE MOBILE SCREENS ARCHITECTURE (Interactive in wireframes.html)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tff.add_paragraph()
    p.text = "\n[Screen 1: Job Queue]  →  [Screen 2: Guided Evidence Capture]  →  [Screen 3: Raise Request / Pause Clock]"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tff.add_paragraph()
    p.text = "• Screen 1: Shows daily route, van inventory (ONTs, patch cords), live SLA badge, and offline outbox status badge.\n• Screen 2: 3 structured photo prompts with on-device blur detection and OCR validation (-18.2 dBm on OPM display).\n• Screen 3: Single-tap category selection (Mis-scoped variation, SLA pause, customer no-show) with instant clock pause."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(s3, "SPEAKER NOTES:\n- Explain that technicians are piece-rate workers: every 5 minutes lost to app friction means one less install per day.\n- Point out why the offline model is foundational: basements and rural fiber drops frequently have zero 4G signal. If an app spins and drops data, techs revolt.\n- Reference wireframes.html where this exact mobile interface can be tested live.")

    # =========================================================================
    # SLIDE 4: OPERATOR CONSOLE & 4-HOUR DECISION SLA (ITEM 2.2)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Item 2.2 Operator Web Console | Management Surface", 
               "Performance Management & 4-Hour Decision SLA", 
               "Connecting regional capacity benchmarking with real-time commercial dispute triage")

    # Feature 1: Scorecard
    c41 = add_card(s4, Inches(0.8), Inches(1.95), Inches(5.7), Inches(3.6))
    tx41 = s4.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.3), Inches(3.3))
    tfx41 = tx41.text_frame
    tfx41.word_wrap = True
    p = tfx41.paragraphs[0]
    p.text = "FIRM PERFORMANCE SCORECARD"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tfx41.add_paragraph()
    p.text = "Real-time benchmarking across 200 subcontractor firms"
    p.font.size = Pt(11)
    p.font.color.rgb = CYAN_ACCENT
    p = tfx41.add_paragraph()
    p.text = "\n• Replaces 2 days of monthly spreadsheet stitching by regional analysts."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_LIGHT
    p = tfx41.add_paragraph()
    p.text = "• Core Tracked Metrics:\n  - SLA Hit Rate (% on-time completion against contract window)\n  - First-Time Fix (FTF) Rate (30-day rework-free installations)\n  - Rate Variation & Dispute Frequency (% claims raised vs peers)\n  - Decision-to-Settlement Velocity (days from job to paid invoice)"
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tfx41.add_paragraph()
    p.text = "\n• Objective Allocation: High-performing firms (e.g., Apex Fiber: 94.2% SLA, 91% FTF) automatically win higher regional dispatch priority."
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

    # Feature 2: Side-by-Side Adjudication
    c42 = add_card(s4, Inches(6.8), Inches(1.95), Inches(5.7), Inches(3.6))
    tx42 = s4.shapes.add_textbox(Inches(7.0), Inches(2.1), Inches(5.3), Inches(3.3))
    tfx42 = tx42.text_frame
    tfx42.word_wrap = True
    p = tfx42.paragraphs[0]
    p.text = "SIDE-BY-SIDE ADJUDICATION QUEUE"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tfx42.add_paragraph()
    p.text = "Adjudicate field claims in <30 seconds with 100% contract fidelity"
    p.font.size = Pt(11)
    p.font.color.rgb = CYAN_ACCENT
    p = tfx42.add_paragraph()
    p.text = "\n• Dispatched Scope vs Claimed Scope: Automatic diff showing line-by-line contract rate card variation (e.g., +25m soft dig: +£45.00)."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_LIGHT
    p = tfx42.add_paragraph()
    p.text = "• Contemporaneous Photo & GPS Proof: High-res images, GPS breadcrumb verification, and OCR readings displayed side-by-side."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tfx42.add_paragraph()
    p.text = "• Binding 4-Hour Decision SLA: Amber countdown at 2 hours, Red at 3.5 hours. If operator fails to respond, claim defaults in subcontractor's favor."
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT
    p = tfx42.add_paragraph()
    p.text = "• Standardized Reason Codes: Rejections require coded audit rationale (e.g., EVID-INSUFFICIENT) to eliminate arbitrary non-payment."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    # Action Banner
    c4b = add_card(s4, Inches(0.8), Inches(5.7), Inches(11.7), Inches(1.25), bg=CARD_BG_ALT)
    t4b = s4.shapes.add_textbox(Inches(1.0), Inches(5.75), Inches(11.3), Inches(1.15))
    tf4b = t4b.text_frame
    tf4b.word_wrap = True
    p = tf4b.paragraphs[0]
    p.text = "OPERATOR ACTIONS: 1-Click Approve (£45)  |  Counter-Offer / Modify  |  Request More Info  |  Reject (Coded)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tf4b.add_paragraph()
    p.text = "Pre-clears self-billing line items before invoice generation, dropping dispute cycle time from 45 days to 1.4 days."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(s4, "SPEAKER NOTES:\n- Emphasize the Operator Decision SLA: this is the biggest olive branch to the subcontractor.\n- For years, operators let variation emails sit in inboxes for weeks. Enforcing a 4-hour decision SLA keeps technicians moving and builds trust.\n- Show how David Vance saves 4 FTEs worth of manual spreadsheet reconciliations.")

    # =========================================================================
    # SLIDE 5: SYSTEM & API ARCHITECTURE (ITEM 2.3)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Item 2.3 System Architecture | Integration & Resilience", 
               "API Architecture & Degraded Resiliency Modes", 
               "Decoupled, event-driven design engineered to thrive despite legacy telco IT downtime")

    # Left: Enterprise Systems of Record
    c51 = add_card(s5, Inches(0.8), Inches(1.95), Inches(5.7), Inches(4.0))
    t51 = s5.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(5.3), Inches(3.8))
    tf51 = t51.text_frame
    tf51.word_wrap = True
    p = tf51.paragraphs[0]
    p.text = "OPERATOR SYSTEMS OF RECORD (SoR)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf51.add_paragraph()
    p.text = "1. Work Orders (WFM / Siebel / Netcracker) [PULL / WEBHOOK]\n   • Payload: Address, premise type, target SLA, dispatched scope code.\n   • Degraded Mode: Redis/Postgres caching + Kafka queue buffers."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf51.add_paragraph()
    p.text = "\n2. Network Inventory / GIS (ESRI / GE Smallworld) [PULL]\n   • Payload: DP locations, duct availability, fiber pair allocations.\n   • Degraded Mode: Static GIS snapshot pre-cached at dispatch time."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf51.add_paragraph()
    p.text = "\n3. Contract Rate Cards & Agreements [PULL / BATCH]\n   • Payload: Line item prices, approved variation codes, penalty rules.\n   • Degraded Mode: Stale-While-Revalidate locks to last-known signed rate."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf51.add_paragraph()
    p.text = "\n4. Billing & ERP (SAP S/4HANA / Oracle Financials) [PUSH]\n   • Payload: Approved job completion tokens, self-billing remittance.\n   • Degraded Mode: Resilient transactional outbox with idempotency keys."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    # Right: 3rd Party Integrations & Edge
    c52 = add_card(s5, Inches(6.8), Inches(1.95), Inches(5.7), Inches(4.0))
    t52 = s5.shapes.add_textbox(Inches(7.0), Inches(2.05), Inches(5.3), Inches(3.8))
    tf52 = t52.text_frame
    tf52.word_wrap = True
    p = tf52.paragraphs[0]
    p.text = "3RD-PARTY FEEDS & EDGE ARCHITECTURE"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tf52.add_paragraph()
    p.text = "1. Weather Intelligence (Tomorrow.io API) [PULL]\n   • Feeds: Sustained winds (>35mph), heavy rain, thunderstorm alerts.\n   • Degraded Mode: Defaults to permissive; allows manual tech pause."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf52.add_paragraph()
    p.text = "\n2. Traffic & Routing (Mapbox API) [PULL]\n   • Feeds: Live drive-time ETAs and route sequence optimization.\n   • Degraded Mode: Local Haversine straight-line distance fallback."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf52.add_paragraph()
    p.text = "\n3. National Fiber Tech Registry [PULL]\n   • Feeds: Working at Heights, Confined Space, Fusion Splice cert dates.\n   • Degraded Mode: 7-day grace period on cached status; warning banner."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf52.add_paragraph()
    p.text = "\n4. Edge & Event Core (React Native, Kong Gateway, Kafka, Postgres)\n   • End-to-end encryption, multi-tenant RBAC, and client CRDT conflict resolution."
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT

    # Footer note
    c5b = add_card(s5, Inches(0.8), Inches(6.1), Inches(11.7), Inches(0.9), bg=CARD_BG_ALT)
    t5b = s5.shapes.add_textbox(Inches(1.0), Inches(6.15), Inches(11.3), Inches(0.8))
    tf5b = t5b.text_frame
    tf5b.word_wrap = True
    p = tf5b.paragraphs[0]
    p.text = "ENTERPRISE REALITY CHECK: On Day 1, we ingest via flat-file SFTP CSV batch drops. We don't block pilot rollout waiting 12 months for telco IT to build REST APIs."
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT

    add_notes(s5, "SPEAKER NOTES:\n- Telco IT systems are notoriously legacy (SOAP, Oracle, Siebel). Address this head-on.\n- We use an asynchronous, circuit-broken thin-integration architecture: flat-file SFTP batch drops on Day 1, Kafka/REST streaming in Phase 2.\n- Explain the Degraded Mode strategy: field technicians never get blocked because an ERP or GIS database is undergoing maintenance.")

    # =========================================================================
    # SLIDE 6: AI WORKFLOW DEEP DIVE (ITEM 2.4)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Item 2.4 AI Architecture | Evidence Verification & Scope Triage", 
               "Where AI Earns Its Place: Scope Triage Workflow", 
               "Automating photographic evidence synthesis and contract matching while keeping financial liability 100% human")

    # 3 Columns: Model Decides, Human Decides, Forbidden
    w6 = Inches(3.64)
    c61 = add_card(s6, Inches(0.8), Inches(1.95), w6, Inches(4.0))
    t61 = s6.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(3.24), Inches(3.8))
    tf61 = t61.text_frame
    tf61.word_wrap = True
    p = tf61.paragraphs[0]
    p.text = "WHAT AI MODEL DECIDES"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf61.add_paragraph()
    p.text = "Computer Vision & OCR Engine\n"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tf61.add_paragraph()
    p.text = "• OCR on Optical Power Meter (-18.2 dBm reading extraction).\n• Validates trench depth (>300mm) and duct clearance from photo.\n• Perceptual hashing detects reused or duplicate photos from previous jobs.\n• Maps field condition to contractual Rate Card Code (e.g., RC-CIV-08).\n• Computes confidence score (0-100%)."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    c62 = add_card(s6, Inches(4.84), Inches(1.95), w6, Inches(4.0))
    t62 = s6.shapes.add_textbox(Inches(5.04), Inches(2.05), Inches(3.24), Inches(3.8))
    tf62 = t62.text_frame
    tf62.word_wrap = True
    p = tf62.paragraphs[0]
    p.text = "WHAT HUMAN DECIDES"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tf62.add_paragraph()
    p.text = "Human-in-the-Loop Vendor Manager\n"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tf62.add_paragraph()
    p.text = "• Reviews pre-populated diff card in under 30 seconds.\n• Executes 100% of binding financial approval clicks.\n• The model NEVER has authority to disburse funds or commit financial liability.\n• Adjudicates ambiguous site conditions.\n• Modifies rates or makes counter-offers."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    c63 = add_card(s6, Inches(8.88), Inches(1.95), w6, Inches(4.0), bg=RGBColor(40, 16, 24), border=ROSE_ACCENT)
    t63 = s6.shapes.add_textbox(Inches(9.08), Inches(2.05), Inches(3.24), Inches(3.8))
    tf63 = t63.text_frame
    tf63.word_wrap = True
    p = tf63.paragraphs[0]
    p.text = "WHERE AI IS FORBIDDEN"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ROSE_ACCENT
    p = tf63.add_paragraph()
    p.text = "Strict Ethical & Operational Boundaries\n"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf63.add_paragraph()
    p.text = "• NO Automated Clawbacks: Machine deductions destroy supplier trust and trigger lawsuits.\n• NO Algorithmic De-ranking: Banning vendors based on black-box scoring breaches labor norms.\n• NO Automatic Rejections: Low confidence flags route to human review queue, never auto-rejected."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    # Bottom KPIs
    c6b = add_card(s6, Inches(0.8), Inches(6.1), Inches(11.7), Inches(0.9), bg=CARD_BG_ALT)
    t6b = s6.shapes.add_textbox(Inches(1.0), Inches(6.15), Inches(11.3), Inches(0.8))
    tf6b = t6b.text_frame
    tf6b.word_wrap = True
    p = tf6b.paragraphs[0]
    p.text = "AI SUCCESS CRITERIA: Triage review latency cut by 80% (<90 seconds)  |  Human override rate <15%  |  Dispute recurrence <2%."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    add_notes(s6, "SPEAKER NOTES:\n- Interviewers love asking 'Where do you NOT use AI?' Stand firm on this: AI should NEVER touch clawbacks, financial deductions, or algorithmic firing/de-ranking.\n- AI pre-populates the diff card and validates OCR and photo freshness; the vendor manager clicks approve.\n- High-confidence low-value variations (<£25) can auto-clear with a 10% random human spot audit.")

    # =========================================================================
    # SLIDE 7: IMPLEMENTATION CHALLENGES & MITIGATIONS (ITEM 2.5)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Item 2.5 Risk Management | Execution Pragmatism", 
               "Implementation Challenges & Enterprise Mitigations", 
               "Navigating technical constraints, behavioral inertia, and multi-tenant commercial boundaries")

    # 3 Challenge Cards
    c71 = add_card(s7, Inches(0.8), Inches(1.95), w6, Inches(4.9))
    t71 = s7.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(3.24), Inches(4.6))
    tf71 = t71.text_frame
    tf71.word_wrap = True
    p = tf71.paragraphs[0]
    p.text = "01 | TECHNICAL CHALLENGE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT
    p = tf71.add_paragraph()
    p.text = "24,000 Photos/Week over Congested Edge Networks\n"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf71.add_paragraph()
    p.text = "• The Reality: 6,000 jobs/wk × 4 photos = ~12GB uncompressed media uploaded by technicians with sub-1 Mbps uplink in rural areas."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_MUTED
    p = tf71.add_paragraph()
    p.text = "\n• The Architectural Solution:\n  - On-device WebP progressive compression (<200KB per image).\n  - Priority metadata sync first (<5KB JSON), followed by chunked background upload queue.\n  - CRDT-based offline conflict resolution."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    c72 = add_card(s7, Inches(4.84), Inches(1.95), w6, Inches(4.9))
    t72 = s7.shapes.add_textbox(Inches(5.04), Inches(2.1), Inches(3.24), Inches(4.6))
    tf72 = t72.text_frame
    tf72.word_wrap = True
    p = tf72.paragraphs[0]
    p.text = "02 | ADOPTION CHALLENGE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf72.add_paragraph()
    p.text = "Dispatcher Inertia & Tech Cynicism ('WhatsApp Habits')\n"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf72.add_paragraph()
    p.text = "• The Reality: Dispatchers run 70 jobs/day via WhatsApp groups; technicians view field software as operator surveillance."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_MUTED
    p = tf72.add_paragraph()
    p.text = "\n• The Adoption Solution:\n  - 1-click WhatsApp deep-link invite bridges during first 30 days.\n  - Immediate technician value: offline premises diagrams, auto customer calling, no evening paperwork.\n  - No background GPS tracking (ephemeral event-only geofence)."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    c73 = add_card(s7, Inches(8.88), Inches(1.95), w6, Inches(4.9))
    t73 = s7.shapes.add_textbox(Inches(9.08), Inches(2.1), Inches(3.24), Inches(4.6))
    tf73 = t73.text_frame
    tf73.word_wrap = True
    p = tf73.paragraphs[0]
    p.text = "03 | COMMERCIAL CHALLENGE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ROSE_ACCENT
    p = tf73.add_paragraph()
    p.text = "Multi-Tenant Data Privacy Between Competitors\n"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf73.add_paragraph()
    p.text = "• The Reality: 200 subcontractor firms compete fiercely for territory and simultaneously contract for rival telcos."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_MUTED
    p = tf73.add_paragraph()
    p.text = "\n• The Governance Solution:\n  - Strict cryptographic tenant isolation.\n  - Firm A never sees Firm B's scorecards, capacity, or rate structures.\n  - Operator sees only work orders dispatched on their own network; third-party telco jobs are completely invisible."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(s7, "SPEAKER NOTES:\n- Address edge network realities: 12GB of photos every week uploaded from rural lanes and basements. Progressive WebP compression is essential.\n- Emphasize multi-tenant privacy: Imran Khan must know that rival firm Apex Fiber cannot see his rates or technician capacity.")

    # =========================================================================
    # SLIDE 8: BUSINESS MODEL & UNIT ECONOMICS (ITEM 2.6)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Item 2.6 Financial Engine | Monetization & ROI", 
               "Business Model, Unit Economics & 2.86x Operator ROI", 
               "Preserving thin subcontractor margins while creating £1.07M in verifiable net annual value for the operator")

    # Left: Commercial Model
    c81 = add_card(s8, Inches(0.8), Inches(1.95), Inches(5.7), Inches(4.9))
    t81 = s8.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.3), Inches(4.6))
    tf81 = t81.text_frame
    tf81.word_wrap = True
    p = tf81.paragraphs[0]
    p.text = "THE COMMERCIAL ARCHITECTURE"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf81.add_paragraph()
    p.text = "Why Charging Subcontractors is Fatal for Adoption:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ROSE_ACCENT
    p = tf81.add_paragraph()
    p.text = "• Subcontractors operate on razor-thin 5% to 8% net profit margins.\n• A 2% SaaS fee wipes out 25–40% of their bottom line; they will immediately redirect their certified workforce to competing broadband operators.\n• CORE PLATFORM IS 100% FREE TO SUBCONTRACTORS."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf81.add_paragraph()
    p.text = "\nMonetization Stream 1: Operator Enterprise SaaS\n• £1.20 per completed job, paid by the Operator.\n• At 312,000 jobs/year = £374,400 Annual Recurring Revenue (ARR)."
    p.font.size = Pt(11)
    p.font.color.rgb = CYAN_ACCENT
    p = tf81.add_paragraph()
    p.text = "\nMonetization Stream 2: Fast-Pay FinTech Module (Optional)\n• Standard Net-45 settlement is always free.\n• Optional 48h settlement via 1.5% dynamic discount factoring, funded by banking facility. Subcontractors unlock working capital."
    p.font.size = Pt(10.5)
    p.font.color.rgb = EMERALD_ACCENT

    # Right: Operator ROI Waterfall
    c82 = add_card(s8, Inches(6.8), Inches(1.95), Inches(5.7), Inches(4.9))
    t82 = s8.shapes.add_textbox(Inches(7.0), Inches(2.1), Inches(5.3), Inches(4.6))
    tf82 = t82.text_frame
    tf82.word_wrap = True
    p = tf82.paragraphs[0]
    p.text = "OPERATOR YEAR-1 ROI WATERFALL"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tf82.add_paragraph()
    p.text = "1. Dispute & Rate Leakage Reduction:  +£450,000 / Yr\n   • Dispute rate drops from 8% to 2% across 312k jobs.\n   • Eliminates £24 average leakage on contentious claims."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf82.add_paragraph()
    p.text = "\n2. First-Time Fix (FTF) Recovery:  +£795,600 / Yr\n   • Baseline 84% FTF lifts to 87% (+3 percentage points).\n   • Eliminates 9,360 second-truck rolls @ £85 average cost."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf82.add_paragraph()
    p.text = "\n3. Vendor Management Admin Overhead:  +£200,000 / Yr\n   • 4 FTEs redeployed from manual spreadsheet audits."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT
    p = tf82.add_paragraph()
    p.text = "\n• Gross Annual Value Creation: £1,445,600 / Yr\n• Less Platform Cost (£1.20/job): (£374,400) / Yr"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf82.add_paragraph()
    p.text = "• NET ANNUAL OPERATOR BENEFIT: £1,071,200\n  → 2.86x Net Return on Investment (Payback < 5 Months)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    add_notes(s8, "SPEAKER NOTES:\n- Walk through the ROI numbers crisply: £1.20/job = £374k ARR. Gross savings = £1.45M. Net savings = £1.07M.\n- Reiterate the strategic principle: do not charge the subcontractor for software the operator mandates. Align incentives through faster payments.")

    # =========================================================================
    # SLIDE 9: GO-TO-MARKET STRATEGY (ITEM 2.7)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Item 2.7 Ecosystem Scaling | Change Management", 
               "Go-To-Market Strategy: Scaling to 200 Firms", 
               "A 4-phase, 26-week rollout combining operational incentives (carrots) with billing compliance (sticks)")

    # 4 Phase Cards across width
    w4 = Inches(2.7)
    c91 = add_card(s9, Inches(0.8), Inches(1.95), w4, Inches(3.8))
    t91 = s9.shapes.add_textbox(Inches(0.95), Inches(2.05), Inches(2.4), Inches(3.6))
    tf91 = t91.text_frame
    tf91.word_wrap = True
    p = tf91.paragraphs[0]
    p.text = "PHASE 1 (W1-6)\nAnchor Pilot"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf91.add_paragraph()
    p.text = "\n• Cohort: 3 Tier-1 tech-forward firms (~150 techs, 1,000 jobs/wk) in 1 region.\n• Focus: Validate offline sync stability, fine-tune AI vision triage, ensure <2 min friction budget.\n• Carrot: Guaranteed Net-7 day payment settlement on platform jobs."
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_LIGHT

    c92 = add_card(s9, Inches(3.8), Inches(1.95), w4, Inches(3.8))
    t92 = s9.shapes.add_textbox(Inches(3.95), Inches(2.05), Inches(2.4), Inches(3.6))
    tf92 = t92.text_frame
    tf92.word_wrap = True
    p = tf92.paragraphs[0]
    p.text = "PHASE 2 (W7-16)\nTop 25 Expansion"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tf92.add_paragraph()
    p.text = "\n• Cohort: Top 25 largest firms representing ~60% of total weekly volume.\n• Focus: Half-day 'Train the Dispatcher' workshops; dispatchers onboard techs via bulk SMS links.\n• Milestones: Dispatcher portal live; rate card variation queue integrated."
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_LIGHT

    c93 = add_card(s9, Inches(6.8), Inches(1.95), w4, Inches(3.8))
    t93 = s9.shapes.add_textbox(Inches(6.95), Inches(2.05), Inches(2.4), Inches(3.6))
    tf93 = t93.text_frame
    tf93.word_wrap = True
    p = tf93.paragraphs[0]
    p.text = "PHASE 3 (W17-26)\nLong-Tail 175"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT
    p = tf93.add_paragraph()
    p.text = "\n• Cohort: Remaining 175 smaller firms (3–15 technicians each).\n• Focus: Self-serve low-touch digital onboarding; zero app-store download (PWA/self-updating APK).\n• Support: 3-min localized video guides and live in-app chat."
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_LIGHT

    c94 = add_card(s9, Inches(9.8), Inches(1.95), w4, Inches(3.8))
    t94 = s9.shapes.add_textbox(Inches(9.95), Inches(2.05), Inches(2.4), Inches(3.6))
    tf94 = t94.text_frame
    tf94.word_wrap = True
    p = tf94.paragraphs[0]
    p.text = "PHASE 4 (W27+)\nNetwork Mandate"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tf94.add_paragraph()
    p.text = "\n• Policy Shift: Operator updates billing terms: unverified paper invoices face 60-day manual audit queue.\n• Fast Path: Platform-verified invoices bypass audit into automated 7-day payment run.\n• Result: 100% digital compliance."
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_LIGHT

    # Bottom Banner: Carrot vs Stick
    c9b = add_card(s9, Inches(0.8), Inches(5.95), Inches(11.7), Inches(1.0), bg=CARD_BG_ALT)
    t9b = s9.shapes.add_textbox(Inches(1.0), Inches(6.0), Inches(11.3), Inches(0.9))
    tf9b = t9b.text_frame
    tf9b.word_wrap = True
    p = tf9b.paragraphs[0]
    p.text = "THE CARROT & STICK BALANCE: Accelerated payment velocity (Net-7) attracts vendor leadership; proof protection against false customer claims wins technician adoption; contract billing rules close the loop."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(s9, "SPEAKER NOTES:\n- Explain enterprise adoption phasing: never force 200 vendors simultaneously. Start with 3 anchor firms to prove value and eliminate bugs.\n- Focus on the 'Carrot & Stick': fast payments pull firms in; contract billing policies prevent regression to messy WhatsApp threads.")

    # =========================================================================
    # SLIDE 10: STRATEGIC ROADMAP (ITEM 2.8)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Item 2.8 Strategic Horizons | Long-Term Platform Moat", 
               "Strategic Roadmap: Beyond the Core Loop", 
               "Expanding from operational dispute resolution into an indispensable ecosystem platform")

    # 3 Horizons across 3 vertical blocks
    c101 = add_card(s10, Inches(0.8), Inches(1.95), w6, Inches(4.9))
    t101 = s10.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(3.24), Inches(4.6))
    tf101 = t101.text_frame
    tf101.word_wrap = True
    p = tf101.paragraphs[0]
    p.text = "HORIZON 1 (M1 – 3)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf101.add_paragraph()
    p.text = "Digitize the Core Loop\n"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf101.add_paragraph()
    p.text = "• Offline-first React Native mobile app with SQLite outbox queue.\n• Operator Request Resolution Console with 4-hour decision countdown.\n• Rate card state machine and automated self-billing invoice generation.\n• Flat-file SFTP batch ingestion and ERP AP export.\n• Single-region anchor pilot (Northern)."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    c102 = add_card(s10, Inches(4.84), Inches(1.95), w6, Inches(4.9))
    t102 = s10.shapes.add_textbox(Inches(5.04), Inches(2.1), Inches(3.24), Inches(4.6))
    tf102 = t102.text_frame
    tf102.word_wrap = True
    p = tf102.paragraphs[0]
    p.text = "HORIZON 2 (M4 – 9)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tf102.add_paragraph()
    p.text = "Smart Field Operations\n"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf102.add_paragraph()
    p.text = "• AI Evidence Triage & OCR (Optical power meter reading verification).\n• Predictive Van Stock Replenishment: Integrates with distributor APIs (Graybar, Rexel) to pre-stage drop cable by geography.\n• Automated Weather Delay Shield: Radar-triggered mass SLA pauses for winds >35mph.\n• Optional Fast-Pay FinTech liquidity module."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    c103 = add_card(s10, Inches(8.88), Inches(1.95), w6, Inches(4.9))
    t103 = s10.shapes.add_textbox(Inches(9.08), Inches(2.1), Inches(3.24), Inches(4.6))
    tf103 = t103.text_frame
    tf103.word_wrap = True
    p = tf103.paragraphs[0]
    p.text = "HORIZON 3 (M10 – 18)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tf103.add_paragraph()
    p.text = "Network Ecosystem\n"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf103.add_paragraph()
    p.text = "• Peer-to-Peer Van Parts Exchange: Non-competing field crews swap optical splitters/splice trays via QR scan.\n• Predictive Rework Prevention: Machine learning flags chronic repeat-fault drop locations.\n• Collective Purchasing Consortium: Bulk group buying for van insurance, fuel cards, and fusion splicer leasing."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(s10, "SPEAKER NOTES:\n- Show long-term product vision: we start by fixing the friction loop (H1), optimize field intelligence (H2), and evolve into the industry operating system (H3).\n- Point out the Peer-to-Peer parts exchange: stops technicians from driving 45 minutes to a distant depot just to grab one optical splitter.")

    # =========================================================================
    # SLIDE 11: ROLEPLAYS — COO PITCH & SCATHING CRITIQUE (TASKS 3 & 4)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "Tasks 3 & 4 Roleplays | Executive Persuasion & Intellectual Rigor", 
               "The COO Executive Pitch & Defensive Teardown", 
               "Demonstrating commercial leadership, operational empathy, and fearless architectural self-awareness")

    # Left: Pitch
    c111 = add_card(s11, Inches(0.8), Inches(1.95), Inches(5.7), Inches(4.9), border=BLUE_ACCENT)
    t111 = s11.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.3), Inches(4.6))
    tf111 = t111.text_frame
    tf111.word_wrap = True
    p = tf111.paragraphs[0]
    p.text = "TASK 3: 5-MIN COO PITCH SUMMARY"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p = tf111.add_paragraph()
    p.text = "Core Talking Track for Operator Leadership:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p = tf111.add_paragraph()
    p.text = "• The Blind Spot: 'You deliver 6,000 fiber jobs/wk; 70% outsourced. Right now that £50M operation is a complete black box between 8am dispatch and 45-day invoice.'\n• The Friction: 'Unverified requests travel over WhatsApp and email. Technicians face arbitrary penalties and reassign their top vans to your competitors.'\n• The Bridge: 'We sit cleanly between your Netcracker/SAP systems and the van. Sub-90-second photo proof, 4-hour decision SLA, guaranteed 7-day payment.'\n• The Financial ROI: '£374k annual platform cost delivers £1.07M net annual savings (2.86x ROI). Payback in <5 months.'\n• The Immediate Next Step: '6-week pilot in Northern Region with 3 key firms (150 technicians).'"
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_LIGHT

    # Right: Critique
    c112 = add_card(s11, Inches(6.8), Inches(1.95), Inches(5.7), Inches(4.9), border=ROSE_ACCENT)
    t112 = s11.shapes.add_textbox(Inches(7.0), Inches(2.1), Inches(5.3), Inches(4.6))
    tf112 = t112.text_frame
    tf112.word_wrap = True
    p = tf112.paragraphs[0]
    p.text = "TASK 4: SCATHING SELF-CRITIQUE & DEFENSE"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ROSE_ACCENT
    p = tf112.add_paragraph()
    p.text = "Anticipating Brutal Real-World Failure Modes:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p = tf112.add_paragraph()
    p.text = "1. Evidence Fraud: Techs take photos of random closed gates to pause SLA.\n   → Defense: Triple-Vector Telemetry (Camera EXIF + 10-min stationary GPS within 30m boundary + OPM OCR).\n\n2. Telco IT Integration Graveyard: Waiting 18 months for legacy SOAP/WFM APIs.\n   → Defense: Decoupled SFTP flat-file CSV ingestion on Day 1; REST/Kafka in Phase 2.\n\n3. Surveillance Backlash: Techs sabotage GPS or strike over 'electronic ankle monitor.'\n   → Defense: Zero continuous background tracking; location polled only at arrival/closeout.\n\n4. Vendor Manager Queue Overload: 200 requests/day breaks the 4h decision SLA.\n   → Defense: Tiered auto-clearance (<£25 auto-approves with 10% spot check; human queue drops to <35/day)."
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(s11, "SPEAKER NOTES:\n- Conclude the presentation by demonstrating both persuasive executive command (Task 3) and brutal intellectual self-honesty (Task 4).\n- Highlight that true senior product managers don't just sell visions; they anticipate every real-world operational failure mode and build resilient defensive countermeasures.")

    # Save Presentation
    output_path = os.path.join(os.getcwd(), "presentation_deck.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    create_presentation()
