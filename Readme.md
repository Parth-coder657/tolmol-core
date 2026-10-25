# Tolmol: Autonomous B2B Procurement & Negotiation Engine

Tolmol is an AI-powered agent designed to automate wholesale purchasing and negotiate optimal bulk pricing with suppliers while strictly respecting preset budget guardrails.

## Tech Stack
* **Language:** Python 3.10+
* **AI Engine:** Google Gemini API (`gemini-1.5-flash`)
* **Architecture:** Modular Agentic Loop + Simulated Vendor Environment

## Setup & Running
1. Clone the repository and open in VS Code.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your `GEMINI_API_KEY`.
6. Run the test simulation: `python test_negotiation.py`