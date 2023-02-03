from pathlib import Path

# Absolute path     # /usr/local/bin
# Relative path

path = Path("ecommerce")
print(path.exists())

path1 = Path()
for file in path1.glob('*.py'):
    print(file)

