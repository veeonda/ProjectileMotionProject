import csv
import random
import math

# Ask user for total number of rows
num_samples = int(input("How many samples do you want to generate? "))

g = 9.8  # m/s^2

param_file = "final_test.csv"
solution_file = "final_test_range.csv"

with open(param_file, mode='w', newline='') as p_file, \
     open(solution_file, mode='w', newline='') as s_file:
    
    param_writer = csv.writer(p_file)
    solution_writer = csv.writer(s_file)
    
    # Headers
    param_writer.writerow(["v0 (m/s)", "h (m)", "theta (degrees)"])
    solution_writer.writerow(["Range (m)"])
    
    for _ in range(num_samples):
        
        # Random floats in given ranges
        v0 = random.uniform(1, 20)
        h = random.uniform(0, 100)
        theta_deg = random.uniform(1, 89)
        theta = math.radians(theta_deg)
        
        # Range formula
        inside_sqrt = (v0 * math.sin(theta))**2 + 2 * g * h
        t = (v0 * math.sin(theta) + math.sqrt(inside_sqrt)) / g
        range_val = v0 * t * math.cos(theta)
        
        # Write parameters
        param_writer.writerow([
            round(v0, 4),
            round(h, 4),
            round(theta_deg, 4)
        ])
        
        # Write solution
        solution_writer.writerow([
            round(range_val, 4)
        ])

print("\nFiles generated successfully!")
print(f"Total rows (including header): {num_samples + 1}")
