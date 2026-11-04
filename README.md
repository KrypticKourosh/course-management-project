<!-- <div dir="rtl"> -->

# مدل‌های پروژه مدیریت دوره‌های آموزشی

## اپ `accounts`

### User (ارث‌بری از AbstractUser)

| فیلد | نوع | توضیح |
|---|---|---|
| username, password, email, first_name, last_name | پیش‌فرض Django | |
| role | CharField (choices) | `student` (دانشجو) / `instructor` (مدرس) |
| phone | CharField | اختیاری |

## اپ `courses`

### Category

| فیلد | نوع | توضیح |
|---|---|---|
| name | CharField | یکتا |

### Course

| فیلد | نوع | توضیح |
|---|---|---|
| title | CharField | عنوان دوره |
| description | TextField | توضیحات |
| category | ForeignKey → Category | `SET_NULL`، اختیاری |
| instructor | ForeignKey → User | مدرس دوره |
| capacity | PositiveIntegerField | ظرفیت |
| start_date | DateField | شروع دوره |
| end_date | DateField | پایان دوره |
| price | DecimalField | هزینه |
| created_at | DateTimeField | خودکار |

### Session

| فیلد | نوع | توضیح |
|---|---|---|
| course | ForeignKey → Course | `CASCADE` |
| title | CharField | عنوان جلسه |
| date | DateField | تاریخ |
| start_time | TimeField | ساعت شروع |
| end_time | TimeField | ساعت پایان |

## اپ `enrollments`

### Enrollment

| فیلد | نوع | توضیح |
|---|---|---|
| student | ForeignKey → User | دانشجو |
| course | ForeignKey → Course | دوره |
| enrolled_at | DateTimeField | خودکار |
| grade | DecimalField | نمره، اختیاری |
| evaluation | TextField | ارزیابی، اختیاری |

قید یکتایی: `(student, course)` (جلوگیری از ثبت‌نام تکراری)

## روابط بین مدل‌ها

- یک **مدرس** (User) ← چند **دوره** (یک‌به‌چند)
- یک **دسته‌بندی** (Category) ← چند **دوره** (یک‌به‌چند)
- یک **دوره** ← چند **جلسه** (یک‌به‌چند)
- **دانشجو** و **دوره**: چند‌به‌چند از طریق **Enrollment**

</div>
