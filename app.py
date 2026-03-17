import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def find_all_partitions(nums):
    """
    Finds all unique subset pairs with equal sums using backtracking.
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return {"possible": False}
    
    target = total_sum // 2
    nums.sort()
    n = len(nums)
    solutions = set()
    limit = 10

    def backtrack(start, current_sum, current_subset):
        if len(solutions) >= limit:
            return
            
        if current_sum == target:
            # Reconstruct the partition
            s1 = list(current_subset)
            s2 = list(nums)
            for x in s1:
                s2.remove(x)
            
            # Use tuple of sorted tuples to avoid duplicates and symmetry
            partition = tuple(sorted([tuple(sorted(s1)), tuple(sorted(s2))]))
            solutions.add(partition)
            return

        for i in range(start, n):
            # Optimization: skip further elements if target is exceeded
            if current_sum + nums[i] > target:
                break
                
            # Skip duplicate numbers at the same recursion level
            if i > start and nums[i] == nums[i-1]:
                continue
            
            current_subset.append(nums[i])
            backtrack(i + 1, current_sum + nums[i], current_subset)
            current_subset.pop()

    backtrack(0, 0, [])
    
    if not solutions:
        return {"possible": False}
    
    # Format solutions for JSON response
    formatted_solutions = []
    for s1, s2 in solutions:
        formatted_solutions.append({
            "subset1": list(s1),
            "subset2": list(s2)
        })
        
    return {
        "possible": True,
        "solutions": formatted_solutions
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/partition', methods=['POST'])
def partition():
    try:
        data = request.get_json()
        print(f"DEBUG: Received request data: {data}")
        
        input_str = data.get('numbers', '')
        if not input_str.strip():
            return jsonify({'success': False, 'message': 'Please enter some numbers.'})
            
        nums = [int(x) for x in input_str.split() if x.strip()]
        print(f"DEBUG: Parsed numbers: {nums}")
        
        if len(nums) < 2:
            return jsonify({'success': False, 'message': 'At least two numbers are required.'})
            
        result = find_all_partitions(nums)
        print(f"DEBUG: Partition found: {result['possible']}, Solutions: {len(result.get('solutions', []))}")
        
        if result["possible"]:
            return jsonify({
                'success': True, 
                'possible': True, 
                'message': f'Equal Partition Possible ({len(result["solutions"])} found)',
                'solutions': result["solutions"]
            })
        else:
            return jsonify({'success': True, 'possible': False, 'message': 'Equal Partition Not Possible'})
            
    except ValueError as e:
        print(f"DEBUG: ValueError: {str(e)}")
        return jsonify({'success': False, 'message': 'Invalid input. Please enter only numbers separated by spaces.'})
    except Exception as e:
        print(f"DEBUG: Unexpected error: {str(e)}")
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'})

if __name__ == '__main__':
    # Use the environment PORT variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
