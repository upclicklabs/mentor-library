---
title: "Claude Skills Marketing Stack: Building a Campaign Workflow System with 8 Skills"
source_url: ""
source_type: youtube
mentor: "Chris"
date_synced: "2026-04-30"
---

# Claude Skills Marketing Stack: Building a Campaign Workflow System with 8 Skills

Claude Skills is one thing I wish every marketer knew about, because once you build them, Claude stops being a tool you have to manage and starts being a system. So in this video, I'll show you how to set up your marketing skills stack to automate most of your marketing - from the design process, the actual building, to creating your own Claude Skills library.

## The Three Types of Marketing Skills

The simplest way to think about your marketing skills is to group them into three types:

1. **Brand skills** - define your brand standard
2. **Function skills** - cover marketing tasks you do day to day
3. **Specialty skills** - handle the rules of your specific domain

Three steps to start:
1. Look at your marketing week and reflect on the tasks you do repeatedly.
2. Sort them into these three skill types.
3. Prioritize. Almost every marketing task needs brand skills as a foundation, so build those first, then build your function or specialty skills next.

In this video, we're building a campaign workflow system with eight Claude skills as the sample to walk you through all three steps. We'll be using Claude Code through the Claude Desktop application.

## Setting Up the Project

First, create the project folder. In this case, the brand is called Carely - a healthcare SaaS brand. Inside, set up:
- A `context` folder (and other system folders)
- A `campaign` folder that stores all the campaign outputs

Load all the important brand context files inside the context folder - brand context, ICP, marketing strategy. Also prepare a `CLAUDE.md` file that tells Claude how to navigate this project folder.

Open Claude Desktop, switch to Claude Code, and select the Carely project folder. The new Claude Code desktop lets you filter by different projects so you can switch immediately.

## Skill 1: Brand Voice Skill

The first skill to build is the brand voice skill. This is a skill every marketer needs.

Ask Claude to create a brand voice skill according to the brand voice guide, and create different examples to be used as the skill's assets. Include versioning - this will be useful when building your Claude Skills library later.

Claude reads all the brand context and builds the examples, and runs evaluations to make sure the skill is high quality. Open the project in an IDE like VS Code and you'll see a new skill has been created under the skills folder.

## Skill 2: Brand Design System Skill

We need to teach Claude how the brand looks visually. The Claude Design tool helps you set up your brand design system much more quickly and make it portable by building a reusable skill.

**Prep:** Have your marketing materials ready in an `assets` folder - in this example, a branded landing page containing the brand color palettes and logos.

Steps in Claude Design:
1. Click "Design System," name it (Carely).
2. You can connect a GitHub repository to extract your design system, or skip it.
3. Attach the project folder containing all materials.
4. Attach any logos or additional marketing assets.
5. Paste in the brand voice notes for safety.
6. Click Generate.

This process takes 10-15 minutes. Review all your materials before clicking generate. You'll get back extracted brand colors, UI mockups, components, font types, logos. Review them one by one and import any missing materials.

If a marketing site mockup has issues (like a tagline overlapping with background color), prompt Claude and it will make the changes. You can also navigate to the Design Files view and make granular changes using the editor by selecting any element. **Warning:** changes are hard to revert, so don't overdo it.

This whole design system is actually an exportable Claude Skill. **The biggest value from Claude Design is exporting this design system skill to be used in your Claude Code project.** Open the project folder and drag the whole design system folder in. Paste back the versioning and maintenance control - immediately, you've installed this brand design skill into the project.

## Skill 3: Campaign Planning Brief Skill

Once you have the design system skill, you can build all the skills on top that will be useful for your marketing tasks - the function skills, particularly for the campaign workflow.

Use this prompt: "Create a campaign planning brief skill that uses the Perplexity research tool for research and calls the design system skill to build an on-brand slide deck and campaign brief from an empty file with our defined sections."

Very quickly the second skill is created, showing the step-by-step process and calling the design system skill for slide deck building.

Ask it to create a campaign planning for an upcoming campaign with a timeline and budget. It starts with Perplexity search, synthesizes data, and builds the presentation. The deck follows the design system skill with brand color and font.

The story it presents is impressive - KPI targets, target persona, funnel mapping (showing where marketing budget is spent), campaign roadmap, and the last slide on accountable team with next actions.

**Bonus:** If you want a slick HTML-style slide deck, use Claude Design - create a new slide deck project, pick your design system, paste the campaign brief outline, and it will create a deck with speaker notes.

## Skill 4: Carousel Design Skill

Build reusable marketing asset templates that you can use to create other marketing skills. This is one of the best ways to use Claude Design.

