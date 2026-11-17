"""Generate FixKardo landing-page image brief PDF for the graphic designer."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    KeepTogether,
    HRFlowable,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("Nirmala", r"C:\Windows\Fonts\Nirmala.ttc", subfontIndex=0))


def hi(text: str) -> str:
    """Wrap Devanagari so Helvetica pages still render Hindi."""
    return f'<font name="Nirmala">{text}</font>'

OUT = r"C:\Users\Lenovo\Desktop\Projects Websites\FixKardo Landing Pages\FixKardo-Landing-Pages-Image-Brief.pdf"

GREEN = HexColor("#0F9F59")
YELLOW = HexColor("#F4B400")
NAVY = HexColor("#0F172A")
MUTED = HexColor("#475569")
LIGHT = HexColor("#E8F5EE")
BORDER = HexColor("#D1E7D9")
DARK = HexColor("#112119")

W, H = A4


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(GREEN)
    canvas.rect(0, H - 8 * mm, W, 8 * mm, fill=1, stroke=0)
    canvas.setFillColor(HexColor("#F1F5F9"))
    canvas.rect(0, 0, W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(18 * mm, 5 * mm, "FixKardo · Meta Ads Landing Pages · Image Brief for Designer")
    canvas.drawRightString(W - 18 * mm, 5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    canvas.setFillColor(GREEN)
    canvas.rect(0, H - 28 * mm, W, 28 * mm, fill=1, stroke=0)
    canvas.setFillColor(YELLOW)
    canvas.rect(0, H - 32 * mm, W, 4 * mm, fill=1, stroke=0)

    canvas.setFillColor(white)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(22 * mm, H - 18 * mm, "SCALERISE  ·  FIXKARDO")

    canvas.setFont("Helvetica-Bold", 28)
    canvas.drawString(22 * mm, H - 70 * mm, "Landing Page")
    canvas.drawString(22 * mm, H - 84 * mm, "Image Brief")

    canvas.setFillColor(YELLOW)
    canvas.rect(22 * mm, H - 92 * mm, 40 * mm, 2.5 * mm, fill=1, stroke=0)

    canvas.setFillColor(HexColor("#CBD5E1"))
    canvas.setFont("Helvetica", 12)
    y = H - 110 * mm
    lines = [
        "For the graphic designer working on Meta ads + LP visuals",
        "Generate assets in Google Flow (agency paid account)",
        "Replace the current solid-color placeholders in /assets",
        "",
        "3 landing pages  ·  13 photo assets  ·  logo already done",
        "Prepared November 2026",
    ]
    for line in lines:
        canvas.drawString(22 * mm, y, line)
        y -= 7 * mm

    canvas.setFillColor(GREEN)
    canvas.roundRect(22 * mm, 28 * mm, W - 44 * mm, 42 * mm, 6, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(30 * mm, 55 * mm, "Deliver as WebP (preferred) or high-quality JPG")
    canvas.setFont("Helvetica", 10)
    canvas.drawString(30 * mm, 45 * mm, "Exact pixel sizes listed per asset · keep subject clear of edges")
    canvas.drawString(30 * mm, 36 * mm, "No text, logos, watermarks, or UI chrome inside the photos")
    canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="H1",
        fontName="Helvetica-Bold",
        fontSize=18,
        textColor=NAVY,
        spaceAfter=8,
        spaceBefore=4,
        leading=22,
    )
)
styles.add(
    ParagraphStyle(
        name="H2",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=GREEN,
        spaceAfter=6,
        spaceBefore=14,
        leading=17,
    )
)
styles.add(
    ParagraphStyle(
        name="H3",
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=NAVY,
        spaceAfter=4,
        spaceBefore=8,
        leading=14,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=NAVY,
        spaceAfter=6,
        leading=13,
    )
)
styles.add(
    ParagraphStyle(
        name="Muted",
        fontName="Helvetica",
        fontSize=9,
        textColor=MUTED,
        spaceAfter=4,
        leading=12,
    )
)
styles.add(
    ParagraphStyle(
        name="Label",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=GREEN,
        spaceAfter=2,
        spaceBefore=2,
        leading=10,
    )
)
styles.add(
    ParagraphStyle(
        name="Prompt",
        fontName="Helvetica",
        fontSize=8.5,
        textColor=NAVY,
        spaceAfter=4,
        leading=11.5,
        backColor=HexColor("#F8FAFC"),
        borderPadding=6,
        leftIndent=4,
        rightIndent=4,
    )
)
styles.add(
    ParagraphStyle(
        name="Small",
        fontName="Helvetica",
        fontSize=8,
        textColor=MUTED,
        spaceAfter=2,
        leading=10,
    )
)
styles.add(
    ParagraphStyle(
        name="BulletItem",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=NAVY,
        leftIndent=12,
        spaceAfter=3,
        leading=12,
    )
)
styles.add(ParagraphStyle(name="Cell", fontName="Helvetica", fontSize=8, textColor=NAVY, leading=10))
styles.add(
    ParagraphStyle(name="CellBold", fontName="Helvetica-Bold", fontSize=8, textColor=NAVY, leading=10)
)
styles.add(
    ParagraphStyle(name="CellGreen", fontName="Helvetica-Bold", fontSize=8, textColor=GREEN, leading=10)
)


def section_rule():
    return HRFlowable(width="100%", thickness=1, color=BORDER, spaceBefore=4, spaceAfter=8)


def meta_row(label, value):
    data = [
        [
            Paragraph(f"<b>{label}</b>", styles["CellGreen"]),
            Paragraph(value, styles["Cell"]),
        ]
    ]
    t = Table(data, colWidths=[38 * mm, 140 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), LIGHT),
                ("BACKGROUND", (1, 0), (1, 0), HexColor("#F8FAFC")),
                ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return t


def asset_block(num, filename, where, ratio, exact, generate, usage, prompt, notes=None):
    bits = [
        Paragraph(f"{num}.  {filename}", styles["H3"]),
        meta_row("Where", where),
        Spacer(1, 2),
        meta_row("Ratio", ratio),
        Spacer(1, 2),
        meta_row("Exact size", exact),
        Spacer(1, 2),
        meta_row("Generate at", generate),
        Spacer(1, 2),
        meta_row("Usage", usage),
        Spacer(1, 4),
        Paragraph("GOOGLE FLOW PROMPT (starter — feel free to refine)", styles["Label"]),
        Paragraph(prompt.replace("\n", "<br/>"), styles["Prompt"]),
    ]
    if notes:
        bits.append(Paragraph(f"<i>Note: {notes}</i>", styles["Small"]))
    bits.append(Spacer(1, 8))
    bits.append(section_rule())
    return KeepTogether(bits)


story = []

story.append(Paragraph("1. Brief overview", styles["H1"]))
story.append(
    Paragraph(
        "FixKardo is a home-services marketplace for cities across Himachal / Punjab / Haryana / nearby. "
        "We have <b>three Meta Ads landing pages</b> ready in HTML. Current images in <b>/assets</b> are solid-color placeholders. "
        "Please generate real photographs (or photoreal AI) in <b>Google Flow</b> using the prompts below, then export to the exact filenames and sizes listed.",
        styles["Body"],
    )
)

story.append(Paragraph("The three pages", styles["H2"]))
page_data = [
    [
        Paragraph("<b>Page</b>", styles["CellBold"]),
        Paragraph("<b>Campaign</b>", styles["CellBold"]),
        Paragraph("<b>Slug / path</b>", styles["CellBold"]),
        Paragraph("<b>Photo assets</b>", styles["CellBold"]),
    ],
    [
        Paragraph("Salon at Home", styles["Cell"]),
        Paragraph("Women's salon at home", styles["Cell"]),
        Paragraph("sales/salon-at-home/", styles["Cell"]),
        Paragraph("1 hero + 5 service/strip", styles["Cell"]),
    ],
    [
        Paragraph("Paonta Home Services", styles["Cell"]),
        Paragraph("Home services in Paonta Sahib", styles["Cell"]),
        Paragraph("sales/paonta-home-services/", styles["Cell"]),
        Paragraph("1 hero + 5 service cards", styles["Cell"]),
    ],
    [
        Paragraph("Join as a Partner", styles["Cell"]),
        Paragraph("Partner onboarding", styles["Cell"]),
        Paragraph("partner/join-as-a-partner/", styles["Cell"]),
        Paragraph("1 hero only", styles["Cell"]),
    ],
]
pt = Table(page_data, colWidths=[42 * mm, 48 * mm, 52 * mm, 36 * mm])
pt.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), GREEN),
            ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("BACKGROUND", (0, 1), (-1, 1), HexColor("#F8FAFC")),
            ("BACKGROUND", (0, 3), (-1, 3), HexColor("#F8FAFC")),
            ("BOX", (0, 0), (-1, -1), 0.6, BORDER),
            ("INNERGRID", (0, 0), (-1, -1), 0.4, BORDER),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]
    )
)
story.append(pt)

story.append(Paragraph("Brand visual direction", styles["H2"]))
for b in [
    "<b>Look:</b> Real Indian home / neighbourhood context (not Western stock). Clean, trustworthy, warm daylight.",
    "<b>People:</b> South Asian professionals and customers. Modest, respectful, everyday clothing. Women beauticians for salon; male + female customers as natural for the scene.",
    "<b>Avoid:</b> Text overlays, logos, watermarks, neon cyber look, purple glow, luxury spa that feels Dubai/US, empty abstract gradients as the main subject.",
    "<b>Colors to echo (optional in props/wardrobe accents):</b> FixKardo green #0F9F59, yellow #F4B400 — do not force branded UI into photos.",
    "<b>Crop safety:</b> Keep faces and key tools away from extreme edges; heroes are cropped to 4:5; service images to 4:3.",
]:
    story.append(Paragraph(f"• {b}", styles["BulletItem"]))

story.append(Paragraph("Delivery checklist", styles["H2"]))
for b in [
    "Generate / refine in Google Flow (agency paid account).",
    "Export <b>WebP</b> preferred (or high-quality JPG we can convert).",
    "Use the <b>exact filenames</b> below so they drop straight into <b>/assets</b>.",
    "Match the <b>Exact size</b> column (or generate larger at the Generate-at size, then crop/export to exact).",
    "Heroes: soft natural light, subject fills most of the frame, shallow depth of field OK.",
    "Service cards: clear action of the trade/beauty service; readable at small mobile card size.",
]:
    story.append(Paragraph(f"• {b}", styles["BulletItem"]))

story.append(
    Paragraph(
        "<b>Logo:</b> <font color='#0F9F59'>fixkardo-logo.png</font> already exists (320×80). "
        "Do not regenerate unless the brand provides a new master.",
        styles["Body"],
    )
)

story.append(PageBreak())

# Salon
story.append(Paragraph("2. Page A — Salon at Home", styles["H1"]))
story.append(
    Paragraph(
        "<b>Campaign:</b> Women's salon / parlour at home · cities like Solan, Chandigarh, Shimla, Mohali, etc.<br/>"
        "<b>Hero line:</b> “Parlour-style beauty, at your doorstep” · Hindi: "
        + hi("पार्लर जाने का टाइम नहीं? अब पार्लर आएगा आपके घर!")
        + "<br/>"
        + "<b>Promise:</b> Verified women beauticians · Pay after service · Upfront pricing",
        styles["Body"],
    )
)
story.append(
    Paragraph(
        "Layout: top logo bar → hero (copy left / photo right on desktop) → service cards → how it works → trust → testimonials → 4-image strip → FAQ → final CTA.",
        styles["Muted"],
    )
)
story.append(section_rule())

story.append(
    asset_block(
        "A1",
        "salon-hero.webp",
        "Hero — right column on desktop; full visual weight on mobile under the headline",
        "4:5 portrait",
        "800 × 1000 px",
        "1600 × 2000 px (then export/crop to 800×1000)",
        "Main hero image for the Salon at Home landing page",
        "Photoreal lifestyle photo of a professional Indian woman beautician giving a facial or clean-up to a young Indian woman customer in a bright, tidy middle-class Indian living room. Beautician wears a neat apron/uniform in soft green or teal tones, opens a professional beauty kit on a side table. Soft morning daylight from a window, warm and trustworthy mood, shallow depth of field, no text, no logos, vertical 4:5 composition, subject centered with space around edges for crop.",
        "Must feel “parlour at home”, not a commercial salon studio.",
    )
)

story.append(
    asset_block(
        "A2",
        "salon-door.webp",
        "“The at-home experience” image strip (first tile) — also storytelling of arrival",
        "4:3 landscape",
        "800 × 600 px",
        "1600 × 1200 px → export 800×600",
        "Beautician arriving at customer's door with kit",
        "Photoreal photo of a friendly Indian woman beautician standing at the doorway of an Indian home, carrying a professional beauty kit bag, greeting a woman customer. Natural daylight, residential Indian house entrance, clean and inviting, no text or logos, 4:3 landscape framing.",
    )
)

story.append(
    asset_block(
        "A3",
        "salon-facial.webp",
        "Service card “Facial & Clean-up” + image strip",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Facial / clean-up service photo",
        "Close-to-medium shot of an Indian woman receiving a facial / clean-up at home from a woman beautician; soft towels, clean products on a tray, glowing skin, calm living-room setting, natural light, photoreal, no text, 4:3.",
    )
)

story.append(PageBreak())
story.append(Paragraph("2. Page A — Salon at Home (continued)", styles["H1"]))
story.append(section_rule())

story.append(
    asset_block(
        "A4",
        "salon-hairspa.webp",
        "Service card “Hair Spa” + image strip",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Hair spa at home",
        "Indian woman getting a hair spa / deep conditioning treatment at home; beautician massaging hair with spa cream, towel around shoulders, warm indoor light, photoreal lifestyle, no text, 4:3.",
    )
)

story.append(
    asset_block(
        "A5",
        "salon-manicure.webp",
        "Service card “Manicure & Pedicure” + image strip",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Manicure at home",
        "Close lifestyle shot of a manicure being done at home on an Indian woman's hands; neat nail tools, soft pastel polish accents, wooden table in an Indian living room, photoreal, no text, 4:3.",
    )
)

story.append(
    asset_block(
        "A6",
        "salon-blowdry.webp",
        "Service card “Hair Styling & Blow-dry” only (not in strip)",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Blow-dry / hair styling at home",
        "Indian woman getting a blow-dry / hair styling at home; beautician using a dryer and brush, hair in motion, bright room, photoreal, energetic but calm brand mood, no text, 4:3.",
    )
)

story.append(
    asset_block(
        "A7",
        "salon-waxing.webp",
        "Service card “Waxing”",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Waxing at home",
        "Indian beautician in dark green FixKardo polo applying wax to a client's leg at home; wax warmer and sticks on a side tray, bright living room, photoreal, no text, 4:3.",
    )
)
story.append(
    asset_block(
        "A8",
        "salon-threading.webp",
        "Service card “Threading”",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Eyebrow threading at home",
        "Indian beautician in dark green FixKardo polo doing eyebrow threading on a relaxed client at home; cotton thread visible, bright living room, photoreal, no text, 4:3.",
    )
)
story.append(
    asset_block(
        "A9",
        "salon-mehendi.webp",
        "Service card “Mehendi”",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Mehendi / henna at home",
        "Indian mehendi artist in dark green FixKardo polo applying henna design on a client's hand at home; henna cones on a tray, bright living room, photoreal, no text, 4:3.",
    )
)

story.append(PageBreak())

# Paonta
story.append(Paragraph("3. Page B — Paonta Home Services", styles["H1"]))
story.append(
    Paragraph(
        "<b>Campaign:</b> Home services specifically in <b>Paonta Sahib</b>.<br/>"
        "<b>Hero line:</b> “Trusted electricians, plumbers &amp; more in Paonta Sahib”<br/>"
        "<b>Hindi:</b> "
        + hi("घर का कोई भी काम? बस एक कॉल या WhatsApp — प्रोफेशनल आपके दरवाज़े पर।")
        + "<br/>"
        + "<b>Services with photos:</b> Electrician, Plumber, RO Service, Water Tank Cleaning, Men's Salon at Home",
        styles["Body"],
    )
)
story.append(
    Paragraph(
        "Layout: hero → service cards (image on each) → how it works → trust → testimonials → FAQ → final CTA.",
        styles["Muted"],
    )
)
story.append(section_rule())

story.append(
    asset_block(
        "B1",
        "paonta-hero.webp",
        "Hero — right column / mobile under headline",
        "4:5 portrait",
        "800 × 1000 px",
        "1600 × 2000 px → export 800×1000",
        "Main hero for Paonta home services",
        "Photoreal portrait-oriented scene of a trustworthy Indian home-service professional (electrician or multi-skill technician) at a customer's home in a North Indian town like Paonta Sahib — tool bag, checking a switchboard or explaining a repair to a homeowner in a bright hallway/living area. Friendly, competent, everyday Indian home interior, natural daylight, no text, no logos, vertical 4:5.",
        "Can show electrician as the lead craft — strongest “home fix” signal.",
    )
)

story.append(
    asset_block(
        "B2",
        "svc-electrician.webp",
        "Service card — Electrician",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Electrician at work",
        "Indian electrician repairing a wall switch or ceiling fan at a middle-class Indian home; tool pouch, voltage tester, safe work, clear action readable at small size, natural light, photoreal, no text, 4:3.",
    )
)

story.append(
    asset_block(
        "B3",
        "svc-plumber.webp",
        "Service card — Plumber",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Plumber at work",
        "Indian plumber fixing a kitchen or bathroom tap / pipe under a sink in an Indian home; wrench and tools visible, clean and professional, photoreal, no text, 4:3.",
    )
)

story.append(PageBreak())
story.append(Paragraph("3. Page B — Paonta Home Services (continued)", styles["H1"]))
story.append(section_rule())

story.append(
    asset_block(
        "B4",
        "svc-ro.webp",
        "Service card — RO Service",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "RO filter service",
        "Technician servicing a domestic RO water purifier in an Indian kitchen; opening the unit, replacing a filter cartridge, clean kitchen backdrop, photoreal, no text, 4:3.",
    )
)

story.append(
    asset_block(
        "B5",
        "svc-tank.webp",
        "Service card — Water Tank Cleaning",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Water tank cleaning",
        "Professional cleaning an overhead or rooftop water storage tank at an Indian house; protective gloves, cleaning brush, rooftop/terrace context, clear sunny day, photoreal documentary style, no text, 4:3.",
    )
)

story.append(
    asset_block(
        "B6",
        "svc-mens-salon.webp",
        "Service card — Men's Salon at Home",
        "4:3 landscape",
        "600 × 450 px",
        "1200 × 900 px → export 600×450",
        "Men's haircut / grooming at home",
        "Indian male barber giving a neat haircut to a young Indian man at home; cape, clippers or scissors, living room setting, professional and friendly, photoreal, no text, 4:3.",
    )
)

story.append(PageBreak())

# Partner
story.append(Paragraph("4. Page C — Join as a Partner", styles["H1"]))
story.append(
    Paragraph(
        "<b>Campaign:</b> Recruit service professionals to join FixKardo.<br/>"
        "<b>Hero line:</b> “Get more jobs in your city with FixKardo”<br/>"
        "<b>Hindi:</b> "
        + hi("अपने शहर में ज़्यादा काम, ज़्यादा कमाई — FixKardo पार्टनर बनें।")
        + "<br/>"
        + "<b>CTA:</b> Join Now, It's Free · form on the page",
        styles["Body"],
    )
)
story.append(
    Paragraph(
        "Layout: hero → benefits + who can join + how it works + signup form → cities strip → FAQ. Only one photo slot (hero).",
        styles["Muted"],
    )
)
story.append(section_rule())

story.append(
    asset_block(
        "C1",
        "partner-hero.webp",
        "Hero — right column / mobile under headline",
        "4:5 portrait",
        "800 × 1000 px",
        "1600 × 2000 px → export 800×1000",
        "Partner / professional pride hero",
        "Confident Indian service professional (can be an electrician, plumber, or beautician) standing proudly outside or just inside a customer's home after a job, tool kit or beauty kit in hand, subtle smile, natural daylight, aspirational but grounded “more work in your city” mood for a partner recruitment ad. Photoreal, vertical 4:5, no text, no logos, no app UI mockups in frame.",
        "Should feel empowering for partners — dignity of skilled work, not corporate headshot.",
    )
)

story.append(PageBreak())

# Master checklist
story.append(Paragraph("5. Master asset checklist", styles["H1"]))
story.append(
    Paragraph(
        "Drop finished files into the repo folder <b>assets/</b> with these exact names. "
        "After push to GitHub <b>main</b>, jsDelivr serves them to the live pages.",
        styles["Body"],
    )
)

rows = [
    [
        Paragraph("<b>#</b>", styles["CellBold"]),
        Paragraph("<b>Filename</b>", styles["CellBold"]),
        Paragraph("<b>Page</b>", styles["CellBold"]),
        Paragraph("<b>Exact px</b>", styles["CellBold"]),
        Paragraph("<b>Ratio</b>", styles["CellBold"]),
        Paragraph("<b>Status</b>", styles["CellBold"]),
    ]
]
checklist = [
    ("A1", "salon-hero.webp", "Salon", "800×1000", "4:5"),
    ("A2", "salon-door.webp", "Salon", "800×600", "4:3"),
    ("A3", "salon-facial.webp", "Salon", "600×450", "4:3"),
    ("A4", "salon-hairspa.webp", "Salon", "600×450", "4:3"),
    ("A5", "salon-manicure.webp", "Salon", "600×450", "4:3"),
    ("A6", "salon-blowdry.webp", "Salon", "600×450", "4:3"),
    ("A7", "salon-waxing.webp", "Salon", "600×450", "4:3"),
    ("A8", "salon-threading.webp", "Salon", "600×450", "4:3"),
    ("A9", "salon-mehendi.webp", "Salon", "600×450", "4:3"),
    ("B1", "paonta-hero.webp", "Paonta", "800×1000", "4:5"),
    ("B2", "svc-electrician.webp", "Paonta", "600×450", "4:3"),
    ("B3", "svc-plumber.webp", "Paonta", "600×450", "4:3"),
    ("B4", "svc-ro.webp", "Paonta", "600×450", "4:3"),
    ("B5", "svc-tank.webp", "Paonta", "600×450", "4:3"),
    ("B6", "svc-mens-salon.webp", "Paonta", "600×450", "4:3"),
    ("C1", "partner-hero.webp", "Partner", "800×1000", "4:5"),
]
for num, fn, page, px, ratio in checklist:
    rows.append(
        [
            Paragraph(num, styles["Cell"]),
            Paragraph(fn, styles["Cell"]),
            Paragraph(page, styles["Cell"]),
            Paragraph(px, styles["Cell"]),
            Paragraph(ratio, styles["Cell"]),
            Paragraph("☐ To generate", styles["Cell"]),
        ]
    )

ct = Table(rows, colWidths=[12 * mm, 48 * mm, 28 * mm, 28 * mm, 18 * mm, 44 * mm])
ct.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), GREEN),
            ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("BOX", (0, 0), (-1, -1), 0.6, BORDER),
            ("INNERGRID", (0, 0), (-1, -1), 0.35, BORDER),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#F8FAFC")]),
        ]
    )
)
story.append(ct)

story.append(Spacer(1, 10))
story.append(Paragraph("Also present (do not replace unless brand updates)", styles["H2"]))
story.append(
    Paragraph(
        "• <b>fixkardo-logo.png</b> — 320×80 — used in top bar + footer on all three pages",
        styles["BulletItem"],
    )
)

story.append(Paragraph("Google Flow tips for this project", styles["H2"]))
for b in [
    "Start with the starter prompt → generate a few variants → pick the clearest action at thumbnail size.",
    "If Flow offers aspect ratio presets: use <b>4:5</b> for heroes, <b>4:3</b> for service/strip shots; then resize to exact pixels.",
    "Keep a consistent lighting family across all 13 shots (daylight, soft, realistic) so the three LPs feel like one brand.",
    "You may tweak prompts for ad creatives later; this brief is the minimum set the landing pages need.",
    "When files are ready, send WebPs named exactly as above to the web team / replace in the GitHub repo <b>assets/</b> folder.",
]:
    story.append(Paragraph(f"• {b}", styles["BulletItem"]))

story.append(Spacer(1, 12))
story.append(section_rule())
story.append(
    Paragraph(
        "Questions on layout placement or crop: check the HTML pages in <b>sales/salon-at-home</b>, "
        "<b>sales/paonta-home-services</b>, and <b>partner/join-as-a-partner</b>, or ping the web team at ScaleRise.",
        styles["Muted"],
    )
)
story.append(Paragraph("Prepared for FixKardo · ScaleRise · November 2026", styles["Small"]))

doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=18 * mm,
    bottomMargin=18 * mm,
    title="FixKardo Landing Pages — Image Brief for Graphic Designer",
    author="ScaleRise",
    subject="Image requirements, dimensions, and Google Flow prompts for 3 FixKardo Meta Ads landing pages",
)

full_story = [Spacer(1, 1), PageBreak()] + story
doc.build(full_story, onFirstPage=cover_page, onLaterPages=header_footer)
print("Wrote", OUT)
