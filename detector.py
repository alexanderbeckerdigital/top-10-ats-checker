import json
import hashlib
import os

DB_FILE = "job_db.json"

def load_known_jobs():
    if not os.path.exists(DB_FILE):
        return set()
    with open(DB_FILE, "r") as f:
        data = json.load(f)
    return set(data)

def save_known_jobs(job_hashes):
    with open(DB_FILE, "w") as f:
        json.dump(list(job_hashes), f)

def hash_job(job):
    # Einfacher Hash aus Titel + URL
    job_id = job["title"] + job["url"]
    return hashlib.sha256(job_id.encode("utf-8")).hexdigest()

def detect_new_jobs(jobs):
    known = load_known_jobs()
    new_jobs = []
    updated_known = set(known)
    for job in jobs:
        job_hash = hash_job(job)
        if job_hash not in known:
            new_jobs.append(job)
            updated_known.add(job_hash)
    save_known_jobs(updated_known)
    return new_jobs

