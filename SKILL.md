---
name: rf-antenna-literature-reader
description: Use this skill when reading, summarizing, comparing, or extracting engineering knowledge from RF, microwave, antenna, LPDA, broadband antenna, miniaturized antenna, matching network, CST, HFSS, ADS, or electromagnetic simulation papers. Use when the user wants literature notes, PDF figure/table extraction, CST/HFSS reproduction guidance, research planning, paper review, or technical-report-ready summaries for antenna and RF engineering literature.
---

# RF Antenna Literature Reader

## Purpose

Read RF, microwave, antenna, and electromagnetic simulation literature in a way that supports engineering reproduction, CST/HFSS modeling, design comparison, and research planning.

Prioritize extracting:

- design motivation and research problem
- antenna structure and radiating/feed/matching parts
- geometry and material parameters
- key formulas and assumptions
- simulation and measurement setup
- S-parameters, gain, efficiency, beamwidth, radiation patterns
- figure/table information that text extraction may miss
- reproducible CST/HFSS modeling steps
- useful ideas for LPDA, broadband, miniaturized antenna, and matching design

## Core Rules

1. Do not invent missing parameters, dimensions, formulas, frequency bands, performance values, or conclusions.
2. If a value is not stated in the paper, write "not stated" or "not given in the paper".
3. If a value is inferred from a figure or page screenshot, clearly mark it as "estimated from figure" / "估读", not as an exact paper value.
4. Do not write estimated values as if they were exact values from the paper.
5. Every important technical claim must cite the paper location: page, section, figure, table, or equation when available.
6. Keep engineering units explicit, such as GHz, MHz, mm, dB, dBi, %, ohm, lambda0, lambdag.
7. Separate paper facts from analysis and design suggestions.
8. For simulation papers, extract software, solver type, boundary conditions, ports, mesh/accuracy settings, material models, and whether each result is simulated or measured.
9. For antenna structures, identify radiating elements, feed structures, matching networks, loading structures, parasitic/director/reflector structures, ground structures, and termination structures.
10. For CST/HFSS reproduction, convert paper information into step-by-step modeling guidance and clearly mark uncertain details.

## PDF Figure and Table Workflow

When the paper is a PDF and figures/tables matter:

1. Prefer PyMuPDF (`fitz`) to render important pages at 300 dpi.
2. Save rendered pages in `extracted_pages/` under the paper's output folder.
3. If a table cannot be extracted from the text layer, read it directly from the rendered page screenshot.
4. For antenna papers, prioritize these pages/figures:
   - antenna structure diagrams
   - design parameter tables
   - S11 / return-loss curves
   - gain, realized gain, efficiency, and beamwidth curves
   - radiation patterns
   - surface-current distributions
   - parameter sweeps
   - measurement setup photos
5. If only visual reading is possible, write "估读" in the value or notes column.
6. If PyMuPDF is unavailable, install/use it when permitted. If installation or rendering is blocked, state the blocker and do not pretend text extraction is sufficient for visual tables.

Use the bundled script when useful:

```powershell
python scripts/render_pdf_pages.py "path\to\paper.pdf" --out "E:\文献整理codex\paper-name\extracted_pages" --pages 1 3 5 6 7 --dpi 300
```

## Output and Archiving

Default long-term output root:

```text
E:\文献整理codex
```

For each paper, create one folder named from the paper title or PDF filename:

```text
E:\文献整理codex\<paper_slug>\
```

Recommended folder contents:

```text
<paper_slug>\
  summary.md
  extracted_pages\
    page_01_300dpi.png
    ...
  tables\
    antenna_metrics.csv
  notes\
    design_ideas.md
  tasks\
    reproduction_plan.md
```

If the sandbox cannot write to `E:\文献整理codex`, request permission to write there. If permission is not available, write to the current workspace `outputs/` folder and tell the user clearly.

Do not overwrite existing summaries or tables unless the user explicitly asks. If a folder/file already exists, create a timestamped or incremented filename.

## Standard Output Structure for One Paper

### 1. Basic Information

- Title:
- Authors:
- Year:
- Journal / conference:
- DOI:
- Research topic:
- Antenna / circuit type:
- Target frequency band:
- Application scenario:

### 2. Research Problem

Explain what problem the paper is trying to solve:

- size reduction
- bandwidth increase
- impedance matching
- gain, efficiency, directivity, F/B ratio, beamwidth, or radiation pattern improvement
- fabrication/integration problem
- new structure vs optimization of known structure

### 3. Core Method

Identify:

- main radiator
- feed structure
- ground structure
- loading structure
- parasitic/director/reflector structure
- matching network
- termination load
- substrate and metal layers
- symmetry or self-similarity
- resonant, traveling-wave, leaky-wave, array-based, or frequency-independent behavior

