import glob
import pandas as pd

    # CONFIG
INPUT_PATTERN = "data/orders_???.csv"
OUTPUT_PATH = "data/orders_all.csv"
    # FUNCTIONS
def validate_columns(files: list) -> bool:
    """Check that all files have identical columns.
    Returns True if valid, False if any mismatch found.
    """
    reference_cols = pd.read_csv(files[0]).columns.tolist()
    for f in files:
        current_cols = pd.read_csv(f).columns.tolist()
        if current_cols != reference_cols:
            print(f"WARNING: {f} has different columns!")
            return False
        print(f"OK: {f}")
    return True


def load_and_merge(files: list) -> pd.DataFrame:
    """Load all CSV files, tag each row with source filename,
    and concat into a single DataFrame.
    """
    dfs = []
    for f in files:
        df = pd.read_csv(f)
        df["source_file"] = f
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

# ---------------
# MAIN
files = glob.glob(INPUT_PATTERN)

if validate_columns(files):
    df_all = load_and_merge(files)
    df_all.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved: {OUTPUT_PATH} — {df_all.shape[0]} rows, {df_all.shape[1]} columns")