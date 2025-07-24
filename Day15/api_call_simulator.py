import random
import time
import logging

# Configure logging
logging.basicConfig(filename="api_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

class InvalidResponseError(Exception):
    """Raised when the API response is invalid."""
    pass

def simulate_api_call():
    """Randomly simulate success, timeout, connection, or invalid response."""
    outcome = random.choice(['success', 'timeout', 'connection', 'invalid'])
    
    if outcome == 'timeout':
        raise TimeoutError("The request timed out.")
    elif outcome == 'connection':
        raise ConnectionError("Could not connect to the server.")
    elif outcome == 'invalid':
        raise InvalidResponseError("Received invalid response.")
    else:
        return {"status": "success", "data": "Fake API Data"}

def api_call_with_retry(max_retries=3):
    attempts = 0
    while attempts < max_retries:
        try:
            print(f"Attempt #{attempts + 1}...")
            response = simulate_api_call()
        except TimeoutError as te:
            print(f"⏱ TimeoutError: {te}")
        except ConnectionError as ce:
            print(f"🌐 ConnectionError: {ce}")
        except InvalidResponseError as ire:
            print(f"⚠️ InvalidResponseError: {ire}")
        else:
            print("✅ API Call Success:", response)
            break
        finally:
            attempts += 1
            logging.info(f"API call attempt {attempts} completed.")
    else:
        print("❌ Failed after 3 attempts. Please try again later.")

# Run the simulation
if __name__ == "__main__":
    api_call_with_retry()
