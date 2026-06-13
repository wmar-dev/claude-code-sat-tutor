---
description: Parses a Bluebook practice test score report PDF and produces a structured performance summary with scores, weak domains, and next steps. Use after a student completes a Bluebook practice test and has a score report PDF to review.
argument-hint: "[path-to-pdf]"
allowed-tools: Read, Write
---

# analyzing-results

## Workflow

Copy and track progress:
```
- [ ] 1. Read the PDF and extract scores
- [ ] 2. Show question accuracy
- [ ] 3. Identify weak domains
- [ ] 4. Compare to prior tests (read assets/student.md)
- [ ] 5. Update assets/student.md
- [ ] 6. Recommend next steps
```

If no path is given, find the most recently added PDF under `assets/`.

## Steps

**1. Score summary table:**
| Section | Score | Range |
|---------|-------|-------|
| Total | | 400–1600 |
| Reading & Writing | | 200–800 |
| Math | | 200–800 |

**2. Question accuracy:**
- Overall: X correct out of Y total (Z%)
- Reading & Writing: X/Y
- Math: X/Y

**3. Weak domains** — any domain where the bar chart appears less than ~75% filled. If domain data is unavailable, tell the student to check "My Practice" in the Bluebook app.

**4. Compare to prior tests** — read `assets/student.md` for score history. Show delta vs. the previous test.

**5. Update `assets/student.md`** — append the new result to the Score History table and refresh the Weak Areas section.

**6. Next steps** — based on weak domains, name which `/suggesting-practice` topics to run next.

Keep the tone encouraging and concise.
