### 1. Создаём виртуальное окружение
```shell
   python -m venv .venv
```

### 2. Активируем виртуальное окружение
```shell
   .venv\Scripts\activate.bat
```

### 3. Устанавливаем основные зависимости и зависимости разработки
```shell
   pip install -r requirements.txt
   pip install -r dev-requirements.txt
```

### 4. Создаём папку для документации
```shell
   mkdir docs
```

### 5. Переходим в созданную папку и формируем файлы `Sphinx`
```shell
   cd docs
   sphinx-quickstart
```

Далее вводим:

`> Separate source and build directories (y/n) [n]: y`

`> Project name: СellularAutomation`

`> Author name(s): AspirantDrago`

`> Project release []: 1.0.0`

`> Project language [en]: ru`

### 6. Настраиваем `Sphinx`

### 7. Добавляем в начало файла `conf.py` путь к проекту:
```python
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
```

### 8. В файле `conf.py` указывеам расширения `Sphinx'a`, заменив
```python
extensions = []
```
на
```python
extensions = [
    'sphinx.ext.autodoc',  # авто документации из docstrings
    'sphinx.ext.viewcode',  # ссылки на исходный код
    'sphinx.ext.napoleon',  # поддержка Google и NumPy стиля документации
    'sphinx.ext.todo',  # поддержка TODO
    'sphinx.ext.coverage',  # проверяет покрытие документации
    'sphinx.ext.ifconfig',  # условные директивы в документации
]
```

### 9. Вернёмся в главный каталог и создадим страницы для нашей документации
```shell
    cd ..
    sphinx-apidoc -o docs\source cellular_automation
```

### 10. В файле `index.rst` указать в содержимом ссылку на созданный файл `cellular_automation.rst`

Результат:
```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   cellular_automation
```

### **11. ИТОГ**. Cоздаём документацию в формате `HTML`:
```shell
    docs\make html
```
