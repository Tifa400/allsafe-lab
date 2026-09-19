# Allsafe Ransomware Simulation Artifact
# Target Extension: .allsafe
# Contact: decrypt_help@proton.me
# Note: Executed via scheduled task (CRON) on /var/www/html/uploads/

ENCRYPTED_EXTENSION = ".allsafe"
TARGET_DIRECTORY = "/var/www/html/uploads/"
CONTACT_EMAIL = "decrypt_help@proton.me"

def log_incident():
    print("[!] Encryption routine triggered.")
    print(f"[!] Target files modified with extension: {ENCRYPTED_EXTENSION}")

if __name__ == "__main__":
    log_incident()