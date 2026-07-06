---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files in `assignments/**/README.md` must follow these rules.

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
- The assignment must be created as a `README.md` file.
- Do not remove, rename, or skip required sections from the template.
- Preserve heading levels exactly (H1 -> H2 -> H3 -> H4 as shown in the template).

## 2. Section Guidance

Use the exact section pattern and icon style from the template.

- **Title (`# 📘 Assignment: [Assignment Title]`)**: Replace `[Assignment Title]` with a short, descriptive name.
- **Objective (`## 🎯 Objective`)**: Write 1-2 sentences describing what students will learn or build.
- **Tasks (`## 📝 Tasks`)**: Include one or more task blocks with this structure:
   - `### 🛠️ [Task Title]`
   - `#### Description`
   - `#### Requirements`
   - The line `Completed program should:` before requirement bullets
   - 2-5 clear, measurable bullet requirements

## 3. Writing Quality

- Use student-friendly, encouraging language.
- Keep instructions concrete and action-oriented.
- Use examples (input/output or sample behavior) when they help clarity.
- Keep scope appropriate for the assignment level.

## 4. Strictness Rules

- Do not include extra sections unless explicitly requested.
- Do not leave placeholder text such as `[Requirement 1]` in final assignment files.
- Ensure each task has both `Description` and `Requirements` subsections.