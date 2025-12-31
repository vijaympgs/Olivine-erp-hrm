# BBP Autoretry Prevention Guide

## __Preventive Lines for Autoretry, Cutoff, File Loss Issues:__

### __EMERGENCY RECOVERY INSTRUCTIONS__

- STOP IMMEDIATELY - Do not continue or regenerate from beginning
- USE THIS RECOVERY PROMPT: [recovery prompt template]
- Read BBP_Template_Reference.md for context
- Read target file to see current content
- Continue from exact stopping point
- Write ONLY the next section ([NEXT_SECTION_NUMBER])
- End with STOP MARKER: --- END OF SECTION [NEXT_SECTION_NUMBER] ---
- WAIT for next instruction before continuing

### __CONTENT LENGTH MANAGEMENT__

- Maximum 120 lines per response to prevent cutting
- Write one section at a time - never multiple sections
- Use STOP MARKERS after each section: `--- END OF SECTION X.Y.Z ---`
- If section exceeds 120 lines, split into subsections with proper numbering

### __CONTEXT PRESERVATION RULES__

- NEVER auto-retry or restart from beginning
- NEVER regenerate completed sections
- ALWAYS continue from exact stopping point
- MAINTAIN state across multiple responses
- VERIFY existing content before adding new content

### __SECTION COMPLETION CHECKLIST__

- BBP_Template_Reference.md has been read
- Target file content has been read
- Module numbering is correct (X.Y pattern)
- Section number is sequential
- 120-line limit will be respected
- STOP MARKER format is correct
- No auto-retry will occur

### __ERROR RECOVERY PROTOCOL__

- STOP writing immediately
- Announce the issue: "Context lost - using recovery protocol"
- Use the emergency recovery prompt
- Wait for confirmation before continuing
