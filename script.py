import os
import re
import socket
from collections import Counter

# Set the correct local output directory inside Downloads/project/
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)  # Create 'output' folder if it doesn't exist

output_file = os.path.join(output_dir, "result.txt")

def process_text(filename, split_contractions=False):
    """ Reads the file, processes words, and optionally splits contractions. """
    with open(filename, 'r') as f:
        text = f.read().lower()
    if split_contractions:
        text = text.replace("'", " ")  # Split contractions like "can't" -> "can t"
    words = re.findall(r'\b\w+\b', text)
    return words

def get_machine_ip():
    """ Gets the machine's IP address. """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address

def main():
    # Use correct file paths for your Downloads/project/ folder
    file1 = 'IF-1.txt'
    file2 = 'AlwaysRememberUsThisWay-1.txt'

    # Read and process files
    words_file1 = process_text(file1)
    words_file2 = process_text(file2, split_contractions=True)

    # Count words
    count_file1 = len(words_file1)
    count_file2 = len(words_file2)
    grand_total = count_file1 + count_file2

    # Find top 3 frequent words
    top3_file1 = Counter(words_file1).most_common(3)
    top3_file2 = Counter(words_file2).most_common(3)

    # Get machine's IP
    ip_address = get_machine_ip()

    # Prepare results
    result_lines = [
        f"Total words in IF-1.txt: {count_file1}",
        f"Total words in AlwaysRememberUsThisWay-1.txt: {count_file2}",
        f"Grand total words: {grand_total}",
        "\nTop 3 frequent words in IF-1.txt:",
        *[f"{word}: {count}" for word, count in top3_file1],
        "\nTop 3 frequent words in AlwaysRememberUsThisWay-1.txt (after splitting contractions):",
        *[f"{word}: {count}" for word, count in top3_file2],
        f"\nMachine IP Address: {ip_address}"
    ]

    # Write results to file
    with open(output_file, 'w') as f:
        f.write("\n".join(result_lines))

    # Print results
    print("\n".join(result_lines))

if __name__ == '__main__':
    main()
