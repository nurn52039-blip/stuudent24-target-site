STUUDENT24 DEPLOY VERSION

Бұл версия интернетке шығару үшін дайындалды.

Файлдар:
- app.py
- requirements.txt
- Procfile
- templates/
- static/

Local компьютерде қосу:
1) py -m pip install -r requirements.txt
2) py app.py
3) Браузер: http://127.0.0.1:5000

Render.com арқылы интернетке шығару:
1) GitHub-та жаңа repository аш.
2) Осы папкадағы файлдарды GitHub repository-ге upload жаса.
3) Render.com сайтына кір.
4) New + -> Web Service таңда.
5) GitHub repository-ді таңда.
6) Build Command:
   pip install -r requirements.txt
7) Start Command:
   gunicorn app:app
8) Deploy бас.
9) Render берген link-ті Instagram рекламаға қоясың.

Ескерту:
- Free Render-де leads.csv тұрақты сақталмауы мүмкін.
- Негізгі мақсат: клиент WhatsApp-қа дайын хабарламамен өтуі.
- Тұрақты база керек болса, кейін Google Sheets немесе PostgreSQL қосамыз.
