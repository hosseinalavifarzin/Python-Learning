# While Loop

---

# مفهوم

While Loop زمانی استفاده می‌شود که تعداد تکرار از قبل مشخص نیست.

برنامه تا زمانی که شرط True باشد، اجرا می‌شود.

وقتی شرط False شود، حلقه متوقف می‌شود.

---

# Syntax

```python
while condition:
    ...
```

---

# مثال

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

خروجی

```
1
2
3
4
5
```

---

# حلقه بی‌نهایت

```python
while True:
    print("Hello")
```

این برنامه هیچ وقت تمام نمی‌شود.

---

# break

برای خارج شدن از حلقه استفاده می‌شود.

```python
while True:
    name = input("Name: ")

    if name == "exit":
        break

    print(name)
```

ورودی

```
Ali
Sara
exit
```

خروجی

```
Ali
Sara
```

بعد برنامه تمام می‌شود.

---

# پروژه User Manager

```python
while True:

    user_choose = input("Choose:")

    if user_choose == "1":
        ...

    elif user_choose == "2":
        ...

    elif user_choose == "6":
        break
```

این دقیقاً همان کاری است که در پروژه انجام دادیم.

---

# اشتباه رایجی که خودم انجام دادم

من این کد را نوشتم:

```python
break
```

اما آن را پایین حلقه قرار دادم.

مثل این:

```python
while True:

    ...

    break
```

نتیجه؟

برنامه بعد از اولین انتخاب بسته می‌شد.

---

# روش صحیح

```python
elif user_choose == "6":
    print("Goodbye!")
    break
```

---

# نکات مهم

✔ اگر از while True استفاده می‌کنی، معمولاً باید یک break هم داشته باشی.

✔ اگر break نداشته باشی، برنامه متوقف نمی‌شود.

✔ اگر شرط هیچ وقت False نشود، حلقه بی‌نهایت اجرا می‌شود.

---

# تفاوت For و While

For

وقتی تعداد تکرار مشخص است.

While

وقتی شرط پایان مشخص است.

---

# خلاصه

while

تا زمانی که شرط برقرار باشد اجرا می‌شود.

break

حلقه را متوقف می‌کند.