import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('// CALL ROOM SIMULATION')
end_idx = content.find('// KADHAI PETTI ORAL HISTORY RECORDING')

if start_idx != -1 and end_idx != -1:
    old_block = content[start_idx:end_idx]
    
    new_block = '''// CALL ROOM SIMULATION WITH REAL JITSI WEBRTC
    function startCall(partnerName, topic, fromRole) {
      document.getElementById('callPartnerName').textContent = partnerName;
      document.getElementById('callTopicBadge').textContent = "தலைப்பு: " + topic;
      document.getElementById('callModal').classList.remove('hidden');

      // Initialize Jitsi WebRTC Room
      const container = document.getElementById('jitsiMeetContainer');
      if (container) {
        container.innerHTML = ''; // Clear container
        if (jitsiApi) { jitsiApi.dispose(); jitsiApi = null; }
        
        const domain = 'meet.jit.si';
        const options = {
            roomName: 'ElderCompanion_SafeRoom_9812',
            width: '100%',
            height: '100%',
            parentNode: container,
            userInfo: {
                displayName: currentRole === 'senior' ? 'முதியோர் (Senior)' : 'தன்னார்வலர் (Volunteer)'
            },
            configOverwrite: { 
               startWithAudioMuted: false, 
               startWithVideoMuted: false,
               prejoinPageEnabled: false
            }
        };
        try {
          jitsiApi = new JitsiMeetExternalAPI(domain, options);
          jitsiApi.addEventListener('audioMuteStatusChanged', function (data) {
             isMuted = data.muted;
             const btn = document.getElementById('muteBtnText');
             if (btn) btn.textContent = isMuted ? 'Unmute' : 'Mute';
          });
          jitsiApi.addEventListener('videoConferenceLeft', function () {
             endCall(); // Auto end call if they hang up inside Jitsi
          });
        } catch (e) {
          console.error("Jitsi API failed to load", e);
        }
      }

      callSeconds = 0;
      updateCallTimer();
      if (callTimerInterval) clearInterval(callTimerInterval);
      callTimerInterval = setInterval(() => {
        callSeconds++;
        updateCallTimer();
      }, 1000);

      subtitleIndex = 0;
      updateSubtitle();
      if (subtitleInterval) clearInterval(subtitleInterval);
      subtitleInterval = setInterval(() => {
        subtitleIndex = (subtitleIndex + 1) % simulatedSubtitles.length;
        updateSubtitle();
      }, 4200);
    }

    function updateCallTimer() {
      const mins = String(Math.floor(callSeconds / 60)).padStart(2, '0');
      const secs = String(callSeconds % 60).padStart(2, '0');
      document.getElementById('callTimer').textContent = `${mins}:${secs}`;
    }

    function updateSubtitle() {
      if (!captionsEnabled) return;
      document.getElementById('liveSubtitleText').textContent = simulatedSubtitles[subtitleIndex];
    }

    function toggleCaptions() {
      captionsEnabled = !captionsEnabled;
      const box = document.getElementById('subtitlesBox');
      const btn = document.getElementById('captionBtnText');
      if (captionsEnabled) {
        box.classList.remove('hidden');
        btn.textContent = "துணை தலைப்புகள்: ON";
      } else {
        box.classList.add('hidden');
        btn.textContent = "துணை தலைப்புகள்: OFF";
      }
    }

    function requestSpeakSlower() {
      document.getElementById('liveSubtitleText').textContent = "⚠️ கார்த்திக், தயவுசெய்து மெதுவாகப் பேசுங்கள்... (Requested to speak slower)";
      if (jitsiApi) jitsiApi.executeCommand('sendChatMessage', 'தயவுசெய்து மெதுவாகப் பேசுங்கள் (Please speak slower)', '', true);
    }

    function sendCulturalReaction(symbol, name) {
      const overlay = document.getElementById('reactionsOverlay');
      const emoji = document.createElement('div');
      emoji.textContent = symbol;
      emoji.className = "absolute bottom-10 left-1/2 -translate-x-1/2 text-6xl animate-[bounce_2s_ease-out_forwards] opacity-0";
      overlay.appendChild(emoji);
      setTimeout(() => emoji.remove(), 2000);
      document.getElementById('liveSubtitleText').textContent = `✨ நீங்கள் '${name}' அனுப்பினீர்கள்!`;
      
      if (jitsiApi) {
          try { jitsiApi.executeCommand('sendEndpointTextMessage', '', `Reaction: ${symbol} ${name}`); } catch(e){}
      }
    }

    let isMuted = false;
    function toggleAudioMute() {
      if (jitsiApi) {
        jitsiApi.executeCommand('toggleAudio');
      } else {
        isMuted = !isMuted;
        const btn = document.getElementById('muteBtnText');
        if (isMuted) {
          btn.textContent = 'Unmute';
          announce("மைக் முடக்கப்பட்டுள்ளது (Muted).");
        } else {
          btn.textContent = 'Mute';
          announce("மைக் இயக்கத்தில் உள்ளது.");
        }
      }
    }

    function injectCallPrompt(prompt) {
      document.getElementById('liveSubtitleText').textContent = "💡 தலைப்பு: " + prompt;
    }

    function endCall() {
      if (callTimerInterval) clearInterval(callTimerInterval);
      if (subtitleInterval) clearInterval(subtitleInterval);
      document.getElementById('callModal').classList.add('hidden');
      
      // Clean up Jitsi
      if (jitsiApi) {
        jitsiApi.dispose();
        jitsiApi = null;
      }

      // Reset mute state for next call
      isMuted = false;
      document.getElementById('muteBtnText').textContent = 'Mute';

      verifiedHours += 0.5;
      document.getElementById('volunteerHoursCounter').textContent = verifiedHours.toFixed(1) + " மணிநேரம்";
      document.getElementById('certHoursNumber').textContent = verifiedHours.toFixed(1) + " மணிநேரம் (Verified Hours)";

      announce("அழைப்பு நிறைவடைந்தது. 30 நிமிடங்கள் NSS சமூக சேவைக் கணக்கில் வரவு வைக்கப்பட்டது!");
    }

    '''
    
    new_content = content[:start_idx] + new_block + content[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully updated Call Javascript.')
else:
    print('Could not find the target blocks.')
