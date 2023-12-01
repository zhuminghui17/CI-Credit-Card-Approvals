[![Format](https://github.com/zhuminghui17/CI-Credit-Card-Approvals/actions/workflows/format.yml/badge.svg)](https://github.com/zhuminghui17/CI-Credit-Card-Approvals/actions/workflows/format.yml)


[![Install](https://github.com/zhuminghui17/CI-Credit-Card-Approvals/actions/workflows/install.yml/badge.svg)](https://github.com/zhuminghui17/CI-Credit-Card-Approvals/actions/workflows/install.yml)

[![Lint](https://github.com/zhuminghui17/CI-Credit-Card-Approvals/actions/workflows/lint.yml/badge.svg)](https://github.com/zhuminghui17/CI-Credit-Card-Approvals/actions/workflows/lint.yml)


[![Test](https://github.com/zhuminghui17/CI-Credit-Card-Approvals/actions/workflows/test.yml/badge.svg)](https://github.com/zhuminghui17/CI-Credit-Card-Approvals/actions/workflows/test.yml)


# Project #1: Continuous Integration in Data Science - Credit Card Approval
Continuous Integration using GitHub Actions of Python Data Science Project

## Dataset Overview
The Credit Card Approval dataset from the University of California Irvine (UCI) Machine Learning Repository is used to build automatic credit card approval predictors. The dataset is multivariate, with categorical, integer, and real feature types. It has 690 instances, with 55.5% of applications being denied and 44.5% being approved.

## Project Requirements:

The project structure must include the following files:
- [x] Jupyter Notebook with:
    - [x] Cells that perform descriptive statistics using Polars or Panda.	
    - [x] Tested by using nbval plugin for pytest
			
- [x] Python Script performing the same descriptive statistics using Polars or Panda		
- [x] lib.py file that shares the common code between the script and notebook
- [x] Makefile with the following:
    - [x] Run all tests (must test notebook and script and lib)
    - [x] Formats code with Python black
    - [x] Lints code with Ruff
	- [x] Installs code via:  pip install -r requirements.txt
		
- [x] test_script.py to test script		
- [x] test_lib.py to test library
- [x] Pinned requirements.txt
- [x] GitHub Actions performs all four Makefile commands with badges for each one in the README.md
		



 ## Rublic