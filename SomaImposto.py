def soma_imposto(taxa,custo):
    return taxa*custo
taxa=float(input("taxa do produto:"))
custo=float(input("custo do produto:"))
print(f"o preço final é :{soma_imposto(taxa,custo)}")