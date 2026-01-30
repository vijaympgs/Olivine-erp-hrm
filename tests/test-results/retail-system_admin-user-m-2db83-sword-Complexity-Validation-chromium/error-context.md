# Page snapshot

```yaml
- generic [ref=e4]:
  - generic [ref=e5]:
    - img [ref=e7]
    - heading "Select Location" [level=1] [ref=e10]
    - paragraph [ref=e11]: Choose a location to work with for this session
  - generic [ref=e13]:
    - img [ref=e15]
    - paragraph [ref=e17]:
      - strong [ref=e18]: "Note:"
      - text: This location selection is for this session only and does not modify your user profile.
  - generic [ref=e19]:
    - generic [ref=e20]:
      - generic [ref=e21]: Select Location *
      - combobox [disabled] [ref=e22]:
        - option "-- Select a location --" [selected]
    - generic [ref=e23]:
      - button "Skip for Now" [ref=e24] [cursor=pointer]
      - button "Continue" [disabled] [ref=e25]:
        - text: Continue
        - img [ref=e26]
  - paragraph [ref=e29]: You can change the location anytime from your profile or settings.
```