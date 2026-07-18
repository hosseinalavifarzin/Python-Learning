# Lists (لیست)

---

# مفهوم

List برای نگهداری چند مقدار استفاده می‌شود.

به جای اینکه ده متغیر بسازیم، همه را داخل یک لیست قرار می‌دهیم.

---

# ساخت لیست

```python
users = [
    "Ali",
    "Sara",
    "Reza"
]
```

---

# چاپ لیست

```python
print(users)
```

خروجی

```
['Ali', 'Sara', 'Reza']
```

---

# چاپ اعضا

```python
for user in users:
    print(user)
```

خروجی

```
Ali
Sara
Reza
```

---

# دسترسی به عضو

```python
print(users[0])
```

خروجی

```
Ali
```

---

# اضافه کردن

```python
users.append("Hossein")
```

---

# حذف کردن

```python
users.remove("Ali")
```

---

# تعداد اعضا

```python
len(users)
```

---

# جستجو

```python
if "Ali" in users:
    print("Found")
```

---

# مثال واقعی

```python
new_user = input("Enter user:")

if new_user in users:

    print("Already exists")

else:

    users.append(new_user)
```

---

# حذف

```python
delete_user = input()

if delete_user in users:

    users.remove(delete_user)

else:

    print("Not Found")
```

---

# اشتباه رایجی که انجام دادم

من نوشتم

```python
for user in users:
    print(users)
```

خروجی

```
['Ali','Sara','Reza']

['Ali','Sara','Reza']

['Ali','Sara','Reza']
```

چون کل لیست را چاپ کردم.

---

# روش صحیح

```python
for user in users:
    print(user)
```

---

# append

همیشه عضو را آخر لیست اضافه می‌کند.

---

# remove

اولین عضو پیدا شده را حذف می‌کند.

---

# len

تعداد اعضا را برمی‌گرداند.

---

# in

بررسی می‌کند آیا عضو وجود دارد یا نه.

---

# خلاصه

append

اضافه کردن

remove

حذف کردن

len

تعداد

in

جستجو