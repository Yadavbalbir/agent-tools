# Contributing to agent-tools

Thanks for contributing.

## Ways to Contribute

- Add a new skill folder
- Improve an existing skill
- Add examples, tests, and portability notes
- Improve docs and onboarding

## Skill Folder Standard

Use this structure:

```text
skills/
  <skill-name>/
    SKILL.md
    assets/
    examples/            # optional
    tests/               # optional
    <skill-name>.zip     # optional release artifact
```

## Authoring Guidelines

- Keep instructions explicit and deterministic.
- Define when to use and when not to use the skill.
- Include tool assumptions, dependencies, and file paths.
- Document failure modes and recovery steps.
- Prefer ASCII unless a format requires otherwise.

## Pull Request Checklist

Before opening a PR:
- [ ] Skill name is clear and consistent in folder and `SKILL.md`
- [ ] `SKILL.md` includes purpose, triggers, steps, and boundaries
- [ ] Assets are organized under `assets/`
- [ ] Example input/output or sample run is provided (if applicable)
- [ ] README/docs updated if behavior changed
- [ ] No secrets or personal data committed

## Commit Style

Use clear commit messages, for example:

- `feat(skill): add invoice-parser skill`
- `fix(resume-formatter): correct template path`
- `docs: improve usage guide for Claude`

## Review Expectations

PRs are reviewed for:
- Correctness
- Clarity and maintainability
- Portability across agent tools
- Safety and non-destructive defaults

## Reporting Issues

Use GitHub Issues with the provided templates and include:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Minimal sample inputs
