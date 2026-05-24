# Lestro Dataset Generator ⭐

This script is an automated data engineering pipeline designed to build a massive, production-grade training dataset for fine-tuning Large Language Models (LLMs) in the DevOps and Systems Engineering domain.

It communicates directly with Google's Gemini API to generate highly realistic technical troubleshooting scenarios, terminal logs, and system configuration blueprints.

----------------------------------------------


What This Script Does & How Much It Creates?

The Problem: Fine-tuning an AI model requires millions of characters of data. Writing thousands of high-quality technical examples by hand is nearly impossible.

The Solution: This script automates the process using Structured Outputs. It forces the cloud model to generate perfect, uncorrupted training data that appends straight onto your hard drive.

Data Yield: * Running the script once executes 12 requests (batches).

Each batch generates 15 distinct technical cases.

Total yield per run = 180 massive, real-world engineering scenarios.

Character Count = Approximately 350,000 to 500,000 characters of high-density text per full run. Running it over 2–3 days easily clears the 1,000,000 character mark.

----------------------------------------------


Prerequisites (What You Need)
Before running the script, you need to have a few basic tools installed on your computer:

[Python 3.10](https://www.python.org/downloads/) or higher installed on your system.

A Free Gemini API Key from [Google AI Studio](https://aistudio.google.com/).

An existing JSON file (Optional). If you already have a dataset.json file, the script will automatically read it and append new data to the end of it without erasing anything.

----------------------------------------------


Step-by-Step Setup Guide

Step 1: Install the Required Libraries
Open your terminal or PowerShell window and install the official Google GenAI and Pydantic libraries by running:

*python -m pip install google-genai pydantic*
----------------------------------------------
Step 2: Save the Script
Create a file named build_massive_dataset.py in your project folder and paste the python script inside it. Ensure your target dataset file name matches the one in the script config line:

*dataset_file = "dataset.json"*
----------------------------------------------

Step 3: Link Your API Key
The script looks for your API key inside your computer's temporary environment variables for security. You must tell your terminal what your key is before starting.

On Windows (PowerShell): *$env:GEMINI_API_KEY="AIzaSyYourActualKeyGoesHere"*
----------------------------------------------
On Linux / macOS (Terminal): *export GEMINI_API_KEY="AIzaSyYourActualKeyGoesHere"*
----------------------------------------------

Step 4: Run the Script
Kick off the generator using Python:

*python build_massive_dataset.py*
----------------------------------------------



# How It Handles Quota Limits? (Free Tier Rules)

Google AI Studio's completely free tier allows a maximum of 20 requests per day for the heavy-duty gemini-2.5-flash model.

Safe Mode: This script is specifically configured to only make 12 requests total per run. This keeps you safely below the 20-request firewall limit so your API key never gets locked out mid-run.

Auto-Save: If your internet drops or you close the window, your data is completely safe. The script saves your progress incrementally to your hard drive after every single successful batch.

Resuming: If you run out of daily quota, just wait 24 hours for the limit to reset, open your terminal, set your key variable again, and run the script. It will pick up exactly where it left off!


# What the Final Output Looks Like?
The script will generate or update a file called dataset.json. The data is formatted perfectly into a structured array that training software (like Unsloth, Axolotl, or LM Studio) can read out-of-the-box.
