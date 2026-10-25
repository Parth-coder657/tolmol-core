from tolmol_agent import TolmolAgent
from vendor_simulator import VendorSimulator

def run_test():
    print("--- STARTING TOLMOL AI NEGOTIATION TEST ---")
    
    # Initialize Agent and Vendor Simulator
    agent = TolmolAgent(item_key="office_chairs", target_quantity=100)
    vendor = VendorSimulator(item_name="Ergonomic Office Chairs", initial_inflated_price=65.0)
    
    # Opening line from vendor
    current_message = "Hello! Thanks for your inquiry. 100 ergonomic office chairs will be $65 per unit."
    print(f"\n[Vendor]: {current_message}")
    
    # Run a 4-round automated negotiation loop
    for round_num in range(1, 5):
        print(f"\n--- Round {round_num} ---")
        
        # Tolmol AI generates counter-offer
        ai_reply = agent.respond(current_message)
        print(f"[Tolmol AI]: {ai_reply}")
        
        # Vendor reacts
        current_message = vendor.respond(ai_reply)
        print(f"[Vendor]: {current_message}")

if __name__ == "__main__":
    run_test()