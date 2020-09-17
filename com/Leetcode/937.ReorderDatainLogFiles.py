def reorderLogFiles(logs):
    let = []
    dig = []
    for i in logs:
        if i[-1].isdigit():
            dig.append(i)
        else:
            temp = i.split(" ")
            let.append([temp[0], temp[1:]])
    let.sort(key=lambda x: (x[1], x[0]))
    result = []
    for i in let:
        result.append(i[0] + " " + " ".join(i[1]))
    return result + dig


print(reorderLogFiles(["dig1 8 1 5 1", "let1 art can",
                       "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
