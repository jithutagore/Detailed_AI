# 28 — Voice Agents

> **Goal:** Build real-time, natural-sounding voice agents with low latency, interruption handling and tool use.
> **Change from original:** Merges the duplicated "Voice Agent" (old 20.6) and "Advanced Voice Agents" (old 21). This fits well with your existing speech/TTS experience.

**Level:** Specialization · **Time:** 2 weeks · **Prerequisites:** 02 (WebSockets), 07, 08

---

## Learning Objectives
- Build both cascaded (STT → LLM → TTS) and speech-to-speech voice agents
- Achieve sub-second response latency
- Handle turn-taking, interruptions and barge-in
- Connect voice agents to phone systems

---

## 28.1 Architectures
**Cascaded pipeline**
```
Microphone → VAD → Streaming STT → Agent (LLM + tools + memory) → Streaming TTS → Speaker
```
**Speech-to-speech (realtime) models**
- OpenAI Realtime API, Gemini Live API, and similar
- Trade-offs: latency and naturalness vs control, tool reliability, cost, and choice of voice

## 28.2 Speech Components
- **Streaming STT**: Deepgram, AssemblyAI, Whisper/faster-whisper, Speechmatics, cloud STT
- **VAD** (Voice Activity Detection): Silero VAD, WebRTC VAD
- **Diarization** (who spoke when): pyannote
- **Speech emotion** / paralinguistics
- **TTS**: ElevenLabs, Cartesia, OpenAI TTS, Azure, open models (e.g. Kokoro, XTTS, Piper); streaming TTS, voice cloning ethics, SSML
- Audio formats, sample rates, codecs (PCM, μ-law for telephony, Opus)

## 28.3 Conversation Dynamics
- **Turn detection** (silence-based vs semantic turn-detection models)
- **Interruptions** and **barge-in** (stopping TTS immediately, truncating context to what was actually spoken)
- Backchanneling ("mm-hmm")
- Endpointing tuning
- **Conversation state** across turns
- Handling noise, accents, crosstalk
- Spelling out and confirming entities (emails, numbers, names)

## 28.4 Latency Optimization
- Latency budget: STT → LLM TTFT → TTS first byte (target < 800 ms voice-to-voice)
- Streaming everything, sentence-level TTS chunking
- Small/fast models for the conversational turn; delegating heavy work to background tools
- Prompt caching, co-locating services
- Filler phrases while tools run

## 28.5 Voice Agent Frameworks
- **LiveKit Agents**
- **Pipecat**
- Vapi, Retell, Bland (hosted platforms)
- WebRTC vs WebSockets transports

## 28.6 Telephony
- SIP, PSTN, Twilio / Telnyx media streams
- DTMF, call transfer to humans, voicemail detection
- Call recording and consent laws

## 28.7 Evaluating Voice Agents
- WER (word error rate) for STT
- Latency percentiles per stage
- Task success on simulated calls
- Interruption-handling tests
- Voice quality (MOS) evaluation

---

## Project — Voice Customer Support Agent
```
Microphone / Phone call
    ↓
VAD + Turn detection
    ↓
Streaming STT
    ↓
Agent
 ↓       ↓
Memory  Tools (order lookup, booking, RAG)
    ↓
Streaming TTS
    ↓
Speaker / Phone
```
- Built with LiveKit Agents or Pipecat
- Barge-in support
- Transfer to a human on request
- Latency dashboard per stage
- Compare cascaded vs a realtime speech-to-speech model

## Definition of Done
- [ ] P50 voice-to-voice latency < 1 s
- [ ] Interruptions handled correctly
- [ ] 20 simulated-call eval scenarios
