import streamlit as st
import os import sys
github_repo = 'https://github.com/CloudGang/q-e-d-g4-g-6-7-a-123-g-5-75-f-323-f-4-c-dw-3-f-wd-2-fs-f-3-/tree/main'
file_path = os.path.join(github_repo, 'o.txt')
with open(file_path, 'r') as f: 
    first_line = f.readline()
with open(file_path, 'w') as g:
    for line in f:
        g.write(line)
print(first_line)
