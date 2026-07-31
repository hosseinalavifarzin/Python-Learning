درسته، این همون چیزیه که تا الان **فقط با هم یاد گرفتیم**، بدون اضافه کردن هیچ مبحث جدید.

---

# کلاس (Class)

کلاس یک **قالب (Template)** یا **نقشه (Blueprint)** برای ساختن شیء (Object) است.

خود کلاس چیزی نیست که از آن استفاده کنیم؛ بلکه از روی آن شیء می‌سازیم.

مثال:

```python
class User:
    pass
```

---

# Object (شیء)

وقتی از روی یک کلاس نمونه می‌سازیم، یک Object ایجاد می‌شود.

```python
user1 = User()
user2 = User()
```

در اینجا:

* `user1` یک Object است.
* `user2` هم یک Object دیگر است.
* هر دو از کلاس `User` ساخته شده‌اند.

---

# تفاوت Class و Object

```python
class User:
    pass
```

این فقط نقشه است.

اما:

```python
user1 = User()
```

یک شیء واقعی است.

اگر بخواهیم مثال دنیای واقعی بزنیم:

```
Class  → نقشه ساخت خانه

Object → خانه‌ای که ساخته شده است.
```

---

# Attribute

Attribute یعنی ویژگی‌های هر Object.

مثال:

```python
class User:
    def __init__(self, name):
        self.name = name
```

اینجا:

```python
self.name
```

یک Attribute است.

بعداً می‌توانیم بنویسیم:

```python
print(user1.name)
```

---

# Method

Method یعنی تابعی که داخل کلاس قرار گرفته است.

مثال:

```python
class User:

    def hello(self):
        print("Hello")
```

`hello` یک Method است.

---

# Function و Method

Function:

```python
def hello():
    print("Hello")
```

به این صورت اجرا می‌شود:

```python
hello()
```

---

Method:

```python
class User:

    def hello(self):
        print("Hello")
```

به این صورت اجرا می‌شود:

```python
user1.hello()
```

---

# self

`self` به همان Objectی اشاره می‌کند که متد روی آن اجرا شده است.

مثال:

```python
user1.hello()
```

در این حالت:

```
self → user1
```

اگر بنویسیم:

```python
user2.hello()
```

در این حالت:

```
self → user2
```

پس `self` همیشه به Object فعلی اشاره می‌کند.

---

# **init**

تابعی است که هنگام ساختن Object به صورت خودکار اجرا می‌شود.

مثال:

```python
class User:

    def __init__(self, name):
        self.name = name
```

وقتی بنویسیم:

```python
user1 = User("Hossein")
```

پایتون به صورت خودکار `__init__` را اجرا می‌کند و مقدار `"Hossein"` را داخل `self.name` قرار می‌دهد.

---

# ساخت Object

```python
user1 = User("Hossein")
```

* `User` کلاس است.
* `user1` Object است.
* `"Hossein"` به `__init__` ارسال می‌شود.

---

# دسترسی به Attribute

```python
print(user1.name)
```

خروجی:

```text
Hossein
```

---

# صدا زدن Method

```python
user1.hello()
```

پرانتز `()` یعنی متد را اجرا کن.

اگر بنویسیم:

```python
user1.hello
```

هیچ اتفاقی نمی‌افتد، چون فقط به خود متد اشاره کرده‌ایم و آن را اجرا نکرده‌ایم.

---

# تفاوت `()` و `[]`

### `()`

برای اجرا کردن تابع یا متد استفاده می‌شود.

```python
hello()

user1.hello()

User("Hossein")
```

---

### `[]`

برای دسترسی به عناصر List یا Dictionary استفاده می‌شود.

List:

```python
users[0]
```

Dictionary:

```python
user["name"]
```

---

# تفاوت `.` و `[]`

نقطه (`.`) برای دسترسی به Attribute یا Method یک Object:

```python
user1.name

user1.hello()
```

براکت (`[]`) برای دسترسی به داده‌های List یا Dictionary:

```python
users[0]

user["name"]
```

---

# چیزی که در پروژه یاد گرفتیم

ما هنوز از OOP در پروژه User Manager استفاده نکرده‌ایم، اما این مفاهیم را تمرین کردیم:

* Class
* Object
* Method
* Attribute
* `self`
* `__init__`
* ساخت Object
* صدا زدن Method
* تفاوت Function و Method
* تفاوت `.` و `[]`
* تفاوت `()` و `[]`

این دقیقاً تمام مباحثی است که تا اینجا درباره کلاس و آبجکت با هم یاد گرفته‌ایم، بدون اضافه کردن موضوع جدید یا جلو رفتن به مباحثی مثل Inheritance، Encapsulation یا Polymorphism.
