
# 🔐 PDF Auto Encryptor using `pypdf`

This Python script automatically detects PDF files in a given folder, encrypts them with a password, and saves the secured versions without overwriting the originals.

## 🚀 Features

- Automatically finds PDF files in a specified directory
- Encrypts PDF using a user-defined password
- Keeps original file intact
- Lightweight and beginner-friendly
- Based on the `pypdf` library (modern replacement of `PyPDF2`)

## 📁 Folder Structure


📂 your-folder/
├── encrypt\_pdf.py
└── sample.pdf

````

## 🧠 How It Works

1. Scans a folder for `.pdf` files
2. Selects the first (or all PDFs)
3. Encrypts using a password (you can modify the script)
4. Saves it as `originalname_encrypted.pdf`

## 📦 Dependencies

- Python 3.11+
- [pypdf](https://pypdf.readthedocs.io)

Install with:

```bash
pip install pypdf
````

## 📝 Usage

```bash
python encrypt_pdf.py
```

You can modify the `folder` variable to point to your target directory and change the password as needed.

## ✅ Example Output

```bash
Encrypted PDF saved as: test_file_encrypted.pdf
```

---

## 📄 License

MIT License

## 🤝 Contributions

Pull requests are welcome! Feel free to fork this repo and improve it.

`



```
🔐 Just built a small utility that auto-detects PDF files in a folder and encrypts them using Python! 💻

✨ Features:
- Encrypts them with a password (without overwriting originals)
- Lightweight, simple, and built using the modern `pypdf` library (replacing `PyPDF2`)

📦 Use Case: Ideal for anyone who needs to secure documents on the fly — especially useful for academic, healthcare, or legal teams working with sensitive info.




Would love feedback or feature suggestions.

#Python #Automation  #PythonScripts
````
