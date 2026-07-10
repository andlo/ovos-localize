# TODO — ovos-localize

Living backlog. Consolidates the former `AUDIT.md`, `SUGGESTIONS.md`, and
`MAINTENANCE_REPORT.md` (deleted — their content either landed here as an
open item, was already fixed, or was historical narration that belongs in
git history, not a tracked file). Durable architectural facts live in
`docs/architecture.md`.

## Open issues

- [ ] #200 Dependency Dashboard
- [ ] #158 [translate] it-IT: OscillateLabsLLC/skill-homeassistant — skill.json
- [ ] #157 [translate] it-IT: OscillateLabsLLC/skill-homeassistant — assist.error.dialog
- [ ] #156 [translate] it-IT: OscillateLabsLLC/skill-homeassistant — assist.intent
- [ ] #139 Edit all in one page or session edit (enhancement)
- [ ] #208 Add language: Kabyle (kab) — PR #211 (support code) + PR #209 (enable) open

Note: most `[translate] ...` issues are translator submissions consumed by `submit_translation.yml`, not engineering tasks.

## Gaps

- [ ] Large generated datasets committed to git: `data/dataset.tsv`, `data/dataset_1.tsv`, `data/dataset_2.tsv` (~100MB) and `data/datasets/**/*.jsonl`. Move to a data branch / HF backend instead of `dev` (ADR needed first — see roadmap Phase B2).
- [ ] No linter or type checker configured (ruff/mypy).
- [ ] No PyPI release automation.
- [ ] Standardize type hints across the project (was `SUGGESTIONS.md`) — low complexity, improves static-error catching.

## Done (kept for issue/PR traceability, remove once merged)

- [x] Standard CI test gating (build-tests + lint via gh-automations) — PR #210
- [x] `ast.Str` deprecation in `ast_analyzer.py` (broke on Python 3.14) — PR #210
- [x] Untracked scratch (`.coverage`, `ovos_localize.egg-info/`) — already gitignored, non-issue

## Code TODOs

None found.
