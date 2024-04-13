from typing import Tuple
import pandas as pd
import pyreadr

import sys
sys.path.append(".")

import modules.utils.paths as path

def from_r(datasets_names: Tuple[str], extension: str):
  datasets_dfs = {}

  for dataset_name in datasets_names:

      dataset_file = f"{ dataset_name }{ extension }"
      dataset_output_file = path.data_raw_dir(dataset_file)

      datasets_dfs[f"{ dataset_name }_df"] = pyreadr.read_r(dataset_output_file).get(dataset_name)

  return datasets_dfs

def from_csv(datasets_names: Tuple[str]):
  datasets_dfs = {}

  for dataset_name in datasets_names:
      dataset_path_file = path.data_raw_dir(f"{ dataset_name }.csv")
      datasets_dfs[f"{ dataset_name }_df"] = pd.read_csv(dataset_path_file)

  return datasets_dfs

if __name__ == "__main__":
  datasets_names = ("oceanbuoys", "pedestrian", "riskfactors")
  extension = ".rda"

  datasets_df = from_r(datasets_names, extension)
  print(datasets_df.keys())
  print(type(datasets_df.keys()))
