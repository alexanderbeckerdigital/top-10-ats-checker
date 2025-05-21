from flask import Flask, request, render_template_string
from scraper import scrape_jobs_from_urls
from config import JOB_URLS, KEYWORDS
from collections import defaultdict
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def check_jobs():
    selected_urls = JOB_URLS
    selected_keywords = KEYWORDS
    results = []

    if request.method == "POST":
        selected_urls = request.form.getlist("urls")
        selected_keywords = request.form.getlist("keywords")
        results = scrape_jobs_from_urls(selected_urls, selected_keywords)

    # Gruppieren nach Quell-URL
    grouped = defaultdict(list)
    for job in results:
        source_url = job.get("source_url", "Unbekannt")
        grouped[source_url].append(job)

    html = """
    <h2>📝 ATS-URL-Checker</h2>
    <form method="POST">
        <p><strong>Welche Seiten sollen geprüft werden?</strong></p>
        {% for url in all_urls %}
            <div>
                <input type="checkbox" name="urls" value="{{ url }}" {% if url in selected_urls %}checked{% endif %}>
                {{ url }}
            </div>
        {% endfor %}

        <p><strong>Nach welchen Begriffen soll gesucht werden?</strong></p>
        {% for keyword in all_keywords %}
            <div>
                <input type="checkbox" name="keywords" value="{{ keyword }}" {% if keyword in selected_keywords %}checked{% endif %}>
                {{ keyword }}
            </div>
        {% endfor %}

        <br>
        <button type="submit">✅ Jetzt prüfen</button>
    </form>

    {% if results %}
        <h3>Gefundene Jobs zu: {{ ', '.join(selected_keywords) }}</h3>
        {% for url, jobs in grouped_results.items() %}
            <h4><a href="{{ url }}" target="_blank">{{ url }}</a></h4>
            <ul>
            {% for job in jobs %}
                <li><a href="{{ job['url'] }}" target="_blank">{{ job['title'] }}</a></li>
            {% endfor %}
            </ul>
        {% endfor %}
    {% elif request.method == 'POST' %}
        <p>🚫 Keine passenden Jobs gefunden.</p>
    {% endif %}
    """
    return render_template_string(html,
        all_urls=JOB_URLS,
        selected_urls=selected_urls,
        all_keywords=KEYWORDS,
        selected_keywords=selected_keywords,
        results=results,
        grouped_results=grouped
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
