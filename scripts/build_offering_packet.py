"""Build 214SouthAve_Offering_Packet.pdf — content source for the offering packet."""
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    ListFlowable, ListItem, KeepTogether, HRFlowable,
)

OUT = Path(__file__).resolve().parents[1] / "docs" / "214SouthAve_Offering_Packet.pdf"
G = HexColor("#2D4A3E")
MUTED = HexColor("#6B6B65")
PEND_BG = HexColor("#FFF3C4")
PEND_FG = HexColor("#8A6D00")
RULE = HexColor("#D5D5D0")
ROW = HexColor("#F7F7F4")

styles = getSampleStyleSheet()
for name, kwargs in [
    ("Kicker", dict(fontName="Helvetica-Bold", fontSize=9, textColor=MUTED, spaceAfter=4)),
    ("PktTitle", dict(fontName="Helvetica-Bold", fontSize=22, textColor=G, spaceAfter=4)),
    ("Sub", dict(fontName="Helvetica", fontSize=11, textColor=MUTED, spaceAfter=10)),
    ("PktBody", dict(fontName="Helvetica", fontSize=9.5, leading=13, spaceAfter=7, textColor=black)),
    ("BodyBold", dict(fontName="Helvetica-Bold", fontSize=9.5, leading=13, spaceAfter=7)),
    ("H1", dict(fontName="Helvetica-Bold", fontSize=13, textColor=G, spaceBefore=12, spaceAfter=7)),
    ("H2", dict(fontName="Helvetica-Bold", fontSize=10.5, textColor=black, spaceBefore=9, spaceAfter=5)),
    ("Small", dict(fontName="Helvetica", fontSize=8.5, leading=11, textColor=MUTED, spaceAfter=6)),
    ("SmallI", dict(fontName="Helvetica-Oblique", fontSize=8.5, leading=11, textColor=MUTED, spaceAfter=6)),
    ("PktBullet", dict(fontName="Helvetica", fontSize=9.5, leading=12.5, spaceAfter=2)),
    ("Cell", dict(fontName="Helvetica", fontSize=8.5, leading=11, textColor=black)),
    ("CellB", dict(fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=black)),
    ("HeadCell", dict(fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=white)),
    ("Pend", dict(fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=PEND_FG, spaceAfter=6)),
]:
    if name in styles.byName:
        styles.byName[name].__dict__.update(kwargs)
    else:
        styles.add(ParagraphStyle(name=name, **kwargs))


def P(text, style="PktBody"):
    return Paragraph(text, styles[style])


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, styles["PktBullet"]), leftIndent=12, bulletColor=black) for i in items],
        bulletType="bullet",
        start="•",
        leftIndent=14,
        spaceBefore=2,
        spaceAfter=6,
    )


def kv_table(rows, col1=1.5 * inch, col2=5.5 * inch):
    data = [[P("Item", "HeadCell"), P("Detail", "HeadCell")]]
    for a, b in rows:
        data.append([P(a, "CellB"), P(b, "Cell")])
    t = Table(data, colWidths=[col1, col2])
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), G),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), ROW))
    t.setStyle(TableStyle(style_cmds))
    return t


def path_table(rows):
    data = [[P("If a buyer wants to", "HeadCell"), P("What it requires", "HeadCell")]]
    for a, b in rows:
        data.append([P(a, "CellB"), P(b, "Cell")])
    t = Table(data, colWidths=[2.4 * inch, 4.6 * inch])
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), G),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), ROW))
    t.setStyle(TableStyle(style_cmds))
    return t


def val_table(rows):
    data = [[P("Source", "HeadCell"), P("Parcel", "HeadCell"), P("Value", "HeadCell")]]
    for a, b, c in rows:
        data.append([P(a, "Cell"), P(b, "Cell"), P(c, "CellB")])
    t = Table(data, colWidths=[2.8 * inch, 2.2 * inch, 2.0 * inch])
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), G),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), ROW))
    t.setStyle(TableStyle(style_cmds))
    return t


def tax_table():
    rows = [
        ["Sale price", "Taxable (40%)", "Est. annual — investment", "Est. annual — owner-occupied"],
        ["$550,000", "$220,000", "~$8,903", "~$7,600"],
        ["$600,000", "$240,000", "~$9,713", "~$8,400"],
        ["$649,000", "$259,600", "~$10,506", "~$9,180"],
        ["$700,000", "$280,000", "~$11,332", "~$9,900"],
        ["$750,000", "$300,000", "~$12,141", "~$10,600"],
    ]
    data = [[P(c, "HeadCell" if i == 0 else "Cell") for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=[1.5 * inch, 1.5 * inch, 2.0 * inch, 2.0 * inch])
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), G),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
    ]
    t.setStyle(TableStyle(style_cmds))
    return t


