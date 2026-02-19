---
title: "Text editor tool"
source_url: "https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Text editor tool

Claude can use an Anthropic-defined text editor tool to view and modify text files, helping you debug, fix, and improve your code or other text documents. This allows Claude to directly interact with your files, providing hands-on assistance rather than just suggesting changes.

## Model compatibility

| Model | Tool Version |
|-------|--------------|
| Claude 4.x models | `text_editor_20250728` |
| Claude Sonnet 3.7 (deprecated) | `text_editor_20250124` |

The `text_editor_20250728` tool for Claude 4 models does not include the `undo_edit` command. If you require this functionality, you'll need to use Claude Sonnet 3.7. Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.

## When to use the text editor tool

Some examples of when to use the text editor tool are:
- **Code debugging**: Have Claude identify and fix bugs in your code, from syntax errors to logic issues.
- **Code refactoring**: Let Claude improve your code structure, readability, and performance through targeted edits.
- **Documentation generation**: Ask Claude to add docstrings, comments, or README files to your codebase.
- **Test creation**: Have Claude create unit tests for your code based on its understanding of the implementation.

## Use the text editor tool

Provide the text editor tool (named `str_replace_based_edit_tool` for Claude 4, or `str_replace_editor` for Claude Sonnet 3.7) to Claude using the Messages API. You can optionally specify a `max_characters` parameter to control truncation when viewing large files.

The text editor tool workflow:
1. Provide Claude with the text editor tool and a user prompt
2. Claude uses the `view` command to examine file contents or list directory contents
3. Execute the view command and return results
4. Claude uses a command such as `str_replace` to make changes or `insert` to add text
5. Execute the edit and return results
6. Claude provides its analysis and explanation

### Text editor tool commands

#### view

Examine the contents of a file or list the contents of a directory. Parameters: `command`, `path`, `view_range` (optional).

#### str_replace

Replace a specific string in a file with a new string. Parameters: `command`, `path`, `old_str`, `new_str`.

#### create

Create a new file with specified content. Parameters: `command`, `path`, `file_text`.

#### insert

Insert text at a specific location in a file. Parameters: `command`, `path`, `insert_line`, `insert_text`.

#### undo_edit

Revert the last edit made to a file (only available in Claude Sonnet 3.7). Parameters: `command`, `path`.

## Implement the text editor tool

The text editor tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema; the schema is built into Claude's model and can't be modified.

The tool type depends on the model version:
- Claude 4: `type: "text_editor_20250728"`
- Claude Sonnet 3.7: `type: "text_editor_20250124"`

### Handle errors

When using the text editor tool, various errors may occur:
- File not found
- Multiple matches for replacement
- No matches for replacement
- Permission errors

Return appropriate error messages in the `tool_result` with `is_error: true`.

### Follow implementation best practices

- Provide clear context when asking Claude to fix or modify code
- Be explicit about file paths
- Create backups before editing
- Handle unique text replacement carefully
- Verify changes after Claude makes them

## Pricing and token usage

The text editor tool uses the same pricing structure as other tools. Additional input tokens needed:
- `text_editor_20250429` (Claude 4.x): 700 tokens
- `text_editor_20250124` (Claude Sonnet 3.7): 700 tokens

## Change log

| Date | Version | Changes |
| ---- | ------- | ------- |
| July 28, 2025 | `text_editor_20250728` | Updated text editor with fixes and optional `max_characters` parameter |
| April 29, 2025 | `text_editor_20250429` | Text editor for Claude 4, removes `undo_edit` command |
| March 13, 2025 | `text_editor_20250124` | Standalone documentation, optimized for Claude Sonnet 3.7 |
| October 22, 2024 | `text_editor_20241022` | Initial release with Claude Sonnet 3.5 |
