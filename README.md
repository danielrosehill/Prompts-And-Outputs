# Prompts And Outputs

## A free-range gathering of raw outputs from large language models (LLMs!)

![alt text](images/1.png)

Vault root:

`/library`

## Purpose Statement

This repository tracks (loosely, non-programatically) the LLM outputs that I share on [Daniel Goes Prompting](https://danielgoesprompting.com). 

*'Daniel Goes Prompting'* is an open access repository of LLM prompts and outputs intended to be a resource to anyone wishing to understand real LLM performance (and track it over time).

---

## Homepage Text

Hello there random person on the internet!

My name is Daniel. 

And this website is a repository of outputs that I've derived from large language models (LLMs). 

Predominantly well-known ones like GPT 4o and Claude Sonnet. But less often, from fine-tuned and niche LLMs that I self-host.

## Why (And When) I Started Saving LLM Outputs

When I realised that LLMs are potentially useful for much more than just generating ridiculous images, I began developing my own little *wiki*, or personal knowledge management system (PKM), from which this repository is derived. 

I treat this as a first-instance glob of potentially useful text. 

Some of it proves to be very valuable for ideating and researching. Often, the code generations work on the first go and allow me to spin up technical systems far quicker than anybody could have coded them. 

In other instances, they're just potentially helpful. But storage is affordable and text files consume minimal space. So I've erred heavily on the side of capturing and including what I can.

I remain a firm believer in the value of storing and organising LLM outputs and have been working on various aspects of this over the past six months. Some of those experiments are available on my [Github](https://github.com/danielrosehill).

## Prompt Engineering, Use-Case Exploration

### Simple File-Based Context Injection

I am particularly interested in exploratory prompting strategies and in finding ways to dramatically improve LLM inference by injecting what I call *"context snippets"* (note: this is my own terminology, although I think it's reasonably decent). In a sense, this is a primitive (but effective!) version of RAG, tailored to the more modest needs of individual versus enterprise users. 

The system I've developed involves curating snippets of data about yourself *(or your job, or your car, or your personal finance objectives)* and storing these in a repository that can be simply dragged-and-dropped into LLM web UIs (I recommend storing the snippets as `JSON` or `.md` for easy parsing although I've noticed that you can even store these as images and LLMs have no trouble parsing them). 

## Warning: Almost No Editing Has Been Done!

Given the scale of information that I've generated, gathered, and shared here, it's long been beyond the realm of possibility for me to manually review and edit all of this content. While I do that for *some* of the data that I capture into my markdown notebooks, this repository is derived at source and, hence, simply reflects what came out of the models.

The collection here is best understood as an (experimentary) LLM-derived "digital garden". To the extent that it is instructive and informative, it's probably through the vantage point of understanding the evolving capabilities of LLMs and exploring use-cases for them (rather than the accuracy of the information provided, which can neither be vouched for nor guaranteed). Frequenty, this is the real motive behind my prompting.

I love chatting about AI and LLMs and if this project has piqued your interest (or you're also interested in the open question of how humans and AI can best work togeher in generating useful information), do be in touch!


## Repository Growth Over Time

### Core Parameters: Agents, Prompts, Outputs, Conversations

For an explanation of the general method that I use to organise (what I see) as the main constituent elements of human interaction with large language models (LLMs), see:

{{< cards >}}
  {{< card link="/notes/hierarchy" title="Data representation approach" tag="Nov 24" >}}

{{< /cards >}}

---

## Notes About The Formatting Used

I capture LLM outputs into a markdown editor. 

I usually use `## Prompts` and `##Outputs` to denote my prompts and outputs. I try to stick to this approximate pattern so that I can run a Python script which extracts the prompts.

However, I'm not particularly consistent in the headings that I use (ie, sometimes I'll use `H2` and sometimes `H3`). Nevertheless, the basic notation is usually good enough for extracting prompts programatically using Python scripting. When I share outputs as archives, I hope this will be reasonably easy. 

Other very minor formatting FYIs with that use-case in mind:

When engaging in a long conversation with an LLM, if there are parts that are particularly useful, I will usually try to capture them as discrete "notes" (hence, multiple notes can belong to one unifying conversation, and be underpinned by one evolving context).

But when these are captured in a single note, I will usually use something like `Prompt 1`, `Prompt 2` to make clear which interjections are me and which are from the LLM. Sometimes, I'll add more descriptive titles like `Challenge` or `Questioning output assumptions.`

But for the most part, a basic template will look something like this and should be reasonably easy to script around:

```
## Prompt

{The text of the prompt I used, when supplied}

---

## Output

{A copy of the markdown supplied back by the LLM. Ie, the inference/output}

```

---

## Additional Reasons I'm Capturing LLM Outputs

There are a few secondary reasons why I've been storing outputs when many would regard the inferences of LLMs as "throwaway" data. 

### I'm working on an LLM KM System

The first is that I'm working on an *(built-in-public, will-be-open-source, passion project)* system for organising this material in a unique type of knowledge management system, one which leans on graph principles and which captures the constituent elements of LLM interactions at source. Gathering my own outputs means that I have a good bank of material for spinning up prototypes.

The second: I think that recording your prompts is important. They are imprints of what motivated you to search for knowledge when engaging with an LLM and they're usually much more descriptive than the keyword searches we've been using since the 90s.

## Secondary Analysis And Topic Cluster Modelling

Finally, I'm interested in exploring secondary analysis: what information can be gleaned if you run AI over AI!? With a cluster analysis program and simple file metadata, you can mine your own knowledge base to see how your interests - and thinking processes - have evolved over time. I find the idea of visualising and exploring this data quite interesting!

When I have this group of data organised into a less amorphous form (ie, with proper and consistent tags), I will share some archives, with the unprobable but hopeful idea that it might prove useful.

## A Footprint Of LLMs' Evolving Capabilities

Finally ...

LLMs are evolving at a rapid pace. 

The outputs that I logged when I began this process were generated using a different model of the same LLM as the ones I might derive today. 

My hope - and aspiration - is that this collection might prove to be a useful prism of sorts through which the evolution of LLM capabilities can be tracked over time. 

---

## Technical Notes, Credits

My LLM outputs "vault" started life as a Postgres database before moving onto its next iteration on Obsidian and now ... I'm attempting an ambitious rearchitecture backed by graph storage. 

---

## General License

If you find anything valuable here, feel free to share it with attribution.

For a broader look at my projects, some LLM-related, visit my GitHub: [github.com/danielrosehill](https://github.com/danielrosehill).

---

## Author

Daniel Rosehill  
(public at danielrosehill dot com)

## Licensing

This repository is licensed under CC-BY-4.0 (Attribution 4.0 International) 
[License](https://creativecommons.org/licenses/by/4.0/)

### Summary of the License
The Creative Commons Attribution 4.0 International (CC BY 4.0) license allows others to:
- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### License Terms
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full legal code, please visit the [Creative Commons website](https://creativecommons.org/licenses/by/4.0/legalcode).