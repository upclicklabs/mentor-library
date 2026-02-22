# Claude Code Beginner's Playbook from a 7-Year SWE

**Source:** Blog Post
**Author:** SWE veteran (Amazon, Disney, Capital One) / Startup CTO
**Topic:** Claude Code best practices and workflow optimization

---

## Background

7 years as a SWE across Amazon, Disney, and Capital One. Code shipped touches millions of users, built systems that couldn't afford to break. Now CTO of a startup building agents for enterprise. Claude Code is a daily driver.

---

## Think First

Most people assume that with Claude Code, the first thing you need to do is type. But that's one of the biggest mistakes. The first thing you actually need to do is **think**.

10 out of 10 times, the output with plan mode did significantly better than just starting talking and spewing everything into Claude Code. It's not even close.

For those without years of SWE experience to think through architecture on their own:

1. **Start learning.** You are handicapping yourself if you never pick up on this, even if just a little bit at a time.
2. **Have a deep back and forth with an LLM** where you describe exactly what you want to build, ask for the various options in terms of system design, and ultimately settle on a solution. You and the LLM should be asking each other questions, not just a one way street.

This applies to everything, including very small tasks like summarizing emails. Before asking Claude to build a feature, think about the architecture. Before asking it to refactor, think about the end state. Before asking it to debug, think about what you actually know about the problem. The more information you have in plan mode, the better your output because the better the input.

The pattern is consistent: **thinking first, then typing, produces dramatically better results** than typing first and hoping Claude figures it out.

### Architecture Matters

Architecture is like giving a person the output and nothing more. This leaves a lot of wiggle room in how to get there, which is essentially what the problem with AI generated code is.

- **Bad:** "Build me an auth system"
- **Good:** "Build email/password authentication using the existing User model, store sessions in Redis with 24-hour expiry, and add middleware that protects all routes under /api/protected."

You click **shift + tab twice**, and you're in plan mode. This will take 5 minutes of your time but will save you hours of debugging later.

---

## CLAUDE.md

CLAUDE.md is a markdown file. When you start a Claude Code session, the first thing Claude does is read your CLAUDE.md file. Every instruction shapes how Claude approaches your project. It's essentially onboarding material that Claude reads before every single conversation.

Most people either ignore it completely or stuff it with garbage that makes Claude worse. There is a threshold where too much or too little information means worse model output.

### What Actually Matters

- **Keep it short.** Claude can only reliably follow around 150 to 200 instructions at a time, and Claude Code's system prompt already uses about 50. Every instruction you add competes for attention. If your CLAUDE.md is a novel, Claude will start ignoring things randomly.
- **Make it specific to your project.** Don't explain what a components folder is. Tell it the weird stuff, like the bash commands that actually matter. Everything that is part of your flow should go into it.
- **Tell it why, not just what.** "Use TypeScript strict mode" is okay. "Use TypeScript strict mode because we've had production bugs from implicit any types" is better. The why gives Claude context for making judgment calls you didn't anticipate.
- **Update it constantly.** Press the **#** key while working and Claude will add instructions to your CLAUDE.md automatically. Every time you find yourself correcting Claude on the same thing twice, that's a signal it should be in the file.

> Bad CLAUDE.md looks like documentation written for a new hire. Good CLAUDE.md looks like notes you'd leave yourself if you knew you'd have amnesia tomorrow.

---

## The Limitations of Context Windows

Opus 4.5 has a 200,000 token context window. But the model starts to deteriorate way before you hit 100%.

At around **20-40% context usage** is where the quality of the output starts to chip away. If you've ever experienced Claude Code compacting and then still giving terrible output afterwards, that's why. The model was already degraded before compaction happened, and compaction doesn't magically restore quality.

Every message you send, every file Claude reads, every piece of code it generates, every tool result - all of it accumulates. Once quality starts dropping, more context makes it worse, not better.

### What Actually Helps

- **Scope your conversations.** One conversation per feature or task. Don't use the same conversation to build your auth system and then also refactor your database layer. The contexts will bleed together.
- **Use external memory.** Have Claude write plans and progress to actual files (SCRATCHPAD.md or plan.md). These persist across sessions. When you come back tomorrow, Claude can read the file and pick up where it left off.
- **The copy-paste reset.** When context gets bloated, copy everything important from the terminal, run `/compact` to get a summary, then `/clear` the context entirely, and paste back in only what matters. Fresh context with critical information preserved.
- **Know when to clear.** If a conversation has gone off the rails or accumulated irrelevant context, just `/clear` and start fresh. Claude will still have your CLAUDE.md. Nine times out of ten, using clear is better than not using it.

> The mental model that works: **Claude is stateless.** Every conversation starts from nothing except what you explicitly give it. Plan accordingly.

---

## Prompts Are Everything

People spend weeks learning frameworks and tools. They spend zero time learning how to communicate with the thing that's actually generating their code.

### What Actually Helps

