from file_handler import scan_files, save_tests
from test_generator import generate_tests
from test_executor import run_tests
from error_analyzer import analyze_results
from test_refiner import refine_tests

def main():
    repo_path = "my-python-project/src"
    max_iterations = 10
    
    # Step 1: Scan files
    files = scan_files(repo_path)
    if not files:
        print("No Python files found.")
        return
    # print(files,"files")
    # Step 2-3: Generate and save initial tests
    test_files = []
    for file_info in files:
        test_code = generate_tests(file_info["content"])
        test_file = save_tests(test_code, file_info["path"])
        test_files.append([test_file,file_info["content"]])
    
    # Step 4-7: Iterate to execute, analyze, and refine tests
    for iteration in range(max_iterations):
        print(f"Iteration {iteration + 1}/{max_iterations}")
        # Step 4: Execute tests
        test_results = run_tests()
        print(test_results,"test_results")
        
        # Step 5: Analyze results
        issues, coverage = analyze_results(test_results, test_results["coverage_report"])
        print(issues,coverage,"issues_cov")
        
        # Step 6: Check success
        if test_results["returncode"] == 0 and coverage >= 80:
            print(f"Success: All tests passed with {coverage:.2f}% coverage.")
            break
        
        # Step 7: Refine tests
        print(f"Issues found: {issues}")
        for test_file,src_file in test_files:
            refine_tests(test_file,src_file, issues)
    
    else:
        print(f"Max iterations reached. Final coverage: {coverage:.2f}%.")
        if issues:
            print("Remaining issues:", issues)

if __name__ == "__main__":
    main()