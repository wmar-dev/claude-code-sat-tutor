---
description: Converts a Bluebook/PSAT score report PDF into a lightweight markdown summary (scores, accuracy, domain performance) saved alongside the PDF. Use once per new score report PDF, typically as a first step before /analyzing-results, so the PDF doesn't need to be read again.
argument-hint: "[path-to-pdf]"
allowed-tools: Read, Write
---

# converting-score-reports

## Workflow

Copy and track progress:
```
- [ ] 1. Locate the PDF
- [ ] 2. Read and extract scores, accuracy, and domain bars
- [ ] 3. Write markdown summary alongside the PDF
- [ ] 4. Report the output path
```

If no path is given, find the most recently added PDF under `assets/` that doesn't already have a matching `.md` file (same name, `.md` extension, same folder).

## Steps

**1. Read the PDF.**

**2. Extract:**
- Test name and date (e.g., "SAT Practice 4", "January 25, 2026") — the test name indicates the scale (see note below)
- Total score + range **as printed on the report** (do not assume — ranges differ by test type)
- Reading & Writing score + range **as printed**
- Math score + range **as printed**
- Question accuracy: overall, R&W, Math (correct/total)
- Domain performance bars — for each of the 8 domains, estimate the filled portion of the bar as a percentage, rounded to the nearest 5%. A fully filled bar = 100%; roughly half = 50%, etc.

> **Score scales differ by test type** — always read the range printed on the report, don't hardcode:
> - SAT: Total 400-1600, sections 200-800
> - PSAT/NMSQT & PSAT 10: Total 320-1520, sections 160-760
> - PSAT 8/9: Total 240-1440, sections 120-720

**3. Write a markdown file** with the same base name as the PDF (e.g., `ELIM_SAT_PRACTICE_4_01252026.md`) in the same folder:

```markdown
# [Test Name] — [Date]

**Test type:** [SAT / PSAT 10 / PSAT 8-9 / etc.]

## Scores
| Section | Score | Range |
|---------|-------|-------|
| Total | [score] | [range as printed] |
| Reading and Writing | [score] | [range as printed] |
| Math | [score] | [range as printed] |

## Question Accuracy
- Overall: [correct]/[total] ([pct]%)
- Reading and Writing: [correct]/[total] ([pct]%)
- Math: [correct]/[total] ([pct]%)

## Domain Performance (estimated fill %)
| Domain | Section | Fill |
|--------|---------|------|
| Information and Ideas | R&W | x% |
| Expression of Ideas | R&W | x% |
| Craft and Structure | R&W | x% |
| Standard English Conventions | R&W | x% |
| Algebra | Math | x% |
| Advanced Math | Math | x% |
| Problem-Solving and Data Analysis | Math | x% |
| Geometry and Trigonometry | Math | x% |
```

**4. Report the output path.** Once this markdown file exists, `/analyzing-results` and other skills should read it instead of the PDF.
