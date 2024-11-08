---
title: "Adding the LLM API functionality into a Mongo app"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. So we're beginning to narrow down the stack a little. So far we've decided upon MongoDB with Mongoose as the ODM. I'm still looking for an easy way to setup an admin panel type project for this that will make it easy for me to build out the CRUD pages I need to make this work. 

Perhaps we can think now about a more ambitious feature. I'd love to be able to write prompts in the app that I can send to an LLM via an API integration. When the LLM returns the output, it should automatically write back to the output collection.

Do you think that this could be achieved with our Mongo architecture and would it add a lot of complication to integrate it into the app?

# Output

Based on your requirements and the decisions made so far (MongoDB with Mongoose as the ODM), I think we can definitely achieve your goal of creating an admin panel with CRUD operations and integrating LLM functionality. Here's how we can approach this:

1. Admin Panel:
For an easy-to-setup admin panel that works well with MongoDB, I would recommend using AdminBro (now called AdminJS). It's specifically designed for Node.js and works seamlessly with MongoDB and Mongoose. Here's why it's a good fit:

- Easy setup with MongoDB and Mongoose
- Automatic CRUD interface generation
- Customizable and extendable
- Built-in authentication and authorization

2. LLM Integration:
Integrating LLM functionality into this architecture is definitely achievable and shouldn't add too much complexity. Here's a high-level approach:

a) Create a new route in your Express.js backend for sending prompts to the LLM.
b) Use an LLM API client (e.g., OpenAI's API) to send the prompt and receive the response.
c) Save the response to the MongoDB 'outputs' collection.
d) Create a custom action in AdminJS to trigger this process.

Here's a basic example of how this could look:

```javascript
// In your Express app
const AdminJS = require('adminjs')
const AdminJSExpress = require('@adminjs/express')
const AdminJSMongoose = require('@adminjs/mongoose')
const mongoose = require('mongoose')
const express = require('express')
const { OpenAIApi, Configuration } = require('openai')

AdminJS.registerAdapter(AdminJSMongoose)

const Prompt = mongoose.model('Prompt', { content: String })
const Output = mongoose.model('Output', { content: String, promptId: mongoose.Schema.Types.ObjectId })

const openai = new OpenAIApi(new Configuration({ apiKey: 'your-api-key' }))

const adminJs = new AdminJS({
  resources: [Prompt, Output],
  rootPath: '/admin',
  actions: {
    runPrompt: {
      actionType: 'record',
      component: false,
      handler: async (request, response, context) => {
        const { record, resource } = context
        const promptContent = record.params.content

        // Call LLM API
        const completion = await openai.createCompletion({
          model: "text-davinci-002",
          prompt: promptContent,
        })

        // Save output
        await Output.create({
          content: completion.data.choices[0].text,
          promptId: record.params._id
        })

        return {
          record: record.toJSON(context.currentAdmin),
          notice: {
            message: 'Prompt processed and output saved',
            type: 'success',
          },
        }
      },
    },
  },
})

const app = express()

app.use(adminJs.options.rootPath, AdminJSExpress.buildRouter(adminJs))
```

This setup allows you to:
1. Have automatic CRUD interfaces for your Prompts and Outputs.
2. Add a custom action to run a prompt through an LLM and save the output.

The beauty of this approach is that it leverages the simplicity of AdminJS for CRUD operations while allowing you to add custom functionality for your LLM integration. You can further customize the admin panel, add more complex logic, and extend the functionality as needed.

This solution maintains your MongoDB architecture and adds the LLM functionality without overly complicating the system. It provides a solid foundation that you can build upon as your requirements grow or change.

 




## Extracted Prompts
[[Prompts/Adding the LLM API functionality into a Mongo app.md#Prompt 1|Prompt 1]]
