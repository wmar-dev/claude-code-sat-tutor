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

Article summaries (student-written, with source URLs) stored in
- `Article Reading Summaries.docx`

## How to Use in a Session

Skills are invoked by telling Claude what to do — they are not slash commands you type yourself.

**After taking a practice test**
1. Export the score report PDF from Bluebook and save it under `assets/<test name>/`
2. Tell Claude: "analyze my results" — Claude will summarize scores, compare to prior tests, and update `assets/student.md`

**Reviewing a missed question**
1. Screenshot the question from Bluebook and save it under the same test folder, or paste the question text
2. Tell Claude: "explain this question" — Claude will walk through the correct approach step by step and name the pattern to watch for

**After a tutoring session**
1. Tell Claude: "write meeting notes" — Claude will ask what was covered and produce a formatted notes entry
2. Confirm to append it to `assets/SAT Prep Meeting.docx`

**Planning the week's practice**
1. Tell Claude: "suggest practice" — Claude reads current weak areas from `assets/student.md` and outputs a weekly Khan Academy plan within the 5 hr/week cap

**Reviewing an article summary**
1. Paste the article URL and the student's written summary
2. Tell Claude: "review this summary" — Claude scores it on main idea, evidence, author's purpose, and conciseness, and maps each dimension to the SAT question type it trains

**Generating practice questions from an article**
1. Paste an article URL or passage text
2. Tell Claude: "generate questions from this article" — Claude produces 4–6 SAT-style Reading and Writing questions with four answer choices, then explains every wrong answer using process of elimination

**Drilling vocabulary in context**
1. Paste an article URL, a passage, or just say "random"
2. Tell Claude: "drill words in context" — Claude presents SAT-style vocabulary questions and teaches the substitution strategy for eliminating wrong choices
