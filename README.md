# agent-tools

A community hub for reusable agent skills and prompt-packaged workflows.

This repository is designed to make it easy to:
- Share production-ready agent skills
- Reuse skills across Claude and other AI coding tools
- Contribute improvements with a predictable structure

## Repository Structure

- `skills/`: Home for all skill folders
- `skills/resume-formatter-skill/`: Converts resumes into a polished LaTeX-based format
- `skills/msft-itr-filing-skill/`: Guides Microsoft India employees through document-driven ITR filing with RSU/ESPP and foreign asset workflows
- `docs/`: Usage and integration guides
- `.github/`: Issue templates and pull request standards

## Quick Start

### 1) Clone

```bash
git clone https://github.com/<your-org>/agent-tools.git
cd agent-tools
```

### 2) Explore Available Skills

Each skill folder should include:
- `SKILL.md`: Skill behavior, instructions, boundaries
- `assets/`: Templates and static resources
- Optional packaged archive (`*.zip`) for distribution

### 3) Use a Skill

For the current skill, read:
- `skills/resume-formatter-skill/SKILL.md`
- `docs/usage.md`

## Using Skills in Claude and Other Tools

See `docs/usage.md` for full instructions. Summary:
- Claude-compatible tools: Load `SKILL.md` instructions and required assets into the conversation or tool context.
- Copilot or editor agents: Keep `SKILL.md` in repo, reference it in workspace instructions, and include examples/tests.
- Other LLM tools: Treat the skill as a prompt contract with explicit input/output behavior and constraints.

## Contribution Workflow

1. Fork and create a branch.
2. Add or improve a skill with docs and examples.
3. Validate that instructions are clear and deterministic.
4. Open a pull request using the PR template.

Please read `CONTRIBUTING.md` before submitting.

## Quality Bar for Skills

A skill should be:
- Specific: clear scope, triggers, and non-goals
- Safe: avoids destructive or ambiguous behavior
- Reproducible: includes exact paths, commands, and expected outputs
- Portable: can be adopted by multiple agent tools with minimal edits

## License

This project is licensed under the MIT License. See `LICENSE`.

## Community and Security

- Code of conduct: `CODE_OF_CONDUCT.md`
- Security reporting: `SECURITY.md`
