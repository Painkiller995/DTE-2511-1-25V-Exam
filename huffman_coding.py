import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):  # Needed for heapq
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if node is None:
        return code_map

    if node.char is not None:
        code_map[node.char] = prefix

    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)

    return code_map


def encode(text, code_map):
    return "".join(code_map[char] for char in text)


def decode(encoded_text, root):
    decoded = ""
    current = root
    for bit in encoded_text:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded += current.char
            current = root
    return decoded


def huffman_coding(text):
    print(f"Original text: '{text}'")
    root = build_huffman_tree(text)
    code_map = generate_codes(root)
    encoded = encode(text, code_map)

    # Print the Huffman code table
    print("\nHuffman Code Table:")
    print(f"{'Character':^10} | {'Code':^10}")
    print("-" * 23)
    for char in sorted(code_map):
        print(f"{char:^10} | {code_map[char]:^10}")

    print("\nEncoded string:", encoded)
    print("Decoded string:", decode(encoded, root))


# Example usage
huffman_coding("wire")
