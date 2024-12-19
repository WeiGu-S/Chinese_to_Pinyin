import pandas as pd
from pypinyin import pinyin, Style

# 加载 Excel 文件
input_file = "input.xlsx"  # 替换为您的文件名
output_file = "output.xlsx"  # 转换后的文件名

# 读取 Excel
df = pd.read_excel(input_file)

# 定义拼音转换函数
def chinese_to_pinyin(text):
    if pd.isna(text):  # 跳过空值
        return ""
    return "".join([item[0] for item in pinyin(str(text), style=Style.NORMAL)])

# 假设 A 列是需要转换的内容
df["拼音"] = df.iloc[:, 0].apply(chinese_to_pinyin)

# 保存结果到新的 Excel 文件
df.to_excel(output_file, index=False)
print(f"转换完成！结果已保存到 {output_file}")