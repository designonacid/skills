# ACID Method for AI

Analyse content through **Abstraction, Creativity, Intention, and Depth**—the ACID Method by **Design On Acid**.

This repository provides an installable Agent Skill and a portable prompt for LLMs. Use ACID to critique writing, designs, images, presentations, campaigns, and concepts with attention to meaning, expression, purpose, and human connection.

**Version 0.1.0 — initial implementation.** The four lenses and their relationships come from the supplied framework diagrams. The LLM workflow is a proposed application for review, rather than an established numerical scoring standard.

![ACID Method by Design On Acid](artwork/acid-method.png)

| Lens | Focus |
| --- | --- |
| **Abstraction** | Perception & Cognition — Analyse, quantify |
| **Creativity** | Expression & Transformation — Disrupt, Create |
| **Intention** | Organization & Operation — Organize, Stabilize |
| **Depth** | Emotion & Connection — Experience, Empathise |

## Start here

- **Install a skill:** follow [installation instructions](docs/installation.md) for Codex or Claude Code.
- **Use another LLM:** copy [the portable prompt](prompts/acid-method.md) into a chat or supported project instructions, then supply your content.
- **Understand the method:** read [the framework reference](skills/acid-method/references/framework.md).
- **See an analysis:** read [worked examples](docs/examples.md).
- **Develop the skill:** use [the evaluation cases](evals/cases.md) and [release plan](docs/plan.md).

Try:

> Analyse this landing-page copy for first-time visitors. Identify what works and what to improve.

Or invoke the skill explicitly:

> Use the ACID Method to compare these two campaign concepts for the same audience.

## Make ACID your default

The skill description includes ordinary content-analysis requests, so supporting hosts can select it without you naming ACID. Installation alone does **not** guarantee activation on every request. Selection, access to references, and persistent instructions depend on the host.

For a stronger preference, add the instruction in [installation → Default analysis](docs/installation.md#default-analysis) to your host's supported persistent instructions. Explicit requests for another method still take precedence. This skill concerns content analysis; it does not redefine database ACID properties.

## What this package does

It connects evidence to interpretation and practical recommendations across all four lenses. It marks missing evidence, avoids invented scores, and adapts detail to the request. It requires no API key, package dependency, or executable installer. Analyse only the material the host can actually access.

The portable prompt is generated from the skill and its framework reference. No live multi-host activation testing has been completed yet; see the [evaluation record](evals/results.md).

## Maintain the package

After editing the skill or framework reference, run `python3 tools/build.py` to regenerate the portable prompt and a self-contained `dist/acid-method.zip`. Run `python3 tools/build.py --check` to check prompt parity without writing files. The ZIP is a local build artifact and is excluded from Git; the source folder is installable directly.

## License and attribution

Copyright © 2026 Design On Acid. Except where otherwise noted, the original materials and authored content in this repository are licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) ([full license](LICENSE)). Commercial reuse and adaptations are permitted under its terms.

Suggested attribution:

> Based on the ACID Method by Design On Acid ([source](https://github.com/designonacid/skills)), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Adapted for LLM-assisted content analysis.

Indicate your own changes when adapting. This license does not grant trademark rights or imply endorsement.
