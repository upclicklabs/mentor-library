---
title: "Obsidian + Claude Code as a Thinking Partner - Greg Eisenberg x Internet Vin"
source_url: "https://www.youtube.com/watch?v=obsidian-claude-code-greg-eisenberg"
source_type: youtube
mentor: "Borris"
date_synced: "2026-04-08T00:00:00Z"
word_count: 8500
---

# Obsidian + Claude Code as a Thinking Partner - Greg Eisenberg x Internet Vin

## Overview

Greg Eisenberg interviews Internet Vin about using Obsidian paired with Claude Code as a thinking partner. Vin demonstrates how to use custom slash commands, the Obsidian CLI, and interconnected markdown files to give Claude Code deep personal context - enabling it to surface patterns, generate ideas, and act as an extension of your thinking.

## What is Claude Code

Claude Code is an agent you can use in a command line interface. It's a tool that can control your computer through natural language. You can say "make a file on my desktop that says hello Greg in plain text" and it will do it. Whatever you can describe to it, it can start to do. The more information it has, the more complex things it can do.

The problem is that if you have a long conversation with an agent about a project, you don't want to have to explain that all over again in a new session. A lot of people using Claude or ChatGPT on the web have things like memory, but you can't control what's in that memory. You don't know what it knows and what it doesn't know. There needs to be some way of passing information into these agents that is easier and faster.

## What is Obsidian

Obsidian is an interface that sits on top of a collection of markdown files. What makes a vault (which is what Obsidian interacts with) different from a regular folder is that Obsidian allows you to connect relationships between files using backlinks.

When you write "today I am on a podcast with Greg Eisenberg" and link to the Greg Eisenberg file, that file is now connected. This ability to form inter-relationships is unique to just having a folder - a folder on your computer cannot show these inter-relationships.

Over time, you build a visualization where each circle is a file showing how it's connected to other files. You can see personal agent infrastructure linked to Agentic AI, Telegram, Shopify founder Toby, and other concepts. It works more like the way your brain works - connecting patterns all the time.

## The Obsidian CLI Game Changer

Obsidian released a tool called Obsidian CLI. What it allows you to do is use Claude Code to read all files in your Obsidian Vault. But with the Obsidian CLI, it can give Claude Code not only those files but also information about the inter-relationships of those files.

Claude Code can see that one file is connected to another file and another file. This gets very interesting in terms of what Claude Code can understand about you and the relationships between things you're working on. It can start to surface patterns about what you're thinking about that you are not seeing for yourself.

Some idea you might have been writing about for a year in the vault - it could be a latent idea and Claude Code can immediately say "hey, did you know that you've been writing about this same pattern in startups or in this particular project across these different domains." Seeing that for the first time can be a huge light bulb effect causing huge progressions in learning and understanding.

## Custom Slash Commands

Vin created custom terminal commands that drive the most out of Claude Code with Obsidian context. These can be created easily by asking Claude Code to create a specific command.

### Context Loading
- **/context** - Loads full context about life, work, and current state. Reads context files, daily notes, and follows backlinks to build a complete picture. One command preloads all key information so you don't have to worry about Claude not knowing what it needs.

### Daily Operations
- **/today** - Morning review. Pulls calendar, tasks, iMessages, and the past week of daily notes into a prioritized plan for the day. Unlike just giving an agent access to your calendar, this includes information about what you're thinking about and why. If you're writing daily notes about a particular technology or project, the agent can more effectively make decisions about what should be in your calendar.
- **/close** - End of day processing. Extracts action items, surfaces vault connections, checks confidence markers on hypotheses.

### Thinking Tools
- **/ghost** - Answers a question the way you would. Builds a voice profile from the vault, writes in that voice, then evaluates the fidelity.
- **/challenge** - Pressure tests current beliefs using the vault's own history. Finds contradictions, counter-evidence, and shifts in thinking. Useful for making sure your POV isn't overly biased or limited.
- **/emerge** - Surfaces ideas the vault implies but never states. Finds conclusions from scattered premises, unnamed patterns, unarticulated directions. Having someone name the idea you keep circling around can create huge breakthroughs.
- **/drift** - Compares stated intentions against actual behavior over 30 to 60 days. Surfaces what you are avoiding.
- **/ideas** - Deep 30-day vault scan with cross-domain pattern detection and graph analysis to generate ideas across all domains. Not just ideas for tools - also ideas for films to watch, products to buy, all influenced by things you're writing about.
- **/trace** - Tracks how an idea has evolved over time across the vault.
- **/connect** - Takes two domains and connects them using the vault's link graph.

## Trace Demo - How Ideas Evolve

Vin demonstrated /trace on how his relationship with Obsidian evolved. The agent went through the vault reading files and seeing connections via the Obsidian CLI.

