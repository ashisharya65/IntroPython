# Import the requests module we just installed
import requests

# Function to get a random fact from an API
def get_random_fact():
    """Fetch a random fun fact from the internet"""
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        # Use requests to get data from the internet
        response = requests.get(url, timeout=5)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data.get('text', "No fact available right now.")
        else:
            return f"Sorry, couldn't fetch a fact (status {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Sorry, couldn't fetch a fact (error: {e})"

# Function to get current time from an API
def get_current_time():
    """Get current UTC time using timeapi.io"""
    url = "https://timeapi.io/api/Time/current/zone?timeZone=UTC"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # timeapi.io returns fields like "dateTime", "year", "month", "hour", etc.
            return data.get("dateTime", "No datetime found")  # Already in ISO 8601 format
        else:
            return f"Couldn't get current time (status {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Couldn't get current time (error: {e})"

def get_random_joke():
    """Get a random programming joke"""
    url = "https://official-joke-api.appspot.com/random_joke"
    try: 
        response = requests.get(url,timeout=5)
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} - {joke_data['punchline']}"
        else:
            return "No jokes available right now!"
    except requests.exceptions.RequestException as e:
        return f"Couldn't get the random joke (error: {e})"
    
# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("WELCOME TO THE INFO FETCHER!")
    print("=" * 50)

    # Test 1: Get a random fact
    print("\n🎯 Here's a random fun fact:")
    fact = get_random_fact()
    print(f"📝 {fact}")

    # Test 2: Get current time
    print("\n⏰ Current UTC time:")
    current_time = get_current_time()
    print(f"🕐 {current_time}")

    # Test 3: Get a random joke
    print("\n🎯 Here's a random joke:")
    joke = get_random_joke()
    print(f"{joke} 😊")

    # Test 4: Show that requests module is working
    print("\n✅ Successfully used the 'requests' module!")
    print(f"📦 Requests module location: {requests.__file__}")

    print("\n" + "=" * 50)
    print("EXERCISE COMPLETED SUCCESSFULLY!")
    print("=" * 50)
