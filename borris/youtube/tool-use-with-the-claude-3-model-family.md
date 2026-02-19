---
title: "Tool use with the Claude 3 model family"
source_url: "https://www.youtube.com/watch?v=6wkFb2_cUik"
source_type: youtube
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Tool use with the Claude 3 model family

One of the newest exciting features of the Claude 3 model family is tool use, also known as function calling. Tools that Claude can use are represented by a JSON schema that tells the model about the capabilities of the tool and the arguments it accepts.

During generation, the model can make a call to any of its tools, which the client can then dispatch and return the results. For example, this Haiku model, which is our fastest and most affordable model, has access to a fetch webpage tool and a sandboxed Python REPL tool, so it can retrieve information from the internet and run code.

We're going to use it to retrieve an implementation of quicksort, one of the most popular sorting algorithms, and check how fast it runs on a sample input. Now because Haiku is pretty fast, I've actually slowed down this demo by 5x so that we can see the tokens being generated. You can see that Haiku is able to link together several different tools to accomplish a task.

Now things get even more interesting when models can call other models as tools. For example, let's say I want to find the fastest implementation of quicksort online. Here I'm asking Opus, our most advanced model, to find 100 permissively licensed quicksort implementations on GitHub. Then 100 Haiku models write tests to determine how fast each implementation is, and then we'll be able to determine which is the quickest quicksort.

While we let this run, here's how it works under the hood. We've given Opus a "dispatch sub-agents" tool to parallelize this work, where it can write a prompt template and provide a list of arguments. The Haiku sub-agents each get the template filled in with their respective argument. Then all of the answers get returned to Opus, which returns the fastest implementation.

And here we see that the fastest result is available here and it has some additional optimizations that some of the other implementations don't have.

Tool use with sub-agents is a great way to combine the intelligence of Opus and the speed and affordability of Haiku to take action on large amounts of information at scale. Hope you try it out soon.
