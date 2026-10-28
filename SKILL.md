---
name: paite-puan-patterns
author: Casey Paite
description: Authentically generate, describe, render, verify, and identify traditional Paite puan (handwoven Zo cloth) patterns. These are traditional cultural cloth patterns and MUST NOT be subject to variations. Any Paite puan design must strictly follow the canonical pattern geometry, color ratios, and sequence order. Covers the 12 authoritative Paite puan designs: Paite Puandum, Siamsin, Thangsuah, Puanlaisan, Galhang, Khephiau, Ngoutekhelh, Mal-am, Aksi, Pangpalek, Lianbuangthuam, and Puanthupi puan.
---

# Paite Puan Patterns

*Skill Author: **Casey Paite***  
*Digital Cloth Reproductions: **Mr. Siam Naulak**, Naulak Web Design ([naulak.com](https://naulak.com))*

Authentic specification, visual assets, and generation rules for the 12 traditional Paite *puan* (handwoven cloths) of the Paite (Zo) people of North-East India.

> [!IMPORTANT]
> **Zero-Variation Cultural Invariance Mandate**  
> Paite puan designs are living, sacred cultural heritage. **They are NOT subject to variations, modern recoloring, or pattern alterations.** Any generation, rendering, physical weaving specification, or analysis called a Paite puan MUST strictly follow the canonical pattern architecture, exact mathematical color ratios, and sequence order without alteration.

---

## Directory Structure & Packaged Assets

When deployed as an Agent Skill or exported for distribution, this skill is completely self-contained:

```text
paite-puan-patterns/
├── SKILL.md                          # Main instruction runbook (this file)
├── MANIFEST.json                     # Package metadata, asset manifest, and checksums
├── assets/                           # Standard skill assets (packaged with the skill)
│   ├── paite-puandum.jpg             # Reference images (1600 px) for image-to-image binding
│   ├── siamsin-puan.jpg
│   ├── thangsuah-puan.jpg
│   ├── puanlaisan.jpg
│   ├── galhang-puan.jpg
│   ├── khephiau-puan.jpg
│   ├── ngoutekhelh-puan.jpg
│   ├── mal-am-puan.jpg
│   ├── aksi-puan.jpg
│   ├── pangpalek-puan.jpg
│   ├── lianbuangthuam-puan.jpg
│   └── puanthupi-puan.jpg
├── puan-images/                      # Full master graphic reproductions (2560 px)
│   ├── INDEX.md                      # Comprehensive image index and fidelity specifications
│   ├── 01_Paite_Puandum.jpeg         # Master digital reproduction by Siam Naulak
│   ├── 02_Siamsin_Puan.jpeg
│   ├── 03_Thangsuah_Puan.jpeg
│   ├── 04_Puanlaisan.jpeg
│   ├── 05_Galhang_Puan.jpeg
│   ├── 06_Khephiau_Puan.jpeg
│   ├── 07_Ngoutekhelh_Puan.jpeg
│   ├── 08_Mal-am_Puan.jpeg
│   ├── 09_Aksi_Puan.jpeg
│   ├── 10_Pangpalek_Puan.jpeg        (canonical Pangpalek cloth)
│   ├── 11_Lianbuangthuam_Puan.jpeg
│   └── 12_Puanthupi_Puan.jpeg
├── references/
│   └── pattern-catalog.md            # Single source of truth: full specifications, ratios, and prompts
└── scripts/
    └── export_skill.py               # Standalone distribution packager and asset validator
```

---

## The Three Pillars of Paite Puan Fidelity

Every rendering or prompt must strictly uphold the following three pillars:

### Pillar 1: Pattern Architecture & Loom Geometry
1. **Loom Texture:** Rendered as a flat-lay, top-down orthographic 2D view of a traditional backstrap-loom handwoven cotton textile filling the entire frame.
2. **Stepped Geometry:** Motifs and lines follow the discrete warp/weft grid of a handloom with crisp thread-interlace texture. Motifs are stepped/pixelated—**never curved, organic, painterly, or printed-looking**.
3. **Warp Fringes:** Short, fine warp fringes appear **exclusively along the far left and right vertical edges** (where warp threads terminate on the loom). Never place fringes on the top or bottom edges.
4. **Exact Grid & Counts:** Strictly preserve band counts, stripe counts, and motif repetitions without adding or omitting elements.

### Pillar 2: Color Ratios & Mathematical Proportions
Every composite band, border, hairline, and interval has a fixed proportional relationship that must never be altered:
- **Band Core vs. Borders:** In banded cloths (Puandum, Siamsin), the central colored core is approximately **3× the combined thickness** of its flanking borders.
- **Bands vs. Intervals:** Solid ground intervals between composite bands are approximately **1.5× the height** of one composite band.
- **Vertical Columns:** Outer vertical borders vs. inner vertical divider columns maintain a **1 : 2 ratio** in thickness; vertical dividers divide the body into **3 equal horizontal columns**.
- **Edge Borders & Splits:** Specific percentage proportions (e.g. 50/50 split in Aksi; 12% top/bottom borders in Lianbuangthuam; 11% header in Puanthupi; 78% plain upper field in Pangpalek) must be strictly maintained.

### Pillar 3: Color Sequence & Spatial Order
1. **Directional Rhythm:** Colors within composite bands must be ordered strictly from outer edge to core (e.g. in Puandum: thin green → lemon yellow → crimson core → lemon yellow → thin green).
2. **Tri-Colour Lozenge Sequences:** White accent lines carrying tri-colour geometric lozenge segments must follow the exact left-to-right color sequence for that cloth:
   - **Green → Magenta-Pink → Royal Blue:** for *Paite Puandum*.
   - **Royal Blue → Magenta-Pink → Green:** for *Siamsin Puan*, *Thangsuah Puan*, and *Puanlaisan*.
3. **Vertical & Horizontal Layer Order:** Never invert headers, borders, or decorative zones (e.g., in Puanthupi, the solid black band is always at the top header; in Pangpalek, the butterfly/diamond border is near the bottom hem).

---

## The 12 Canonical Paite Puan Designs

| # | Pattern Name | Aspect | Primary Colors | Pattern Architecture, Exact Color Ratio & Order |
|---|---|---|---|---|
| **01** | **Paite Puandum** | 16:9 | Black `#000000`, Crimson `#E31E24`, Yellow `#FFF200`, Green `#00A83F` | **Ratio:** 5 composite bands (core 3× border width); 4 black intervals (1.5× band height); 4 vertical stripes (ratio 1:2:2:1) dividing cloth into 3 equal columns.<br>**Order:** Outside-in: green → yellow → crimson core → yellow → green. Lozenge sequence: green → magenta → blue. |
| **02** | **Siamsin Puan** | 3:2 | Black `#000000`, Hot Pink `#FF0088`, Green `#00A83F`, Royal Blue `#1E32FA` | **Ratio:** 5 composite bands (pink core 3× green/blue border width); 4 black intervals (~1.5× band height); exactly 10 lozenge motifs per line.<br>**Order:** Outside-in: white hairline → royal blue → kelly green → hot pink core → kelly green → royal blue → white hairline. Lozenge sequence: blue → pink → green. Only 2 thin red side pinstripes; NO interior vertical dividers. |
| **03** | **Thangsuah Puan** | 16:9 | Black `#000000`, Crimson `#C81428`, Yellow `#FFF200`, Green `#00A83F` | **Ratio:** 5 crimson composite bands evenly spaced across 6 black intervals; each crimson band is split by a white line of 8 lozenge segments; each black gap has 3 hairlines in 1:1:1 spacing.<br>**Order:** Outside-in: yellow hairline → green hairline → crimson → white motif line → crimson → green → yellow. Gap hairlines: red → white → red. Lozenge sequence: blue → pink → green. |
| **04** | **Puanlaisan** | 3:2 | Crimson `#B81428`, White `#FFFFFF`, Black `#000000`, Green `#14823B` | **Ratio:** 9 mirror-symmetric horizontal zones: Zones 1 & 9 (~12% height each), Zones 2, 4, 6, 8 (~8.5% white each), Zones 3 & 7 (~7% composite secondary), Zone 5 (~26% central core with 3 motif lines of 9 lozenges each).<br>**Order:** Top-to-bottom: Crimson border (with green-yellow-blue-pink-black trim) → White → Secondary band → White → Central Laisan band → White → Secondary band → White → Crimson border. Lozenge sequence: blue → pink → green. |
| **05** | **Galhang Puan** | 3:2 | Black `#000000`, Crimson `#C81E32`, White `#FFFFFF`, Amber `#8B4513` | **Ratio:** 11 horizontal lines spaced evenly; Lines 1, 5, 9 are rope-twist bands (~1.8× single white line width); 2 vertical edge columns (~3.5% width each).<br>**Order:** Line rhythm: Rope (1) → Solid white (2) → Beaded chain (3) → Solid (4) → Rope (5) → Solid (6) → Chain (7) → Solid (8) → Rope (9) → Solid (10) → Chain (11). Vertical column: amber → golden-orange → crimson → white zigzag → crimson → golden-orange → amber. |
| **06** | **Khephiau Puan** | 3:2 | Black `#000000`, White `#FFFFFF`, Grey `#CDCDCD` | **Ratio:** Orthogonal square plaid grid: 9 vertical columns × 7 horizontal rows; composite bands occupy ~5.5% canvas dimension each.<br>**Order:** Symmetrical assembly: thin white line → black space → grey basketweave core → black space → thin white line. Midway between assemblies: 3 ultra-thin white pinstripes. |
| **07** | **Ngoutekhelh Puan** | 3:2 | Black `#000000`, White `#FFFFFF`, Off-white `#EBEBEB` | **Ratio:** 3 equal central panels divided by 2 solid black columns (~4.5% width each); 16 white bands separated by 15 thin black stripes (~3:1 width ratio); top/bottom black borders + 5 white stripes.<br>**Order:** Edge-inward: black border → 5 white stripes / 4 black hairlines → black buffer stripe → central 16 white bands. Each black column flanked by white dotted hairline. |
| **08** | **Mal-am Puan** | 3:2 | Black `#000000`, White `#FFFFFF` | **Ratio:** 4 wide vertical bands (~6.5% width each) and 3 narrow accent strips (~0.8% width) separated by wide black intervals (~15% width).<br>**Order:** Vertical zones inside wide bands: upper 88% is dense interlocking triangle/pinwheel lattice; lower 12% transitions cleanly into fine herringbone twill. Purely vertical structure (NO horizontal stripes). |
| **09** | **Aksi Puan** | 3:2 | Midnight Indigo `#030322`, White `#FFFFFF` | **Ratio:** Exact 50/50 horizontal split: upper 50% completely plain; lower 50% filled with 18 offset rows of small white stars (~30 stars per row).<br>**Order:** Top-to-bottom: solid plain midnight ground → central single-thread seam → dense quincunx lattice of stepped 8-point octagonal stars (*Aksi*), each with an indigo center dot and 8-dot ring. |
| **10** | **Pangpalek Puan** | 3:2 | Midnight Indigo `#06051A`, Crimson `#B81D13`, Orange `#E67E22`, Green `#1E8449` | **Ratio:** Upper ~78% and bottom ~8% completely plain; lower horizontal decorative border occupies ~14% canvas height, centered and spanning ~85% width.<br>**Order:** Top-to-bottom: plain ground → row of 27 white butterfly motifs (*Pangpalek*) → center row of 26 interlocking stepped concentric diamonds (crimson/orange/green/white cross) → row of 27 white butterflies → plain ground. |
| **11** | **Lianbuangthuam Puan** | 4:3 | Maroon `#61071C`, White `#FFFFFF`, Pink `#FF1493`, Green `#00A83F` | **Ratio:** Top and bottom wide plain maroon borders (~12% height each); central zone of 12 multicolored bands separated by 11 maroon intervals; white side strips (~3% width) along central zone only.<br>**Order:** Alternating decorative weave: Odd bands (1, 3, 5, 7, 9, 11) feature diamond-lattice weave with white crosses; Even bands (2, 4, 6, 8, 10, 12) feature stepped diagonal chevrons. Red dotted pinstripe bisects white side margins. |
| **12** | **Puanthupi Puan** | 16:10 | Burgundy `#4A0414`, Black `#000000`, Gold `#FFD700`, Green `#00A83F` | **Ratio:** Solid black top header (~11% height); 7 stacked decorative bands alternating 4 flame-chevron bands (~11.5% each) and 3 diamond-lattice bands (~10% each), separated by 6 three-hairline dividers (~1.5% each).<br>**Order:** Top-to-bottom: Black header → Flame 1 → Lattice 2 → Flame 3 → Lattice 4 → Flame 5 → Lattice 6 → Flame 7. Flame bands contain 4 shaded vertical sawtooth tiers: (1) yellow/orange, (2) white/grey, (3) white/pink/crimson, (4) golden-yellow. Dividers: lime green → white → blue. |

---

## Workflow: Generating, Rendering & Verifying

1. **Identify the Pattern:**
   - Match the requested name or alias against the 12 canonical cloths.
   - If the user asks for a Paite cloth without naming one, list the 12 canonical cloths with their one-line signatures and ask them to select one.
2. **Load Authoritative Specification:**
   - Read the pattern's section in `references/pattern-catalog.md`.
   - Never generate from memory or allow modern synthetic variations.
3. **Compose Prompt with Strict Ratios & Order:**
   - Use the pattern's canonical prompt and attach the global rendering rules.
   - Enforce the exact aspect ratio, band counts, color ratios, and sequence order.
   - Append the mandatory negative prompt:
     ```text
     variations, modern recoloring, synthetic colors, teal, purple, perspective, 3D drape, folds, wrinkles, shadows, gradient lighting, model, mannequin, hands, background scene, text, logo, watermark, blurry, painterly, printed look, curved or floral organic motifs, extra colors, uneven spacing, asymmetry, missing fringes, fringes on top/bottom edges
     ```
4. **Bind Visual Reference Asset:**
   - Attach `assets/<pattern-id>.jpg` or `puan-images/<canonical_file>.jpeg` as reference when using image generation tools.
5. **Verify Before Presentation:**
   - Check every item in the pattern's **Must-check** list:
     1. Are band and stripe counts exact?
     2. Are mathematical color ratios preserved (e.g. 3× core, 1.5× interval, 50/50 split)?
     3. Is sequence order intact (layers, lozenge colors, header at top)?
     4. Are fringes strictly on the left and right edges?
6. **Report:**
   - State the canonical pattern name and aspect ratio.
   - Summarize the pattern structure, color ratios, and sequence order.
   - Provide the canonical hex palette codes.

---

## Packaging the Skill for Distribution

To export this skill as a self-contained, validated distribution archive containing all code, documentation, specifications, and 24 graphic assets:

```bash
# Verify skill integrity and assets
python3 scripts/export_skill.py --verify-only

# Package into distribution directory and ZIP archive
python3 scripts/export_skill.py --format both
```

The packager validates:
- Presence and image validity of all 12 standard reference assets in `assets/`.
- Presence and image validity of all 12 master 2560 px graphic files in `puan-images/`.
- Valid YAML frontmatter and zero-variation rules in `SKILL.md`.
- Dereferencing of symlinks to ensure the export is 100% portable across operating systems.
- Generates `MANIFEST.json` with SHA-256 checksums and provenance metadata.

---

## Authorship & Image Credits

- **Skill Author:** **Casey Paite**
- **Digital Cloth Reproductions:** **Mr. Siam Naulak**, **Naulak Web Design** ([naulak.com](https://naulak.com))
- **Design Origin:** Originally created as design material for the **2027 Calendar of the Young Paite Association (YPA), West Delhi Unit**.

Turning a handwoven cloth into a digital image is careful, skilled work. Each puan has been rebuilt thread by thread. The proportions of every band are kept, the exact colours of the yarn are matched, and the stepped geometry of each loom-woven motif is drawn as it was woven. The result is a set of clear, faithful images of Paite weaving. They honour the women weavers who have carried these designs through generations, and they let the patterns be studied, shared and preserved for the digital age.

*Digital reproductions © Siam Naulak, Naulak Web Design. When using, sharing, or referencing these reference images, credit Mr. Siam Naulak of Naulak Web Design (naulak.com).*
