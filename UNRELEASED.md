# Unreleased

## Fixed

- Fix pattern-not-regex rules (C12, E3, E4, E5) firing on every heading line instead of checking file-level content. Changed anchor from `^#` to `(?s)\A#[\s\S]+` to match entire file and evaluate pattern-not-regex against full content.