def pend(text):
    t = Table([[P("PENDING — " + text, "Pend")]], colWidths=[7 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PEND_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def build():
    story = []
    story += [
        P("OFFERING PACKET", "Kicker"),
        P("214 + 0 South Ave SE", "PktTitle"),
        P("Atlanta, GA 30315  ·  Summerhill", "Sub"),
        P("<b>$649,000 — both parcels, one closing, delivered vacant.</b>"),
        P("A three-bedroom house that has helped pay for itself for fifteen years, and the corner parcel beside it that most people mistake for a side yard. You can live in it. You can rent rooms in it. You can build on the lot, subject to what follows. You can do all three."),
        HRFlowable(width="100%", thickness=1, color=RULE, spaceAfter=8),
        P("Savage Props, LLC  ·  Nichole Wleklinski  ·  217-621-5151  ·  www.214southave.com", "Small"),
        P("Prepared August 2026 · Last updated August 14, 2026. Items marked PENDING are being confirmed and will be added as received.", "SmallI"),
    ]

    # 1 Summary
    story += [
        P("1. Summary", "H1"),
        kv_table([
            ("Address", "214 South Ave SE + 0 South Ave SE, Atlanta GA 30315"),
            ("Parcels", "14 -0054-0009-010-6 (Acct 1022835)  ·  14 -0054-0009-011-4 (Acct 1022843)"),
            ("Note on address", "0 South Ave SE appears in City of Atlanta records as 212 South Avenue SE"),
            ("Lot sizes", "3,107 SF improved + 3,016 SF vacant = ~6,123 SF combined"),
            ("Zoning", "R-4B-C conditional — Summerhill rezoning Z-06-24 / Ord. 06-O-0567"),
            ("House", "~1,800 SF, 3 BR / 2.5 BA, built 2005, corner lot"),
            ("Deck", "1,100 SF, built 2011, reinforced joists"),
            ("Delivery", "Vacant at closing. All current agreements expire August 25, 2026."),
            ("Terms", "Both parcels are offered together as one transaction. Proposals for the parcels separately will be considered."),
        ]),
        Spacer(1, 6),
        P("Seller is completing a 1031 exchange. No part of the transaction can be structured as a credit or payment to the buyer. Price is the lever; concessions are not.", "SmallI"),
    ]

    # 2 Walk through
    story += [
        P("2. What You'll See When You Walk Through", "H1"),
        P("This is a lived-in house, not a staged one. Here is what needs work, before you drive over."),
        bullets([
            "Carpets need replacing throughout",
            "Kitchen cabinets need touch-ups — not a full refinish",
            "Several deck boards are soft; railings need attention",
            "Exterior stairs need repair or replacement",
            "One bathroom still has the original 2008 fiberglass shower surround — structurally sound, but noisy and due for replacement",
            "Roof is original to 2005 construction, approximately 21 years old. A drone inspection in August 2026 identified missing shingles; roof structure reported sound from inside the attic. An independent scope of work is pending and will be added to this packet. An independent insurance agent has confirmed the roof is insurable on an actual cash value basis once the shingles are addressed.",
            "The crawl space HVAC unit lacks a proper shutoff (noted by Coolray, August 2026)",
            "A fixture shutoff valve does not fully close when the supply line is disconnected; it does not leak in normal operation. Replacement scheduled.",
        ]),
        P("All of it is reflected in the asking price."),
        P("What you will also see: a clean, safe, functioning house. Upstairs HVAC replaced 2023 with transferable lifetime warranty (see Section 3). An 1,100 SF deck with reinforced joists. A driveway updated in 2023 that fits two cars. Smart water shutoff, Nest thermostats, hardwired cameras. Three bedrooms that have housed working professionals continuously for years."),
        P("<b>Seller will remove carpet prior to closing at buyer's request, at no cost. This is a condition of sale, not a credit.</b>"),
        P("The list above is the disclosure. A written contractor scope with pricing is being prepared and will be added to this packet."),
    ]

    # 3 The House
    hvac = (
        "Upstairs system fully replaced by Coolray in 2023: Carrier 2-ton heat pump and matching air handler, "
        "new disconnect box and whip kit, plenums mastic-sealed, line set flushed. Permitted; City of Atlanta "
        "inspection completed July 2023. Lifetime parts and labor warranty, transferable. The crawl space unit "
        "serving the first floor is older — the house was gutted and renovated in 2010 following a foreclosure, "
        "so that system most likely dates to the 2010 renovation rather than to 2005 construction."
    )
    story += [
        P("3. The House", "H1"),
        kv_table([
            ("Heated area", "~1,800 SF (per Fulton County tax record)"),
            ("Configuration", "3 BR / 2.5 BA"),
            ("Year built", "2005 · purchased by current owner 2010"),
            ("Lot", "3,107 SF (0.0713 acres), corner"),
            ("Deck", "1,100 SF, built 2011. Reinforced joists on the north end — engineered to carry roughly 700 gallons of water plus multiple people"),
            ("HVAC", hvac),
            ("Water", "Moen smart shutoff with remote monitoring"),
            ("Controls", "Nest thermostats; hardwired camera system; Nest/Google cameras at driveway and door"),
            ("Utilities", "All electric (Georgia Power); water via Atlanta Watershed"),
            ("Parking", "Driveway updated 2023, two vehicles"),
        ]),
    ]

    # 4 Land / Zoning
    story += [
        P("4. The Land — 0 South Ave SE", "H1"),
        kv_table([
            ("Size", "3,016 SF (0.0692 acres)"),
            ("Zoning", "R-4B-C conditional (Z-06-24 / Ord. 06-O-0567)"),
            ("Configuration", "Corner parcel"),
            ("County codes", "Class R3 · Land code 6 · LUC 100"),
            ("Topography", "County TOPO: LEVEL"),
            ("Title", "Cleared through quiet title action"),
        ]),
        P("Zoning and development potential — please read", "H2"),
        P("<b>The City of Atlanta Office of Zoning and Development has confirmed in writing that 0 South Ave SE is a legal lot of record, buildable as-of-right for a single-family structure.</b>"),
        P("The parcel is subject to the Summerhill rezoning conditions adopted under Z-06-24 (Ordinance 06-O-0567), which supersede standard R-4B controls where the two conflict. Those conditions are summarized in Section 5 and attached to this packet in full."),
        P("<b>The most consequential is Section 6(a): a house must be a minimum of 20 feet wide, measured between the side walls. Because this is a condition of a rezoning rather than a zoning control, it is NOT eligible for a variance. Modifying it requires a rezoning from R-4B-C to R-4B-C for a change of conditions.</b>"),
        P("City staff have advised that neither parcel independently meets the minimum width, and that some combination of variances and a change of conditions would likely be required to build on the vacant parcel standing alone."),
        P("Setbacks are separately confirmed. Where a lot has multiple street frontages, the front yard is applied from the shortest frontage — South Avenue in this case — and remaining street frontages are treated as half-depth front yards. Per City staff, these definitions cannot be modified. An architect who has built on this street calculates the resulting as-of-right envelope at roughly 11 ft x 90 ft."),
        P("Consolidation", "H2"),
        P("Consolidating the two parcels would produce a single lot of roughly 50 feet of frontage, which satisfies the 20-foot minimum width. City staff previously indicated administrative lot consolidation may be possible."),
        P("What R-4B-C permits, and what it does not", "H2"),
        P("<b>City staff confirmed in writing on August 4, 2026: R-4B and the conditional R-4B-C permit single-family residential only. Accessory dwelling units and two-family dwellings are NOT permitted.</b> ADUs are allowed in R-4, R-4A and R-5; duplexes in R-5 only. Absent a rezoning, these parcels can accommodate a single-family residence and a guest house."),
        P("A guest house is distinguished from an ADU by two things: no full kitchen, and a size limit of under 30% of the principal structure. Per City staff a guest house is an accessory structure and is not governed by the same regulations as the principal structure — which means Section 6(a)'s 20-foot minimum width does not apply to it. Accessory setback and placement rules do still apply."),
        P("On placement, City staff advised that on a consolidated lot any accessory structure must sit behind the principal structure, and that a variance from the Board of Zoning Adjustment would be required to place a structure between the principal structure and the street."),
        P("What each path requires", "H2"),
        path_table([
            ("Build a duplex", "Rezoning to R-5. Legislative — NPU-V, Zoning Review Board, City Council. Not a variance."),
            ("Build an accessory dwelling unit with its own kitchen", "Rezoning to R-4, R-4A or R-5. Not permitted in R-4B-C at any size."),
            ("Build a new house on the vacant parcel standing alone", "A change of conditions to modify Section 6(a)'s 20-foot minimum width, AND setback variances for the roughly 11 ft x 90 ft envelope. Two separate processes."),
            ("Consolidate the two parcels", "City staff indicated administrative consolidation may be possible. No public hearing. Not reversible without a subdivision."),
            ("Enlarge the existing house", "Nothing, if the addition stays within the setbacks. A BZA variance if it does not. Section 6(a) is already satisfied — the existing house exceeds 20 feet."),
            ("Add a guest house (no kitchen, under 30% of the principal structure)", "Permitted as an accessory structure. Not subject to the 20-foot minimum width. Must sit behind the principal structure on a consolidated lot; placing it between the house and the street requires a BZA variance."),
        ]),
        Spacer(1, 4),
        P("<b>The pattern: anything that adds a second kitchen is legislative. Everything else is either a variance or requires no relief at all.</b>"),
        P("Consolidation is not reversible without a subdivision, and would foreclose selling the parcels separately. It is offered as one path among several, not a recommendation."),
        P("A Zoning Verification Letter has been requested under record PLN-ONLINE-26-001614. Note that a ZVL confirms zoning district and overlays only. The substantive conditions in this section come from written correspondence with the Office of Zoning and Development, available on request."),
        Spacer(1, 4),
        pend("Plat or survey for both parcels. Lot dimensions above derive from County GIS geometry."),
        P("Buyers must independently verify all zoning, setback, and development parameters with the City of Atlanta Office of Zoning and Development. No representation is made beyond what the City has confirmed in writing.", "SmallI"),
    ]

    # 5 Rezoning
    story += [
        P("5. Summerhill Rezoning Conditions — Z-06-24", "H1"),
        P("Both parcels fall under Ordinance 06-O-0567, adopted May 1, 2006. Section 6 applies to all R-4B-C property in the Summerhill Neighborhood and governs design as well as dimensions. The full text is attached to this packet."),
        P("Section 6 in summary", "H2"),
        bullets([
            "(a) Minimum house width of 20 feet, measured between the side walls — the walls perpendicular to the wall containing the primary entrance",
            "(b) The primary pedestrian entrance must face and be visible from a public or private street",
            "(c) Attached garages recessed at least 5 feet from the street-facing façade, and no more than 50% of its width",
            "(d) Detached accessory structures to the side and/or rear of the principal structure, within the buildable area, set back at least 15 feet from its street-facing façade",
            "(e) No parking pad between the principal structure and the street",
            "(f) Driveway must extend at least 20 feet beyond the front façade, maximum 10 feet wide in the front yard, or be a ribbon driveway with a grass strip",
            "(g) Street-facing façades: fenestration between 20% and 40% of wall area; no window unit over 28 SF",
            "(h) Gabled or hipped roof, minimum 6:12 pitch",
            "(i) Street-facing chimneys must originate at grade",
            "(j) First floor elevated 1.5 to 4 feet above grade. Slab-on-grade is not permitted. No unfinished concrete block or stacked stone",
        ]),
        P("The existing house at 214 South Ave SE was built in 2005, predating these conditions."),
        P("Variance versus change of conditions — the distinction that matters", "H2"),
        P("Setback requirements are zoning controls and the Board of Zoning Adjustment can grant relief from them. Six setback variances have been heard on South Ave SE and Little St SE since 2018 — V-25-104, V-21-036, V-20-081, V-19-110, V-19-109 and V-18-387 — with approvals across the range, and two were followed by new-construction permits."),
        P("Those cases addressed setbacks. They do not address Section 6(a). <b>The 20-foot minimum width is a condition of the rezoning, and per City staff it cannot be varied by the Board at any price. Only a change of conditions can modify it.</b>"),
        P("Buyers evaluating this parcel should price both processes separately. Case data pulled from the City of Atlanta Accela portal, August 2026; verify current status with the Office of Zoning and Development.", "Small"),
    ]

    # 6 Neighborhood
    story += [
        P("6. The Neighborhood", "H1"),
        P("Summerhill is one of Atlanta's oldest neighborhoods, immediately south of downtown and adjacent to the former Turner Field site. Georgia Avenue, two blocks away, has become an award-winning adaptive-reuse business district."),
        P("Nearby", "H2"),
        bullets([
            "Atlanta BeltLine — Southside Trail access within the immediate area",
            "Grant Park — and the Grant Park Farmers Market, held weekly",
            "The Beacon — adaptive-reuse retail, dining, and workspace complex on Grant Street",
            "Center Parc Stadium and the Georgia State athletics district",
            "Downtown Atlanta — immediately north",
        ]),
        P("Georgia Avenue — walking distance", "H2"),
        bullets([
            "Talat Market — Thai-focused, rotating menu; among the most acclaimed restaurants in the city",
            "Little Bear — chef-driven neighborhood restaurant",
            "Halfway Crooks — brewery and beer garden",
            "Wood's Chapel BBQ — opened 2019, named for one of the first churches to serve Summerhill after the Civil War",
            "Southern National — chef-driven dining",
        ]),
        P("Schools — Atlanta Public Schools", "H2"),
        bullets([
            "Elementary: Parkside Elementary — serves Summerhill, Grant Park, Ormewood Park, Boulevard Heights, Cabbagetown",
            "Middle: Martin Luther King Jr. Middle School",
            "High: Maynard H. Jackson High School",
        ]),
        P("Attendance zones change. Verify current zoning at maps.apsk12.org.", "SmallI"),
        P("Development context", "H2"),
        bullets([
            "Kaiser Permanente purchased approximately 7 acres near the former Turner Field site (January 2026)",
            "Georgia State University and Center Parc Stadium anchor ongoing mixed-use redevelopment",
            "Peoplestown flood-mitigation greenspace and stormwater infrastructure under construction nearby",
            "Mercedes-Benz Stadium hosts global events, including World Cup matches",
        ]),
        P("Proposed indoor track and field facility", "H2"),
        P("The Atlanta Track Club has proposed a 175,000 SF indoor track and field facility adjacent to Cheney Stadium in Summerhill — which would be Georgia's first — with an estimated $100M capital raise. Plans as presented include a hydraulic oval, a healthcare clinic, a STEM center, and community meeting space. The Atlanta Public Schools Board of Education is expected to consider the proposal in August 2026."),
        P("<b><i>This project is proposed and not approved. Included as context, not certainty.</i></b>"),
        pend("Verified point-to-point distances: Georgia Ave, The Beacon, Beltline access, Grant Park, Center Parc Stadium, nearest MARTA."),
    ]

    # 7 Valuation
    story += [
        P("7. Valuation", "H1"),
        P("Asking price: $649,000 — both parcels, one closing."),
        P("Improved comparables, 18 months", "H2"),
        bullets([
            "Median closed sale: $601,000",
            "Mean closed sale: $621,361",
        ]),
        P("Land comparables — county neighborhood code 14275", "H2"),
        bullets([
            "Fraser St SE — 5,920 SF, sold October 2025, $440,000 → $74.32/SF",
            "80 Little St SE — 1,040 SF, sold May 2025, $75,000 → $72.12/SF",
            "Applied to 3,016 SF: approximately $217,000 – $224,000 indicated",
        ]),
        P("These comps reflect qualified sales in the same county neighborhood code. They do not adjust for the corner-lot setback constraint in Section 4. Buyers should weigh that constraint in their own valuation."),
        P("Both comparables are unconstrained parcels. Neither adjusts for the Section 6(a) minimum-width condition or the double front-yard setback treatment. A separate market read on comparable lot inventory in 30315 indicates a materially lower standalone figure. The parcel's realistic value is as a consolidation with 214 South Ave SE rather than as a standalone building site."),
        P("Indicated combined value", "H2"),
        val_table([
            ("Fulton County 2025 assessment (FMV)", "214 South Ave SE", "$481,700"),
            ("Fulton County 2024 assessment (FMV)", "214 South Ave SE", "$496,000"),
            ("Qualified land comps, code 14275", "0 South Ave SE", "$217,000 – $224,000"),
            ("<b>Indicated combined</b>", "<b>Both parcels</b>", "<b>$698,000 – $706,000</b>"),
        ]),
        Spacer(1, 4),
        P("The combined figure applies the unadjusted land range. The constraints above argue for a lower land component."),
        P("The asking price reflects a discount to indicated value in exchange for a clean, as-is, single-closing transaction."),
        P("Upper-end reference", "H2"),
        P("218 South Ave SE — 2,668 SF, 4 BR / 4 BA with garage and major upgrades, on a 7,688 SF lot — sold for $825,000 on August 21, 2025. Larger in both structure and land; a ceiling reference, not a direct comparable."),
        P("Market color", "H2"),
        P("Two newly built homes across the street are currently offered in the $800,000–$900,000 range. Those are asking prices, not closed sales. The valuation above uses qualified sold data only."),
    ]

    # 8 Tax
    story += [
        P("8. Tax Profile", "H1"),
        P("Georgia taxes property at 40% of fair market value. Following a sale the county typically resets fair market value to the purchase price for the following tax year, so a buyer's bill is based on what they pay, not on the seller's prior assessment."),
        tax_table(),
        Spacer(1, 4),
        P("Owner-occupied estimates assume standard homestead exemptions, including the Atlanta Public Schools exemption; these must be applied for with Fulton County by April 1 and are not automatic. Figures use approximately 40.47 mills combined; 2026 rates are set later in the year. A 2026 assessment appeal is pending on the basis of the disclosed deferred maintenance. Verify with the Fulton County Board of Assessors.", "SmallI"),
    ]

    # 9 Income
    rent = [
        [P("Room", "HeadCell"), P("Bath", "HeadCell"), P("Monthly rate", "HeadCell")],
        [P("Master bedroom", "Cell"), P("Private", "Cell"), P("$1,200", "CellB")],
        [P("Room 2", "Cell"), P("Shared", "Cell"), P("$850", "CellB")],
        [P("Room 3", "Cell"), P("Shared", "Cell"), P("$850", "CellB")],
        [P("<b>Total at current asking rates</b>", "Cell"), P("", "Cell"), P("<b>$2,900</b>", "CellB")],
    ]
    rt = Table(rent, colWidths=[2.5 * inch, 2.0 * inch, 2.5 * inch])
    rt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), G),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story += [
        P("9. The Income Option", "H1"),
        P("Optional. The property delivers vacant and a buyer is free to occupy it, rent it whole, or redevelop. This section is included because the model is documented and transfers with the house."),
        P("Current room schedule", "H2"),
        rt,
        Spacer(1, 4),
        P("Occupancy", "H2"),
        P("The house has operated at full occupancy. The most recent stabilized configuration ran at $1,100 + $850 + $850; the $1,100 was a legacy rate on the master and current asking is $1,200."),
        P("Rooms are let individually under separate written agreements. Tenancies typically run from a few months to a year, tracking hospital rotation blocks, with incoming tenants frequently overlapping departing ones."),
        P("A redacted rent roll showing room, rate, and tenancy period accompanies this packet. Tenant identities are withheld; unredacted agreements can be made available in diligence."),
        P("How rooms get filled", "H2"),
        bullets([
            "Tenants are sourced through RotatingRoom, a platform for medium-term room rentals, supplemented by referral from departing tenants",
            "The tenant base is residents, fellows, and healthcare professionals on hospital rotations — Grady, Emory, and Piedmont are all within a short commute",
            "Rotations run in fixed blocks, producing a steady supply of people who need a clean, quiet room for a defined period and who leave on schedule",
            "Departing tenants routinely show the house to incoming ones, which keeps turnover cost near zero",
            "Rooms have been priced below market deliberately, for occupancy stability. Rates can be adjusted",
            "This is long-term and medium-term room rental. The property is not operated as a short-term rental",
        ]),
        P("<b>All current agreements expire August 25, 2026. The property is delivered vacant at closing. Nothing is inherited and no tenant has a right to remain.</b>"),
    ]

    # 10 Offer
    story += [
        P("10. How to Make an Offer", "H1"),
        bullets([
            "Both parcels are offered together as one transaction. Proposals for the parcels separately will be considered.",
            "Offers accepted by email or through the form at www.214southave.com; no listing agent involved",
            "Proof of funds or lender pre-approval requested to confirm a showing, and required with any offer",
            "Contracts handled through seller's closing attorney",
            "Buyer representation welcome",
            "Showings by appointment only",
            "Seller is completing a 1031 exchange — no credits or payments to buyer can be structured",
            "Seller will remove carpet prior to closing at buyer's request, at no cost",
            "Seller can accommodate an expedited closing, including for buyers in a 1031 identification window",
        ]),
        HRFlowable(width="100%", thickness=1, color=RULE, spaceBefore=10, spaceAfter=8),
        P("<b>Nichole Wleklinski  ·  Savage Props, LLC</b>"),
        P("217-621-5151  ·  savagepropsllc@gmail.com  ·  www.214southave.com", "Small"),
        P("All figures are provided in good faith from Fulton County records, City of Atlanta records, and the seller's own documentation. Buyers should independently verify everything material to their decision.", "SmallI"),
    ]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        title="214 + 0 South Ave SE Offering Packet",
        author="Savage Props, LLC",
    )
    doc.build(story)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build()
