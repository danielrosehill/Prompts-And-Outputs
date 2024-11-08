---
title: "Automatically categorising LLM outputs - exploring feasibility"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm working on developing a system for managing GPT outputs at scale. One of the features that would be great would be something like being able to automatically assign metadata to outputs. For instance, there might be a taxonomy with output types and the output you just generated could be of the type "Product recommendations". Can you think of any way that could be implemented? It would require (I think) an LLM running over LLM outputs!

# Output

You’re right in thinking that a system for automatically assigning metadata to GPT outputs could involve running an LLM over the outputs themselves. Here’s a way this concept could be implemented:

### 1. **Define a Clear Taxonomy**:
   Start by creating a predefined taxonomy of output types. For example:
   - Product recommendations
   - Code snippets
   - Summaries
   - FAQs
   - Creative writing
   - Technical explanations

   Each category should be well-defined to ensure the system can accurately classify outputs.

### 2. **Create a Metadata Assignment Pipeline**:
   You could set up a pipeline where the output from a GPT model is fed into a secondary LLM or a rule-based system to determine the metadata tags. Here’s how it might work:

   - **Step 1: Generate Output** – The GPT generates the initial content (e.g., a product recommendation or a code snippet).
   - **Step 2: Analyze Output** – The output is passed to a secondary LLM, or you fine-tune a smaller model designed specifically for classification tasks. This model would be trained to recognize the types of outputs based on examples from your taxonomy.
   - **Step 3: Assign Metadata** – The LLM assigns the appropriate metadata based on the structure, content, and context of the output. This could involve:
     - **Text classification**: The LLM predicts the category or categories based on a prompt like, “Classify the following text into one of the following types: product recommendation, creative writing, etc.”
     - **Confidence scores**: The system could generate a confidence score for the assigned category and flag any ambiguous outputs for manual review.

### 3. **Train an LLM on Examples of Outputs**:
   To improve the accuracy of classification, you can fine-tune an existing LLM (e.g., GPT-3.5, GPT-4) with examples of various outputs and their corresponding categories. The training process would involve:
   - Feeding it thousands of labeled examples (e.g., product recommendations, summaries).
   - Having the model learn patterns in the structure, keywords, and tone that help it assign the correct metadata.

### 4. **Incorporate Heuristic-Based Filtering (Optional)**:
   You can enhance this system with heuristic rules. For example, you could use keyword matching or pattern detection in combination with the LLM:
   - If an output contains phrases like “best product,” “recommended,” or “suggested,” the system could more confidently classify it as a product recommendation.

### 5. **User-Feedback Loop**:
   Build a feedback loop into the system:
   - Allow users to manually adjust metadata if it’s incorrectly assigned.
   - Use this feedback to retrain and improve the LLM’s accuracy over time.

### 6. **Integration and Scalability**:
   Once this system is developed, you could scale it to handle large volumes of GPT outputs automatically. This could be integrated with existing systems like NoCodeDB, where outputs are stored and metadata is assigned automatically via the pipeline.

### Technologies to Use:
   - **OpenAI GPT-4 or GPT-3.5**: For initial fine-tuning and classification tasks.
   - **Hugging Face Models**: You can explore Hugging Face’s library of models that are specifically trained for text classification.
   - **NoCode Tools**: Integrate this into your current NoCodeDB setup for easier data management.

This approach, running an LLM over LLM outputs, provides the flexibility to handle a variety of output types and should streamline managing GPT outputs at scale.