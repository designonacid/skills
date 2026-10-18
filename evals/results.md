# Validation record

Date: 18 October 2026.

## Version 0.1.1 package checks

- Skill-creator validator passes with the complete four-lens assessment and heat-map requirements.
- Portable prompt regenerated; `python3 tools/build.py --check` confirms parity.
- The bundled framework SVG parses and is byte-identical to `artwork/acid-framework.svg`.
- Built ZIP passes its integrity check and includes the original framework asset, skill, reference, host metadata, and license.
- All local Markdown file links resolve, including the percent-encoded SVG filename.
- Git whitespace check passes.
- Added review cases for the required visual, Depth without audience research, genuine evidence gaps, explicit visual overrides, and portable asset access.

These are package checks, not independent host-behaviour tests. The new evaluation cases still need fresh-session runs before claiming multi-host reliability.

## Version 0.1.0

## Completed review

- Read all three source diagrams, including a rendered preview of the SVG.
- Cross-checked quadrant names, domain labels, elements, actions, and orientation against the supplied artwork.
- Reviewed the workflow for unsupported scoring, inferred audience responses, unavailable media, conflicting user instructions, and embedded commands.
- Created two illustrative worked examples and twelve host-level behaviour cases.

## Passed package checks

- Bundled skill-creator validator: skill is valid.
- Portable prompt matches the skill body and framework reference.
- Local Markdown file links resolve.
- SHA-256 comparisons confirm all three artwork copies match the originals.
- ZIP integrity check passes; it contains SKILL.md, the framework reference, optional host metadata, and the full license.
- Git whitespace check passes on the staged content.

These checks cannot prove that a host selects the skill or that another model follows the method reliably.

## Still to verify

No independent live Codex, Claude Code, or other-model behaviour runs have been performed. Run cases.md before claiming verified host compatibility or reliable automatic activation. The worked examples are authored illustrations, not observed evaluation outputs.

The method owner should review the proposed analytical questions and synthesis workflow before promoting this draft as an authoritative application of ACID.
