# Laboratorna robota 2

Tema: tekhnolohii konteineryzatsii Python-dodatkiv, osnovy roboty z Docker.

Student: Holub O. A.

## Sklad proiektu

- `lab2.py` - prohrama perekladu z funktsiiamy `TransLate`, `LangDetect`, `CodeLang`.
- `requirements.txt` - zalezhnist `googletrans==3.1.0a0`.
- `Dockerfile` - konteiner na bazi Linux z Python 3.11.
- `.gitignore` - tekhnichni papky ta faily, yaki ne treba dodavaty v GitHub.

## Lokalnyi zapusk

```powershell
py -3.11 -m venv Holub
.\Holub\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python lab2.py
```

## Zapusk u Docker

```powershell
docker build -t holub_lab2 .
docker run -it --name HolubOA holub_lab2
```

Perevirka struktury konteinera:

```powershell
docker run --rm holub_lab2 pwd
```

Ochikuvanyi shliakh:

```text
/Holub
```

## Pryklad roboty funktsii

```python
txt = "Dobroho dnia. Yak spravy?"
lang = "en"
print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang("En"))
print(CodeLang("English"))
```

## GitHub

```powershell
git init
git add .
git commit -m "Add lab2 Docker Python translator"
git branch -M main
git remote add origin <repository-url>
git push -u origin main
```
