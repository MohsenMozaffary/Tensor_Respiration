"""
thermal and respiratory signals will be inside two seperate folders with names of thermal and resp in main_path directory
"""

import os

def detect_data(main_path):
    main_thermal_path = os.path.join(main_path, 'thermal')
    main_resp_path = os.path.join(main_path, 'resp')
    file_names = os.listdir(main_thermal_path)
    all_thermal_dir = []
    all_resp_dir = []
    for name in file_names:
        all_thermal_dir.append(os.path.join((main_thermal_path), name))
        all_resp_dir.append(os.path.join((main_resp_path), name))

    return all_thermal_dir, all_resp_dir