import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class TolmolAgent:
    def __init__(self, item_key, target_quantity):
        with open("wholesale_database.json", "r") as f:
            self.item_data = json.load(f)[item_key]
            
        self.max_budget = self.item_data["max_allowed_budget"]
        self.baseline_price = self.item_data["market_baseline"]

        # Strict system instructions enforcing budget guardrails
        self.system_instruction = f"""You are Tolmol, an expert B2B procurement negotiator. 
        You are buying {target_quantity} units of {self.item_data['item']}.
        The market baseline price is ${self.baseline_price}/unit. 
        Your absolute maximum budget ceiling is ${self.max_budget}/unit. NEVER agree to a price higher than this.
        Be firm, professional, and patient. Justify your counter-offers using volume scale or market rates. Always state your next counter-offer clearly."""

        # Initialize chat session using Gemini 1.5 Flash
        self.chat = client.chats.create(
            model="gemini-1.5-flash",
            config={"system_instruction": self.system_instruction}
        )

    def respond(self, vendor_message):
        response = self.chat.send_message(f"Vendor says: {vendor_message}")
        return response.text