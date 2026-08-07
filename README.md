# 🤖 Enterprise RAG Chatbot

An advanced, beginner-friendly **Retrieval-Augmented Generation (RAG)** chatbot supporting PDF documents, powered by **LlamaIndex**, **Gradio**, and custom **OpenAI-compatible API Endpoints** (`gpt-4o` & `text-embedding-3-large`).

---

# 📚 فهرست مطالب | Table of Contents

- [🇮🇷 راهنمای کامل فارسی (برای افراد مبتدی)](#-راهنمای-کامل-فارسی-برای-افراد-مبتدی)
  - [۱. معرفی پروژه](#۱-معرفی-پروژه)
  - [۲. راهنمای گام‌به‌گام اجرا در Kaggle](#۲-راهنمای-گامبهگام-اجرا-در-kaggle)
  - [۳. راهنمای گام‌به‌گام نصب روی سیستم شخصی (ویندوز / مک / لینوکس)](#۳-راهنمای-گامبهگام-نصب-روی-سیستم-شخصی-ویندوز--مک--لینوکس)
  - [۴. راهنمای اجرا در محیط VS Code یا Google Antigravity](#۴-راهنمای-اجرا-در-محیط-vs-code-یا-google-antigravity)
  - [۵. راهنمای اجرا با داکر (Docker)](#۵-راهنمای-اجرا-با-داکر-docker)
  - [۶. نحوه کار با محیط چت‌بات](#۶-نحوه-کار-با-محیط-چتبات)
- [🇬🇧 Complete English Guide (Step-by-Step)](#-complete-english-guide-step-by-step)
  - [1. Overview](#1-overview)
  - [2. Step-by-Step Kaggle Deployment](#2-step-by-step-kaggle-deployment)
  - [3. Local System Setup Guide](#3-local-system-setup-guide)
  - [4. Running in VS Code & Google Antigravity IDE](#4-running-in-vs-code--google-antigravity-ide)
  - [5. Docker Setup Guide](#5-docker-setup-guide)
  - [6. How to Use the Chatbot UI](#6-how-to-use-the-chatbot-ui)

---

# 🇮🇷 راهنمای کامل فارسی (برای افراد مبتدی)

این راهنما طوری نوشته شده است که حتی اگر هیچ تجربه قبلی در برنامه‌نویسی ندارید، بتوانید به راحتی این چت‌بات را اجرا کنید!

---

## ۱. معرفی پروژه

این چت‌بات به شما اجازه می‌دهد فایلهای PDF خود (مثل کتاب، جزوه، مقاله یا قرارداد) را آپلود کنید و با هوش مصنوعی درباره محتوای آن‌ها گفتگو کنید.

### 🔑 ویژگی‌های اصلی:
- **مدل هوش مصنوعی چت**: `gpt-4o`
- **مدل تبدیل متن به بردار (Embedding)**: `text-embedding-3-large`
- **پشتیبانی از سرویس‌دهنده‌های OpenAI و GapGPT**: با آدرس `https://api.gapgpt.app/v1`
- **رابط کاربری ساده و فارسی/انگلیسی**

---

## ۲. راهنمای گام‌به‌گام اجرا در Kaggle (بدون نیاز به سیستم قوی)

اگر سیستم یا کارت گرافیک قوی ندارید، می‌توانید این برنامه را کاملاً رایگان روی سرورهای ابری Kaggle اجرا کنید.

### گام ۱: ساخت حساب در Kaggle
1. به سایت [Kaggle.com](https://www.kaggle.com) بروید.
2. یک حساب کاربری رایگان بسازید یا با اکانت گوگل خود وارد شوید.

### گام ۲: ایجاد یک نوت‌بوک جدید (New Notebook)
1. از منوی سمت چپ روی دکمه **Create** و سپس **New Notebook** کلیک کنید.
2. از پنل سمت راست (منوی Notebook options):
   - گزینه **Internet** را پیدا کرده و آن را روی **Internet On** قرار دهید (این مرحله بسیار مهم است تا نوت‌بوک به اینترنت دسترسی داشته باشد).

### گام ۳: آپلود نوت‌بوک پروژه
1. فایل `notebooks/kaggle.ipynb` موجود در این پروژه را دانلود کنید.
2. در صفحه Kaggle، از منوی بالا روی **File** ◄ **Import Notebook** کلیک کرده و فایل `kaggle.ipynb` را آپلود کنید.

### گام ۴: دریافت توکن Ngrok (برای مشاهده محیط گرافیکی برنامه)
1. به سایت رایگان [Ngrok.com](https://ngrok.com) بروید و یک اکانت بسازید.
2. از پنل Ngrok به بخش **Your Authtoken** بروید و کد توکن اختصاصی خود را کپی کنید.

### گام ۵: اجرای کدهای نوت‌بوک
در نوت‌بوک Kaggle کدهای زیر قرار دارند:

1. **دستور دانلود پروژه**:
   ```bash
   !git clone https://github.com/your-username/rag-chatbot.git
   %cd rag-chatbot
   ```
2. **دستور نصب پیش‌نیازها**:
   ```bash
   !pip install -r pyproject.toml
   ```
3. **تنظیم فایل تنظیمات (.env)**:
   یک سلول کد جدید بسازید و کد زیر را اجرا کنید:
   ```python
   with open(".env", "w") as f:
       f.write("OPENAI_API_BASE=https://api.gapgpt.app/v1\n")
       f.write("OPENAI_API_KEY=YOUR_OPENAI_API_KEY\n")
   ```
4. **تنظیم توکن Ngrok**:
   عبارت `<YOUR_NGROK_TOKEN>` را با توکنی که از سایت Ngrok کپی کرده‌اید جایگزین کرده و سلول را اجرا کنید:
   ```bash
   !ngrok config add-authtoken کد_توکن_شما
   ```
5. **اجرای چت‌بات**:
   ```bash
   !python -m rag_chatbot --host localhost
   ```

پس از چند ثانیه، یک لینک مانند `https://xxxx.ngrok-free.app` در خروجی ظاهر می‌شود. روی آن کلیک کنید تا وارد محیط چت‌بات شوید!

---

## ۳. راهنمای گام‌به‌گام نصب روی سیستم شخصی (ویندوز / مک / لینوکس)

### پیش‌نیازها:
- پایتون (نسخه 3.11 یا بالاتر). می‌توانید از سایت [python.org](https://www.python.org/downloads/) دانلود کنید.
- نرم‌افزار Git (از سایت [git-scm.com](https://git-scm.com/)).

### گام ۱: دانلود پروژه (Clone)
کلیدهای `Win + R` را بزنید، `cmd` را تایپ کنید و Enter بزنید. سپس دستورات زیر را وارد کنید:

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### گام ۲: ساخت فایل تنظیمات (.env)
یک فایل متنی جدید به نام `.env` در پوشه اصلی پروژه بسازید و خطوط زیر را درون آن قرار دهید:

```env
OPENAI_API_BASE=https://api.gapgpt.app/v1
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

### گام ۳: نصب کتابخانه‌ها
دستور زیر را اجرا کنید تا تمام کتابخانه‌های مورد نیاز نصب شوند:

```bash
pip install -r pyproject.toml
```

یا اگر از `uv` استفاده می‌کنید:

```bash
uv sync
```

---

## ۴. راهنمای اجرا در محیط VS Code یا Google Antigravity

این پروژه کاملاً با **VS Code** و **Google Antigravity IDE** سازگار است. شما به دو روش می‌توانید آن را اجرا کنید:

### روش ۱: استفاده از ترمینال داخلی VS Code / Antigravity (پیشنهادی)
1. محیط **VS Code** یا **Antigravity IDE** را باز کنید.
2. پوشه پروژه را باز کنید (`File ◄ Open Folder`).
3. ترمینال را باز کنید: کلیدهای ترکیب `Ctrl + ~` (یا `Ctrl + Shift + ~`) را فشار دهید.
4. در صورت استفاده از محیط مجازی (Virtual Environment)، آن را فعال کنید:
   - **ویندوز**: `.\.venv\Scripts\Activate.ps1`
   - **مک / لینوکس**: `source .venv/bin/activate`
5. دستور زیر را برای اجرای چت‌بات وارد کنید:
   ```bash
   python -m rag_chatbot --host localhost
   ```
6. آدرس **`http://localhost:7860`** را در مرورگر باز کنید.

### روش ۲: اجرای مستقیم با کلید F5 (Run & Debug)
پروژه شامل فایل پیکربندی اختصاصی `.vscode/launch.json` است:
1. پروژه را در VS Code یا Antigravity باز کنید.
2. کلید **`F5`** را روی کیبورد فشار دهید (یا از منوی سمت چپ به بخش **Run & Debug** رفته و روی دکمه سبز رنگ **Run RAG Chatbot** کلیک کنید).
3. برنامه به طور خودکار اجرا شده و لینک آدرس وب در ترمینال نمایش داده می‌شود.

---

## ۵. راهنمای اجرا با داکر (Docker)

اگر نرم‌افزار Docker Desktop روی سیستم شما نصب است، تنها با یک دستور می‌توانید پروژه را اجرا کنید!

1. مطمئن شوید نرم‌افزار **Docker Desktop** روشن است.
2. فایل `.env` را طبق توضیحات بالا ایجاد کنید.
3. در مسیر پروژه، دستور زیر را اجرا کنید:

```bash
docker compose up --build
```

4. مرورگر خود را باز کرده و به آدرس **`http://localhost:7860`** بروید.

---

## ۶. نحوه کار با محیط چت‌بات

1. **انتخاب مدل (Choose Model)**: مدل `gpt-4o` را انتخاب کنید.
2. **انتخاب زبان (Language)**: زبان `eng` یا `vi` را تعیین کنید.
3. **آپلود فایل‌ها (Add Documents)**: فایلهای PDF خود را بکشید و در کادر مشخص‌شده رها کنید (یا روی Upload کلیک کنید).
4. **پرسش و پاسخ**: سوال خود را در کادر متنی پایین بنویسید و ارسال کنید. هوش مصنوعی بر اساس محتوای فایلهای PDF شما پاسخ خواهد داد!

---
---

# 🇬🇧 Complete English Guide (Step-by-Step)

This guide provides absolute beginners with clear, step-by-step instructions to get the RAG Chatbot running on Kaggle, a local computer, VS Code / Antigravity IDE, or Docker.

---

## 1. Overview

This RAG Chatbot empowers you to upload PDF documents and ask questions about their content in natural language.

- **LLM Engine**: `gpt-4o`
- **Embedding Engine**: `text-embedding-3-large`
- **API Base URL**: `https://api.gapgpt.app/v1`
- **UI Framework**: Gradio

---

## 2. Step-by-Step Kaggle Deployment

Run the chatbot in the cloud using Kaggle's free computing environment.

### Step 1: Create a Kaggle Account
1. Visit [Kaggle.com](https://www.kaggle.com).
2. Sign up for a free account.

### Step 2: Create a New Notebook & Enable Internet
1. Click **Create** ◄ **New Notebook**.
2. On the right-hand panel under **Notebook options**, toggle **Internet** to **Internet On**.

### Step 3: Import the Notebook
1. Download [`notebooks/kaggle.ipynb`](notebooks/kaggle.ipynb) from this repository.
2. In Kaggle, click **File** ◄ **Import Notebook** and upload `kaggle.ipynb`.

### Step 4: Obtain an Ngrok Authtoken
1. Create a free account at [Ngrok.com](https://ngrok.com).
2. Copy your authtoken from the **Your Authtoken** section.

### Step 5: Execute Notebook Cells
1. **Clone the repository**:
   ```bash
   !git clone https://github.com/your-username/rag-chatbot.git
   %cd rag-chatbot
   ```
2. **Install dependencies**:
   ```bash
   !pip install -r pyproject.toml
   ```
3. **Create environment file (`.env`)**:
   ```python
   with open(".env", "w") as f:
       f.write("OPENAI_API_BASE=https://api.gapgpt.app/v1\n")
       f.write("OPENAI_API_KEY=YOUR_OPENAI_API_KEY\n")
   ```
4. **Configure Ngrok token**:
   Replace `<YOUR_NGROK_TOKEN>` with your actual token:
   ```bash
   !ngrok config add-authtoken YOUR_ACTUAL_TOKEN
   ```
5. **Start the server**:
   ```bash
   !python -m rag_chatbot --host localhost
   ```

Click the generated `https://xxxx.ngrok-free.app` URL to open the Web UI!

---

## 3. Local System Setup Guide

### Prerequisites
- Python `3.11` or higher ([python.org](https://www.python.org))
- Git ([git-scm.com](https://git-scm.com))

### Step 1: Clone Repository
Open terminal / command prompt and run:

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### Step 2: Configure Environment Variables
Create a file named `.env` in the root folder with the following contents:

```env
OPENAI_API_BASE=https://api.gapgpt.app/v1
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

### Step 3: Install Required Packages

```bash
pip install -r pyproject.toml
```

Or using `uv`:

```bash
uv sync
```

---

## 4. Running in VS Code & Google Antigravity IDE

This repository is fully optimized for **Visual Studio Code** and **Google Antigravity IDE**.

### Option A: Via Integrated Terminal (Recommended)
1. Open the project folder in VS Code or Antigravity IDE (`File ◄ Open Folder`).
2. Open the integrated terminal (`Ctrl + ~`).
3. Activate your virtual environment if applicable:
   - **Windows**: `.\.venv\Scripts\Activate.ps1`
   - **Mac / Linux**: `source .venv/bin/activate`
4. Launch the application:
   ```bash
   python -m rag_chatbot --host localhost
   ```
5. Open your browser at **`http://localhost:7860`**.

### Option B: One-Click Launch via F5 Key (Run & Debug)
The repository includes pre-configured `.vscode/launch.json`:
1. Press **`F5`** on your keyboard (or click **Run & Debug** ◄ **Run RAG Chatbot**).
2. The application will start automatically in the integrated debugger terminal.

---

## 5. Docker Setup Guide

If you have Docker Desktop installed:

1. Ensure Docker Desktop is running.
2. Create the `.env` file as shown above.
3. Build and launch containers:

```bash
docker compose up --build
```

4. Access the web interface at **`http://localhost:7860`**.

---

## 6. How to Use the Chatbot UI

1. **Select Model**: Choose `gpt-4o` from the model dropdown.
2. **Upload Documents**: Drag and drop your PDF files into the file upload box.
3. **Ask Questions**: Type your prompt in the chat box and press enter to receive responses based on your uploaded documents.

---

## 📜 License

Distributed under the MIT License.
