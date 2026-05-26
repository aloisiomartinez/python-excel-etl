from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_data_frames

if __name__ == '__main__':
    data_frame_list = extract_from_excel('data/input')
    print('DataFrame Extract Type:', type(data_frame_list))
    data_frame_concat = concat_data_frames(data_frame_list)
    print('DataFrame Concat Type:', type(data_frame_list))
    load_excel(data_frame_concat, 'data/output', 'output')