**Step 1: Build a carousel template in Claude Design.**
- Pick "Prototype," name it "Social Carousel Template"
- Pick the design system, "high fidelity" (polished mockup ready to use)
- Claude asks clarifying questions: color, direction, type treatment, tweak variations
- It generates carousel design with three variations - all on-brand and professional

If text is too small, export the whole project and edit on Claude Code. Make back-and-forth changes there because Claude Design burns tokens fast.

Copy the exported carousel template folder inside your project's `templates` folder.

**Step 2: Create the carousel design skill.** It references the carousel template, proposes content angles, uses the Nano Banana tool to generate cover images, and exports each slide into individual images.

Test: ask it to read the campaign brief and generate the carousel. It calls the skill, generates cover images for three variations, all looking good and decent, using the same template generated from Claude Design. **That's why it's important to get the template right in the first place - because then you can always control the final quality.**

For an educational carousel the text length is fine, but for performance marketing you'd want shorter, punchier lines. Slides are saved as individual images, ready to publish.

**The pattern:** Build your marketing asset templates in Claude Design, then use that to build skills to further automate your workflow.

## Skill 5: Animated Video Skill

Carousels are static, but the same skill style can generate motion. Using the Claude Design motion engine, build branded motion skills.

In Claude Design, create a new prototype project called "Animated Video," pick your brand design system, and ask it to design animated videos for the product launch. After some time, you'll get generated motion - not professional grade, but good for simple marketing storytelling or as a landing page explainer.

Export this project and copy the animated video folder under the templates folder.

Back in Claude Code, create a new skill called "Carely Animated Video" that generates 30-second motion videos in HTML format. It should always propose a storyboard before generating, so every motion video is distinct.

Test: create an animated video for the same campaign. It reads the campaign brief, generates the storyboard, and creates the video. Process takes almost 15 minutes. The result tells the story with punchy lines, typical storytelling video format, all using the same brand style and design system. Embed it into your campaign landing page for an engaging brand motion piece.

## Building the Campaign Manager Agent

Using similar approach, seven marketing skills are created. The next level is creating a campaign manager agent to orchestrate all these skills.

Since Claude Code Desktop doesn't support the agent command directly, initiate a session, click to open a terminal view, initiate Claude Code, and use the agent command to create a campaign manager agent.

This agent orchestrates the full campaign workflow and calls different skills. After creating the agent, update the `CLAUDE.md` file to register this agent so Claude knows when to call it and the expected behavior.

**Test run:** Ask it to launch a campaign about a new product feature with very little detail. The campaign manager asks questions about goal, budget, target audience, then starts the research process and initiates the campaign brief.

It builds the campaign planning deck. Since it spins up other agents, it doesn't take up the context of the main agent window. Then it moves on to generate the assets.

**Bonus tip:** Click the task view at any time to check what Claude is working on.

After almost 25 minutes, Claude returns all deliverables:
- **Campaign brief** - more practical than the Claude Design version, easy to edit text. Solid starting point with tactics plan, channel strategy, budget allocation.
- **Campaign performance tracker** - Excel formulas built in for actual vs. forecast planning, channel performance, content performance, pipeline attribution.
- **Social carousel posts** - on-brand and aligned with the campaign (some overflow issues to refine in the skill).
- **Animated videos** - storyboard matches campaign theme with on-brand motion graphics.
- **Campaign landing page** - with call to action, embedded video, all aligned with brand design system.

Now every time you want to design a new campaign, just give the details to the campaign manager and everything follows through.

## Building a Claude Skills Library on Notion

The whole system only exists on one machine. Share with the team by building a Claude Skills library on Notion. **This is where a personal system becomes a team system.**

The Notion library stores: skill name, description, category, version, and the actual skill file. The versioning added to each skill earlier is how Claude tracks changes and keeps the library on the latest version.

Push and populate all the project-level skills to this skill library. The skill library manager skill (built earlier) pushes a test entry and continues with all the skills. Skills get populated automatically with all detail filled in - description, category - and it zips all the skill files so anyone can download from the library.

Your team or clients can browse through the full skill library, filter by what they need, and know what's available. Whenever a skill is updated, ask Claude to sync the skill library and it scans which skill needs to be pushed (e.g., if v2 of the animated video skill is available).

## Automating with Scheduled Routines

Take it further with the Routines feature on Claude Code:

1. Go to Routines on the sidebar.
2. Create a new local routine.
3. Define schedule, task name, description, instructions ("check if there are new skills that haven't been published, push them to the skills library").
4. Pick auto-mode (Claude approves lower-risk actions automatically).
5. Select the project folder.
6. Set it to run weekly at 9:00 AM.

Now you don't need to manually upload skills to this library. This is how you scale your Claude Skills value further.

## The Takeaway

Start with one skill, get it working really well, then build the next one. That's how your real system grows.
