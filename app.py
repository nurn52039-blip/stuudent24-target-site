from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import csv
import os
from urllib.parse import quote_plus

app = Flask(__name__)

LEADS_FILE = "leads.csv"

SERVICES = [
    "Курстық жұмыс",
    "Дипломдық жұмыс",
    "Диссертация",
    "Практика есебі",
    "СӨЖ / реферат",
    "Презентация",
    "Антиплагиат",
    "Word оформление"
]

def ensure_csv():
    if not os.path.exists(LEADS_FILE):
        with open(LEADS_FILE, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date_time",
                "name",
                "phone",
                "service",
                "language",
                "deadline",
                "topic",
                "comment"
            ])

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", services=SERVICES)

@app.route("/send", methods=["POST"])
def send():
    ensure_csv()

    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    service = request.form.get("service", "").strip()
    language = request.form.get("language", "").strip()
    deadline = request.form.get("deadline", "").strip()
    topic = request.form.get("topic", "").strip()
    comment = request.form.get("comment", "").strip()

    with open(LEADS_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            name,
            phone,
            service,
            language,
            deadline,
            topic,
            comment
        ])

    whatsapp_number = "77783674384"  # Өз WhatsApp нөмірің. Мысалы: 77783674384

    message = f"""Сәлеметсіз бе! Мен @stuudent24 арқылы тапсырыс қалдырғым келеді.

Атым: {name}
Телефон: {phone}
Қызмет түрі: {service}
Тілі: {language}
Қорғау/тапсыру күні: {deadline}
Тақырыбы: {topic}
Қосымша: {comment}

10% жеңілдік бойынша ақпарат беріңізші."""

    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={quote_plus(message)}"

    return render_template(
        "thanks.html",
        name=name,
        whatsapp_url=whatsapp_url
    )

@app.route("/leads", methods=["GET"])
def leads():
    ensure_csv()
    rows = []
    with open(LEADS_FILE, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    rows.reverse()
    return render_template("leads.html", rows=rows)

if __name__ == "__main__":
    ensure_csv()
    app.run(debug=True)
