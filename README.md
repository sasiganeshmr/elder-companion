# Elder Companion (முதியோர் தோழன்) 🤝
### தமிழ் & English Intergenerational Social Connection Platform

**Elder Companion (முதியோர் தோழன் / Periyavar Thozhan)** connects senior citizens in Tamil Nadu with passionate university student volunteers (NSS / Anna University) for affectionate companionship, oral heritage archiving, and safe digital literacy.

---

## 🌟 தமிழ் & English Features & Innovations

1. **🔐 Multi-Persona Login Portal (`#loginView`)**:
   - **👴 முதியோர் (Senior Citizen Login)**: Accessible entry with 10-digit mobile number, voice guidance (`🔊` in Tamil), and **One-Click Quick Entry**.
   - **🎓 இளைஞர் (Youth Volunteer Login)**: University student email (`.edu` / `.ac.in`) + NSS Volunteer Roll Number.
   - **🛡️ குடும்பம் (Family / Caregiver Login)**: Dedicated view for sons/daughters monitoring elderly parents from afar (e.g., Bengaluru/Singapore to Chennai).

2. **🎙️ கதை பெட்டி (Kadhai Petti — Oral Heritage Archiving)**:
   - Elders record their life memories with real-time audio waveform simulation (e.g., *"1983ல் சென்னை சென்ட்ரல் இரயில்வேயில் முதல் மின்சார ரயில் பயணம்"*).
   - Automated speech transcription into Tamil & English, preserved forever in the Family Heritage Vault.

3. **📱 டிஜிட்டல் உதவியாளர் (Digital Udhaviyalar — Safe Tech Micro-Tutoring)**:
   - Safe 10-minute micro-lessons by student volunteers for senior essentials:
     - TNEB மின் கட்டணம் (Electricity bill payment online).
     - IRCTC ரயில் டிக்கெட் முன்பதிவு (Train ticket booking).
     - வாட்ஸ்அப் வீடியோ அழைப்பு (WhatsApp video calling with grandchildren).
   - **ScamGuard India Anti-Fraud Shield**: Automatic filters strictly forbid asking for UPI PIN, OTP, or net banking passwords.

4. **📻 பழைய வானொலி 102.1 MHz (AIR FM Rainbow 102.1 - Trichy & Chennai)**:
   - Dedicated Web Audio synthesizer and live player tuned to **102.1 MHz** playing authentic Carnatic Mohanam rāga flute melodies and Tanpura drone (inspired by **இளையராஜா & எம்.எஸ். சுப்புலட்சுமி**).
   - Real-time animated equalizer soundwaves, frequency preset tuner (`102.1 MHz`, `100.5 MHz`, `105.0 MHz`), and live on-air indicator.

5. **📜 National Service Scheme (NSS) Certified Service Hours**:
   - Automated hour tracker with a formal, printable **Certificate of Intergenerational Service** bearing Tamil Nadu NSS & University coordinator endorsements.

---

## 👥 Personas (Tamil Male Focus)

- **Senior Elder**: **Thiru. Krishnan Ramaswamy (76, Mylapore, Chennai, TN)**
  - *Background*: Retired Chief Mechanical Engineer, Southern Railway.
  - *Interests*: Southern Railway history, Carnatic Music (Margazhi Kutcheris), Chess.
  - *Peers*: **Prof. Gopalakrishnan Iyer (78, Srirangam, Tiruchirappalli)**, **Captain K. Jayaraman (Retd., 75, Madurai)**, **Dr. N. Sundararajan (80, Coimbatore)**.

- **Student Volunteer**: **Karthik Subramanian (21, Chennai, TN)**
  - *Background*: B.Tech Computer Science, Anna University (CEG Guindy) • NSS Youth Fellow.
  - *Interests*: Oral history archiving, tech micro-tutoring, listening to Southern Railway heritage.
  - *Peers*: **Ashwin Sundaram (21, CEG)**, **Vignesh (20, Loyola College)**.

- **Family Caregiver**: **Dr. Senthil Krishnan (44, Bengaluru, KA)**
  - *Role*: Senior Tech Director, son of Krishnan Ayya.
  - *Portal*: Tracks father's weekly social time, happiness sentiment (4.9/5.0), and Kadhai Petti audio recordings.

---

## 💻 How to Run Locally

### Option 1: Direct Browser
Open [index.html](file:///C:/Users/dmani/.gemini/antigravity/scratch/elder-companion/index.html) in Chrome, Edge, Firefox, or Safari.

### Option 2: Run with Python Local Server
```powershell
cd C:\Users\dmani\.gemini\antigravity\scratch\elder-companion
python server.py 8080
```
Visit `http://localhost:8080`.

---

## 📂 Key Code Links
- [`index.html`](file:///C:/Users/dmani/.gemini/antigravity/scratch/elder-companion/index.html) — Interactive SPA with Login Screen, Tamil & English UI, Kadhai Petti, and Call Room.
- [`server.py`](file:///C:/Users/dmani/.gemini/antigravity/scratch/elder-companion/server.py) — Python REST mock server with [`ElderCompanionHandler`](file:///C:/Users/dmani/.gemini/antigravity/scratch/elder-companion/server.py#L79-L135).
- [`elder_companion_prototype.html`](file:///C:/Users/dmani/.gemini/antigravity/brain/106bd32b-0d9d-4abb-9113-c3dacfddfc24/elder_companion_prototype.html) — Artifact viewable directly inside the Antigravity preview pane.
