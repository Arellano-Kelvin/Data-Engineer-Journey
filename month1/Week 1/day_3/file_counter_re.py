#ATBS sample code
"""
import shutil
from pathlib import Path
h = Path.home()
shutil.copy(h / 'spam/file1.txt', h)
'C:\\Users\\Al\\file1.txt'
shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt')
WindowsPath('C:/Users/Al/spam/file2.txt')
"""