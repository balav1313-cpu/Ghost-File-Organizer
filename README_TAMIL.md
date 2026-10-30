# 👻 Ghost File Organizer

Hacktoberfest 2026 — “Ghost in the Machine” project starter.

இந்த project உங்கள் Linux கணினியில் உள்ள folder-இல் இருக்கும் files-ஐ வகைப்படுத்த உதவும்.

## உள்ளடக்கம்

- `ghost_organizer.py` — AI இல்லாத எளிய Python version.
- `ghost_ai_organizer.py` — Ollama மூலம் local AI பயன்படுத்தும் version.
- AI version-ல் file உள்ளடக்கத்தைப் படிப்பதில்லை; filename மட்டும் model-க்கு அனுப்பப்படும்.
- கோப்புகளை நகர்த்துவதற்கு முன் உறுதிப்படுத்தல் கேட்கும்.

## 1. Linux-ல் Python சரிபார்க்கவும்

```bash
python3 --version
```

## 2. முதலில் சாதாரண version-ஐச் சோதிக்கவும்

Project folder-இல் terminal திறந்து:

```bash
mkdir -p ~/GhostTest
touch ~/GhostTest/notes.txt
touch ~/GhostTest/photo.jpg
touch ~/GhostTest/song.mp3
python3 ghost_organizer.py
```

Folder path கேட்கும்போது `~/GhostTest` என்று கொடுக்கவும். Files நகர்த்த `yes` என்று type செய்யவும்.

## 3. Local AI அமைக்கவும்

Ollama அதிகாரப்பூர்வ Linux வழிமுறை:
https://docs.ollama.com/linux

Ollama நிறுவிய பிறகு:

```bash
ollama run llama3.2:1b
```

Model download முடிந்ததும் `Ctrl+D` மூலம் Ollama prompt-இலிருந்து வெளியேறலாம். Ollama service இயங்கிக் கொண்டிருக்க வேண்டும்.

பின்னர்:

```bash
python3 ghost_ai_organizer.py
```

AI version வேலை செய்ய Ollama-வில் `llama3.2:1b` model கிடைக்க வேண்டும். Model மாற்ற வேண்டுமெனில் `ghost_ai_organizer.py`-ல் `MODEL` value-ஐ மாற்றவும்.

## பாதுகாப்பு

- முதலில் test folder-ல் மட்டும் சோதிக்கவும்.
- முக்கியமான கோப்புகளை ஒழுங்குபடுத்துவதற்கு முன் backup எடுக்கவும்.
- `YES` என்று உறுதிப்படுத்தினால் மட்டுமே AI version files-ஐ நகர்த்தும்.
- இந்த starter version AI-க்கு filename மட்டும் அனுப்புகிறது; file contents அல்ல.
- Model output தவறாக இருக்கலாம். AI version-ல் நகர்த்துவதற்கு முன் பட்டியலைச் சரிபார்க்கவும்.

## GitHub-க்கு push செய்வது

```bash
git status
git add ghost_organizer.py ghost_ai_organizer.py README_TAMIL.md .gitignore
git commit -m "Add spooky local AI file organizer"
```

உங்கள் branch மற்றும் GitHub permission சரியாக இருப்பதை உறுதிசெய்த பிறகு push செய்யவும்.
