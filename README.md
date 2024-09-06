# DNS Record Checker

This Python program uses the `tkinter` library to create a GUI application that checks DNS records for a given domain. It specifically retrieves the DMARC record for the domain.

## Prerequisites

- Python 3.x
- `tkinter` library (usually included with Python)
- `dnspython` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/butyoucancallmesteve/record_checker.git
    cd dns-record-checker
    ```

2. Install the required Python packages:
    ```sh
    pip install dnspython
    ```

## Usage

1. Run the program:
    ```sh
    python record_checker.py
    ```

2. Enter the domain name in the GUI and click the button to check the DNS records.

## Example

When you enter a domain like `example.com`, the program will attempt to retrieve the DMARC record for `_dmarc.example.com`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [dnspython](https://www.dnspython.org/) for DNS record resolution.
- [tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI components.
