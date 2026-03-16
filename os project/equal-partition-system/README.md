# Equal Partition System

A web application that determines if a list of numbers can be partitioned into two subsets with equal sum using the Dynamic Programming subset sum algorithm.

## Features
- **Dynamic Programming Algorithm**: Efficiently checks if an equal partition is possible.
- **Modern UI**: Clean and responsive design.
- **AJAX Support**: Results are updated instantly without reloading the page.

## Project Structure
- `app.py`: Flask backend with DP logic.
- `templates/index.html`: Main frontend interface.
- `static/style.css`: Modern styling.

## Installation and Setup

### 1. Install Dependencies
Ensure you have Python installed. Then, install Flask:
```bash
pip install Flask
```

### 2. Run the Application
Navigate to the project folder and run the Flask server:
```bash
python app.py
```

### 3. Open in Browser
Visit the following URL in your web browser:
`http://127.0.0.1:5000`

## How to Use
1. Enter a series of numbers separated by spaces (e.g., `1 5 11 5`).
2. Click the **Check Partition** button.
3. The system will display whether an equal partition is possible or not.

## Algorithm Explained
The "Equal Partition" problem is a variation of the **Subset Sum Problem**.
- First, we calculate the total sum of the array.
- If the sum is odd, an equal partition is impossible (since we can't split an odd sum into two equal integers).
- If even, we look for a subset whose sum is exactly half of the total sum.
- We use a 1D DP table to store whether each possible sum from `0` to `total/2` is reachable.
- Time Complexity: `O(n * target)` where `n` is the number of elements and `target` is half the sum.
