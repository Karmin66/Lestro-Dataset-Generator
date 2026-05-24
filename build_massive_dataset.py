import os
import json
import time
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# 1. STRUCTURAL CONTRACT FOR THE API
class TroubleshootingCase(BaseModel):
    text: str = Field(description="A highly verbose engineering case structure: 'User: Technical Issue: [log] \\nAssistant: Root Cause & Resolution Blueprint: [fix]'")

class DatasetBatch(BaseModel):
    cases: list[TroubleshootingCase]

client = genai.Client()
dataset_file = "dataset.json"

# 2. FREE TIER OPTIMIZED LIMITS
# 12 requests stays safely away from the 20 daily cap, preventing total lockout
total_batches = 12  
cases_per_batch = 15 # High density packaging per request

master_prompt = """
Act as an elite Principal DevOps and Systems Infrastructure Engineer. Generate exactly {cases_count} unique, highly dense technical troubleshooting cases for training a model named Lestro.

Every item in the cases list must strictly use this text formatting style inside its string:
"User: Technical Issue: [Describe a highly specific system failure here. Include long, realistic multi-line terminal error logs, stack traces, or broken configuration snippets.]\\nAssistant: Root Cause & Resolution Blueprint: [Provide an exhaustive, deep architectural explanation. Then, provide a bulleted, step-by-step resolution blueprint using exact terminal commands and corrected configuration blocks.]"

CRITICAL FOR DENSITY: Do not summarize, use placeholders, or truncate code blocks. Write fully realized, verbose, long-form system logs and complete multi-line config files (e.g., Kubernetes manifests, complex Nginx rules, Dockerfiles). Make every case as long and wordy as possible to generate maximum character volume.
"""

all_records = []
if os.path.exists(dataset_file):
    try:
        with open(dataset_file, "r", encoding="utf-8") as f:
            all_records = json.load(f)
            print(f"🔄 Loaded {len(all_records)} existing cases from backup. Standing by to append...")
    except Exception as e:
        print(f" Could not read backup file, starting fresh: {e}")

print("\n Maximum-Efficiency Dataset Engine Initialized.")
print(f"Target: Running {total_batches} total requests to stay safely below your 20-request daily limit.")

for batch in range(1, total_batches + 1):
    print(f" Requesting batch {batch}/{total_batches} ({cases_per_batch} high-density cases)...")
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-pro', # Pro provides much deeper, longer text generation than Flash
            contents=master_prompt.format(cases_count=cases_per_batch),
            config=types.GenerateContentConfig(
                temperature=1.0,
                response_mime_type="application/json",
                response_schema=DatasetBatch,
            )
        )
        
        if not response.text:
            print("Safety fallback triggered (empty response). Skipping to next request...")
            time.sleep(5)
            continue
            
        # Parse the structured cloud data flawlessly
        batch_json = json.loads(response.text)
        extracted_cases = batch_json.get("cases", [])
        
        all_records.extend(extracted_cases)
        print(f"Success! Added {len(extracted_cases)} records. Current total dataset size: {len(all_records)}")
        
        # Incremental save to disk
        with open(dataset_file, "w", encoding="utf-8") as f:
            json.dump(all_records, f, indent=2, ensure_ascii=False)
            
        # Generous wait time ensures we do not hit requests-per-minute (RPM) limits either
        print("Waiting 20 seconds to keep the API quota completely stable...")
        time.sleep(20)
        
    except Exception as e:
        print(f"Anomaly encountered: {e}")
        print("Cooling down for 30 seconds before trying the next request step...")
        time.sleep(30)

print(f"\n Process Complete! Your file '{dataset_file}' is securely saved with {len(all_records)} total cases.")
