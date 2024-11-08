---
title: "How to do text to audio conversion programatically"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I think it makes the most sense to convert the markdown files into audio programatically and locally. I would be happy to use an API or whatever would offer the best and most realistic sounding voices. Can you suggest some options and provide approximate costs?

# Output

Here are some of the best options for converting markdown files to audio using **APIs** that provide **realistic-sounding voices** along with **cost estimates**:

### 1. **Google Cloud Text-to-Speech (TTS)**
   - **Description**: Google Cloud TTS offers high-quality, lifelike voices using WaveNet and Neural2 technologies. It supports various languages and provides realistic speech generation with customization options for pitch, speed, and volume.
   - **Features**:
     - Offers **WaveNet voices**, which are some of the most natural-sounding AI-generated voices.
     - Supports over 220 voices across 40+ languages and dialects.
     - Can export audio in different formats like MP3, WAV, and OGG.
     - Customize voice parameters like speaking rate, pitch, and volume.
   - **Costs**:
     - **Standard Voices**: $4 per 1 million characters.
     - **WaveNet Voices**: $16 per 1 million characters.
     - **Neural2 Voices**: $16 per 1 million characters (more realistic than WaveNet).
     - **Free Tier**: 4 million characters per month with standard voices, 1 million characters per month with WaveNet voices.
   - **How to Use**:
     - You can easily integrate Google Cloud TTS into your Python program with the `google-cloud-texttospeech` library.
     ```bash
     pip install google-cloud-texttospeech
     ```

   **Example Python script**:
   ```python
   from google.cloud import texttospeech

   # Set up the client
   client = texttospeech.TextToSpeechClient()

   # Read markdown file
   with open("example.md", "r") as file:
       text = file.read()

   # Set text input
   synthesis_input = texttospeech.SynthesisInput(text=text)

   # Select the voice
   voice = texttospeech.VoiceSelectionParams(
       language_code="en-US",
       name="en-US-Wavenet-D",
       ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
   )

   # Set audio config
   audio_config = texttospeech.AudioConfig(
       audio_encoding=texttospeech.AudioEncoding.MP3
   )

   # Perform the text-to-speech request
   response = client.synthesize_speech(
       input=synthesis_input, voice=voice, audio_config=audio_config
   )

   # Write the audio file to disk
   with open("output_audio.mp3", "wb") as out:
       out.write(response.audio_content)
   ```

### 2. **Amazon Polly**
   - **Description**: Amazon Polly is an AI-powered text-to-speech service that converts text into lifelike speech. It offers standard voices as well as **Neural TTS** (NTTS) voices, which sound highly natural.
   - **Features**:
     - Supports **NTTS** for higher-quality voices.
     - Over 60 voices in 30+ languages.
     - Speech customization options like speech rate, pronunciation, and intonation using **SSML tags**.
     - Can output to MP3, OGG, and PCM.
   - **Costs**:
     - **Standard Voices**: $4 per 1 million characters.
     - **Neural Voices (NTTS)**: $16 per 1 million characters.
     - **Free Tier**: 5 million characters per month for the first 12 months.
   - **How to Use**:
     You can integrate Polly into Python using the **boto3** library.
     ```bash
     pip install boto3
     ```

   **Example Python script**:
   ```python
   import boto3

   # Initialize Polly client
   polly_client = boto3.Session().client('polly')

   # Read markdown file
   with open("example.md", "r") as file:
       text = file.read()

   # Perform TTS request
   response = polly_client.synthesize_speech(
       Text=text, OutputFormat='mp3', VoiceId='Joanna'
   )

   # Write the audio stream to a file
   with open("output_audio.mp3", 'wb') as file:
       file.write(response['AudioStream'].read())
   ```

### 3. **Microsoft Azure Speech Service**
   - **Description**: Microsoft's Azure Speech offers highly realistic **Neural TTS voices** with a variety of customization options and control over the speech synthesis.
   - **Features**:
     - Over 400 voices in 140 languages and dialects.
     - **Neural TTS** provides lifelike, human-like speech.
     - Extensive customization options including speaking styles, emotions, and pitch control.
     - Outputs audio in MP3, WAV, or OGG formats.
   - **Costs**:
     - **Standard Voices**: $4 per 1 million characters.
     - **Neural Voices**: $16 per 1 million characters.
     - **Free Tier**: 5 million characters per month for 12 months with the standard tier.
   - **How to Use**:
     Integrate Azure TTS using the **azure-cognitiveservices-speech** library.
     ```bash
     pip install azure-cognitiveservices-speech
     ```

   **Example Python script**:
   ```python
   import azure.cognitiveservices.speech as speechsdk

   # Set up the client
   speech_config = speechsdk.SpeechConfig(subscription="YourSubscriptionKey", region="YourRegion")

   # Read markdown file
   with open("example.md", "r") as file:
       text = file.read()

   # Create the synthesizer
   synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

   # Perform speech synthesis
   result = synthesizer.speak_text_async(text).get()

   # Save the result to an audio file
   if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
       with open("output_audio.wav", "wb") as audio_file:
           audio_file.write(result.audio_data)
   ```

### 4. **IBM Watson Text-to-Speech**
   - **Description**: IBM Watson TTS provides **AI-driven, natural-sounding voices**. Watson’s neural voices are designed to sound realistic and provide a human-like experience.
   - **Features**:
     - High-quality neural voices.
     - Supports SSML customization for control over pitch, rate, and emphasis.
     - Outputs in MP3, WAV, OGG.
   - **Costs**:
     - **Standard Voices**: $2 per 1 million characters.
     - **Neural Voices**: $20 per 1 million characters.
     - **Free Tier**: 10,000 characters per month.
   - **How to Use**:
     You can use the **ibm_watson** Python SDK.
     ```bash
     pip install ibm-watson
     ```

   **Example Python script**:
   ```python
   from ibm_watson import TextToSpeechV1
   from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

   # Set up the client
   authenticator = IAMAuthenticator('YourAPIKey')
   text_to_speech = TextToSpeechV1(authenticator=authenticator)
   text_to_speech.set_service_url('YourServiceURL')

   # Read markdown file
   with open("example.md", "r") as file:
       text = file.read()

   # Perform the text-to-speech request
   with open('output_audio.mp3', 'wb') as audio_file:
       response = text_to_speech.synthesize(text, voice='en-US_AllisonV3Voice', accept='audio/mp3').get_result()
       audio_file.write(response.content)
   ```

### Cost Summary:
| **Service**                  | **Free Tier**                           | **Standard Cost**              | **Neural/Advanced Cost**         |
|------------------------------|-----------------------------------------|--------------------------------|----------------------------------|
| **Google Cloud TTS**          | 4 million chars/month (standard)        | $4 per 1M chars                | $16 per 1M chars (WaveNet/Neural2)|
| **Amazon Polly**              | 5 million chars/month (first 12 months) | $4 per 1M chars                | $16 per 1M chars (NTTS)          |
| **Microsoft Azure Speech**    | 5 million chars/month (12 months)       | $4 per 1M chars                | $16 per 1M chars (Neural)        |
| **IBM Watson TTS**            | 10,000 chars/month                     | $2 per 1M chars                | $20 per 1M chars (Neural)        |

### Conclusion:
If you’re looking for **high-quality, realistic voices** and are open to using APIs, the most cost-effective solutions with excellent voice quality are **Google Cloud TTS** and **Amazon Polly**. Both services offer **Neural TTS voices** that are very natural-sounding, with reasonable costs for large text volumes. You can programmatically convert markdown content to audio locally and integrate with these APIs for the best results.

