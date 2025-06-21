from pulp import LpProblem, LpMaximize, LpVariable, value

# Створюємо задачу
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні рішення — кількість Лимонаду (x) та Фруктового соку (y)
x = LpVariable(name="lemonade", lowBound=0, cat='Continuous')
y = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

# Цільова функція — максимізувати сумарну кількість продуктів
model += x + y, "Total_Production"

# Обмеження ресурсів
model += (2 * x + 1 * y <= 100), "Water_limit"
model += (1 * x <= 50), "Sugar_limit"
model += (1 * x <= 30), "Lemon_juice_limit"
model += (2 * y <= 40), "Fruit_puree_limit"

# Розв’язуємо задачу
model.solve()

# Вивід результатів
print(f"Статус: {model.status}, {model.solver.status}")
print(f"Кількість Лимонаду: {x.value()}")
print(f"Кількість Фруктового соку: {y.value()}")
print(f"Максимальна загальна кількість продуктів: {value(model.objective)}")