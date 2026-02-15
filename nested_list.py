characters = [
    ['ayato', 'tartaglia', 'barbara', 'xingqiu'], 
    ['zhongli', 'navia', 'noelle', 'albedo'], 
    ['fishchl', 'raiden', 'lisa', 'keqing'], 
    ['bennett', 'xiangling', 'thoma', 'diluc'],
    ['kaeya', 'ganyu', 'qiqi', 'ayaka'], 
    ['venti', 'jean', 'kazuha', 'heizou']
]

# print(characters[2][1])

for i, value in enumerate(characters):
    for j, name in enumerate(value): 
        print(f"row:{i+1}, column:{j+1}, name:{name}")

