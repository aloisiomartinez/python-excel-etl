from typing import List

import pandas as pd


def concat_data_frames(data_frames_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frames_list, ignore_index=True)
