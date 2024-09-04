import tkinter as tk
from tkinter import messagebox
import dns.resolver 

# Function to get DNS records
def get_dns_records(domain):
    results = {}

    # Get DMARC Record
    try:
        dmarc_record = dns.resolver.resolve(f'_dmarc.{domain}', 'TXT')
        for txt in dmarc_record:
            if 'v=DMARC1' in txt.to_text():
                results['DMARC'] = txt.to_text()
                break
    except dns.resolver.NoAnswer:
        results['DMARC'] = 'Not found'
    except dns.resolver.NXDOMAIN:
        results['DMARC'] = 'Domain does not exist'
    except Exception as e:
        results['DMARC'] = f'Error: {e}'

    # Get SPF Record
    try:
        spf_record = dns.resolver.resolve(domain, 'TXT')
        for txt in spf_record:
            if 'v=spf1' in txt.to_text():
                results['SPF'] = txt.to_text()
                break
    except dns.resolver.NoAnswer:
        results['SPF'] = 'Not found'
    except dns.resolver.NXDOMAIN:
        results['SPF'] = 'Domain does not exist'
    except Exception as e:
        results['SPF'] = f'Error: {e}'

    # Get CNAME Record
    try:
        cname_record = dns.resolver.resolve(domain, 'CNAME')
        results['CNAME'] = cname_record[0].to_text()
    except dns.resolver.NoAnswer:
        results['CNAME'] = 'Not found'
    except dns.resolver.NXDOMAIN:
        results['CNAME'] = 'Domain does not exist'
    except Exception as e:
        results['CNAME'] = f'Error: {e}'

    return results

# Function to display the DNS records in the output area
def show_dns_records():
    domain = domain_entry.get().strip()
    if domain:
        results = get_dns_records(domain)
        output_text.delete(1.0, tk.END)  # Clear the output area
        output_text.insert(tk.END, f"DMARC Record: {results['DMARC']}\n")
        output_text.insert(tk.END, f"SPF Record: {results['SPF']}\n")
        output_text.insert(tk.END, f"CNAME Record: {results['CNAME']}\n")
    else:
        messagebox.showerror("Input Error", "Please enter a domain or subdomain.")

# Create the main application window
root = tk.Tk()
root.title("DNS Record Checker")

# Create and place the domain entry label and field
domain_label = tk.Label(root, text="Enter Domain/Subdomain:")
domain_label.pack(pady=5)

domain_entry = tk.Entry(root, width=50)
domain_entry.pack(pady=5)

# Create and place the check button
check_button = tk.Button(root, text="Check DNS Records", command=show_dns_records)
check_button.pack(pady=10)

# Create and place the output text area
output_text = tk.Text(root, height=10, width=60)
output_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()