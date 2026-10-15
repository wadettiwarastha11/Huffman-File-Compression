
import heapq
import gzip
import os
from collections import Counter


# Node for Huffman Tree
class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None


# Build Huffman Tree
def build_huffman_tree(text):
    if not text:
        return None

    frequency = Counter(text)
    heap = []
    counter = 0

    for char, freq in frequency.items():
        node = Node(char, freq)
        heapq.heappush(heap, (freq, counter, node))
        counter += 1

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        parent = Node(None, freq1 + freq2)
        parent.left = left
        parent.right = right

        heapq.heappush(
            heap, (parent.frequency, counter, parent)
        )
        counter += 1

    return heap[0][2]


# Generate Huffman Codes
def generate_codes(root, prefix="", codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = prefix or "0"
        return codes

    generate_codes(root.left, prefix + "0", codes)
    generate_codes(root.right, prefix + "1", codes)

    return codes


# Demonstrate Huffman Encoding and Decoding
def huffman_demo():
    text = input("Enter text to encode: ")

    if not text:
        print("Text cannot be empty.")
        return

    root = build_huffman_tree(text)
    codes = generate_codes(root)

    encoded = "".join(codes[char] for char in text)

    print("\nCharacter Frequencies:")
    for char, freq in Counter(text).items():
        print(repr(char), ":", freq)

    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(repr(char), ":", code)

    print("\nEncoded Binary String:")
    print(encoded)

    # Decode the encoded bit string
    decoded = ""
    current = root

    for bit in encoded:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded += current.char
            current = root

    print("\nDecoded Text:")
    print(decoded)


# Compress a file using GZIP
def compress_file():
    source = input("Enter file path to compress: ").strip()

    if not os.path.isfile(source):
        print("File not found.")
        return

    destination = source + ".gz"

    try:
        with open(source, "rb") as file:
            data = file.read()

        with gzip.open(destination, "wb") as gz_file:
            gz_file.write(data)

        print("File compressed successfully!")
        print("Compressed file:", destination)
        print("Original size:", len(data), "bytes")
        print("Compressed size:", os.path.getsize(destination), "bytes")

    except OSError as error:
        print("Compression failed:", error)


# Decompress a GZIP file
def decompress_file():
    source = input("Enter .gz file path: ").strip()

    if not os.path.isfile(source):
        print("File not found.")
        return

    if not source.endswith(".gz"):
        print("Please provide a .gz file.")
        return

    destination = source[:-3]

    if os.path.exists(destination):
        print("Output file already exists. Choose another name.")
        return

    try:
        with gzip.open(source, "rb") as gz_file:
            data = gz_file.read()

        with open(destination, "wb") as file:
            file.write(data)

        print("File decompressed successfully!")
        print("Restored file:", destination)

    except (OSError, EOFError) as error:
        print("Decompression failed:", error)


# Main menu
while True:
    print("\n===== File Compression System =====")
    print("1. Huffman Encoding and Decoding")
    print("2. Compress File using GZIP")
    print("3. Decompress GZIP File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        huffman_demo()

    elif choice == "2":
        compress_file()

    elif choice == "3":
        decompress_file()

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
