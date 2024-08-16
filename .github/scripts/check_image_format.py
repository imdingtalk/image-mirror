import sys
import re

def is_image_format(text):
    # Regular expression pattern to match the specified image formats
    pattern = re.compile(r'^\s*([a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+:[a-zA-Z0-9\*._-]+|[a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+:[a-zA-Z0-9\*._-]+|[a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+:[a-zA-Z0-9\*._-]+|[a-zA-Z0-9\*._-]+:[a-zA-Z0-9\*._-]+)\s*$', re.MULTILINE)
    lines = text.strip().split('\n')
    for line in lines:
        if not pattern.match(line):
            return False
    return True

def main():
    body = sys.argv[1]
    result = is_image_format(body)
    print(f"::set-output name=is_image_format::{str(result).lower()}")

if __name__ == "__main__":
    main()
