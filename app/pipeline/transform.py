import pandas as pd
from typing import List


def concat_data_frames(data_frames_list: List[pd.DataFrame]) -> pd.DataFrame:
  return pd.concat(data_frames_list, ignore_index= True)