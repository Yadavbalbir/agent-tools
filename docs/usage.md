# Using Skills Across Tools

This guide explains how to leverage skills from this repository in Claude and other agent tools.

## What Is a Skill?

A skill is an instruction package that defines:
- Purpose and trigger conditions
- Steps and tool usage patterns
- Constraints and safety boundaries
- Inputs, outputs, and expected artifacts

In this repository, each skill is anchored by `SKILL.md` plus supporting assets.

## Recommended Skill Anatomy

```text
skills/
  skill-name/
    SKILL.md
    assets/
    examples/   # optional
    tests/      # optional
```

## Using Skills in Claude-compatible Workflows

1. Open the skill folder and review `SKILL.md`.
2. Provide the model with the task plus any source files.
3. Ensure referenced assets exist and paths are correct.
4. Ask the model to follow `SKILL.md` exactly.
5. Validate output artifacts (for example PDF, JSON, code files).

Tips:
- Keep instructions explicit and order-sensitive.
- Include exact command lines and output paths.
- Define clear non-goals to reduce drift.

## Using Skills in Copilot/Editor Agents

1. Keep skill folders under `skills/` in the workspace.
2. Reference the target `SKILL.md` in your agent instructions.
3. Include examples to improve consistency.
4. Use issue/PR templates to track quality and regressions.

## Using Skills in Other LLM Tools

Most tools can consume the same structure if you:
- Paste or import `SKILL.md` as the system/task instruction layer
- Attach assets/templates used by the skill
- Preserve the execution order and constraints

If a tool has no filesystem access, provide path-aware snippets directly in prompt text.

## Portability Checklist

- Avoid tool-specific assumptions unless documented
- Use stable file paths and naming
- Keep command examples cross-platform when possible
- Document dependencies clearly

## Example: resume-formatter

- Skill definition: `skills/resume-formatter-skill/SKILL.md`
- Template resource: `skills/resume-formatter-skill/assets/template.tex`
- Packaged artifact: `skills/resume-formatter-skill/resume-formatter.zip`

Use case:
- Input: resume files (PDF, DOCX, or text) and optional edit instructions
- Output: formatted resume source and compiled PDF per skill contract
