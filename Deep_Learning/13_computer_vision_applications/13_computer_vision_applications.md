# 13 — Computer Vision Applications

> **Goal:** Apply the CNN/Transformer foundations (Sections 04–05, 07) to the standard production CV tasks: object detection, segmentation, and OCR — going beyond classification into "where" and "what shape" questions.

**Level:** Applied · **Time:** 2–3 weeks · **Prerequisites:** 04, 05; 07 recommended for ViT-based methods

---

## Learning Objectives
- Distinguish classification, detection, and segmentation as progressively harder localization tasks
- Implement or fine-tune object detection and segmentation models
- Build an OCR pipeline
- Evaluate each task with its correct metric

---

## 13.1 The Vision Task Hierarchy
- **Image classification** (Sections 04–05): "what is in this image?" — one label per image
- **Object detection**: "what objects, and where?" — bounding boxes + labels for multiple objects
- **Semantic segmentation**: "which pixels belong to which class?" — per-pixel classification
- **Instance segmentation**: segmentation that also distinguishes individual object instances (two overlapping dogs are separate, not one blob)
- Each task builds on the last conceptually, and often architecturally (a detector/segmenter typically has a CNN backbone doing feature extraction, recap Section 05's transfer learning)

## 13.2 Object Detection
- Classical era recap (`AI\07.6`): sliding window, HOG+SVM, Viola-Jones — why they didn't scale to general object detection
- **Two-stage detectors**: R-CNN → Fast R-CNN → **Faster R-CNN** — region proposals, then classify/refine each region; accurate but slower
- **One-stage detectors**: **YOLO** (You Only Look Once) — predicting boxes and classes directly in a single pass, trading some accuracy for large speed gains; **SSD** (Single Shot Detector)
- Anchor boxes: predefined box shapes/sizes the model adjusts, and anchor-free alternatives (awareness)
- Non-Maximum Suppression (NMS): removing duplicate overlapping detections
- Modern detection transformers: **DETR** — framing detection as direct set prediction using a Transformer (recap Section 07), removing the need for anchor boxes and NMS
- Evaluation: **Intersection over Union (IoU)**, mean Average Precision (mAP) — the standard detection metric, and why it's more involved than classification accuracy

## 13.3 Semantic & Instance Segmentation
- **Fully Convolutional Networks (FCN)**: adapting classification CNNs for dense, per-pixel prediction by replacing fully-connected layers with convolutions
- **U-Net** (recap Section 11.3 — you already built this for diffusion models): encoder-decoder with skip connections, originally designed for biomedical image segmentation, now a general-purpose segmentation workhorse
- **Mask R-CNN**: extending Faster R-CNN with a segmentation branch — the standard instance segmentation architecture
- Modern segmentation foundation models: **Segment Anything Model (SAM)** — awareness of promptable, zero-shot segmentation
- Evaluation: pixel accuracy, **Intersection over Union (IoU) / Jaccard index** per class, Dice coefficient

## 13.4 Optical Character Recognition (OCR)
- The OCR pipeline: text detection (finding where text is, a specialized object detection problem) → text recognition (reading the characters, a sequence prediction problem)
- **CRNN** (CNN + RNN): CNN extracts visual features, RNN/LSTM (recap Section 06) reads them as a sequence, trained with **CTC loss** (Connectionist Temporal Classification) — handling the alignment problem between image regions and output characters without needing character-level position labels
- Modern OCR: Transformer-based approaches (recap Section 07), pretrained OCR models and APIs
- Practical OCR tools: Tesseract (classical/hybrid, recap link to `AI_Agents\09.2`'s document parsing discussion), EasyOCR, PaddleOCR, cloud OCR APIs
- Document-specific challenges: skew/rotation correction (recap `AI\07.7`'s document scanner project), handwriting vs printed text, table/layout-aware OCR (direct link forward to `AI_Agents\09.2`'s document parsing for RAG)

## 13.5 Vision Transformers in Practice
- Recap Section 05.1's introduction to ViT: treating image patches as a token sequence, applying the Transformer encoder (Section 07) directly
- ViT vs CNN trade-offs: ViT needs more data to match CNN performance from scratch (CNNs have built-in inductive biases — locality, translation invariance — that ViT must learn from data instead), but ViT scales better with very large datasets
- Hybrid architectures (CNN backbone + Transformer head, or vice versa) — awareness
- Using pretrained ViT models via transfer learning (recap Section 05.3's workflow, applied to ViT instead of CNN backbones)

## 13.6 Practical Production Considerations
- Real-time constraints: detection/segmentation model choice under latency budgets (YOLO-family for speed, Mask R-CNN-family for accuracy)
- Model size vs accuracy trade-offs (recap Section 05.5, extended to detection/segmentation)
- Data annotation for detection/segmentation: bounding box and polygon/mask labeling tools and their cost, compared to classification's simpler per-image labels

---

## Hands-on Exercises
1. Fine-tune a pretrained Faster R-CNN or YOLO model on a custom object-detection dataset (even a small one, e.g. 3–5 object classes you photograph yourself); evaluate with mAP.
2. Fine-tune a pretrained U-Net or Mask R-CNN for a segmentation task; visualize predicted masks against ground truth.
3. Build a small CRNN + CTC loss text recognizer for a constrained text domain (e.g. digit sequences, license plates); compare against a pretrained OCR tool.
4. Compare a CNN-based and a ViT-based classifier (both transfer-learned) on the same small custom dataset; document which needs more data/epochs to reach comparable accuracy.

## Project — Document Understanding Pipeline
Build an end-to-end pipeline that takes a photographed document and produces structured text: text detection → text recognition (OCR) → layout analysis (grouping text into logical blocks: title, paragraphs, tables). Compare a classical CV preprocessing step (recap `AI\07.7`'s document scanner — deskewing, perspective correction) feeding into your OCR model, against OCR without that preprocessing — quantify the accuracy difference. This project's output format is exactly what `AI_Agents\09.2` (document parsing for RAG) needs as input.

## Recommended Resources
- CS231n (Stanford) — detection and segmentation lecture notes
- Redmon et al., "You Only Look Once" (YOLO, 2016) and subsequent YOLO version papers
- Ronneberger et al., "U-Net: Convolutional Networks for Biomedical Image Segmentation" (2015)
- He et al., "Mask R-CNN" (2017)
- Kirillov et al., "Segment Anything" (2023)
- Carion et al., "End-to-End Object Detection with Transformers" (DETR, 2020)

## Definition of Done
- [ ] Your fine-tuned detector reports mAP on a held-out test set, not just qualitative examples
- [ ] Your OCR pipeline's accuracy improvement from classical CV preprocessing is quantified, not assumed
- [ ] You can explain the trade-off between two-stage and one-stage detectors in terms of the speed/accuracy trade-off, with numbers from your own experiments
