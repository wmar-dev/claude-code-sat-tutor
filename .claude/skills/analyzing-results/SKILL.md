---
description: Parses a Bluebook practice test score report PDF and produces a structured performance summary with scores, weak domains, and next steps. Use after a student completes a Bluebook practice test and has a score report PDF to review.
argument-hint: "[path-to-pdf]"
allowed-tools: Read, Write
---

# analyzing-results

## Workflow

Copy and track progress:
```
- [ ] 1. Get markdown summary (convert PDF if needed) and extract scores
- [ ] 2. Show question accuracy
- [ ] 3. Identify weak domains
- [ ] 4. Compare to prior tests (read assets/student.md)
- [ ] 5. Update assets/student.md
- [ ] 6. Recommend next steps
```

If no path is given, find the most recently added PDF under `assets/`.

## Steps

**1. Get a markdown summary.** Check for a `.md` file with the same base name as the PDF in the same folder. If it exists, read that instead of the PDF. If it doesn't exist, run `/converting-score-reports` on the PDF first, then read the resulting markdown.

Show the score summary table directly from the markdown (Total/R&W/Math scores and ranges) — **ranges vary by test type** (SAT: 400-1600/200-800; PSAT 10/NMSQT: 320-1520/160-760; PSAT 8/9: 240-1440/120-720), so use whatever the markdown reports, not a fixed range.

**2. Question accuracy:**
- Overall: X correct out of Y total (Z%)
- Reading & Writing: X/Y
- Math: X/Y

**3. Weak domains** — any domain with fill < 75% in the Domain Performance table is weak. If domain data is unavailable, tell the student to check "My Practice" in the Bluebook app.

**4. Compare to prior tests** — read `assets/student.md` for score history. PSAT 8/9, PSAT 10/NMSQT, and SAT all share the same vertical scale (see `assets/sat-psat-scale-reference.md`), so a numeric point delta vs. the previous test is meaningful even across test types. **Ceiling effect:** if a score equals its test's max for that section (e.g., 760/760 on PSAT 10 Math, 720/720 on PSAT 8/9), flag that true skill could be higher than reported — the lower-ceiling test can't distinguish further at the top.

**5. Update `assets/student.md`** — append the new result to the Score History table and refresh the Weak Areas section.

**6. Next steps** — based on weak domains, name which `/suggesting-practice` topics to run next.

Keep the tone encouraging and concise.
