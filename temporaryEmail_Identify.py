# pip install dnspython 

import dns.resolver

# List of known temporary email domains (example subset)
temporary_email_domains = [
    "mailinator.com",
    "10minutemail.com",
    "guerrillamail.com",
    "yopmail.com",
    "fna6.com",
    "ilebi.com",
    "cwmxc.com"
    # Add more domains as needed
]

def is_temporary_email(email):
    domain = email.split('@')[-1]
    if domain in temporary_email_domains:
        return True
    
    # Perform DNS check for MX records
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if not mx_records:
            return True
    except dns.resolver.NoAnswer:
        return True
    except dns.resolver.NXDOMAIN:
        return True

    return False

# Test the function
email = "kfhkiyemtazilybksa@cwmxc.com"
if is_temporary_email(email):
    print(f"{email} is a temporary email address.")
else:
    print(f"{email} is not a temporary email address.")
