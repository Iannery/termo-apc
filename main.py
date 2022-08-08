from termo import retorna_termo

resposta = retorna_termo()
print("DEBUG: a resposta é", resposta)
# 🟩🟨🟫
i = 0
while i < 5:
    tentativa = input()
    if len(tentativa) != 5:
        pass
    else:
        if tentativa == resposta:
            print("🟩🟩🟩🟩🟩 acertou!!!!!!")
            break
        else:
            for idx in range(len(tentativa)):
                if tentativa[idx] == resposta[idx]:
                    print("🟩", end="")
                elif tentativa[idx] in resposta:
                    print("🟨", end="")
                else:
                    print("🟫", end="")
            print("")