传统的文件路径问题

我们使用 os.path.join dirname 等处理


现在使用python3 的 标准库

pathlib

```python
from pathlib import Path

config_path = (Path(__file__).parent.parent / 'conf' / 'config.ini')
print(config_path.read_text())
print(config_path.stem) # 获取文件名字
print(config_path.is_dir()
print(config_path.exists())
```