## Висновки щодо точності методу Монте-Карло для обчислення інтегралів

### Опис проблеми
Метою цього дослідження було визначити значення визначеного інтегралу для функції `y = x^3` на відрізку `[0, 1]` за допомогою методу Монте-Карло та порівняти результат з точним методом, використовуючи функцію `quad` з бібліотеки `SciPy`.

### Результати
`Метод Монте-Карло`: Отримані результати залежать від кількості точок, що використовуються для оцінки. Наприклад, при `100000` вибірках результат був наближений до точного аналітичного значення.
Функція `quad`: Це високоточний метод чисельного обчислення визначених інтегралів. Для нашої функції результат склав приблизно `0.25`.

### Порівняння
Метод `Монте-Карло`: точність залежить від кількості вибірок. Зі збільшенням вибірок результат стає точнішим. При `100000` вибірках отримане значення було дуже близьким до аналітичного `(0.25)`.
Метод `quad`: забезпечує точне значення інтегралу, яке виступає еталоном для порівняння з методом Монте-Карло.

### Висновок
Метод Монте-Карло корисний у випадках, коли аналітичний розрахунок інтегралу неможливий або складний, наприклад, для багатовимірних інтегралів. Однак його точність залежить від кількості вибірок. Для задач із високими вимогами до точності потрібно використовувати достатньо велику кількість вибірок. У нашому прикладі для обчислення інтегралу на обмеженому інтервалі метод Монте-Карло показав результати, близькі до аналітичних значень, при великій кількості вибірок.
