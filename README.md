# Medical Expense Modeling: BMI, Age, and Linear Regression

**Nu Quynh Chau Nguyen | MSBA 265 | Business analytics portfolio**

Does age improve the prediction of medical expenses beyond BMI alone? This project compares a BMI-only baseline against a two-feature model using the Normal Equation and Gradient Descent. Adding age increases full-data R² from **0.0394 to 0.1173**. Both methods agree, but the remaining prediction errors are too large to justify deployment. See the [stakeholder memo](memo.md).

## Project map

```text
medical-expense-linear-regression/
├── data/
│   ├── insurance-premium-prediction/insurance.csv  Input dataset
│   └── model_comparison_bmi_expenses.png          Chart from script 04
├── reports/
│   └── assignment_results.csv                    Main results: three models
├── src/
│   └── assignment_two_feature_model.py           Your two-feature analysis
├── 01_simple_linear.py                           Explore the data
├── 02_ols_normal_equation.py                     Fit the BMI-only baseline
├── 03_gradient_descent.py                        Fit BMI-only with Gradient Descent
├── 04_compare_models_visual.py                   Compare BMI-only methods on train/test data
├── linear_regression_lab.ipynb                   Interactive version of the learning lab
├── memo.md                                      Interpret the two-feature results
├── README.md                                    Setup and execution instructions
└── requirements.txt                             One list of required libraries
```

**Learning sequence:** 01 → 02 → 03 → 04 → the two-feature script → memo.
The two-feature script can also run directly after installation; it loads the data and fits its own baseline. It does not depend on running the four learning scripts first.

## Start here: reproduce the analysis

You need a Windows or Mac computer, an internet connection for setup, and permission to install Python. No paid software or Kaggle account is required. Git is used to obtain the repository; VS Code is optional. The dataset is already included. Once packages are installed, the main analysis runs offline.

A **terminal** is a window where you type commands and press Enter. Copy only the text inside each command box; do not copy the surrounding backticks. Run each line separately and wait until the prompt returns before the next line. Keep the same terminal window open through setup and execution.

### 1. Install Python

Use **Python 3.13** for the closest match to the tested environment (Python 3.11 or newer is supported by the project).

