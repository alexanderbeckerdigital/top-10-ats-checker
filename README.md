# 🕵️‍♂️ Top 10 ATS Checker

Ein kleines, praxisorientiertes Python-Tool, das regelmäßig ausgewählte Jobseiten auf neue Einträge mit bestimmten Keywords wie "DevOps", "SRE", etc. scannt – und dir nur dann eine E-Mail schickt, wenn neue relevante Jobs auftauchen.

Dieses Projekt soll langfristig auf Google Cloud Run betrieben und später auf Kubernetes migriert werden. Der Fokus liegt auf operativer Nützlichkeit für tägliche Nutzung.

---

## 🚀 Features

- ✅ Regelmäßiges Scannen von bis zu 10 Jobseiten (HTML, JSON, RSS)
- ✅ Keyword-Detection (konfigurierbar)
- ✅ Deduplikation über Firestore (nur neue Treffer werden gemeldet)
- ✅ Benachrichtigung via E-Mail (SMTP)
- ✅ Bereit für Cloud Run & Containerisierung
- 🛠 Lokal entwickelbar mit Flask

---

## 📦 Setup (Lokal)

1. **Clone das Repo**

```bash
git clone https://github.com/alexanderbeckerdigital/top-10-ats-checker.git
cd top-10-ats-checker

# Trigger redeploy
