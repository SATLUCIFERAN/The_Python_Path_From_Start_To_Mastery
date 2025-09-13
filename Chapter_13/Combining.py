
import pandas as pd

# The main report, with some missing data
main_report = pd.Series([100, 200, None, 400], index=['A', 'B', 'C', 'D'])

# The backup report, with data for the missing parts
backup_report = pd.Series([150, 250, 350, 450], index=['A', 'B', 'C', 'D'])

print("--- Main Report (with missing data) ---")
print(main_report)
print("\n--- Backup Report ---")
print(backup_report)

# Combine the main report with the backup report to fill in missing values

patched_report = main_report.combine_first(backup_report)
print("\n--- Patched Report ---")
print(patched_report)