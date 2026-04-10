---
description: Generates a structured notes entry for a tutoring session and optionally appends it to the Word doc. Use at the start or end of each SAT tutoring session to record what was covered and set action items.
allowed-tools: Read, Write, Bash
---

# writing-meeting-notes

## Workflow

```
- [ ] 1. Gather session details (date, topics, tips, action items)
- [ ] 2. Produce formatted notes entry
- [ ] 3. Update assets/student.md action items
- [ ] 4. Confirm before appending to Word doc
```

## Steps

**1. Gather** (use conversation context or ask):
- Date
- Questions/topics reviewed
- Tips or patterns that came up
- Action items for the student before next session

**2. Produce this entry format:**
```
---
[DATE] | SAT Prep Meeting

Topics Reviewed
- [topic]: [correct approach in 2–3 sentences]

Tips & Patterns
- [tip name]: [one-sentence rule to remember]

Action Items
- [ ] [task]
```

**3. Update `assets/student.md`** — replace the Action Items section with the new list.

**4. Word doc** — if the user confirms, append the entry to `assets/SAT Prep Meeting.docx` using python-docx. Show the command first; do not run it without confirmation.
