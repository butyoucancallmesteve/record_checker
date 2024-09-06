import tkinter as tk
import dns.resolver

def check_cname_records(domain):
    subdomains = [
        f"inbound.{domain}",
        f"nc2048._domainkey.{domain}",
        f"nc2048.{domain}"
    ]
    
    results = {}
    for subdomain in subdomains:
        try:
            answers = dns.resolver.resolve(subdomain, 'CNAME')
            results[subdomain] = [rdata.to_text() for rdata in answers]
        except dns.resolver.NoAnswer:
            results[subdomain] = ["No CNAME record found"]
        except dns.resolver.NXDOMAIN:
            results[subdomain] = ["Domain does not exist"]
        except Exception as e:
            results[subdomain] = [str(e)]
    
    return results

def check_dmarc_record(domain):
    dmarc_domain = f"_dmarc.{domain}"
    try:
        answers = dns.resolver.resolve(dmarc_domain, 'TXT')
        return [rdata.to_text() for rdata in answers]
    except dns.resolver.NoAnswer:
        return ["No DMARC record found"]
    except dns.resolver.NXDOMAIN:
        return ["Domain does not exist"]
    except Exception as e:
        return [str(e)]

def check_spf_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        spf_records = [rdata.to_text() for rdata in answers if "v=spf1" in rdata.to_text()]
        return spf_records if spf_records else ["No SPF record found"]
    except dns.resolver.NoAnswer:
        return ["No SPF record found"]
    except dns.resolver.NXDOMAIN:
        return ["Domain does not exist"]
    except Exception as e:
        return [str(e)]

def show_dns_records():
    domain = domain_entry.get()
    if not domain:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter a domain.\n")
        return
    
    output_text.delete(1.0, tk.END)
    
    # Check CNAME records
    cname_results = check_cname_records(domain)
    output_text.insert(tk.END, "CNAME Records:\n")
    for subdomain, cnames in cname_results.items():
        output_text.insert(tk.END, f"{subdomain}:\n")
        for cname in cnames:
            output_text.insert(tk.END, f"  {cname}\n")
        output_text.insert(tk.END, "\n")
    
    # Check DMARC record
    dmarc_results = check_dmarc_record(domain)
    output_text.insert(tk.END, "DMARC Record:\n")
    for dmarc in dmarc_results:
        output_text.insert(tk.END, f"  {dmarc}\n")
    output_text.insert(tk.END, "\n")
    
    # Check SPF record
    spf_results = check_spf_record(domain)
    output_text.insert(tk.END, "SPF Record:\n")
    for spf in spf_results:
        output_text.insert(tk.END, f"  {spf}\n")
    output_text.insert(tk.END, "\n")

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
output_text = tk.Text(root, height=20, width=80)
output_text.pack(pady=10)

root.mainloop()