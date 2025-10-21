"""
Sorting Algorithm Visualizer
Author: AI Assistant
GitHub: https://github.com/fineanmol/hacktoberfest
Language: Python
Description: Interactive visualization tool for various sorting algorithms with step-by-step animations
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import time
from matplotlib.patches import Rectangle


class SortingVisualizer:
    """Interactive sorting algorithm visualizer"""
    
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.data = []
        self.comparisons = 0
        self.swaps = 0
        self.accesses = 0
        self.algorithm_name = ""
        
    def generate_data(self, size=50, data_type='random'):
        """Generate data for sorting"""
        if data_type == 'random':
            self.data = [random.randint(1, 100) for _ in range(size)]
        elif data_type == 'sorted':
            self.data = list(range(1, size + 1))
        elif data_type == 'reverse':
            self.data = list(range(size, 0, -1))
        elif data_type == 'nearly_sorted':
            self.data = list(range(1, size + 1))
            # Randomly swap some elements
            for _ in range(size // 10):
                i, j = random.randint(0, size-1), random.randint(0, size-1)
                self.data[i], self.data[j] = self.data[j], self.data[i]
        elif data_type == 'duplicates':
            self.data = [random.randint(1, 10) for _ in range(size)]
        
        self.reset_stats()
        return self.data
    
    def reset_stats(self):
        """Reset algorithm statistics"""
        self.comparisons = 0
        self.swaps = 0
        self.accesses = 0
    
    def visualize_array(self, highlight_indices=None, title_suffix=""):
        """Visualize the current state of the array"""
        self.ax.clear()
        
        # Create bars
        bars = self.ax.bar(range(len(self.data)), self.data, 
                          color='lightblue', edgecolor='black', linewidth=1)
        
        # Highlight specific indices
        if highlight_indices:
            for i in highlight_indices:
                if i < len(bars):
                    bars[i].set_color('red')
        
        # Set labels and title
        self.ax.set_xlabel('Index')
        self.ax.set_ylabel('Value')
        self.ax.set_title(f'{self.algorithm_name} - {title_suffix}')
        
        # Add statistics
        stats_text = f'Comparisons: {self.comparisons} | Swaps: {self.swaps} | Array Accesses: {self.accesses}'
        self.ax.text(0.02, 0.98, stats_text, transform=self.ax.transAxes, 
                   verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat'))
        
        # Set limits
        self.ax.set_xlim(-0.5, len(self.data) - 0.5)
        self.ax.set_ylim(0, max(self.data) + 5)
        
        plt.tight_layout()
        plt.pause(0.1)
    
    def bubble_sort(self, show_steps=True):
        """Bubble Sort Algorithm"""
        self.algorithm_name = "Bubble Sort"
        data = self.data.copy()
        n = len(data)
        
        if show_steps:
            self.visualize_array(title_suffix="Starting")
            time.sleep(1)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.comparisons += 1
                self.accesses += 2
                
                if show_steps:
                    self.visualize_array(highlight_indices=[j, j+1], 
                                       title_suffix=f"Comparing {data[j]} and {data[j+1]}")
                    time.sleep(0.3)
                
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    self.swaps += 1
                    self.accesses += 2
                    swapped = True
                    
                    if show_steps:
                        self.visualize_array(highlight_indices=[j, j+1], 
                                           title_suffix=f"Swapped {data[j+1]} and {data[j]}")
                        time.sleep(0.3)
            
            if not swapped:
                break
        
        self.data = data
        if show_steps:
            self.visualize_array(title_suffix="Complete!")
            time.sleep(1)
        
        return data
    
    def selection_sort(self, show_steps=True):
        """Selection Sort Algorithm"""
        self.algorithm_name = "Selection Sort"
        data = self.data.copy()
        n = len(data)
        
        if show_steps:
            self.visualize_array(title_suffix="Starting")
            time.sleep(1)
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.comparisons += 1
                self.accesses += 2
                
                if show_steps:
                    self.visualize_array(highlight_indices=[min_idx, j], 
                                       title_suffix=f"Finding minimum from index {i}")
                    time.sleep(0.2)
                
                if data[j] < data[min_idx]:
                    min_idx = j
            
            if min_idx != i:
                data[i], data[min_idx] = data[min_idx], data[i]
                self.swaps += 1
                self.accesses += 2
                
                if show_steps:
                    self.visualize_array(highlight_indices=[i, min_idx], 
                                       title_suffix=f"Swapped {data[min_idx]} and {data[i]}")
                    time.sleep(0.3)
        
        self.data = data
        if show_steps:
            self.visualize_array(title_suffix="Complete!")
            time.sleep(1)
        
        return data
    
    def insertion_sort(self, show_steps=True):
        """Insertion Sort Algorithm"""
        self.algorithm_name = "Insertion Sort"
        data = self.data.copy()
        
        if show_steps:
            self.visualize_array(title_suffix="Starting")
            time.sleep(1)
        
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            
            self.accesses += 1
            
            if show_steps:
                self.visualize_array(highlight_indices=[i], 
                                   title_suffix=f"Inserting {key} at position {i}")
                time.sleep(0.3)
            
            while j >= 0 and data[j] > key:
                self.comparisons += 1
                self.accesses += 2
                
                if show_steps:
                    self.visualize_array(highlight_indices=[j, j+1], 
                                       title_suffix=f"Shifting {data[j]} to position {j+1}")
                    time.sleep(0.2)
                
                data[j + 1] = data[j]
                j -= 1
            
            data[j + 1] = key
            self.accesses += 1
            
            if show_steps:
                self.visualize_array(highlight_indices=[j+1], 
                                   title_suffix=f"Placed {key} at position {j+1}")
                time.sleep(0.3)
        
        self.data = data
        if show_steps:
            self.visualize_array(title_suffix="Complete!")
            time.sleep(1)
        
        return data
    
    def merge_sort(self, show_steps=True):
        """Merge Sort Algorithm"""
        self.algorithm_name = "Merge Sort"
        data = self.data.copy()
        
        if show_steps:
            self.visualize_array(title_suffix="Starting")
            time.sleep(1)
        
        def merge_sort_recursive(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                
                if show_steps:
                    self.visualize_array(highlight_indices=list(range(left, right+1)), 
                                       title_suffix=f"Dividing array from {left} to {right}")
                    time.sleep(0.5)
                
                merge_sort_recursive(arr, left, mid)
                merge_sort_recursive(arr, mid + 1, right)
                merge(arr, left, mid, right)
        
        def merge(arr, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid
            
            L = [0] * n1
            R = [0] * n2
            
            for i in range(n1):
                L[i] = arr[left + i]
                self.accesses += 1
            
            for j in range(n2):
                R[j] = arr[mid + 1 + j]
                self.accesses += 1
            
            i = j = 0
            k = left
            
            if show_steps:
                self.visualize_array(highlight_indices=list(range(left, right+1)), 
                                   title_suffix=f"Merging subarrays from {left} to {right}")
                time.sleep(0.5)
            
            while i < n1 and j < n2:
                self.comparisons += 1
                self.accesses += 2
                
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                self.accesses += 1
                
                if show_steps:
                    self.visualize_array(highlight_indices=[k-1], 
                                       title_suffix=f"Placing element at position {k-1}")
                    time.sleep(0.1)
            
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
                self.accesses += 1
            
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1
                self.accesses += 1
        
        merge_sort_recursive(data, 0, len(data) - 1)
        self.data = data
        
        if show_steps:
            self.visualize_array(title_suffix="Complete!")
            time.sleep(1)
        
        return data
    
    def quick_sort(self, show_steps=True):
        """Quick Sort Algorithm"""
        self.algorithm_name = "Quick Sort"
        data = self.data.copy()
        
        if show_steps:
            self.visualize_array(title_suffix="Starting")
            time.sleep(1)
        
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            
            if show_steps:
                self.visualize_array(highlight_indices=[high], 
                                   title_suffix=f"Pivot: {pivot} at index {high}")
                time.sleep(0.5)
            
            for j in range(low, high):
                self.comparisons += 1
                self.accesses += 2
                
                if show_steps:
                    self.visualize_array(highlight_indices=[j, high], 
                                       title_suffix=f"Comparing {arr[j]} with pivot {pivot}")
                    time.sleep(0.2)
                
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    self.swaps += 1
                    self.accesses += 2
                    
                    if show_steps:
                        self.visualize_array(highlight_indices=[i, j], 
                                           title_suffix=f"Swapped {arr[j]} and {arr[i]}")
                        time.sleep(0.2)
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            self.swaps += 1
            self.accesses += 2
            
            if show_steps:
                self.visualize_array(highlight_indices=[i+1, high], 
                                   title_suffix=f"Placed pivot at position {i+1}")
                time.sleep(0.3)
            
            return i + 1
        
        def quick_sort_recursive(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_recursive(arr, low, pi - 1)
                quick_sort_recursive(arr, pi + 1, high)
        
        quick_sort_recursive(data, 0, len(data) - 1)
        self.data = data
        
        if show_steps:
            self.visualize_array(title_suffix="Complete!")
            time.sleep(1)
        
        return data
    
    def heap_sort(self, show_steps=True):
        """Heap Sort Algorithm"""
        self.algorithm_name = "Heap Sort"
        data = self.data.copy()
        n = len(data)
        
        if show_steps:
            self.visualize_array(title_suffix="Starting")
            time.sleep(1)
        
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n:
                self.comparisons += 1
                self.accesses += 2
                if arr[left] > arr[largest]:
                    largest = left
            
            if right < n:
                self.comparisons += 1
                self.accesses += 2
                if arr[right] > arr[largest]:
                    largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                self.swaps += 1
                self.accesses += 2
                
                if show_steps:
                    self.visualize_array(highlight_indices=[i, largest], 
                                       title_suffix=f"Heapifying: swapped {arr[largest]} and {arr[i]}")
                    time.sleep(0.3)
                
                heapify(arr, n, largest)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(data, n, i)
        
        if show_steps:
            self.visualize_array(title_suffix="Max heap built")
            time.sleep(1)
        
        # Extract elements from heap
        for i in range(n - 1, 0, -1):
            data[0], data[i] = data[i], data[0]
            self.swaps += 1
            self.accesses += 2
            
            if show_steps:
                self.visualize_array(highlight_indices=[0, i], 
                                   title_suffix=f"Extracted {data[i]} to position {i}")
                time.sleep(0.3)
            
            heapify(data, i, 0)
        
        self.data = data
        if show_steps:
            self.visualize_array(title_suffix="Complete!")
            time.sleep(1)
        
        return data
    
    def counting_sort(self, show_steps=True):
        """Counting Sort Algorithm (for non-negative integers)"""
        self.algorithm_name = "Counting Sort"
        data = self.data.copy()
        
        if show_steps:
            self.visualize_array(title_suffix="Starting")
            time.sleep(1)
        
        # Find the maximum element
        max_val = max(data)
        count = [0] * (max_val + 1)
        
        # Count occurrences
        for num in data:
            count[num] += 1
            self.accesses += 1
        
        if show_steps:
            self.visualize_array(title_suffix="Count array created")
            time.sleep(1)
        
        # Modify count array to store positions
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        # Build output array
        output = [0] * len(data)
        for i in range(len(data) - 1, -1, -1):
            output[count[data[i]] - 1] = data[i]
            count[data[i]] -= 1
            self.accesses += 2
            
            if show_steps:
                self.visualize_array(highlight_indices=[i], 
                                   title_suffix=f"Placing {data[i]} in output")
                time.sleep(0.2)
        
        self.data = output
        if show_steps:
            self.visualize_array(title_suffix="Complete!")
            time.sleep(1)
        
        return output
    
    def compare_algorithms(self, algorithms=['bubble_sort', 'selection_sort', 'insertion_sort', 'merge_sort', 'quick_sort']):
        """Compare multiple sorting algorithms"""
        print("=== Sorting Algorithm Comparison ===\n")
        
        results = {}
        
        for algo_name in algorithms:
            print(f"Running {algo_name.replace('_', ' ').title()}...")
            
            # Generate fresh data
            self.generate_data(20, 'random')
            
            # Run algorithm
            start_time = time.time()
            getattr(self, algo_name)(show_steps=False)
            end_time = time.time()
            
            # Store results
            results[algo_name] = {
                'comparisons': self.comparisons,
                'swaps': self.swaps,
                'accesses': self.accesses,
                'time': end_time - start_time
            }
            
            print(f"  Comparisons: {self.comparisons}")
            print(f"  Swaps: {self.swaps}")
            print(f"  Array Accesses: {self.accesses}")
            print(f"  Time: {end_time - start_time:.4f}s\n")
        
        return results


def demo_sorting_algorithms():
    """Demonstrate various sorting algorithms"""
    print("=== Sorting Algorithm Visualization Demo ===\n")
    
    viz = SortingVisualizer()
    
    # Generate sample data
    print("Generating sample data...")
    viz.generate_data(15, 'random')
    
    # Show initial data
    viz.visualize_array(title_suffix="Initial Data")
    time.sleep(1)
    
    # Demonstrate different algorithms
    algorithms = [
        ('bubble_sort', 'Bubble Sort'),
        ('selection_sort', 'Selection Sort'),
        ('insertion_sort', 'Insertion Sort'),
        ('merge_sort', 'Merge Sort'),
        ('quick_sort', 'Quick Sort'),
        ('heap_sort', 'Heap Sort')
    ]
    
    for algo_func, algo_name in algorithms:
        print(f"\nRunning {algo_name}...")
        
        # Generate fresh random data
        viz.generate_data(15, 'random')
        
        # Run algorithm with visualization
        getattr(viz, algo_func)(show_steps=True)
        
        print(f"{algo_name} completed!")
        print(f"Comparisons: {viz.comparisons}")
        print(f"Swaps: {viz.swaps}")
        print(f"Array Accesses: {viz.accesses}")
        
        time.sleep(2)
    
    print("\n=== Demo Complete ===")


def interactive_sorting_demo():
    """Interactive demo for sorting algorithms"""
    viz = SortingVisualizer()
    
    print("=== Interactive Sorting Algorithm Demo ===")
    print("1. Generate random data")
    print("2. Generate sorted data")
    print("3. Generate reverse sorted data")
    print("4. Generate nearly sorted data")
    print("5. Run Bubble Sort")
    print("6. Run Selection Sort")
    print("7. Run Insertion Sort")
    print("8. Run Merge Sort")
    print("9. Run Quick Sort")
    print("10. Run Heap Sort")
    print("11. Run Counting Sort")
    print("12. Compare all algorithms")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-12): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            size = int(input("Array size (default 20): ") or "20")
            viz.generate_data(size, 'random')
            viz.visualize_array(title_suffix="Random Data Generated")
        elif choice == '2':
            size = int(input("Array size (default 20): ") or "20")
            viz.generate_data(size, 'sorted')
            viz.visualize_array(title_suffix="Sorted Data Generated")
        elif choice == '3':
            size = int(input("Array size (default 20): ") or "20")
            viz.generate_data(size, 'reverse')
            viz.visualize_array(title_suffix="Reverse Sorted Data Generated")
        elif choice == '4':
            size = int(input("Array size (default 20): ") or "20")
            viz.generate_data(size, 'nearly_sorted')
            viz.visualize_array(title_suffix="Nearly Sorted Data Generated")
        elif choice in ['5', '6', '7', '8', '9', '10', '11']:
            algorithms = {
                '5': 'bubble_sort',
                '6': 'selection_sort',
                '7': 'insertion_sort',
                '8': 'merge_sort',
                '9': 'quick_sort',
                '10': 'heap_sort',
                '11': 'counting_sort'
            }
            algo = algorithms[choice]
            getattr(viz, algo)(show_steps=True)
        elif choice == '12':
            viz.compare_algorithms()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    # Run the demo
    demo_sorting_algorithms()
    
    # Uncomment the line below for interactive mode
    # interactive_sorting_demo()
