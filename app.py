import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def can_partition(nums):
    """
    Determines if the array can be partitioned into two subsets with equal sum.
    Uses Dynamic Programming (Subset Sum Problem).
    """
    total_sum = sum(nums)
    
    # If total sum is odd, it's impossible to split into two equal integer sums
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    
    # dp[i] will be true if sum 'i' is possible
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        # Iterate backwards to ensure each element is used only once
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    
    return dp[target]

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
        
        if result:
            return jsonify({
                'success': True, 
                'possible': True, 
                'message': 'Equal Partition Possible'
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
