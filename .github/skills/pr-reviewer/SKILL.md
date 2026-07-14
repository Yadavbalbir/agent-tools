---
name: repo-pr-reviewer
scope: repository-specific
triggers:
  - Pull request opened
  - Pull request synchronized
  - Pull request marked ready for review
---

# PR Reviewer Skill

This skill defines the baseline review quality bar for pull requests in this repository.

## Goals

- Catch correctness issues and regressions early
- Ensure documentation and structure stay consistent
- Keep changes clear, safe, and maintainable

## Review Priorities

1. Correctness
- Validate that behavior matches the stated intent
- Check for edge cases and obvious failure paths

2. Scope and Structure
- Confirm changes are scoped to the PR purpose
- Ensure repository layout conventions are followed
- Skills should live under `skills/`

3. Documentation
- Verify README/docs are updated when workflows or paths change
- Confirm user-facing instructions are accurate

4. Safety and Security
- No secrets, private data, or credentials in committed files
- No destructive commands in instructions without safeguards

5. Contributor Experience
- PR description clearly explains what and why
- Includes validation notes or manual test evidence

## Required Checks

A PR should generally satisfy the following:

- [ ] Change is understandable and focused
- [ ] Paths and file references are valid
- [ ] Related docs updated
- [ ] No obvious security/privacy risk introduced
- [ ] Follows repository conventions and templates

## Reviewer Output Format

When leaving a review summary, prefer this order:

1. Findings by severity (high to low)
2. Open questions/assumptions
3. Optional change summary

If there are no findings, explicitly say so and note any residual risk or testing gaps.
