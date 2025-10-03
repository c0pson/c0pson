from collections import defaultdict
import os

def sort_files(files):
    return sorted(files, key=lambda x: int(x.split('_')[1].split('.')[0]))

def sort_files_by_sets_and_extension(file_list):
    def group_and_sort(files):
        ext_groups = defaultdict(list)
        for f in files:
            _, ext = os.path.splitext(f)
            ext_groups[ext].append(f)
        sorted_files = []
        for ext in sorted(ext_groups):
            sorted_files.extend(sorted(ext_groups[ext]))
        return sorted_files
    set_files = [f for f in file_list if f.startswith("set_")]
    other_files = [f for f in file_list if not f.startswith("set_")]
    sorted_sets = group_and_sort(set_files)
    sorted_others = group_and_sort(other_files)
    return sorted_sets + sorted_others
