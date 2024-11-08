---
title: "LLM number approximations"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Have there been any approximations as to how many LLMs have been conducted to date? Also: what is the average development cost of an LLM? I always assumed that it was so cost prohibitive that only major tech corporations could afford to develop one. Is that the case? Or is it possible for an "agile" small team to build their own model?

# Output

The development of large language models (LLMs) has been a rapidly evolving field, with numerous models being created over the past few years. While it's challenging to provide an exact count, we can examine some trends and statistics to give you an idea of the scale and costs involved.

## Number of LLMs Developed

As of 2024, there have been dozens of notable LLMs developed, with the number growing steadily:

- A dataset tracking large-scale AI models identified 81 models that exceeded 10^23 FLOP (floating point operations) in training, which is considered a threshold for "large-scale" models[6].
- The pace of large-scale model releases is accelerating. In 2020, only 11 models exceeded this threshold, but by 2024, this number had grown to 81[6].
- A list of prominent LLMs includes at least 19 models from various developers[4].

It's important to note that these numbers primarily represent publicly known and prominent models. Many companies and research institutions may be developing LLMs that are not publicly disclosed.

## Development Costs

The development costs for LLMs can indeed be substantial, often making them prohibitively expensive for smaller organizations:

- Training OpenAI's GPT-3 model reportedly cost at least $5 million in GPU resources alone for a single training run[5].
- The total cost of developing GPT-3, including multiple training runs, is estimated to be significantly higher, potentially in the range of $50 million to $100 million or more[5].
- Sam Altman of OpenAI has suggested that the cost of training foundation models is "more than that" and is increasing[5].
- Some estimates suggest that training the next generation of large language models could pass $1 billion within a few years[5].

These high costs are due to several factors:

1. Computational resources: LLMs require thousands of GPUs and extensive data center infrastructure[5].
2. Energy consumption: Running inference on models like ChatGPT can consume around 1 GWh each day[5].
3. Human resources: Skilled AI engineers and human reviewers are needed, adding to the cost[5].

## Possibilities for Smaller Teams

While developing large-scale LLMs remains primarily the domain of major tech corporations and well-funded research institutions, there are some possibilities for smaller teams:

1. Small Language Models (SLMs): These are more efficient, require less data to train, and can run on less powerful hardware[7]. They're becoming increasingly popular for specific enterprise applications.

2. Fine-tuning existing models: Smaller teams can take pre-trained models and fine-tune them for specific tasks, which is less resource-intensive than training from scratch.

3. Open-source models: Some organizations have released open-source LLMs (like Meta's LLaMA) that can be adapted by smaller teams[4].

4. Collaborative efforts: Smaller teams might participate in collaborative projects or leverage cloud-based AI services to access LLM capabilities without bearing the full development cost.

5. Specialized models: Focusing on narrow domains or specific tasks can reduce the scale and cost of model development[8].

In conclusion, while the development of large-scale, general-purpose LLMs remains largely the domain of major tech companies due to the enormous costs involved, there are increasingly accessible paths for smaller teams to leverage and customize language models for specific applications. The trend towards more efficient, specialized models may further democratize access to this technology in the future.
 