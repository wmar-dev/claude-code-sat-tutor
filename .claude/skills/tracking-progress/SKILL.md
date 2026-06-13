---
description: Reviews score history and weak-area trends across all completed practice tests in assets/student.md — flags domains that stay weak test after test, tracks score trajectory, and checks whether past action items paid off. Use periodically (every few sessions) to step back from a single test and look at overall progress.
allowed-tools: Read, Write
---

# tracking-progress

## Workflow

Copy and track progress:
```
- [ ] 1. Read assets/student.md
- [ ] 2. Show score trajectory
- [ ] 3. Flag recurring weak domains
- [ ] 4. Note improved areas
- [ ] 5. Check action-item follow-through
- [ ] 6. Recommend focus and update Trends section
```

## Steps

**1. Read `assets/student.md`.** If it doesn't exist, or the Score History table has fewer than 2 entries, say there isn't enough data for trends yet and suggest running `/analyzing-results` after the next practice test. Stop here in that case.

**2. Score trajectory:**
| Test | Date | Total | R&W | Math |
|------|------|-------|-----|------|

Fill from the Score History table. Add a delta vs. the previous test for each score column (e.g., "+40") — PSAT 8/9, PSAT 10/NMSQT, and SAT share the same vertical scale (see `assets/sat-psat-scale-reference.md`), so deltas are meaningful across test types too. **Ceiling effect:** if a score equals its test's max for that section, note that the true gain may be larger than the delta shows — the lower-ceiling test topped out.

**3. Recurring weak domains** — compare the Weak Areas noted at each test in the history. List any domain/subdomain flagged as weak in 2 or more consecutive tests, e.g.:
- "Craft and Structure — Words in Context: weak in Bluebook #3 and #4 (2 tests running)"

These are the highest-priority targets — practice so far hasn't moved the needle.

**4. Improved areas** — domains that were weak in an earlier test but are no longer flagged. Call these out as wins worth mentioning to the student.

**5. Action item follow-through** — compare past Action Items (and recent meeting notes, if relevant) against the latest test results. Did the targeted practice show up as improvement in that domain, or is the same gap still there?

**6. Recommend focus** — name 1–2 domains to prioritize next with `/suggesting-practice`, favoring recurring weak domains over ones that only appeared once. Then update the **Trends** section in `assets/student.md`:

```
## Trends
- Recurring weak domains: [list with test count]
- Improved domains: [list]
- Score trajectory: [Total/R&W/Math deltas across tests]
```

Replace any existing Trends section with the refreshed one.

Keep the tone encouraging — frame recurring weaknesses as "where the next gains are," not failures.
