# Data Types (انواع داده)

---

# مفهوم

هر اطلاعاتی که در برنامه ذخیره می‌کنیم، یک نوع (Type) دارد.

پایتون باید بداند که با آن اطلاعات چگونه رفتار کند.

مثلاً:

25 یک عدد است.

"Hossein" یک متن است.

True یک مقدار منطقی است.

---

# انواع مهم

| Type | مثال |
|------|------|
| int | 10 |
| float | 3.14 |
| str | "Hello" |
| bool | True / False |

---

# Integer

عدد صحیح

```python
age = 25
```

---

# Float

عدد اعشاری

```python
price = 12.5
```

---

# String

متن

```python
name = "Hossein"
```

---

# Boolean

درست یا غلط

```python
is_admin = True

is_login = False
```

---

# فهمیدن نوع متغیر

```python
name = "Ali"

print(type(name))
```

خروجی

```
<class 'str'>
```

---

# تبدیل نوع

```python
age = "25"

age = int(age)
```

---

```python
number = 10

text = str(number)
```

---

# اشتباه رایج

```python
age = input()

print(age + 5)
```

خطا

چون input همیشه String برمی‌گرداند.

باید بنویسیم

```python
age = int(input())
```

---

# خلاصه

int

اعداد صحیح

float

اعداد اعشاری

str

متن

bool

True یا False