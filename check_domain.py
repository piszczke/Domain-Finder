import whois
from whois import whois

def check_domain_availability(domain):
    try:
        # Query WHOIS information for the domain
        domain_info = whois(domain)
        # Check if the domain has a 'registrar' field; if not, it's available
        if not domain_info['registrar']:
            return True
        else:
            return False
    except Exception as e:
        # Handle any exceptions (e.g., domain not found)
        print(f"Error: {e}")
        return True

# Example usage
if __name__ == "__main__":
    domain = input("Enter domain to check availability: ")
    if check_domain_availability(domain):
        print(f"The domain {domain} is available.")
    else:
        print(f"The domain {domain} is not available.")
