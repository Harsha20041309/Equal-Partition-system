import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def can_partition(nums):
    """
    Determines if the array can be partitioned into two subsets with equal sum.
    Uses Dynamic Programming and backtracking to reconstruct the subsets.
    """
    total_sum = sum(nums)
    
    # If total sum is odd, it's impossible to split into two equal integer sums
    if total_sum % 2 != 0:
        return {"possible": False}
    
    target = total_sum // 2
    n = len(nums)
    
    # dp[i][j] will be true if a sum of j can be achieved using first i numbers
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base case: Sum 0 is always possible with an empty subset
    for i in range(n + 1):
        dp[i][0] = True
        
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                
    if not dp[n][target]:
        return {"possible": False}
    
    # Backtrack to reconstruct Subset 1
    subset1 = []
    subset2 = list(nums)
    curr_sum = target
    for i in range(n, 0, -1):
        # If the sum curr_sum was not possible without the current number
        if curr_sum >= nums[i-1] and dp[i-1][curr_sum - nums[i-1]]:
            val = nums[i-1]
            subset1.append(val)
            curr_sum -= val
            # Remove one instance of val from subset2
            for k in range(len(subset2)):
                if subset2[k] == val:
                    subset2.pop(k)
                    break
                    
    return {
        "possible": True,
        "subset1": subset1,
        "subset2": subset2
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    try:
        data = request.get_json()
        input_str = data.get('numbers', '')
        # Convert space-separated string to list of integers
        nums = [int(x) for x in input_str.split() if x.strip()]
        
        if not nums:
            return jsonify({'success': False, 'message': 'Please enter some numbers.'})
        
        result = can_partition(nums)
        
        if result["possible"]:
            return jsonify({
                'success': True, 
                'possible': True, 
                'message': 'Equal Partition Possible',
                'subset1': result["subset1"],
                'subset2': result["subset2"]
            })
        else:
            return jsonify({
                'success': True, 
                'possible': False, 
                'message': 'Equal Partition Not Possible'
            })
            
    except ValueError:
        return jsonify({'success': False, 'message': 'Invalid input. Please enter only numbers.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    # Use the environment PORT variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
