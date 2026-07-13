---
name: resume-to-latex-template
description: Converts any resume (PDF, Word/.docx, plain text, or a mix of these) into the user's personal LaTeX resume template and returns a freshly compiled PDF. Use this skill whenever the user shares a resume — their own or someone else's — and asks to reformat it, "convert it," "put it in my template," "make it match my format," or similar, even if they don't say "LaTeX" explicitly. Also use it whenever they ask to add, remove, or modify specific bullet points, entries, or sections on a resume they want output in this template. Each run is a fresh one-shot conversion — it does not carry state between conversations. Do NOT use this skill for generic resume writing/critique requests that don't involve producing a formatted output document.
---

# Resume to LaTeX Template Converter

Converts a source resume (any format) into the user's personal LaTeX
resume template, and compiles it straight to a PDF.

## Overview

This is a **one-shot conversion** skill: every time the user provides a source
resume (or edit instructions), treat it as a fresh conversion into the
target template. There is no persistent `.tex` file carried across turns —
the previous conversion's content can be reused as context if he asks for
"the same resume but tweak X", but always regenerate the full `.tex` from
scratch and recompile.

## Step 1: Extract content from the source resume

The input can be a PDF, a `.docx`, plain pasted text, or a mix (e.g. a PDF
plus some extra bullet points typed in chat). Extract text appropriately:

- **PDF**: use `pdftotext -layout <file> -` (add `-layout` to preserve
  columns/structure better) or read via the `view` tool if it's already in
  context as an image/document.
- **.docx**: use `python-docx` (already installed) to pull paragraph and
  table text, or the `docx` skill if deeper structure inspection is needed.
- **Plain text / chat-pasted content**: use as-is.
- **Mixed sources**: combine extracted text from each into one working set
  before mapping into the template.

Don't overthink extraction — a reasonably faithful text dump is enough,
since you (Claude) will do the actual structuring in Step 2.

## Step 2: Map content into the target template structure

Read `assets/template.tex` — this is the user's actual LaTeX template with the
real preamble, macros, and styling. Copy it as your starting point and fill
it in; do not redesign the styling, fonts, spacing, or macros.

The template has two custom commands you must use for their respective
sections:

```latex
\entry{Company}{Location}{Title}{Dates}
```
Used for **Experience** entries. Followed by a
`\begin{itemize}[noitemsep,topsep=0pt,parsep=0pt,partopsep=0pt]...\end{itemize}`
block of bullet points. Escape LaTeX special characters (`&`, `%`, `#`,
`_`, etc.) in all extracted text. Bold key metrics/technologies within
bullets using `\textbf{}` sparingly, matching the density/style already
shown in `assets/template.tex` (roughly 1-3 bolded terms per bullet, not
every noun).

```latex
\project{Project Name}{Context/Org}{Dates}
```
Used for **Projects** entries, followed by the same itemize bullet style.

**Education** and **Technical Skills** sections follow the plain patterns
shown in the template comments (no custom macro) — mirror the exact
`\hfill` / `\textbf{}` layout from `assets/template.tex`'s history (see the
worked example in `references/example_filled.tex` if present, or infer
directly from the macro definitions).

Use `\vspace{2mm}` between consecutive entries within a section, matching
the template's existing spacing convention.

### Handling edit instructions

If the user asks to add/remove/modify specific points rather than (or in
addition to) providing a fresh source resume, apply those edits directly
while re-generating the `.tex` — e.g. "remove the CodingJudge multi-tenant
bullet" means drop that one `\item`; "add a new project called X" means
insert a new `\project{}` block in the Projects section.

### Handling sections not in the template

If the source resume has a section the template doesn't define (e.g.
Certifications, Awards, Publications, Volunteering), **add a new
`\section{}`** for it, styled consistently with the existing ones:

- Use the same `\section{}` command (it already inherits the template's
  `\titleformat`/`\titlerule` styling automatically).
- For itemized content, reuse the exact
  `itemize[noitemsep,topsep=0pt,parsep=0pt,partopsep=0pt]` pattern.
- Place new sections in a sensible position (e.g. Certifications/Awards
  typically go after Education, before or after Technical Skills) — use
  judgment based on section importance, don't just always append at the end.

## Step 3: Compile to PDF

Save the filled `.tex` file to `/home/claude/resume/resume.tex`, then compile:

```bash
cd /home/claude/resume && pdflatex -interaction=nonstopmode resume.tex && pdflatex -interaction=nonstopmode resume.tex
```

Run it twice (harmless if unnecessary, but ensures hyperref references
settle). Check the exit status and tail `resume.log` if it fails —
common issues are unescaped `&`, `%`, `#`, `_`, `$` characters pulled
verbatim from the source resume, or curly quotes/em-dashes that need
escaping or replacing with plain ASCII equivalents. Fix and recompile
rather than surfacing raw LaTeX errors to the user.

## Step 4: Deliver

Copy the compiled PDF to `/mnt/user-data/outputs/` (name it something
sensible, e.g. `Resume_Name.pdf` or based on context if
target-role-specific), and use `present_files` to share it. Don't also hand
back the `.tex` source unless they ask for it — the agreed output is the
compiled PDF only.

## Notes

- Always preserve the user's actual contact info/header (name, email, phone,
  institution line) from `assets/template.tex` unless the source resume or
  their instructions explicitly say to change them.
- Keep bullet phrasing tight and consistent with the resume's existing
  voice (concise, metric-driven, bolded key terms) rather than copying
  source resume phrasing verbatim if it's verbose or in a different style.
- If the source resume is much longer than the template can gracefully fit
  on one page at 10pt, prioritize the most relevant/impressive content
  and trim rather than shrinking fonts/margins drastically — flag to
  the user if significant trimming was needed.