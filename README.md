# Multi-Stage XSS Attack Simulation 🔒

## TL;DR
1. Clone repo
2. Run locally in an isolated VM or Docker
3. Do not attack public sites — lab only

**Authors:** Sneha Chiliveru @snehachiliveru
             Srikota Shashank @srikotashashank
**Author:** Sneha Chiliveru  
**Course:** Cyber Security | Major Project  
**Date:** 10 Oct 2025

## 🧠 Overview
This project demonstrates **Reflected**, **Stored**, and **DOM-based XSS** attacks in a **safe, isolated lab** environment using DVWA on VMware.

All payloads are **benign** (no real data exfiltration).  
Includes **logging, forensics, and layered mitigations** such as:
- Output encoding
- Content Security Policy (CSP)
- Cookie hardening

## ⚙️ Setup
1. Create 3 VMs (DVWA, Attacker, Logger).
2. Configure **host-only network**.
3. Run `safe_logger.py` on VM3.
4. Deploy DVWA on VM1 with security level `Low`.
5. Use provided POC scripts from `/Proof_of_Concepts`.

## 🧩 Features
- Reflected, Stored, DOM XSS demos  
- Safe escalation simulation (synthetic tokens only)  
- Centralized log collection via `safe_logger.py`  
- Step-by-step forensics and mitigation validation

## 🧰 Technologies Used
- Kali Linux (VMware)
- Apache, PHP, MySQL
- DVWA
- Python 3

## 🛡️ Safety Notice
All testing is **fully isolated** and does **not target any live systems**.  
Use only in a controlled lab.

## 📁 Files
- `safe_logger.py` — Local receiver for synthetic POSTs  
- `Mitigations/` — Secure coding examples  
- `Proof_of_Concepts/` — Payloads and screenshots  
- `Forensics_Logs/` — Example logs and HAR excerpts  
<<<<<<< HEAD
- `SnehaChiliveru_CybersecurityProject.pdf` — Full report
=======
- `SnehaChiliveru_CybersecurityProject.pdf` — Full report
>>>>>>> cac5a97 (Initial commit)
