# analyze-results

Analyze a Bluebook practice test score report and produce a structured performance summary.

## Usage
```
/analyze-results [path-to-pdf]
```
If no path is given, look for the most recently added PDF under `assets/`.

## Instructions

You are an SAT tutor assistant. The user has uploaded a Bluebook practice score report PDF.

Do the following:

1. **Read the PDF** at the provided path (or find the latest one under `assets/`).

2. **Extract and display a score summary table:**
   | Section | Score | Range |
   |---------|-------|-------|
   | Total | | 400–1600 |
   | Reading & Writing | | 200–800 |
   | Math | | 200–800 |

3. **Show question accuracy:**
   - Overall: X correct out of Y total (Z% correct)
   - Reading & Writing: X/Y correct
   - Math: X/Y correct

4. **Identify weak domains** — list any domain where the bar chart in the PDF appears incomplete (less than ~75% filled). If domain-level data is unavailable in the report, note that the student should check "My Practice" in the Bluebook app.

5. **Compare to previous tests** by reading `assets/student.md` for score history. Show delta vs. prior test if available.

6. **Update `assets/student.md`** — append the new test result to the Score History table and update the Weak Areas section.

7. **Recommend next steps** — based on weak domains, suggest which `/suggest-practice` topics to run next.

Keep the tone encouraging and concise.
