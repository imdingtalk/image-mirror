import sys
import re

def is_image_format(text):
    # 支持多种格式：如 nginx:latest、myrepo/nginx:v1、gcr.io/org/nginx:1.0.0 等
    pattern = re.compile(
        r'^\s*('
        r'[a-zA-Z0-9*._-]+/[a-zA-Z0-9*._-]+:[a-zA-Z0-9*._-]+|'                           # repo/image:tag
        r'[a-zA-Z0-9*._-]+/[a-zA-Z0-9*._-]+/[a-zA-Z0-9*._-]+:[a-zA-Z0-9*._-]+|'           # domain/repo/image:tag
        r'[a-zA-Z0-9*._-]+/[a-zA-Z0-9*._-]+/[a-zA-Z0-9*._-]+/[a-zA-Z0-9*._-]+:[a-zA-Z0-9*._-]+|'  # domain/group/repo/image:tag
        r'[a-zA-Z0-9*._-]+:[a-zA-Z0-9*._-]+'                                              # image:tag
        r')\s*$',
        re.MULTILINE
    )

    # 跳过第一行（label），只校验实际镜像行
    lines = text.strip().split('\n')[1:]

    for line in lines:
        if not line.strip():  # 跳过空行
            continue
        if not pattern.match(line.strip()):
            return False
    return True

def main():
    body = sys.argv[1]
    result = is_image_format(body)
    print(f"::set-output name=is_image_format::{str(result).lower()}")

if __name__ == "__main__":
    main()
