# Dictionary Methods

---

keys()

نمایش تمام کلیدها

```python
user.keys()
```

---

values()

نمایش تمام مقادیر

```python
user.values()
```

---

items()

نمایش کلید و مقدار

```python
for key, value in user.items():
    print(key, value)
```

---

get()

دریافت مقدار

```python
user.get("name")
```

مزیت:

اگر کلید وجود نداشته باشد خطا نمی‌دهد.

---

update()

ویرایش دیکشنری

```python
user.update({
    "age":30
})
```

---

pop()

حذف یک کلید

```python
user.pop("age")
```