​Writeup: Allsafe Ransomware Incident Response
​Overview
​This room simulates a realistic incident response scenario where the Allsafe corporate network and web servers were compromised through web application vulnerabilities, leading to a ransomware attack. Analysts are required to investigate web access logs, trace initial compromise vectors, analyze file artifacts, and examine network packet captures to solve the case.
​Task-by-Task Walkthrough
​Task 1: Allsafe Emergency Briefing
​Objective: Understand the incident briefing and review the scenario background.
​Solution: Read through the emergency briefing to understand the scope and objectives of the investigation.
​Task 2: Web Log Analysis & Breach Detection
​Objective: Analyze the web server's access.log to trace the attacker's steps.
​Key Findings:
​The attacker performed directory enumeration and accessed administrative login endpoints (/admin/login.php).
​A file upload vulnerability was exploited via /admin/upload.php.
​The attacker successfully uploaded and executed a web shell named shell.php.
​Answers:
​Attacker IP: Extract from the log entries (e.g., matching the suspicious scanning activity).
​Malicious File: shell.php
​Task 3: Ransomware Artifacts & File Analysis
​Objective: Investigate the ransomware infection artifacts left on the system.
​Solution: Examine the provided file artifacts and system indicators to identify the ransomware variant, extension, and malicious behavior.
​Task 4: Investigating Network Traffic & Packet Streams
​Objective: Analyze the network_traffic.pcap file stream to uncover reconnaissance steps and exfiltrated data.
​Key Findings:
​Initial reconnaissance via robots.txt leaked the /secret_backup_2026/ directory.
​An archived confidential file (confidential_keys.zip) was downloaded from the hidden directory.
​A custom user-agent string (AllsafeScanner/2.4-beta) was utilized by the attacker's scanner