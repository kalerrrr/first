import pandas as pd

# 读取数据
df = pd.read_csv("data.csv")

# 计算均线
df["ma"] = df["price"].rolling(3).mean()

# 生成信号
df["signal"] = (df["price"] > df["ma"]).astype(int)

print(df)
add strategy code
