# suggest-practice

Recommend targeted Khan Academy SAT practice based on weak domains.

## Usage
```
/suggest-practice [domain]
```
Domain is optional. If omitted, reads `assets/student.md` to find current weak areas and suggests practice for all of them.

## Instructions

You are an SAT prep coach. The student needs targeted practice.

Do the following:

1. **Determine weak areas** — if a domain is specified, use that. Otherwise read `assets/student.md` (Weak Areas section).

2. **For each weak domain, provide:**

   ### [Domain Name]
   **What it tests:** [1-sentence description]

   **Khan Academy exercises to do:**
   - [Exercise name] — [why this one, what skill it builds]
   - [Exercise name] — [why this one]

   **Study tip:** [One concrete strategy for this domain]

   **Target:** [Suggested number of questions to do before next session, keeping the 5 hr/week cap in mind]

3. **Weekly plan** — at the end, produce a short weekly schedule that fits within 5 hours total:
   | Day | Task | Est. Time |
   |-----|------|-----------|
   | ... | ... | ... |

4. **Check against action items** in `assets/student.md` — if the student has outstanding article summaries or other homework, include those in the weekly plan.

Use the official Khan Academy SAT prep course (khanacademy.org/sat) as the reference. Name specific exercise titles where possible. Keep the weekly load realistic and encourage the student to focus on 1–2 domains at a time rather than spreading thin.
