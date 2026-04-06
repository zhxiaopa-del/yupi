from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent #加resolve是绝对路径
print(PROJECT_ROOT)

p = Path(__file__)
print(p)
print(p.parent)