- **Be specific about what you want.** "Build an auth system" gives Claude creative freedom it will use poorly. "Build email/password authentication using this existing User model, store sessions in Redis, and add middleware that protects routes under /api/protected" gives Claude a clear target.
- **Tell it what NOT to do.** Claude has tendencies. Claude 4.5 in particular likes to overengineer. If you want something minimal, say "Keep this simple. Don't add abstractions I didn't ask for. One file if possible." Always cross-reference what Claude produces to avoid technical debt.
- **Give it context about why.** "We need this to be fast because it runs on every request" changes how Claude approaches the problem. "This is a prototype we'll throw away" changes what tradeoffs make sense. Claude can't read your mind about constraints you haven't mentioned.

> Remember: output is everything, but it only comes from input. If your output sucks, your input sucked.

---

## Bad Input == Bad Output

If you're getting bad output with a good model like Opus 4.5, your input and prompting sucks. Full stop.

The model matters a lot, but model quality is table stakes at this point. The bottleneck is almost always on the human side.

### Fix These Things

- **How you write prompts.** Specific > vague. Constraints > open-ended. Examples > descriptions.
- **How you structure requests.** Break complex tasks into steps. Get agreement on architecture before implementation. Review outputs and iterate.
- **How you provide context.** What does Claude need to know to do this well? What assumptions are you making that Claude can't see?

### Model Differences

- **Sonnet** is faster and cheaper. Excellent for execution tasks where the path is clear - writing boilerplate, refactoring based on a specific plan, implementing features where you've already made the architectural decisions.
- **Opus** is slower and more expensive. Better for complex reasoning, planning, and tasks where you need Claude to think deeply about tradeoffs.

> A workflow that works: use **Opus to plan** and make architectural decisions, then switch to **Sonnet** (Shift+Tab in Claude Code) for implementation.

---

## MCP, Tools, and Configurations

Claude has a ridiculous amount of features. MCP servers. Hooks. Custom slash commands. Settings.json configurations. Skills. Plugins.

You don't need all of them. But you should experiment because you're probably leaving time or money on the table.

- **MCP (Model Context Protocol)** lets Claude connect to external services (Slack, GitHub, databases, APIs). If you find yourself constantly copying information from one place into Claude, there's probably an MCP server that can do it automatically. You can also create your own MCP server for whatever tool you need.
- **Hooks** let you run code automatically before or after Claude makes changes. Want Prettier to run on every file Claude touches? Hook. Want type checking after every edit? Hook. This catches problems immediately. Also helps remove technical debt.
- **Custom slash commands** are just prompts you use repeatedly, packaged as commands. Create a `.claude/commands` folder, add markdown files with your prompts, and run them with `/commandname`.

> Don't get shut off if something doesn't work on the first try. These models improve basically every week. Something that didn't work a month ago might work now.

---

## When Claude Gets Stuck

Sometimes Claude just loops. It tries the same thing, fails, tries again, and keeps going. Or it confidently implements something completely wrong.

When this happens, **change the approach entirely** instead of pushing harder.

- **Clear the conversation.** The accumulated context might be confusing it. `/clear` gives you a fresh start.
- **Simplify the task.** Break it into smaller pieces. If Claude is struggling with a complex task, your plan mode is insufficient.
- **Show instead of tell.** Write a minimal example yourself. "Here's what the output should look like. Now apply this pattern to the rest." Claude is extremely good at following examples.
- **Be creative.** Try a different angle. Reframing ("implement this as a state machine" vs "handle these transitions") can unlock progress.

> The meta-skill is recognizing when you're in a loop early. If you've explained the same thing three times and Claude still isn't getting it, more explaining won't help. Change something.

---

## Build Systems

The people who get the most value from Claude aren't using it for one-off tasks. They're building systems where Claude is a component.

Claude Code has a **-p flag for headless mode**. It runs your prompt and outputs the result without entering the interactive interface. This means you can script it. Pipe output to other tools. Chain it with bash commands. Integrate it into automated workflows.

Enterprises are using this for automatic PR reviews, automatic support ticket responses, automatic logging and documentation updates. All of it logged, auditable, and improving over time.

> The flywheel: Claude makes a mistake, you review the logs, you improve the CLAUDE.md or tooling, Claude gets better next time. This compounds.

---

## TLDR

1. **Think before you type.** Planning produces dramatically better results than just starting to talk.
2. **CLAUDE.md is your leverage point.** Keep it short, specific, tell it why, and update constantly.
3. **Context degrades at 30%, not 100%.** Use external memory, scope conversations, and use the copy-paste reset trick.
4. **Architecture matters more than anything.** You cannot skip planning.
5. **Output comes from input.** If you're getting bad results, your prompting needs work.
6. **Experiment with tools and configuration.** MCP, hooks, slash commands. Stay curious.
7. **When stuck, change the approach.** Don't loop. Clear, simplify, show, reframe.
8. **Build systems, not one-shots.** Headless mode, automation, logged improvements over time.
