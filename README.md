# Equal Partition System

A web application that determines if a list of numbers can be partitioned into two subsets with equal sum using the Dynamic Programming subset sum algorithm.

## Features
- **Dynamic Programming Algorithm**: Efficiently checks if an equal partition is possible.
- **Modern UI**: Clean and responsive design.
- **AJAX Support**: Results are updated instantly without reloading the page.

## Project Structure
- `app.py`: Flask backend with DP logic.
- `requirements.txt`: Project dependencies for deployment.
- `templates/index.html`: Main frontend interface.
- `static/style.css`: Modern styling.

## Installation and Local Setup

### 1. Install Dependencies
Ensure you have Python installed. Then, install the requirements:
```bash
pip install -r requirements.txt
```

### 2. Run the Application
Navigate to the project folder and run the Flask server:
```bash
python app.py
```

### 3. Open in Browser
Visit the following URL in your web browser:
`http://127.0.0.1:5000`

## Deployment on Render

To deploy this project on [Render](https://render.com/):

1. **Create a New Web Service**: Connect your GitHub repository.
2. **Environment**: Select `Python`.
3. **Build Command**: 
   ```bash
   pip install -r requirements.txt
   ```
4. **Start Command**:
   ```bash
   gunicorn app:app
   ```

## Algorithm Explained
The "Equal Partition" problem is a variation of the **Subset Sum Problem**.
- First, we calculate the total sum of the array.
- If the sum is odd, an equal partition is impossible.
- If even, we look for a subset whose sum is exactly half of the total sum.
- We use a 1D DP table to store whether each possible sum from `0` to `total/2` is reachable.
