from huffman import build_huffman_tree, build_codes
from visualize import plot_frequency

text = "this is an example for huffman encoding"
plot_frequency(text)

tree = build_huffman_tree(text)
codes = build_codes(tree)

encoded = ''.join(codes[c] for c in text)
print("Original length (bits):", len(text) * 8)
print("Compressed length (bits):", len(encoded))
print("Compression rate: {:.2f}%".format(100 * len(encoded) / (len(text) * 8)))
