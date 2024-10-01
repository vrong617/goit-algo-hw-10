import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total_Products"

model += 2 * lemonade + fruit_juice <= 100, "Water_Limit"
model += lemonade <= 50, "Sugar_Limit"
model += lemonade <= 30, "LemonJuice_Limit"
model += fruit_juice <= 20, "FruitPuree_Limit"

model.solve()

print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість виробленого лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого фруктового соку: {fruit_juice.varValue}")
print(f"Максимальна кількість продуктів: {pulp.value(model.objective)}")
