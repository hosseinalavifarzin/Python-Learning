# Input & Output

---

# مفهوم

برنامه باید بتواند

اطلاعات را از کاربر بگیرد

و

به کاربر نمایش دهد.

---

# دریافت اطلاعات

```python
name = input("Name: ")
```

کاربر

```
Ali
```

متغیر

```
name = "Ali"
```

---

# نمایش اطلاعات

```python
print(name)
```

---

# مثال

```python
name = input("Name: ")

print(name)
```

ورودی

```
Hossein
```

خروجی

```
Hossein
```

---

# چند print

```python
print("Hello")
print("Python")
```

خروجی

```
Hello

Python
```

---

# چاپ متن و متغیر

```python
name = "Ali"

print("Hello", name)
```

خروجی

```
Hello Ali
```

---

# f-string

بهترین روش چاپ

```python
name = "Hossein"

print(f"Hello {name}")
```

خروجی

```
Hello Hossein
```

---

# دریافت عدد

اشتباه

```python
age = input()
```

این مقدار String است.

درست

```python
age = int(input())
```

---

# مثال

```python
age = int(input("Age: "))

print(age)
```

---

# اشتباه رایج

```python
age = input()

print(age + 5)
```

خطا

چون age رشته است.

باید

```python
age = int(input())
```

---

# خلاصه

input

اطلاعات می‌گیرد.

print

اطلاعات را نمایش می‌دهد.

برای عدد از int استفاده می‌کنیم.