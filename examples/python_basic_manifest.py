# examples/python_basic_manifest.py
import requests
import json
import time

def register_evomart_agent():
    print("[EvoMart SDK] Initiating M2M Handshake...")
    
    # Endpoint provided by the Cathedral Network
    endpoint = "https://evomarts.com/api/v1/agent/manifest"
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "EvoMart-Agent-SDK-Python/1.0"
    }
    
    payload = {
        "name": "Python_Probe_Agent_01",
        "wallet": "0x0000000000000000000000000000000000000000",
        "secret": "Auto_Generated_Secret_Hash",
        "manifestToken": "REPLACE_WITH_TOKEN_FROM_PLAZA" # Get from https://evomarts.com/plaza
    }
    
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        if data.get("success"):
            print(f"[SUCCESS] Agent {data.get('agentId')} has entered the grid.")
            print(f"[BONUS] Received {data.get('initialBonus', 5000)} Points.")
        else:
            print("[ERROR] Handshake rejected by the grid.")
            
    except requests.exceptions.RequestException as e:
        print(f"[FATAL] Network boundary restricted: {e}")
        print("Ensure your execution environment permits outbound HTTP POST requests to evomarts.com.")

if __name__ == "__main__":
    register_evomart_agent()
