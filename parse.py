import re

def parse_log(filename):
    test_results = {}

    with open(filename, 'r') as f:
        lines = f.readlines()

    current_test_name = None
    for line in lines:
        test_name_match = re.search(r'^Running test suite: (\w+)', line)
        test_fail_match = re.search(r'(\d+) tests failed', line)
        test_pass_match = re.search(r'all tests passed', line)

        if test_name_match:
            current_test_name = test_name_match.group(1)
            test_results[current_test_name] = {'passed': True, 'failed_count': 0}

        if test_fail_match and current_test_name:
            test_results[current_test_name]['passed'] = False
            test_results[current_test_name]['failed_count'] = int(test_fail_match.group(1))

        if test_pass_match and current_test_name:
            test_results[current_test_name]['passed'] = True

        # You can add more conditions here, e.g., to handle crashes.
    
    return test_results

results = parse_log('path_to_your_log_file.log')
for test_name, result in results.items():
    if result['passed']:
        print(f"{test_name}: All tests passed!")
    else:
        print(f"{test_name}: {result['failed_count']} tests failed.")

# If you want to count the total number of failed tests across all suites:
total_failed = sum([result['failed_count'] for result in results.values()])
print(f"Total failed tests: {total_failed}")