### 4. Geometry and Material Parameters

Use tables when possible.

| Parameter | Value | Unit | Source | Notes |
|---|---:|---|---|---|
| Operating frequency |  |  |  |  |
| Substrate |  |  |  |  |
| Relative permittivity epsilon_r |  |  |  |  |
| Loss tangent tan delta |  |  |  |  |
| Substrate thickness |  |  |  |  |
| Copper thickness |  |  |  |  |
| Overall size |  |  |  |  |
| Radiator length |  |  |  |  |
| Radiator width |  |  |  |  |
| Feedline width |  |  |  |  |
| Feed gap / port gap |  |  |  |  |
| Load / termination |  |  |  |  |
| Ground size |  |  |  |  |
| Other key dimensions |  |  |  |  |

For LPDA/log-periodic structures, additionally extract:

| Parameter | Value | Unit | Source | Notes |
|---|---:|---|---|---|
| Scale factor tau |  |  |  |  |
| Spacing factor sigma |  |  |  |  |
| Apex angle alpha |  |  |  |  |
| Number of elements |  |  |  |  |
| Longest element length |  |  |  |  |
| Shortest element length |  |  |  |  |
| Element spacing |  |  |  |  |
| Feedline impedance |  |  |  |  |
| Termination method |  |  |  |  |

### 5. Key Equations

For each formula:

- original equation
- physical meaning
- variables and units
- assumptions
- theoretical / empirical / simulation-optimized nature
- how it can be used in CST/HFSS/ADS design

Do not simplify a formula in a way that changes its meaning.

### 6. Simulation and Measurement Setup

| Item | Information |
|---|---|
| Simulation software |  |
| Solver type |  |
| Frequency sweep range |  |
| Boundary conditions |  |
| Excitation / port type |  |
| Mesh settings |  |
| Material model |  |
| Fabrication method |  |
| Measurement instrument |  |
| Calibration method |  |
| Measured or simulated results |  |

### 7. Performance Metrics

| Metric | Value | Frequency / Band | Simulated or Measured | Source | Notes |
|---|---:|---|---|---|---|
| S11 / return loss |  |  |  |  |  |
| VSWR |  |  |  |  |  |
| Impedance bandwidth |  |  |  |  |  |
| Gain |  |  |  |  |  |
| Realized gain |  |  |  |  |  |
| Radiation efficiency |  |  |  |  |  |
| Total efficiency |  |  |  |  |  |
| Directivity |  |  |  |  |  |
| F/B ratio |  |  |  |  |  |
| HPBW / beamwidth |  |  |  |  |  |
| Cross-polarization |  |  |  |  |  |
| Input impedance |  |  |  |  |  |

### 8. Figures and Current Distribution

Extract the engineering meaning of geometry diagrams, equivalent circuits, S-parameter curves, radiation patterns, current distributions, gain/efficiency curves, and parameter sweeps.

For current distribution, explain:

- strong-current regions
- whether the current path is extended
- whether loading changes electrical length
- whether radiation comes from the main radiator or loading/parasitic part
- whether current directions may cause cancellation

### 9. Reproducibility for CST/HFSS

Provide practical modeling guidance:

1. objects to create first
2. coordinate system
3. material setup
4. port setup
5. boundary setup
6. sweep setup
7. monitors to add
8. parameters to scan
9. expected curves
10. main uncertainties

For CST, pay special attention to discrete port / waveguide port / coaxial feed, open boundary distance, mesh near feed/gaps, lossy substrates, finite copper thickness, baluns, explicit feeding line modeling, and lumped/physical terminations.

### 10. Relation to the User's Research

Use this structure:

- Useful idea:
- Why it may help:
- What problem it targets:
- Possible implementation in the user's LPDA / antenna model:
- Expected benefit:
- Possible risk:
- What needs to be verified by simulation:

Pay special attention to miniaturization, S11, broadband matching, gain/efficiency degradation, current path extension, loading structures, folded/meandered/T-shaped/capacitive/inductive structures, termination loads, feedline design, LPDA self-similarity, and size-performance tradeoffs.

### 11. Critical Evaluation

Discuss:

- fairness of comparison
- whether measured results are included
- simulation detail sufficiency
- fabrication difficulty
- missing parameters
- whether improvement is radiation enhancement or only impedance matching
- efficiency/gain sacrifice
- scalability to other bands
- usefulness for the user's current research

### 12. Final Concise Conclusion

End with:

- One-sentence summary:
- Most useful technical point:
- Most important limitation:
- Recommended next action for the user:
