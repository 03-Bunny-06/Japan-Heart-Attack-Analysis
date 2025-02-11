# Japan Heart Attack Analysis

## Project Description
This script processes and analyzes the `japan_heart_attack_dataset.csv`  , this project analyzes heart attack data in Japan, focusing on gender-based differences in risk factors such as smoking, diabetes, alcohol consumption, and regional variations. The dataset is cleaned and processed using Pandas and NumPy, extracting insights on affected individuals based on lifestyle and health conditions.

## Features & Functionality
- **Data Cleaning:**
  - Removes unnecessary columns.
  - Fills missing values with zero.
- **Gender-based Analysis:**
  - Determines the proportion of males and females affected by heart attacks.
- **Health Condition Impact:**
  - Analyzes smoking and diabetes history in relation to heart attack cases.
- **Urban vs. Rural Impact:**
  - Compares smoking history between urban and rural populations.
- **Alcohol Consumption Influence:**
  - Examines heart attack cases based on alcohol consumption levels (High, Moderate, Low).
- **Age Statistics:**
  - Calculates the minimum, maximum, and average ages of smokers affected by heart attacks.

## Requirements
- Python 3.x
- Required libraries:
  ```bash
  pip install numpy pandas
  ```

## Installation & Setup
1. Clone the repository or download the script.
2. Ensure the dataset `japan_heart_attack_dataset.csv` is in the script directory.
3. Install required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python script.py
   ```

## How to Use
1. Place `japan_heart_attack_dataset.csv` in the script directory.
2. Run the script:
   ```bash
   python script.py
   ```
3. Modify the dataset and re-run to analyze different patterns.

## Notes
- The dataset should contain at least the following columns: `Gender`, `Smoking_History`, `Diabetes_History`, `Region`, `Alcohol_Consumption`, and `Age`.
- Additional filtering and analysis can be applied as needed.

## Author
This script was created to provide insights into heart attack trends using data analytics techniques.
