def generate_brackets(groups):
    brackets = []
    for group in groups:
        names = group["Name"].tolist()
        while len(names) % 2 != 0:
            names.append("BYE")
        bracket = [(names[i], names[i+1]) for i in range(0, len(names), 2)]
        brackets.append(bracket)
    return brackets
