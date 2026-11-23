def saudar(nome):
    print(f"Olá, {nome}!")

saudar("João")
saudar("Maria")
saudar("Pedro")

def estatistica(nums):
    total = sum(nums)
    media = total / len(nums)
    return total, media

t,m = estatistica([8,9,7])
print(f"Total: {t}, Média: {m}")