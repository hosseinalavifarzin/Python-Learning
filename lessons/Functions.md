# 08-Functions.md

# Functions (توابع)

---

# مفهوم

Function یعنی یک قطعه کد که یک بار نوشته می‌شود و هر زمان که نیاز داشتیم آن را اجرا می‌کنیم.

هدف اصلی Function جلوگیری از تکرار کد است.

به جای اینکه یک کد را چند بار بنویسیم، آن را داخل یک Function قرار می‌دهیم.

---

# چرا Function؟

فرض کن این کد را سه بار نوشته‌ای.

```python
print("\nUsers:")

for user in users:
    print(user)
```

اگر فردا بخواهی ظاهر لیست را تغییر بدهی باید هر سه قسمت را تغییر بدهی.

اما اگر از Function استفاده کنیم فقط یک جا تغییر می‌دهیم.

---

# Syntax

```python
def function_name():
    ...
```

کلمه def یعنی:

دارم یک Function تعریف می‌کنم.

---

# اولین Function

```python
def hello():
    print("Hello")
```

نکته مهم

این کد چیزی چاپ نمی‌کند.

فقط Function ساخته شده است.

---

# اجرای Function

```python
hello()
```

خروجی

```
Hello
```

---

# اجرای چندباره

```python
hello()

hello()

hello()
```

خروجی

```
Hello

Hello

Hello
```

---

# مثال

```python
def welcome():

    print("Welcome")
```

اجرا

```python
welcome()
```

---

# مثال واقعی پروژه

قبل

```python
print("\nUsers:")

for user in users:
    print(user)
```

بعد

```python
def show_users():

    print("\nUsers:")

    for user in users:
        print(user)
```

و هرجا لازم بود

```python
show_users()
```

---

# مزیت

قبلاً

```
نمایش کاربران

↓

۵ خط کد

↓

نمایش کاربران

↓

۵ خط کد

↓

نمایش کاربران

↓

۵ خط کد
```

بعد از Function

```
show_users()

show_users()

show_users()
```

---

# اشتباهی که خودم انجام دادم

من این را نوشتم

```python
show_user
```

ولی اجرا نشد.

چرا؟

چون فقط اسم تابع را نوشتم.

---

# روش صحیح

```python
show_user()
```

وجود () یعنی

Function را اجرا کن.

---

# مثال

غلط

```python
hello
```

درست

```python
hello()
```

---

# چه زمانی Function بسازیم؟

اگر یک تکه کد بیشتر از یک بار تکرار شد.

تقریباً همیشه باید به Function فکر کنیم.

---

# قانون DRY

Don't Repeat Yourself

خودت را تکرار نکن.

این یکی از مهم‌ترین اصول برنامه‌نویسی است.

---

# نکات مهم

✔ ابتدا Function تعریف می‌شود.

✔ بعد اجرا می‌شود.

✔ هر Function فقط یک مسئولیت داشته باشد.

✔ اسم Function باید معنی داشته باشد.

مثلاً

```python
show_users()

delete_user()

search_user()
```

بهتر از

```python
run()

go()

test()
```

---

# سوال مصاحبه

Function چیست؟

پاسخ کوتاه

Function یک قطعه کد قابل استفاده مجدد است که برای جلوگیری از تکرار کد و افزایش خوانایی برنامه استفاده می‌شود.

---

# تمرین

یک Function بنویس

```python
def welcome():
```

که چاپ کند

```
Welcome Hossein
```

---

یک Function دیگر

```python
def bye():
```

که چاپ کند

```
Goodbye
```

و آن را سه بار اجرا کن.

---

# خلاصه

Function

یک بار نوشته می‌شود.

چند بار اجرا می‌شود.

باعث خواناتر شدن کد می‌شود.

باعث حذف کدهای تکراری می‌شود.