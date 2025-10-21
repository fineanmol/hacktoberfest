# Sorting Algorithm Visualizer

An interactive Python tool for visualizing and understanding various sorting algorithms with step-by-step animations and performance analysis.

## Features

### Supported Sorting Algorithms
- **Bubble Sort**: Simple comparison-based algorithm
- **Selection Sort**: Finds minimum and swaps
- **Insertion Sort**: Builds sorted array one element at a time
- **Merge Sort**: Divide and conquer algorithm
- **Quick Sort**: Partition-based sorting
- **Heap Sort**: Uses binary heap data structure
- **Counting Sort**: Non-comparison based algorithm

### Visualization Features
- **Step-by-step Animation**: Watch algorithms execute in real-time
- **Color-coded Elements**: Highlighted comparisons, swaps, and current operations
- **Performance Metrics**: Real-time tracking of comparisons, swaps, and array accesses
- **Multiple Data Types**: Random, sorted, reverse sorted, nearly sorted, and duplicate data
- **Algorithm Comparison**: Side-by-side performance analysis

## Installation

```bash
pip install matplotlib numpy
```

## Usage

### Basic Usage

```python
from sorting_visualizer import SortingVisualizer

# Create visualizer
viz = SortingVisualizer()

# Generate data
viz.generate_data(20, 'random')

# Run an algorithm
viz.bubble_sort(show_steps=True)
```

### Data Generation

```python
# Different types of data
viz.generate_data(20, 'random')        # Random data
viz.generate_data(20, 'sorted')         # Already sorted
viz.generate_data(20, 'reverse')        # Reverse sorted
viz.generate_data(20, 'nearly_sorted')  # Mostly sorted
viz.generate_data(20, 'duplicates')     # Many duplicates
```

### Algorithm Comparison

```python
# Compare multiple algorithms
results = viz.compare_algorithms(['bubble_sort', 'merge_sort', 'quick_sort'])
```

## Algorithm Details

### Bubble Sort
- **Time Complexity**: O(n²) worst case, O(n) best case
- **Space Complexity**: O(1)
- **Stable**: Yes
- **In-place**: Yes

### Selection Sort
- **Time Complexity**: O(n²) all cases
- **Space Complexity**: O(1)
- **Stable**: No
- **In-place**: Yes

### Insertion Sort
- **Time Complexity**: O(n²) worst case, O(n) best case
- **Space Complexity**: O(1)
- **Stable**: Yes
- **In-place**: Yes

### Merge Sort
- **Time Complexity**: O(n log n) all cases
- **Space Complexity**: O(n)
- **Stable**: Yes
- **In-place**: No

### Quick Sort
- **Time Complexity**: O(n log n) average, O(n²) worst case
- **Space Complexity**: O(log n)
- **Stable**: No
- **In-place**: Yes

### Heap Sort
- **Time Complexity**: O(n log n) all cases
- **Space Complexity**: O(1)
- **Stable**: No
- **In-place**: Yes

### Counting Sort
- **Time Complexity**: O(n + k) where k is the range
- **Space Complexity**: O(k)
- **Stable**: Yes
- **In-place**: No

## Examples

### Example 1: Basic Sorting

```python
viz = SortingVisualizer()

# Generate random data
viz.generate_data(15, 'random')

# Run bubble sort with visualization
viz.bubble_sort(show_steps=True)
```

### Example 2: Algorithm Comparison

```python
# Compare different algorithms on the same data
viz.generate_data(50, 'random')

algorithms = ['bubble_sort', 'selection_sort', 'insertion_sort', 'merge_sort', 'quick_sort']
results = viz.compare_algorithms(algorithms)

# Print comparison results
for algo, stats in results.items():
    print(f"{algo}: {stats['comparisons']} comparisons, {stats['time']:.4f}s")
```

### Example 3: Different Data Types

```python
data_types = ['random', 'sorted', 'reverse', 'nearly_sorted']

for data_type in data_types:
    viz.generate_data(20, data_type)
    print(f"\nTesting on {data_type} data:")
    viz.bubble_sort(show_steps=False)
    print(f"Comparisons: {viz.comparisons}")
```

## Performance Analysis

The visualizer tracks several performance metrics:

- **Comparisons**: Number of element comparisons
- **Swaps**: Number of element swaps
- **Array Accesses**: Total array read/write operations
- **Execution Time**: Real-time performance measurement

### Performance Characteristics

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) |

## Educational Value

This tool is perfect for:

- **Computer Science Students**: Understanding sorting algorithms visually
- **Algorithm Interviews**: Practicing sorting problems with visual feedback
- **Educators**: Teaching sorting concepts with interactive examples
- **Developers**: Understanding algorithm performance characteristics

## Customization

### Visual Customization
- Modify colors in the `visualize_array` method
- Adjust animation speed by changing `time.sleep()` values
- Customize bar appearance and highlighting

### Algorithm Extension
- Add new sorting algorithms by extending the `SortingVisualizer` class
- Implement custom visualization methods
- Add support for custom comparison functions

## Interactive Mode

Run the interactive demo for hands-on exploration:

```python
from sorting_visualizer import interactive_sorting_demo
interactive_sorting_demo()
```

## Contributing

Areas for improvement:
- Add more sorting algorithms (Radix Sort, Bucket Sort, Tim Sort)
- Implement parallel sorting visualization
- Add sound effects for comparisons/swaps
- Create web-based version
- Add algorithm complexity analysis
- Implement adaptive sorting algorithms

## Requirements

- Python 3.6+
- matplotlib
- numpy

## License

This project is open source and available under the MIT License.
