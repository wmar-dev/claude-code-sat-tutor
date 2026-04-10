# meeting-notes

Generate a structured meeting notes entry and append it to the Word doc, or display notes ready to paste.

## Usage
```
/meeting-notes
```
Run at the start or end of a tutoring session. Claude will ask what was covered and produce formatted notes.

## Instructions

You are the note-taker for an SAT tutoring session.

Do the following:

1. **Ask for (or use context already in the conversation) the following:**
   - Today's date
   - Questions or topics reviewed in this session
   - Any tips or patterns that came up
   - Action items for the student before next session

2. **Produce a formatted notes entry** using this structure:

   ```
   ---
   [DATE] | SAT Prep Meeting

   Topics Reviewed
   - [Question or topic]: [brief explanation of what was discussed and what the correct approach is]

   Tips & Patterns
   - [Tip name]: [one-sentence rule the student should remember]

   Action Items
   - [ ] [task]
   - [ ] [task]
   ```

3. **Update `assets/student.md`** — replace the Action Items section with the new list.

4. **Optionally append to the Word doc** — if the user confirms, use python-docx to append the entry to `assets/SAT Prep Meeting.docx`. Show the code you would run and ask for confirmation before executing.

Keep entries concise. Each topic entry should be 2–4 sentences max.
