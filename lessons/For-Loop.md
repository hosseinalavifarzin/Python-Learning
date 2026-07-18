# For Loop

---

# مفهوم

وقتی بخواهیم کاری را چند بار انجام دهیم از Loop استفاده می‌کنیم.

اگر تعداد تکرار مشخص باشد، معمولاً از For استفاده می‌کنیم.

---

# مثال

```python
for i in range(5):
    print(i)
```

خروجی

```
0
1
2
3
4
```

---

# range()

```python
range(start, stop)
```

مثال

```python
range(1,6)
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

سه پارامتر

```python
range(start, stop, step)
```

مثال

```python
range(2,11,2)
```

خروجی

```
2
4
6
8
10
```

---

# شمارش معکوس

```python
for i in range(5,0,-1):
    print(i)
```

خروجی

```
5
4
3
2
1
```

---

# چاپ ستاره

```python
for i in range(1,6):
    print("*"*i)
```

خروجی

```
*
**
***
****
*****
```

---

# پیمایش لیست

```python
users = ["Ali","Sara","Reza"]

for user in users:
    print(user)
```

---

# enumerate

اگر شماره هم بخواهیم

```python
for index,user in enumerate(users,start=1):
    print(index,user)
```

خروجی

```
1 Ali

2 Sara

3 Reza
```

---

# اشتباه رایج

غلط

```python
print(users)
```

اگر بخواهیم اعضا جداگانه چاپ شوند.

درست

```python
for user in users:
    print(user)
```

---

# خلاصه

For برای زمانی است که تعداد تکرار مشخص است.
