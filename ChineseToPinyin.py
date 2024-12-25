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

# 获取用户输入的需要转换的列
columns_to_convert = input("请输入需要转换的列（例如 A, B, C...）：").split(',')

# 将列名转换为 DataFrame 的列索引
columns_to_convert = [col.strip() for col in columns_to_convert]

# 检查输入的列是否存在于 DataFrame 中
invalid_columns = [col for col in columns_to_convert if col not in df.columns]
if invalid_columns:
    print(f"以下列不存在于 Excel 文件中：{', '.join(invalid_columns)}")
else:
    # 转换指定的列
    for col in columns_to_convert:
        df[f"{col}_拼音"] = df[col].apply(chinese_to_pinyin)

    # 保存结果到新的 Excel 文件
    df.to_excel(output_file, index=False)
    print(f"转换完成！结果已保存到 {output_file}")
