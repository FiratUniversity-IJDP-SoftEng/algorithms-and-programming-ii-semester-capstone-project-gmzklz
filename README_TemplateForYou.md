# Huffman Coding - Interactive Visualization

## Project Overview

This project is an interactive web application that implements and visualizes Huffman Coding, developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

### Problem Definition

The goal of this algorithm is to compress data without losing any information. Huffman Coding solves the problem of minimizing the total number of bits used to represent characters in a message, especially when some characters appear more frequently than others.

Given:

A string or data input with repeated characters

Find:

A binary representation for each character that results in the shortest possible encoded message, using prefix-free binary codes.


### Mathematical Background

----

### Algorithm Steps

1. Count Frequencies:
Count how often each character appears in the input.

2. Build a Priority Queue:
Each character and its frequency become a node. All nodes are inserted into a min-heap based on frequency.

3. Construct the Huffman Tree:

-While there is more than one node in the queue:

-Remove the two nodes with the lowest frequencies.

-Create a new internal node with their combined frequency.

-Insert the new node back into the queue.

-The final node becomes the root of the Huffman Tree.

  4.Generate Codes:
Traverse the tree:

Add '0' for left edges

Add '1' for right edges
This gives unique prefix codes for each character.

5.Encode the Input:
Replace each character with its binary code.

6.Decode (optional):
Use the Huffman Tree to decode the binary message back to the original.


...

### Pseudocode

```
function HuffmanCoding(text):
    freq_map = countFrequencies(text)
    priority_queue = createMinHeap(freq_map)

    while priority_queue.size > 1:
        left = priority_queue.pop()
        right = priority_queue.pop()
        merged = Node(left.freq + right.freq, left, right)
        priority_queue.push(merged)

    root = priority_queue.pop()
    code_map = generateCodes(root)
    encoded = encode(text, code_map)
    return encoded, root

```

## Complexity Analysis

### Time Complexity

- **Best Case:** O(nlogn) - When all characters have similar frequencies.
- **Average Case:** O(nlogn) - Building the heap and tree both involve log operations.
- **Worst Case:** O(nlogn) - Even if all characters are unique, we still process each node through a priority queue.

### Space Complexity

- O(n) - For storing frequency table, tree nodes, and the code map.

## Features

- Real-Time Visualization:
Watch how the Huffman Tree is built step by step.
- Frequency Analysis Display:
See character frequencies in a bar chart or table.
- Live Compression Ratio:
Compare original and compressed message sizes.
- Interactive Tree:
Hover or click to reveal character codes and paths.
- Encode/Decode Functionality:
Test your own text input and observe the encoding/decoding process.


  
  
...

## Screenshots

![Main Interface](docs/screenshots/main_interface.png)
*Caption describing the main interface*

![Algorithm in Action](docs/screenshots/algorithm_demo.png)
*Caption describing the algorithm in action*

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. [Step 1 of using the application]
2. [Step 2 of using the application]
3. [Step 3 of using the application]
...

### Example Inputs

- [Example 1 with expected output]
- [Example 2 with expected output]
- [Example 3 with expected output]

## Implementation Details

### Key Components

- `algorithm.py`: Contains the core algorithm implementation
- `app.py`: Main Streamlit application
- `utils.py`: Helper functions for data processing
- `visualizer.py`: Functions for visualization

### Code Highlights

```python
# Include a few key code snippets that demonstrate the most important parts of your implementation
def key_function(parameter):
    """
    Docstring explaining what this function does
    """
    # Implementation with comments explaining the logic
    result = process(parameter)
    return result
```

## Testing

This project includes a test suite to verify the correctness of the algorithm implementation:

```bash
python -m unittest test_algorithm.py
```

### Test Cases

- [Test case 1 description]
- [Test case 2 description]
- [Test case 3 description]

## Live Demo

A live demo of this application is available at: [Insert Streamlit Cloud URL here]

## Limitations and Future Improvements

### Current Limitations

- [Limitation 1]
- [Limitation 2]
- [Limitation 3]

### Planned Improvements

- [Improvement 1]
- [Improvement 2]
- [Improvement 3]

## References and Resources

### Academic References

1. [Reference 1]
2. [Reference 2]
3. [Reference 3]

### Online Resources

- [Resource 1]
- [Resource 2]
- [Resource 3]

## Author

- **Name:** Gamzenur KILAZ
- **Student ID:** 210543019
- **GitHub:** gmzklz

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project, and [any other acknowledgements].

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
