# 基础交互程序：计算两个数的和
def calculate_sum():
    # 提示用户输入并获取值（转换为浮点数支持小数）
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    
    # 计算求和
    total = num1 + num2
    
    # 输出结果（格式化字符串展示）
    print(f"\n{num1} + {num2} = {total}")

# 程序入口
if __name__ == "__main__":
    print("=== 简易加法计算器 ===")
    calculate_sum()