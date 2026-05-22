import os
import glob
import pandas as pd
from typing import List

path = "data/input"

def extract_from_excel(path: str) -> List[pd.DataFrame]:
  all_files = glob.glob(os.path.join(path, "*.xlsx"))

  data_frame_list = []
  for file in all_files:
    data_frame_list.append(pd.read_excel(file))

  return data_frame_list




  