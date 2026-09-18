# Adaptive Writing · B2 → C1

Adaptive Writing is the writing-focused sibling of **Adaptive English** and **Adaptive HOTI0108**.

## Core loop

**Shuffled English chunks → tap to build a numbered vertical sentence → 10 seconds → feedback → next.**

The interaction type never changes. Variety comes from the content, chunk combinations, topics and difficulty.

## Campaign 1

- 300 fixed canonical sentences
- 15 writing patterns × 20 curated variations
- 15 questions per level
- Fixed 10-second clock
- B2-dominant progression with B2+ and a small C1 layer
- Chunk-level and sentence-level mastery with five states: Seen → Familiar → Secure → Automatic → Durable
- Durable mastery requires successful retrieval across separate sessions and spaced reviews
- Adaptive selection reserves attention for due material, weak chunks, unseen sentences and recent errors
- English-only play: the Spanish source remains in content metadata but is not displayed during the timed game
- Candidate chunks are rendered in lowercase so capitalization cannot reveal the first position
- Selected chunks occupy numbered vertical slots; incorrect answers snap to the canonical order in the same slots
- Position colour sequence using **Adrián Visual System · AVS 2.0**
- Adaptive English-style alternating timer ticks, stronger 3-2-1 ticks, answer sounds and short position notes generated with Web Audio
- Export/import of progress JSON
- Offline-capable PWA

## Architecture

Content and user progress are deliberately separate.

- `data/content.js` → curated content source
- `app.js` → compilation, adaptive engine, timing, audio, scoring and persistence
- `adrian-visual-system.js` → shared AVS 2.0 colour language
- browser storage key → `adaptive_writing_v1`

The 300 sentences are deterministic. No AI generates sentences during play.

## Ecosystem

- `adrianxds-ads/adaptive-english` — grammar/adaptive quiz reference
- `adrianxds-ads/adaptive-hoti0108` — tourism study sibling and AVS reference
- `adrianxds-ads/limpieza-2.0` — separate private automation project in the same personal ecosystem
- `adrianxds-ads/adaptive-writing` — this project

See `docs/ADAPTIVE_WRITING_SPEC.md` for the learning and data contract.
