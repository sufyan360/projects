Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 87, in <module>
    gui = Coin(window)
  File "/Users/sufyan/Python/coinGui.py", line 58, in __init__
    int_penny = int(penny1.get())
ValueError: invalid literal for int() with base 10: ''
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 87, in <module>
    gui = Coin(window)
  File "/Users/sufyan/Python/coinGui.py", line 58, in __init__
    int_penny = int(penny1.get())
ValueError: invalid literal for int() with base 10: ''
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 86, in <module>
    gui = Coin(window)
  File "/Users/sufyan/Python/coinGui.py", line 57, in __init__
    compute = Button(window, text="Compute", command=calculate()).grid(column=1, row=8)
NameError: name 'calculate' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 3, in <module>
    class Coin():
  File "/Users/sufyan/Python/coinGui.py", line 82, in Coin
    compute = Button(window, text="Compute", command=calculate()).grid(column=1, row=8)
NameError: name 'window' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 87, in <module>
    gui = Coin(window)
  File "/Users/sufyan/Python/coinGui.py", line 83, in __init__
    compute = Button(window, text="Compute", command=calculate()).grid(column=1, row=8)
TypeError: calculate() missing 1 required positional argument: 'self'
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 87, in <module>
    gui = Coin(window)
  File "/Users/sufyan/Python/coinGui.py", line 83, in __init__
    compute = Button(window, text="Compute", command=calculate()).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 59, in calculate
    int_penny = int(penny1.get())
ValueError: invalid literal for int() with base 10: ''
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 88, in <module>
    compute = Button(window, text="Compute", command=window.calculate()).grid(column=1, row=8)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 2354, in __getattr__
    return getattr(self.tk, attr)
AttributeError: '_tkinter.tkapp' object has no attribute 'calculate'
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 88, in <module>
    compute = Button(window, text="Compute", command=coin.calculate()).grid(column=1, row=8)
NameError: name 'coin' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 88, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate()).grid(column=1, row=8)
TypeError: calculate() missing 1 required positional argument: 'self'
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 88, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate(self)).grid(column=1, row=8)
NameError: name 'self' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 88, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("self")).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 60, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 88, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("self")).grid(column=1, row=8)
TypeError: calculate() takes 0 positional arguments but 1 was given
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 88, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate()).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 60, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 88, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("work")).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 60, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 94, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("work")).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 63, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 96, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("work")).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 65, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 96, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("work")).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 65, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 96, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("work")).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 65, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 96, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("work")).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 65, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 96, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("work")).grid(column=1, row=8)
  File "/Users/sufyan/Python/coinGui.py", line 65, in calculate
    int_penny = int(penny1.get())
NameError: name 'penny1' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 6, in <module>
    self.window = window
NameError: name 'self' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Traceback (most recent call last):
  File "/Users/sufyan/Python/coinGui.py", line 97, in <module>
    compute = Button(window, text="Compute", command=Coin.calculate("work")).grid(column=1, row=10)
NameError: name 'Coin' is not defined
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 1892, in __call__
    return self.func(*args)
  File "/Users/sufyan/Python/coinGui.py", line 69, in calculate
    penny2.config(text=pennyMoney)
NameError: name 'penny2' is not defined

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 1892, in __call__
    return self.func(*args)
  File "/Users/sufyan/Python/coinGui.py", line 71, in calculate
    int_nickel = int(nickel1.get())
ValueError: invalid literal for int() with base 10: ''
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 1892, in __call__
    return self.func(*args)
  File "/Users/sufyan/Python/coinGui.py", line 71, in calculate
    int_nickel = int(nickel1.get())
ValueError: invalid literal for int() with base 10: ''

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 1892, in __call__
    return self.func(*args)
  File "/Users/sufyan/Python/coinGui.py", line 110, in calculate
    total.config(text="$ %.2f" %str(totalMoney))
TypeError: must be real number, not str

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
>>> 
=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 1892, in __call__
    return self.func(*args)
  File "/Users/sufyan/Python/coinGui.py", line 109, in calculate
    totalMoney = pennyMoney + nickelMoney + dimeMoney + quarterMoney + halfdollarMoney + dollarcoinMoney
UnboundLocalError: local variable 'dollarcoinMoney' referenced before assignment

=================== RESTART: /Users/sufyan/Python/coinGui.py ===================
>>> 