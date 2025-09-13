# GroupBy & Aggregation (Serious Jedi Moves)
# ------------------------------------------------------------
# Mantra: split → apply → combine

import pandas as pd
import numpy as np

# --- Sample Data: Battle of Yavin Combat Log ---
combat_log = pd.DataFrame({
    'Pilot ID':     ['Luke', 'Luke', 'Wedge', 'Biggs', 'Wedge', 'Han', 'Han'],
    'Squadron':     ['Red',  'Red',  'Red',   'Red',   'Red',   'Gold','Gold'],
    'Kills':        [5,       2,      1,       3,       2,       4,     1],
    'Damage Taken': [10,      5,      2,       8,       3,      15,     6]
})

print("--- Full Combat Log ---")
print(combat_log)

# --- Multi-Index GroupBy + Named Aggregation ---
# We group by Squadron and Pilot ID → creates a Multi-Index.
# Use .agg to compute totals. Then compute a custom metric using both totals.
summary = (
    combat_log
    .groupby(['Squadron', 'Pilot ID'])  # Multi-Index: (Squadron, Pilot)
    .agg(
        TotalKills=('Kills', 'sum'),
        TotalDamage=('Damage Taken', 'sum')
    )
)

print("----After .groupby & . agg --------")
print(summary)
print("------------")

# Custom metric across multiple columns (post-agg, clean & fast)
summary['CombatEfficiency'] = summary['TotalKills'] / summary['TotalDamage'].replace(0, np.nan)
print("------ Post-Aggregation Calculation ------")
print(summary)
print("------------")


# Sort by TotalKills (chaining)
summary = summary.sort_values(by='TotalKills', ascending=False)
print("\n--- Sort by TotalKills---")
print(summary)
print("------------")



# --- Top Pilot per Squadron by TotalKills ---
# Reset → sort → groupby → head(1) → set index back
top_pilots_per_squadron = (
    summary
    .reset_index()
    .sort_values(['Squadron', 'TotalKills'], ascending=[True, False])
    .groupby('Squadron')
    .head(1)
    .set_index(['Squadron', 'Pilot ID'])
)

print("\n--- Top Pilot per Squadron (by Total Kills) ---")
print(top_pilots_per_squadron[['TotalKills']])

# --- (Optional) Flat Index for Export/Display ---

flat_summary = summary.reset_index()
print("\n--- Flat Summary (Easy to export to CSV) ---")
print(flat_summary)

# --- (Optional) Multiple aggregations per column (bonus demo) ---
# Shows how to compute multiple stats at once, still with named agg.

multi_stats = (
    combat_log
    .groupby(['Squadron', 'Pilot ID'])
    .agg(
        Kills_sum=('Kills', 'sum'),
        Kills_mean=('Kills', 'mean'),
        Damage_sum=('Damage Taken', 'sum'),
        Damage_mean=('Damage Taken', 'mean'),
    )
    .sort_values(by='Kills_sum', ascending=False)
)
print("\n--- Bonus: Multiple Aggregations per Column ---")
print(multi_stats)
