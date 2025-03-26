import shodan
import os

# Store your API key securely (replace with your actual key)
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY", "your_api_here")

# Initialize Shodan API
api = shodan.Shodan(SHODAN_API_KEY)

# Check if the API key is valid
try:
    info = api.info()
    print(f"API Plan Info: {info}")
except shodan.APIError as e:
    print(f"Shodan API Error: {e}")
    exit()

def shodan_ip_lookup(ip):
    """Looks up details about a specific IP address using Shodan."""
    try:
        result = api.host(ip)
        print("\n--- Shodan IP Lookup Results ---")
        print(f"IP: {result['ip_str']}")
        print(f"Organization: {result.get('org', 'N/A')}")
        print(f"Country: {result.get('country_name', 'N/A')}")
        print(f"Open Ports: {', '.join(map(str, result['ports']))}")
        print(f"Operating System: {result.get('os', 'N/A')}")
        print("\n--- Banners ---")
        for item in result.get("data", []):
            print(f"Port {item['port']}: {item.get('data', '').strip()}")
        print("-" * 50)
    except shodan.APIError as e:
        print(f"Shodan API Error: {e}")

def shodan_search(query):
    """Search Shodan for public devices matching the query."""
    try:
        results = api.search(query)
        print(f"\n[+] Found {results['total']} results for '{query}':\n")
        for result in results['matches'][:5]:  # Limit to 5 results
            print(f"IP: {result['ip_str']}")
            print(f"Organization: {result.get('org', 'N/A')}")
            print(f"Port: {result['port']}")
            print(f"Banner:\n{result.get('data', 'N/A')}\n")
            print("-" * 50)
    except shodan.APIError as e:
        print(f"[-] Shodan API Error: {e}")

# Menu loop
while True:
    print("\n--- Shodan OSINT Tool ---")
    print("1. IP Lookup")
    print("2. Search Shodan (Requires Paid API)")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        ip = input("Enter an IP to lookup: ")
        shodan_ip_lookup(ip)

    elif choice == "2":
        query = input("Enter a search query (e.g., 'Apache server'): ")
        shodan_search(query)

    elif choice == "3":
        print("Exiting tool.")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
