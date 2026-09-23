# 15 — Speech & Audio Deep Learning

> **Goal:** Apply deep learning to audio: speech recognition, speech synthesis, and general audio understanding. Given your speech/TTS background, this section connects everything in this folder directly to production-relevant work, and to `AI_Agents\28_voice_agents`.

**Level:** Applied · **Time:** 2 weeks · **Prerequisites:** 06, 07; 04 recommended (spectrograms are image-like)

---

## Learning Objectives
- Represent and process audio for deep learning
- Understand modern ASR (speech-to-text) and TTS (text-to-speech) architectures
- Build a basic speech recognition or synthesis pipeline
- Connect every architecture here back to the section that introduced its core mechanism

---

## 15.1 Audio Representation for Deep Learning
- Raw waveforms: sample rate, amplitude — why raw audio is rarely fed directly into most models (extremely high sequence length)
- **Spectrograms**: converting audio into a time-frequency representation via the Short-Time Fourier Transform (STFT) — once converted, a spectrogram is a 2D image-like representation, which is exactly why CNN techniques (Section 04) apply directly to audio
- **Mel spectrograms**: frequency-warped to match human auditory perception — the standard input representation for most modern speech models
- MFCCs (Mel-Frequency Cepstral Coefficients) — the classical feature-engineering approach, still used in lightweight/classical pipelines (parallel to `AI\07`'s classical-vs-deep-learning framing for CV)

## 15.2 Automatic Speech Recognition (ASR) — Architecture Evolution
- Classical era recap (`AI\06.5`): HMM-based ASR, with Gaussian Mixture Models or early neural networks for acoustic modeling — historically dominant before end-to-end deep learning
- **CTC-based ASR**: recap Section 13.4's CRNN+CTC treatment (the exact same alignment-free training technique, here mapping audio frames to characters/phonemes instead of image regions to characters) — architectures like DeepSpeech
- **Encoder-decoder ASR with attention**: recap Section 06.6's seq2seq+attention — directly applicable to "translating" audio into text
- **Transformer/Conformer-based ASR**: recap Section 07 — Conformer combines convolution (local feature extraction, Section 04) with self-attention (global context, Section 07) in one architecture; the modern standard for high-accuracy ASR
- **Whisper-style models**: large-scale, weakly-supervised encoder-decoder Transformers trained on massive multilingual audio-text data — recap Section 09's scaling-laws discussion, applied to audio
- Streaming vs non-streaming ASR: why streaming (real-time, one chunk at a time) is architecturally harder — direct link to Section 06.7's discussion of where RNNs still beat Transformers for exactly this reason, and to `AI_Agents\28.2`'s streaming STT coverage

## 15.3 Text-to-Speech (TTS) — Architecture Evolution
- The TTS pipeline: text → linguistic/phonetic features → acoustic features (typically a mel spectrogram) → waveform
- **Acoustic models**: predicting a mel spectrogram from text
  - Tacotron-style: encoder-decoder with attention (recap Section 06.6 directly — this is a seq2seq problem, text sequence to spectrogram-frame sequence)
  - Transformer-based acoustic models (recap Section 07) — FastSpeech-style non-autoregressive generation for speed
- **Vocoders**: converting a mel spectrogram back into an actual audio waveform
  - Classical: Griffin-Lim (a signal-processing algorithm, no learning)
  - Neural vocoders: WaveNet (an autoregressive, dilated-convolution architecture — awareness), and modern GAN-based vocoders (recap Section 10.4's GAN treatment, applied here for fast, high-quality waveform generation) or diffusion-based vocoders (recap Section 11)
- Voice cloning / speaker adaptation: conditioning generation on a speaker embedding (recap the embedding concept from Section 08.5, applied to speaker identity instead of text meaning)
- Prosody and naturalness: why this remains one of the harder open problems in TTS

## 15.4 Speaker & Audio Understanding Tasks
- Speaker identification/verification: embedding-based similarity (recap Section 08.5's embedding approach, applied to voice instead of text)
- Speaker diarization ("who spoke when") — recap link to `AI_Agents\28.2`
- Voice Activity Detection (VAD) — a simpler classification task, recap Section 02/04's classification foundations, applied to audio frames
- Speech emotion recognition (classification on audio features, recap Section 04's CNN-on-spectrogram approach)
- General audio classification (sound event detection, music genre classification) — the same CNN-on-spectrogram pattern applied broadly

## 15.5 End-to-End vs Pipeline Approaches
- Classical pipelines: separate ASR → NLU → dialogue → NLG → TTS stages (recap Section 14.5's dialogue-system pipeline, now with the audio bookends added)
- Modern speech-to-speech models: directly modeling audio-in to audio-out (or audio-in to text/audio-out) without a hard intermediate text bottleneck — recap `AI_Agents\28.1`'s realtime speech-to-speech model discussion; this section provides the architectural grounding for why that's now possible

## 15.6 Where This Connects to AI_Agents
- `AI_Agents\28_voice_agents` covers voice agent *application engineering*: turn detection, barge-in, latency budgets, framework choice (LiveKit, Pipecat), telephony — all assuming the model-level understanding built in this section
- This section is the deep learning foundation that `AI_Agents\28` builds its production voice-agent architecture on top of

---

## Hands-on Exercises
1. Convert raw audio into mel spectrograms and visualize them; compare spectrograms of different speakers/sounds to build visual intuition.
2. Build a small CTC-based ASR model (CNN or Conformer-lite encoder + CTC loss, recap Section 13.4) on a small speech dataset (e.g. a subset of Common Voice or a similarly accessible dataset); report Word Error Rate (WER).
3. Fine-tune a pretrained Whisper-family model on a narrow-domain or low-resource-language dataset; compare WER before/after fine-tuning.
4. Build a basic Tacotron-style TTS acoustic model (encoder-decoder + attention, recap Section 06.6) on a small single-speaker dataset; pair it with a Griffin-Lim vocoder as a simple (if lower-quality) end-to-end baseline, and separately try a pretrained neural vocoder.

## Project — Domain-Specific Speech Pipeline
Given your speech/TTS background, build an ASR or TTS system fine-tuned for a specific narrow domain or language variety (e.g. a specific Indic language or code-mixed speech, a specific accent, or a narrow vocabulary domain like medical or legal dictation). Document: baseline pretrained model performance (WER for ASR, or MOS/subjective quality notes for TTS), fine-tuning approach and data requirements, and post-fine-tuning performance. Write up how this project's architecture choices connect to `AI_Agents\28`'s production voice-agent requirements (latency, streaming).

## Recommended Resources
- *Speech and Language Processing* (Jurafsky & Martin) — ASR chapters (free draft online)
- Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision" (Whisper paper, 2022)
- Shen et al., "Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions" (Tacotron 2, 2018)
- Gulati et al., "Conformer: Convolution-augmented Transformer for Speech Recognition" (2020)
- Hugging Face `transformers`/`speechbrain` documentation for ASR/TTS pipelines

## Definition of Done
- [ ] Your ASR project reports WER on a held-out test set
- [ ] Your fine-tuned model measurably outperforms the pretrained baseline on your target domain/language
- [ ] You can trace each audio architecture (CTC-ASR, Tacotron, Conformer) back to the specific general-purpose section (04, 06, 07, 10/11) whose mechanism it reuses
