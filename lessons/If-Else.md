# If / Elif / Else

---

# مفهوم

گاهی برنامه باید تصمیم بگیرد.

اگر شرط برقرار بود، یک کار انجام دهد.

اگر برقرار نبود، کار دیگری انجام دهد.

---

# ساختار

```python
if condition:
    ...

elif condition:
    ...

else:
    ...
```

---

# مثال

```python
age = 20

if age >= 18:
    print("Allowed")
else:
    print("Not Allowed")
```

---

خروجی

```
Allowed
```

---

# مثال دوم

```python
number = 10

if number > 0:
    print("Positive")

elif number == 0:
    print("Zero")

else:
    print("Negative")
```

---

# عملگرها

بزرگتر

```python
>
```

کوچکتر

```python
<
```

برابر

```python
==
```

نابرابر

```python
!=
```

بزرگتر مساوی

```python
>=
```

کوچکتر مساوی

```python
<=
```

---

# اشتباه رایج

غلط

```python
if age = 18:
```

درست

```python
if age == 18:
```

---

# اشتباه رایج دوم

غلط

```python
if user == "1" or "new_user":
```

این همیشه True می‌شود.

درست

```python
if user == "1" or user == "new_user":
```

یا بهتر

```python
if user in ["1", "new_user"]:
```

---

# خلاصه

if

اگر

elif

وگرنه اگر

else

در غیر این صورت