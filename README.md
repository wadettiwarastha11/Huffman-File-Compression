# Huffman-File-Compression
This program demonstrates frequency-based Huffman encoding and decoding, along with real GZIP file compression and decompression using Python's built-in gzip module.

# Huffman File Compression Using Python

## Description
This project demonstrates frequency-based data encoding
using the Huffman Tree and file compression using GZIP.

Huffman coding assigns variable-length binary codes
to characters based on their frequency. Frequently
occurring characters generally receive shorter codes,
while less frequent characters receive longer codes.

The application also uses Python's gzip module to
compress and decompress files.

## Objectives
- Understand Huffman Trees and frequency-based encoding.
- Implement a priority queue using a min-heap.
- Generate Huffman codes for characters.
- Encode and decode text.
- Compress and decompress files using GZIP.

## Features
- Calculate character frequencies.
- Construct a Huffman Tree.
- Generate binary codes.
- Encode and decode text.
- Compress files into .gz format.
- Restore files through decompression.

## Technologies Used
- Python 3
- Heap / Priority Queue
- Huffman Tree
- gzip module
- Counter from collections

## How to Run
1. Install Python 3.
2. Save the code as huffman_compression.py.
3. Open the terminal in the project folder.
4. Execute:

   python huffman_compression.py

5. Select an operation from the menu.

## Applications
- Data compression
- File storage optimization
- Data transmission
- Text encoding
- Compression utilities

## Conclusion
This project demonstrates how Huffman Trees can
encode text using character frequencies and how GZIP
can compress and restore files. It provides practical
understanding of trees, heaps, encoding, and compression.
