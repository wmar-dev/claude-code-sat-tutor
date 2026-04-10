The SAT Tutor aims to help a high school student prepare for the SATs by leveraging skills and agents in Claude Code. The tutor aims to be efficient and cap work to 5 hours a week.

- Upload PDF results from Bluebook.
- Keep meeting notes on work done since last meeting and what to work on for the next meeting.
- Suggest practice material.
- Explain incorrect answers.

College board provides free digital practice test application called Bluebook. Tests are added over time and removed as older tests get outdated. They provide a great source for seeing how you are doing on your SAT prepartion.

Khan Academy is partnered College Board with official SAT preparation materials. 

Results from practice test stored under 
- `assets/Bluebook #4/`
- `assets/PSAT 8:9 #1/`

Meeting Notes stored under
- `assets/SAT Prep Meeting.docx`

## How to Use in a Session

**After taking a practice test**
1. Export the score report PDF from Bluebook and save it under `assets/<test name>/`
2. Run `/analyze-results` — Claude will summarize scores, compare to prior tests, and update `assets/student.md`

**Reviewing a missed question**
1. Screenshot the question from Bluebook and save it under the same test folder, or paste the question text
2. Run `/explain-question` — Claude will walk through the correct approach step by step and name the pattern to watch for

**After a tutoring session**
1. Run `/meeting-notes` — Claude will ask what was covered and produce a formatted notes entry
2. Confirm to append it to `assets/SAT Prep Meeting.docx`

**Planning the week's practice**
1. Run `/suggest-practice` — Claude reads current weak areas from `assets/student.md` and outputs a weekly Khan Academy plan within the 5 hr/week cap
