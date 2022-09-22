# **SRI API.**

## 📘 **Documentación.**

### **1. Formato del archivo .env**

---

"Cree un archivo .env en la raíz del proyecto con nombre .env y añada lo siguiente.

```.env

# localhost server
DEV_SERVER_NAME=""

# production server
SERVER_NAME=""

TIMEOUT=

# url for scraping
SCRAP_URL=""

# endpoints
SECRET_KEY=
```

**Note:** DEV_SERVER_NAME and DEV_SERVER_NAME use this format `0.0.0.0:Port`

You can use this command to generate SECRET_KEY.

```python
python -c 'import secrets; print(secrets.token_hex())'
```
