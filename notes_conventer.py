import re
import sys

def convert(original_line) -> str:

    # 使用正则表达式匹配整行
    match = re.search(r"^(.*\!\[([\w.]+)\].*)$", original_line)

    if match:
        line = match.group(0)
        # 进行字符串替换
        return line.replace(".tiff)", "_tiff_preview.png)")
    else:
        return original_line

if __name__ == "__main__":
    
    data = ""
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
            line = convert(line)
            
            print(line, end="")
            data += line
            
            
    with open(sys.argv[1], 'w') as file:
        file.write(data)  # Write the modified content back to the file
        
    
        
    