The output showed a full evolution trace:
- **Pre-vault (December 2024)**: A complete system where Obsidian played no role - audio dumps via Mac Whisper, LLM dialogue loops, Canopia for spatial mapping, physical notebooks.
- **Discovery and skepticism (January-May 2025)**: First daily notes with excitement mixed with uncertainty. Original backlinking to general terms like "podcast" or "physical fitness" was not useful.
- **Pivotal realization**: The most important thing is to create notes for each pattern, theory, project, or perspective and get them documented and out of your head, then link to those notes.
- **Phase four (January 2026)**: Explosive building. The friction moved from Obsidian itself to the boundary between the vault and agent execution.

This historical trace across 13 months of notes would be impossible for a human to compile manually.

## Ideas Generation Demo

The /ideas command ran a comprehensive generation by gathering vault structure and context in parallel:
- Read Obsidian orphans (files not connected to things), dead ends, resolved links, tag counts
- Read daily notes, project context files, personal workflow context, personal agent infrastructure files
- Took about 5-10 minutes due to reading massive amounts of information

The output included:
- **Structural highlights**: Orphans worth noting (defense technology, agentic software)
- **What's working**: Obsidian + Claude Code as a combined system producing genuine breakthroughs
- **Tools to build**: A /graduate command (daily note idea extractor), an Obsidian vault for team use
- **Systems to implement**: "One sentence in Obsidian, agent handles the rest" - inline delegation from notes
- **Subjects to investigate**: Christopher Alexander's pattern language, Black Mountain College as a model
- **Things to write and publish**: Context architecture essay, the computer as a place, software will become fashion
- **Conversations to have**: Specific people to meet based on vault patterns
- **Top five high-impact actions**: Prioritized next steps

The agent even suggested building the /graduate command, and Vin could just say "build it" and it was created automatically.

## Connect Demo

The /connect command linked filmmaking and world building by reading files across the vault:
- Bridge one: The interview portal and the constructed world in filmmaking
- Bridge two: Always-on documentary equals continuous world building
- Connected scattered notes about creative strategy, documentary, and worldbuilding into coherent bridges

## Higher Levels of Abstraction

Instead of manually thinking of commands, Vin asks the agent: "Based on my Obsidian vault and what you know about me, form an understanding of where my skill level is, and based on that suggest commands that would take me from the level I'm at to a higher level."

The agent then suggests commands based on vault analysis. For example, it suggested the /graduate command because it noticed ideas accumulate in daily notes but rarely graduate into standalone notes where they can compound through backlinks.

## Meeting Notes and Team Use

You can put meeting transcripts (from Granola or similar tools) directly into the vault. Create a meetings folder, drop transcripts in, and tag them back to relevant projects or people. The agent will discover these connections and have more context for future queries.

## Strict Separation Principle

Vin maintains a strict rule: the agent should never write files into the Obsidian vault. He wants to control all files because he always wants the agent to pull from what he thinks about things, not what the agent thinks. If the agent starts making its own files, you can't tell whether patterns found are from your writing or the agent's writing.

The agent writes outputs on the side (in the terminal or separate output files), and Vin decides what should be included in the vault.

## The Scheduling Command

The /schedule command demonstrates context-aware decision making. When asked "Can I take a meeting with Greg Eisenberg today at 2pm?", the agent:
- Checks the calendar
- Reads daily notes about what you care about
- Provides perspective: "Your day is stacked. You're already recording on Greg's podcast this morning. Your Feb 17 note shows the Greg episode has been top of mind. The vault has a dedicated Greg Eisenberg note."
- Recommendation: "No, not at 2pm, but you might not need a separate meeting at all."

This is the correct answer - showing how vault context enables better decisions than calendar access alone.

## Implications for Autonomous Agents

With OpenClaw (autonomous agents), the same vault context enables agents to make decisions on your behalf with deeper understanding. Instead of managing an agent or explaining things to another human, you focus on managing the vault. The vault becomes the new source - continually updated so agents can pull from it and make decisions.

If the agent isn't making the right decisions, you change something in the vault rather than working with the agent specifically.

## Key Takeaways

1. **Markdown files are the oxygen of LLMs** - not tokens. The files are the memories that give agents their power.
2. **Writing is how you generate ideas** - and now it's also how you delegate to agents. A writing habit dramatically increases what you can delegate and build.
3. **The quality of information the agent has entirely determines what it can do for you** - if it doesn't know a lot about you, it can't do a lot for you.
4. **Files are perfect memory** - unlike human memory which distorts over time, markdown files are an exact record of what you thought at that moment.
5. **Start now** - 99.99% of people won't spend the time to set this up, which is exactly where the alpha is for those who do.
6. **Privacy considerations are real** - you have to think about how much information you're sharing with agents and whether that's the right decision.
7. **Obsidian + Claude Code connects the dots** - similar to what coaches and therapists do, but at a scale and speed impossible for humans.
