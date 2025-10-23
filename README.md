# UTS

Dokumentasi ini menjelaskan langkah-langkah membuat lingkungan kerja (virtual environment) menggunakan **[uv](https://github.com/astral-sh/uv)**, lalu memasang **Jupyter** dan **Streamlit** untuk pengembangan data science.

---

install lewat curl

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

atau

pip

```bash
pip install uv
```

untuk membuat venv nya

```sh
uv venv [option] [path]
```

setalah itu untuk install jupiter lab menggunakan uv

```bash
 uv run --with jupyter jupyter lab
```

jika kalian tidak pernah install jupiter lab ini akan meninstall package yang di butuhkan oleh jupiter

untuk menjalankan nya tinggal perintah

```bash
jupiter lab
```
