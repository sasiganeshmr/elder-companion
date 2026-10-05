"""
Elder Companion (முதியோர் தோழன் / Periyavar Thozhan) - Prototype Local Development Server
Provides static file serving and simulated API endpoints for Tamil Nadu intergenerational matching,
Kadhai Petti (கதை பெட்டி) life story archiving, Digital Udhaviyalar tech micro-tutoring, and NSS service logging.
"""

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import json
import os
import sys
import urllib.request

PORT = int(os.environ.get("PORT", 8080))

MOCK_SENIORS = [
    {
        "id": "s1",
        "name": "Thiru. Krishnan Ramaswamy",
        "age": 76,
        "location": "Mylapore, Chennai, Tamil Nadu",
        "languages": ["Tamil", "English"],
        "interests": ["Southern Railways History", "Carnatic Music (MS Subbulakshmi)", "Chess"],
        "matchScore": 98,
        "mood": "Peaceful & Eager to Share Stories (மனநிறைவு)",
        "profession": "Retd. Chief Mechanical Engineer, Southern Railway",
        "avatar": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=160&h=160&q=80"
    },
    {
        "id": "s2",
        "name": "Prof. Gopalakrishnan Iyer",
        "age": 78,
        "location": "Srirangam, Tiruchirappalli, Tamil Nadu",
        "languages": ["Tamil", "English"],
        "interests": ["Thirukkural Discussions", "Temple Architecture", "Vedic Mathematics"],
        "matchScore": 95,
        "mood": "Ready for a Chess Game & Friendly Banter",
        "profession": "Retd. Dean of Mathematics, St. Joseph's College",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=160&h=160&q=80"
    },
    {
        "id": "s3",
        "name": "Captain K. Jayaraman (Retd.)",
        "age": 75,
        "location": "KK Nagar, Madurai, Tamil Nadu",
        "languages": ["Tamil", "English"],
        "interests": ["Military Service Memories", "Rose Gardening", "Sangam Poetry"],
        "matchScore": 91,
        "mood": "Needs Assistance with UPI / GPay Electricity Bill",
        "profession": "Indian Army Veteran & Agriculturalist",
        "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=160&h=160&q=80"
    },
    {
        "id": "s4",
        "name": "Dr. N. Sundararajan",
        "age": 80,
        "location": "RS Puram, Coimbatore, Tamil Nadu",
        "languages": ["Tamil", "English"],
        "interests": ["Classic Tamil Literature", "Vintage Ilaiyaraaja Melodies", "Health Talks"],
        "matchScore": 88,
        "mood": "Craving Nostalgic Evening Adda & Filter Coffee Talks",
        "profession": "Retd. Chief Civil Surgeon, Coimbatore Medical College",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=160&h=160&q=80"
    }
]

MOCK_KADHAI_STORIES = [
    {
        "id": "k1",
        "title": "Chennai Central Electrification & Southern Railways Golden Era (1983)",
        "narrator": "Krishnan Ramaswamy (76)",
        "duration": "16 mins",
        "date": "28 Sep 2026",
        "summary": "Krishnan Ayya recalls the memorable day the first electric locomotive rolled into Chennai Central station and how local loco pilots celebrated.",
        "tags": ["Southern Railway", "Chennai Central", "Heritage"]
    },
    {
        "id": "k2",
        "title": "Margazhi Music Festival at Mylapore Music Academy (1976)",
        "narrator": "Prof. Gopalakrishnan Iyer (78)",
        "duration": "24 mins",
        "date": "22 Sep 2026",
        "summary": "Memories of attending evening kutcheris, steaming filter coffee at the canteen, and listening to legendary masters of Carnatic violin.",
        "tags": ["Margazhi", "Mylapore", "Carnatic Music"]
    }
]

class ElderCompanionHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        elif self.path == "/api/seniors":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(MOCK_SENIORS, ensure_ascii=False).encode("utf-8"))
            return
        elif self.path in ["/api/kadhai-stories", "/api/kahaani-stories"]:
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(MOCK_KADHAI_STORIES, ensure_ascii=False).encode("utf-8"))
            return
        elif self.path.startswith("/api/live-radio"):
            # Relay 102.1 MHz Live Tamil Radio Stream
            target_stream = "https://cp11.serverse.com/proxy/hgsmgluv?mp=/stream"
            try:
                req = urllib.request.Request(
                    target_stream,
                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                )
                stream_resp = urllib.request.urlopen(req, timeout=10)
                self.send_response(200)
                self.send_header("Content-Type", "audio/mpeg")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                self.end_headers()
                while True:
                    chunk = stream_resp.read(4096)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
            except Exception:
                pass
            return
        elif self.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy", "service": "ElderCompanion-TamilNadu"}).encode("utf-8"))
            return
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/log-session":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            data = json.loads(body) if body else {}
            
            self.send_response(201)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            response = {
                "success": True,
                "message": "NSS / University youth community service session successfully certified.",
                "data": data
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return
        elif self.path in ["/api/save-kadhai", "/api/save-kahaani"]:
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            data = json.loads(body) if body else {}
            self.send_response(201)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            response = {
                "success": True,
                "message": "Oral history safely preserved in Kadhai Petti with automated Tamil & English transcription.",
                "storyId": f"kp-{len(MOCK_KADHAI_STORIES) + 1}"
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return
        
        self.send_response(404)
        self.end_headers()

def run(port=PORT):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server_address = ("", port)
    httpd = ThreadingHTTPServer(server_address, ElderCompanionHandler)
    print(f"Elder Companion server running at: http://localhost:{port}")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run(port)
