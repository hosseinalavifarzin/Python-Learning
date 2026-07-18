# Parameters (پارامترها)

---

# مفهوم

گاهی لازم است Function هر بار با اطلاعات متفاوتی کار کند.

در این حالت از Parameter استفاده می‌کنیم.

Parameter یعنی اطلاعاتی که هنگام اجرای Function به آن ارسال می‌کنیم.

---

# بدون Parameter

```python
def hello():

    print("Hello")
```

همیشه

```
Hello
```

چاپ می‌شود.

---

# با Parameter

```python
def hello(name):

    print(f"Hello {name}")
```

---

# اجرا

```python
hello("Ali")
```

خروجی

```
Hello Ali
```

---

```python
hello("Sara")
```

خروجی

```
Hello Sara
```

---

# مثال

```python
def welcome(name):

    print(f"Welcome {name}")
```

---

# ارسال متغیر

```python
person = "Hossein"

welcome(person)
```

در واقع مقدار متغیر ارسال می‌شود.

---

# مثال عدد

```python
def square(number):

    print(number ** 2)
```

اجرا

```python
square(5)
```

خروجی

```
25
```

---

# مثال دیگر

```python
def cube(number):

    print(number ** 3)
```

---

# چند پارامتر

```python
def add(a,b):

    print(a+b)
```

اجرا

```python
add(3,5)
```

خروجی

```
8
```

---

# اشتباه رایج

تعریف

```python
def hello(name):
```

اجرا

```python
hello()
```

خطا

چون پارامتر ارسال نشده است.

---

# روش صحیح

```python
hello("Ali")
```

---

# اشتباه رایج دوم

من فکر می‌کردم

```
name
```

خودش مقدار دارد.

اما هنگام اجرای

```python
hello("Ali")
```

در واقع

```
name = "Ali"
```

می‌شود.

---

# نکات مهم

Parameter داخل Function ساخته می‌شود.

بعد از پایان Function از بین می‌رود.

---

# سوال مصاحبه

تفاوت Function و Parameter چیست؟

Function

یک قطعه کد است.

Parameter

اطلاعات ورودی Function است.

---

# تمرین

تابعی بنویس

```python
def greet(name):
```

که چاپ کند

```
Welcome Ali
```

---

تابعی بنویس

```python
def multiply(a,b):
```

که حاصل ضرب را چاپ کند.

---

# خلاصه

Parameter

اطلاعات ورودی Function است.

باعث می‌شود یک Function برای داده‌های مختلف قابل استفاده باشد.