# Adaptive Writing · Architecture v0.1

## Non-negotiable rule

Do not add new exercise types simply to create variety. The game remains:

**English chunks → tap → numbered vertical order → 10 seconds → feedback → next.**

## Content contract

Campaign 1 compiles exactly **300 canonical sentences** from 15 validated writing patterns and five curated sets of 20 content variations. Each sentence has stable sentence and chunk identifiers, CEFR level, topic, writing function and canonical English/Spanish text.

Chunk boundaries are learning units, not arbitrary word splits. A chunk must be large enough to be useful and small enough to recombine.

## CEFR distribution

The pattern layer is intentionally B2-heavy:

- 10/15 patterns B2
- 4/15 patterns B2+
- 1/15 pattern C1

This yields approximately 66.7% B2, 26.7% B2+ and 6.7% C1 in the initial 300-sentence bank.

## Progress contract

Progress is stored separately from content and includes sentence stats, chunk stats, attempts, level history, rating, XP and streak. Import/export uses schema version 1 and the content version recorded in the content source.

Mastery combines accuracy, exposure, speed, successful retrieval across separate sessions and spaced retrieval. The five visible states are Seen, Familiar, Secure, Automatic and Durable. Durable cannot be reached from a single pass through the bank. Adaptive session composition favours due material, weak seen material and recent errors while keeping a smaller exploration quota for unseen sentences. The Spanish source remains stored as metadata but is intentionally not displayed in the timed game. Because removing the semantic prompt makes same-pattern content distractors potentially ambiguous, runtime distractors are disabled until a bank of specifically validated incompatible distractors exists.

## Audio-visual sequence

Candidate chunks remain neutral and are displayed in lowercase before selection, preventing capitalization from revealing the first chunk. After a tap, the chosen chunk moves into a numbered vertical slot and is rendered in the colour assigned to its **position**, using AVS ranks 1 → 4 → 7 → 10 → 13 → 15. The same positions trigger a short ascending note sequence. The timer copies the Adaptive English alternating tick pattern with stronger 3-2-1 ticks. On an incorrect answer, the same numbered slots snap to the canonical order so the correction can be read top-to-bottom without changing visual grammar.

## Timing

The timer is fixed at 10 seconds. Correctness has priority over speed. A sentence auto-submits when every chunk has been selected; timeout submits the partial sequence as incorrect.

## Recombination

Recombination is controlled. The content compiler creates only combinations defined by curated pattern/set pairings. Runtime play never invents arbitrary sentences.

## Lineage

Reference implementation: `adrianxds-ads/adaptive-english`.
Visual system: AVS 2.0 from `adrianxds-ads/adaptive-hoti0108`.
