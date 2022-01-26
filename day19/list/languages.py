# for ~ in
# 컴파일러 vs 인터프리터
languages = ['Python', 'C', 'Java', 'Javascript' ]

for lang in languages:
    if lang in ['Python', 'Javascript']:
        print(lang + " need interpreter")
    elif lang in ['Java', 'C']:         #if를 써도 나오긴 함.
        print(lang + " need compiler")
