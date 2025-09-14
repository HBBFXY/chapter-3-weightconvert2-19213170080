current_earth_weight = float(input("请输入你当前在地球上的体重(kg):"))
moon_weight_ratio = 0.165
print("未来10年你在地球和月球上的体重变化:")
for year in range(1,11):
  earth_weight = current_earth_weight + year * 0.5
  moon_weight = earth_weight*moon_weight_ratio
  print(f"第{year}年: 地球上的体重为{earth_weight:.2f}kg,月球上的体重为{moon_weight:.2f}kg")

