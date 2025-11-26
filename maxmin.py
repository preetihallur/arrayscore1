def process_scores(s):
    total = sum(s)
    average = total / len(s)
    maximum = max(s)
    minimum = min(s)
    return total, average, maximum, minimum
if __name__=="__main__":
    import sys
    print("=== Score Processing Calculator ===")
    
    try:
        
        if len(sys.argv) > 1:
            s=list(map(float, sys.argv[1:]))
        else:
            
            s=input("Enter Scores Separated by space:")
            s = list(map(float, s.split()))
            
        print("\n=== Program Parameters ===")
        print(f"Scores entered: {s}")
        
        total, avg, maximum, minimum =process_scores(s)
        
        print("\n=== Result ===")
        print(f"Sum of scores: {total}")
        print(f"Average of scores: {avg:.2f}")
        print(f"Maximum score: {maximum}")
        print(f"Minimum score: {minimum}")
        
    except valueError:
        print("Invalid input. Please enter only numeric values.")