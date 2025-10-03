from enum import StrEnum
import os

class PATH(StrEnum):
    # 
    PHYSICS_REPORTS = os.path.join('static', 'physics_reports')
    DATABASES_REPORTS = os.path.join('static', 'databases_reports')
    PROGRAMMING_REPORTS = os.path.join('static', 'programming_reports')
    NETWORKS_REPORTS = os.path.join('static', 'networks_reports') 
    DCT_REPORTS = os.path.join('static', 'dct_reports')
    ASSEMBLER_REPORTS= os.path.join('static', 'assembler_reports')
    # 
    PYTHON_PROJECTS = os.path.join('static', 'python_projects')
    CPP_PROJECTS = os.path.join('static', 'cpp_projects')
    R_PROJECTS = os.path.join('static', 'r_projects')
    # 
    PHYSICS_NOTES = os.path.join('static', 'physics_notes')
    DCT_NOTES = os.path.join('static', 'dct_notes')
    ASSEMBLER_NOTES = os.path.join('static', 'assembler_notes')
