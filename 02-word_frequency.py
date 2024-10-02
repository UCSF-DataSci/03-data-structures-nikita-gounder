#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>
- tar -xzvf alice_in_wonderland.tar.gz #extract txt from gz file
- python 02-word_frequency.py alice_in_wonderland.txt


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys
import string

def word_frequency(text):
    frequencies = {} # Dictionary to store word frequencies
    words = text.lower().split() #full text with ignore case + split

    for i in words:    # Remove punctuation, whitespace?
        i = i.strip(string.punctuation)
        frequencies[i] = frequencies.get(i, 0) + 1

    frequencies = dict(sorted(frequencies.items())[:20]) #ordered and only first 20

    return frequencies


# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)

    