---
id: E4
title: Memory Reference
category: efficiency
type: behavioral
detection: Runtime behavior — not detectable from file content
level: L4+
sources: [9, 25]
---

# Memory Reference

4,000-16,500 tokens saved per session.

Once a file is read, reference it from memory rather than re-reading.

**Observed waste:** Files re-read 3-4x per session in production usage.
