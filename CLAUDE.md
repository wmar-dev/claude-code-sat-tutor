# SAT Tutor — Claude Code Project

## Overview
This project helps a high school student prepare for the SAT using Claude Code skills and agents.
Work is capped at ~5 hours per week.

## Assets
- Practice test PDFs (Bluebook score reports): `assets/<test name>/`
- Meeting notes (Word doc): `assets/SAT Prep Meeting.docx`
- Screenshots of missed questions: stored alongside PDFs in the test folder
- Student score history and details: `assets/student.md`
- SAT/PSAT vertical scale reference (for cross-test score comparisons): `assets/sat-psat-scale-reference.md`

## Privacy
Everything under `assets/` that identifies or describes the student is private and must never be committed (enforced via `.gitignore`):
- `assets/student.md` — score history and personal details
- `assets/SAT Prep Meeting.docx` — meeting notes
- `assets/SAT Prep Meeting.md` — generated markdown cache of meeting notes (from `extract_meeting_notes.py`)
- `assets/<test name>/*.pdf` — score report PDFs
- `assets/<test name>/*.png` — question screenshots
- `assets/<test name>/*.md` — generated score summaries (from `/converting-score-reports`)

Only generic reference material (e.g. `assets/sat-psat-scale-reference.md`) is tracked in git. When adding new asset types or test folders, update `.gitignore` to match this pattern.

## Available Skills
| Skill | Description |
|-------|-------------|
| `/converting-score-reports` | Convert a score report PDF to a lightweight markdown summary (run once per PDF) |
| `/analyzing-results` | Parse a Bluebook PDF score report and summarize performance |
| `/tracking-progress` | Review score history and weak-area trends across all tests |
| `/explaining-questions` | Walk through a missed question (from screenshot or description) step-by-step |
| `/writing-meeting-notes` | Update the meeting notes doc with what was covered and next action items |
| `/suggesting-practice` | Recommend specific Khan Academy exercises based on weak areas |
| `/reviewing-summaries` | Score and give feedback on a student's article summary (ties to SAT R&W skills) |
| `/generating-questions` | Generate SAT-style R&W questions from any article URL or passage |
| `/words-in-context` | Drill SAT vocabulary-in-context questions using an article or built-in set |

## SAT Structure
**Reading and Writing (200–800)**
- Information and Ideas (26%, ~12–14 Qs)
- Expression of Ideas (20%, ~8–12 Qs)
- Craft and Structure (28%, ~13–15 Qs)
- Standard English Conventions (26%, ~11–15 Qs)

**Math (200–800)**
- Algebra (35%, ~13–15 Qs)
- Advanced Math (35%, ~13–15 Qs)
- Problem-Solving and Data Analysis (15%, ~5–7 Qs)
- Geometry and Trigonometry (15%, ~5–7 Qs)

## Key Tutoring Principles
- Work by process of elimination on Reading/Writing questions
- For math: always think in terms of multiplying by a factor (e.g. "increase by 167%" = × 2.67, not × 1.67)
- Distinguish "by" (relative change) vs "to" (absolute value)
- Keep explanations concrete and short — show the reasoning step by step
- Sessions are capped at ~5 hours/week total prep time

## Meeting Notes Format
Each meeting entry in `assets/SAT Prep Meeting.docx` should include:
- Date and attendees
- Questions reviewed (with explanations)
- Tips/patterns identified
- Action items for next session
