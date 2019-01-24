# -*- coding: utf-8 -*-

def main():
    tabl = []
    columnLength = []

    # Excel表読み込み
    while True:
        line = input()
        if line == "":
            break
        tab = line.split("\t")
        tabl.append(tab)

    # 列の最大文字数格納リスト生成
    for i in range(len(tabl[0])):
        columnLength.append([0, 0, 0])

    # 列の最大文字数カウント
    for indexes, names in enumerate(tabl[1:]):
        for index, name in enumerate(names):
            num = floatSplit(name)

            if len(name) > columnLength[index][0]:
                columnLength[index][0] = len(name)
            if num[0]    > columnLength[index][1]:
                columnLength[index][1] = num[0]
            if num[1]    > columnLength[index][2]:
                columnLength[index][2] = num[1]

    # TeXヘッダー作成
    for index, header in enumerate(tabl[0]):
        if index == len(tabl[0])-1:
            tabl[0][index] = header + " \\\\"
        else:
            tabl[0][index] = header + " & "
        print(tabl[0][index], end="")
    print()

    # TeX表作成
    for indexes, names in enumerate(tabl[1:]):
        for index, name in enumerate(names):
            num = floatSplit(name)

            tabl[indexes][index] = " "*(columnLength[index][1]-num[0]) + name + " "*(columnLength[index][2]-num[1])
            if index == len(names)-1:
                tabl[indexes][index] += " \\\\"
            else:
                tabl[indexes][index] += " & "
            print(tabl[indexes][index], end="")
        print()

def floatSplit(name):
    num = [0, 0]
    if name.find(".") != -1:
        sp = name.split(".")
        num[0] = len(sp[0])
        num[1] = len(sp[1])+1
    else:
        num[0] = len(name)
        num[1] = 0
    return num


if __name__ == '__main__':
    main()