- **Windows:** visit [Python downloads for Windows](https://www.python.org/downloads/windows/), choose a Python 3.13 release, download its installer for your computer, and run it. If the installer offers **Add Python to PATH**, select that option. Complete installation and close/reopen your terminal.
- **Mac:** visit [Python downloads for macOS](https://www.python.org/downloads/macos/), choose a Python 3.13 release, download the macOS installer, and complete installation. Use the Python you installed, not an older system Python.

### 2. Install Git and get this project

1. Install Git from [the official Git download page](https://git-scm.com/downloads) for your operating system, then reopen your terminal.
2. On Windows, open **PowerShell** from the Start menu. On Mac, press **Command + Space**, type **Terminal**, and press Enter.
3. Run the following commands one line at a time. Cloning creates a folder named `medical-expense-linear-regression` in your terminal's current folder.

```bash
git --version
git clone https://github.com/Nuquynhchaunguyen/medical-expense-linear-regression.git
cd medical-expense-linear-regression
```

If that folder already exists, open the existing checkout instead of cloning over it. For a peer verification attempt, use a fresh clone of the final published version. Do not use an old download.

### 3. Open a terminal in the project folder

**Windows:** open the project folder in File Explorer, click its address bar, type `powershell`, and press Enter. In the PowerShell window, type `dir` and press Enter. Confirm `requirements.txt` and `src` are listed.

**Mac:** open Terminal using Spotlight (Command + Space, type Terminal, press Enter). Type `cd ` including a space, drag the project folder from Finder into the Terminal window, and press Enter. Type `ls` and press Enter. Confirm `requirements.txt` and `src` are listed.

**Already using VS Code:** choose **File > Open Folder** and select the folder containing `requirements.txt`, then choose **Terminal > New Terminal**. Use the instructions for your computer below; on Windows choose PowerShell as the terminal type. If using an existing Git checkout, its folder may have a different name, which is fine.

### 4. Create an isolated Python environment and install packages

An environment keeps this project's packages separate from other projects. These commands use its Python directly, so you do not need to activate it or change PowerShell security settings.

**Windows (PowerShell)**

```powershell
py -3.13 --version
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If `py` is unavailable but `python --version` shows Python 3.13, use `python -m venv .venv` for the second line. If using another supported version, replace `-3.13` with your installed version.

**Mac (Terminal)**

```bash
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

If `python3 --version` shows an older version, use `python3.13 -m venv .venv` after installing Python 3.13. If `.venv` already exists for a supported Python, you can reuse it and run the installation line.

### 5. Run the learning scripts in order

For full project reproduction and peer verification, run all four commands for your operating system. Wait for each to finish before running the next.

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\python.exe 01_simple_linear.py
.\.venv\Scripts\python.exe 02_ols_normal_equation.py
.\.venv\Scripts\python.exe 03_gradient_descent.py
.\.venv\Scripts\python.exe 04_compare_models_visual.py
```

**Mac (Terminal)**

```bash
.venv/bin/python 01_simple_linear.py
.venv/bin/python 02_ols_normal_equation.py
.venv/bin/python 03_gradient_descent.py
.venv/bin/python 04_compare_models_visual.py
```

Script 01 prints summaries of the included data. Script 02 prints the BMI-only coefficients and scores. Script 03 prints training progress and the corresponding Gradient Descent coefficients. Script 04 compares the two BMI-only methods on train/test data and saves `data/model_comparison_bmi_expenses.png`; double-click that image to view it. Script 01 uses the local CSV when present and only downloads data if the file is missing.

### 6. Run the two-feature analysis

**Windows**

```powershell
.\.venv\Scripts\python.exe src/assignment_two_feature_model.py
```

**Mac**

```bash
.venv/bin/python src/assignment_two_feature_model.py
```

The script follows six numbered sections: load data; define metrics; fit the BMI baseline; fit the two-feature Normal Equation; fit two-feature Gradient Descent; print and export the comparison.

Look for **Number of rows: 1338**, three sets of model results, a comparison table and the final **Results saved to:** line. Open `reports/assignment_results.csv` in a text editor or spreadsheet viewer, then read `memo.md`. Rerunning the script replaces the CSV with freshly calculated results.

| Model | w0 | w1 (BMI) | w2 (age) | R² | RMSE (USD) |
|---|---:|---:|---:|---:|---:|
| BMI-only baseline | 1178.18 | 394.33 | — | 0.0394 | 11864.41 |
| Normal Equation (BMI + age) | -6437.35 | 333.39 | 241.90 | 0.1173 | 11373.64 |
| Gradient Descent (BMI + age) | -6437.35 | 333.39 | 241.90 | 0.1173 | 11373.64 |

The CSV contains three rows and eight columns: model, w0, w1_bmi, w2_age, MSE, RMSE, MAE and R2. A blank age coefficient for the baseline means age is not included. Small floating-point differences are normal.

### 7. Run the notebook

The notebook presents the instructor's learning exercises interactively. For full peer verification, run it too. The same `requirements.txt` has already installed its packages.

**Windows**

```powershell
.\.venv\Scripts\python.exe -m notebook
```

**Mac**

```bash
.venv/bin/python -m notebook
```

A browser page should open; if it does not, copy the local URL printed in the terminal into your browser. Click `linear_regression_lab.ipynb`, select the Python kernel from this environment, and choose **Run > Run All Cells**. Wait until all cells finish and check for error messages. Keep the terminal running while using the notebook; stop the server afterward with **Control + C** in the terminal.

In VS Code, install the Microsoft Python and Jupyter extensions if needed, open the notebook, click **Select Kernel** at the top right, choose **Python Environments**, and select the project's `.venv` Python. Then click **Run All**. The notebook and script 04 use train/test examples; their scores need not match the full-data two-feature table above.

**Expected warning in the standardization experiment:** You may see a red or pink message reading `RuntimeWarning: overflow encountered in square`. In this experiment, Gradient Descent on the raw (unstandardized) feature uses a learning rate of `0.01`; its prediction errors grow so large that squaring them exceeds the numerical range. This run deliberately demonstrates divergence and is compared with a standardized run and a raw-feature run using a smaller learning rate. It is an expected outcome of this experiment, not a successful fitted model.

The warning alone does not stop the notebook. Confirm that the comparison plots and table appear and that the remaining cells finish. An infinite (`inf`) loss in the diverging run is expected; the successful comparison runs should have finite losses. If execution stops with a traceback, or a different section produces non-finite results, treat that as an issue to investigate rather than assuming it is the same expected warning. This experiment is separate from the two-feature results in `reports/assignment_results.csv`.

## Method and interpretation

The two-feature script uses the general matrix solve `np.linalg.solve(X.T @ X, X.T @ y)`. Gradient Descent standardizes both BMI and age, uses learning rate 0.05 for 6,000 epochs, and converts coefficients back to original units. All three models in `assignment_results.csv` use the same full dataset to match the assigned comparison.

MSE measures average squared error in USD²; RMSE is its square root in USD; MAE is average absolute error in USD. Lower error is better. R² measures explained variation relative to the sample-mean baseline. These full-data scores describe in-sample fit rather than performance on unseen customers. Agreement between optimization methods establishes numerical consistency, not deployment readiness.

## Data and attribution

The included CSV has 1,338 records and seven columns. The two-feature script selects BMI, age and expenses and drops rows missing these values; no rows are dropped in the supplied file. The main analysis retains the source records without outlier filtering. The data originate from the course starter, which cites [Insurance Premium Prediction on Kaggle](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction). Original sampling methods and present-day representativeness have not been independently verified.

The numbered learning scripts and notebook come from [Shyla Solis's learning lab](https://github.com/shylasolis/linear-regression-with-standardization). The two-feature analysis and memo form the student's assignment contribution, developed using the course examples. AI assistance was used to revise documentation and check reproducibility. This project uses medical expense data, not the French motor claims dataset from Module 1.

## Reflection and verification status

I followed the professor's examples and ran the commands without encountering major difficulties. My main reproducibility concern is that Python environments and dependency versions may differ across computers. The project therefore uses one requirements file and explicit environment commands for both operating systems. Automated reproduction has been checked on macOS; Windows execution and independent peer validation still need to be confirmed by a real reviewer.

## Troubleshooting

| Problem | Action |
|---|---|
| `git` not found | Finish installing Git, then close and reopen the terminal. |
| Python command not found | Complete Python installation and reopen the terminal; Mac commands use `python3`. |
| `requirements.txt` not found | Run `dir` (Windows) or `ls` (Mac); move into the folder containing README.md and requirements.txt. |
| Missing Python package | Repeat step 4's installation command; use the exact `.venv` Python path shown when running scripts. |
| PowerShell activation blocked | No activation is needed; call `.\.venv\Scripts\python.exe` directly. |
| Missing `insurance.csv` | Obtain the complete repository; the file belongs in `data/insurance-premium-prediction/`. |
| A command gives `SyntaxError` at `>>>` | Type `exit()` to leave Python, then paste the command into the terminal. |
| Notebook cannot import packages | Select the same `.venv` kernel used for package installation. |
| No chart window appears | Script 04 saves a PNG; open `data/model_comparison_bmi_expenses.png`. |
| Installation fails | Check internet access and Python version, retry the installation command and retain the full error if it persists. |
| Results differ | Use the included CSV without editing it and compare the full-data script with the table in step 6, not script 04's train/test scores. |
