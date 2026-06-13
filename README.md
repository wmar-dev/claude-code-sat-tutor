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

## Setup

Some skills rely on Python scripts (e.g. converting Word docs to markdown) managed with [uv](https://docs.astral.sh/uv/).

- `make install` — install Python dependencies with uv
- `make install-system` — install system dependencies (pandoc, via Homebrew)
- `make clean` — remove the virtual environment and cached files

## How to Use in a Session

Each skill can be run directly as a slash command, or triggered automatically — just tell Claude what you want and it picks the right skill based on context.

**After taking a practice test**
1. Export the score report PDF from Bluebook and save it under `assets/<test name>/`
2. Run `/converting-score-reports` or tell Claude: "convert this score report" — Claude turns the PDF into a lightweight markdown summary saved alongside it (run once per new PDF)
3. Run `/analyzing-results` or tell Claude: "analyze my results" — Claude will summarize scores, compare to prior tests, and update `assets/student.md`

**Reviewing a missed question**
1. Screenshot the question from Bluebook and save it under the same test folder, or paste the question text
2. Run `/explaining-questions` or tell Claude: "explain this question" — Claude will walk through the correct approach step by step and name the pattern to watch for

**After a tutoring session**
1. Run `/writing-meeting-notes` or tell Claude: "write meeting notes" — Claude will ask what was covered and produce a formatted notes entry
2. Confirm to append it to `assets/SAT Prep Meeting.docx`

**Checking overall progress**
1. After a few practice tests have been logged in `assets/student.md`
2. Run `/tracking-progress` or tell Claude: "track my progress" — Claude shows score trajectory over time, flags domains that stay weak test after test, and notes which weak areas have improved

**Planning the week's practice**
1. Run `/suggesting-practice` or tell Claude: "suggest practice" — Claude reads current weak areas from `assets/student.md` and outputs a weekly Khan Academy plan within the 5 hr/week cap

**Reviewing an article summary**
1. Paste the article URL and the student's written summary
2. Run `/reviewing-summaries` or tell Claude: "review this summary" — Claude scores it on main idea, evidence, author's purpose, and conciseness, and maps each dimension to the SAT question type it trains

**Generating practice questions from an article**
1. Paste an article URL or passage text
2. Run `/generating-questions` or tell Claude: "generate questions from this article" — Claude produces 4–6 SAT-style Reading and Writing questions with four answer choices, then explains every wrong answer using process of elimination

**Drilling vocabulary in context**
1. Paste an article URL, a passage, or just say "random"
2. Run `/words-in-context` or tell Claude: "drill words in context" — Claude presents SAT-style vocabulary questions and teaches the substitution strategy for eliminating wrong choices
