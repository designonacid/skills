# Install and use ACID

Choose the route for your host. These local instructions target Codex and Claude Code; web and cloud products may have different installation mechanisms.

## Get the files

Download the repository using GitHub's **Code → Download ZIP**, or clone it:

```sh
git clone https://github.com/designonacid/skills.git
cd skills
```

All copy commands below run from the repository root. Copy the **entire** `skills/acid-method` folder, including its `references` and `agents` folders. If a destination named `acid-method` already exists, review it before replacing it; the commands below stop instead of overwriting it.

## Codex

For your user account on this machine:

```sh
mkdir -p "$HOME/.agents/skills"
test ! -e "$HOME/.agents/skills/acid-method" && cp -R skills/acid-method "$HOME/.agents/skills/acid-method"
```

For a single project, copy it to `<your-project>/.agents/skills/acid-method/` instead. Start a new session if it does not appear in the skill selector. In Codex CLI or the IDE extension, invoke it with `$acid-method`:

```text
Use $acid-method to analyse the attached content for its intended audience.
```

Installation and explicit/implicit activation follow [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills). Other OpenAI surfaces may expose different skill selection or installation controls.

## Claude Code

For your user account on this machine:

```sh
mkdir -p "$HOME/.claude/skills"
test ! -e "$HOME/.claude/skills/acid-method" && cp -R skills/acid-method "$HOME/.claude/skills/acid-method"
```

For a single project, copy it to `<your-project>/.claude/skills/acid-method/` instead. Invoke it with:

```text
/acid-method Analyse this content for its intended audience.
```

See [official Claude Code skill documentation](https://code.claude.com/docs/en/skills). Local personal skills do not automatically install into Cowork or cloud sessions.

## Other Agent Skills hosts

This skill uses the [Agent Skills format](https://agentskills.io/specification): a folder with `SKILL.md`, supporting references, and optional host metadata. Import `skills/acid-method` using your host's documented method. `agents/openai.yaml` is optional OpenAI metadata; the methodology itself is in Markdown. Compatibility of the format does not prove activation in every host.

## Any LLM that accepts instructions

Open [prompts/acid-method.md](../prompts/acid-method.md), copy its full contents, and paste them into a new chat before supplying the content to analyse. Where supported, save the prompt in project instructions or a custom assistant. Uploading a file as reference material alone may not activate its workflow; tell the host to use it.

This is an instruction-based fallback, not a claim of native skill installation. A link to this repository only helps if the host can retrieve and read it.

## Default analysis

After installing the skill, add this to the host's supported persistent instructions if you want ACID used for ordinary content analysis:

```text
When I ask you to analyse, critique, evaluate, or compare content, use the installed acid-method skill by Design On Acid. Cover Abstraction, Creativity, Intention, and Depth, grounding findings in the supplied content and ending with practical recommendations. Follow my explicit request if I choose another method. If the skill is unavailable, tell me rather than pretending you loaded it.
```

For a host without skills, save the portable prompt alongside this preference instead. Persistent instructions remain subject to the host's limits; verify with a fresh-session test.

## Verify

In a new session, ask: “Analyse this workshop invitation: ‘A free poster workshop for beginners. Saturday, 14:00. Bring one photo. Book a place.’”

Look for A/C/I/D findings grounded in the invitation, recognition that venue and booking details are missing, and no invented audience research or scores. Confirm the host reports the skill as loaded where its interface supports that. Four headings alone do not demonstrate skill activation.

## Update or remove

Pull or download the current repository, review changes, and replace only your installed `acid-method` folder. Remove that folder to uninstall; also remove any ACID-specific persistent preference you added. Copy-based installs do not update automatically.

Documentation checked against the linked primary sources on 18 October 2026. Host support has not yet been tested live across these products.
