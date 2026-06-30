# TRIANGLE - Media & Assets Guide

## 📹 Video Assets

### Demo Videos

#### 1. Quick Demo (30 seconds)
- Real-time detection on sample video
- Shows: Input → Processing → Output
- Location: `assets/videos/demo-quick.mp4`

#### 2. Performance Showcase (1 minute)
- CPU vs GPU comparison
- Real vs Fake detection
- Accuracy metrics display
- Location: `assets/videos/demo-performance.mp4`

#### 3. Full Technical Demo (5 minutes)
- Architecture explanation
- Model walkthrough
- Live detection demo
- Performance benchmarks
- Location: `assets/videos/demo-technical.mp4`

### How to Generate Demo Videos

```bash
# Generate 30-second demo
python scripts/generate_demo.py \
  --output assets/videos/demo-quick.mp4 \
  --duration 30 \
  --fps 30

# Generate performance comparison
python scripts/generate_comparison.py \
  --output assets/videos/demo-performance.mp4 \
  --show-metrics

# Generate from actual video file
python scripts/process_video.py \
  --input sample_video.mp4 \
  --output demo_annotated.mp4 \
  --show-bbox \
  --show-confidence
```

---

## 🖼️ Image Assets

### Badges

Generated using `scripts/generate_badges.py`:

- Accuracy Badge
- Speed Badge
- Python Version Badge
- PyTorch Version Badge
- FastAPI Badge
- Docker Badge
- License Badge
- Status Badge

### Screenshots

Store in `assets/images/`:

```
assets/images/
├── api-docs.png           # Swagger UI
├── detection-result.png   # Sample detection
├── performance.png        # Metrics dashboard
├── architecture.png       # System architecture
├── model-arch.png         # Model diagram
├── deployment.png         # Azure deployment
└── comparison.png         # Real vs Fake
```

### Creating Screenshots

```bash
# API documentation screenshot
python scripts/screenshot_api.py \
  --output assets/images/api-docs.png

# Performance metrics
python scripts/screenshot_metrics.py \
  --output assets/images/performance.png
```

---

## 🎨 Design Assets

### Logo

- Primary: `assets/logos/triangle-logo.png` (256x256)
- Icon: `assets/logos/triangle-icon.png` (64x64)
- Banner: `assets/logos/triangle-banner.png` (1200x630)

### Color Palette

```
Primary Blue:      #1F77B4
Secondary Orange:  #FF7F0E
Success Green:     #2CA02C
Danger Red:        #D62728
Background:        #F5F5F5
Text:              #333333
```

### Typography

- Display: Inter Bold (24px+)
- Body: Inter Regular (14-16px)
- Code: JetBrains Mono (12px)

---

## 📊 Diagram Assets

### System Architecture

```
Input → Validation → Face Detection (MTCNN) → Preprocessing
→ CNN Inference → Post-Processing → Output (JSON)
```

### Data Flow

```
Image/Video Input
    ↓
[File Validation]
    ↓
[MTCNN Face Detection]
    ↓
[Image Preprocessing]
    ↓
[CNN Inference]
    ↓
[Confidence Thresholding]
    ↓
[JSON Response]
```

### Model Architecture

```
Input: (Batch, 3, 224, 224)
  ↓ Conv2D + BatchNorm + ReLU (3→64)
  ↓ MaxPool (2x2)
  ↓ Conv2D + BatchNorm + ReLU (64→128)
  ↓ MaxPool (2x2)
  ↓ Conv2D + BatchNorm + ReLU (128→256)
  ↓ Conv2D + BatchNorm + ReLU (256→256)
  ↓ MaxPool (2x2)
  ↓ Conv2D + BatchNorm + ReLU (256→512)
  ↓ MaxPool (2x2)
  ↓ GlobalAvgPool
  ↓ Linear (512→256) + ReLU + Dropout
  ↓ Linear (256→128) + ReLU + Dropout
  ↓ Linear (128→2) + Softmax
Output: [Real_Prob, Fake_Prob]
```

### Deployment Architecture

```
GitHub Repository
    ↓
GitHub Actions (CI/CD)
    ↓ Testing & Build
    ↓
Docker Image (nahidpn/triangle:latest)
    ↓
Azure Container Registry
    ↓
Azure App Service
    ↓
Production Deployment
```

---

## 📹 YouTube Content Strategy

### Channel Structure

1. **Introduction Series** (Week 1)
   - What is deepfake detection?
   - Why TRIANGLE?
   - Project overview

2. **Technical Deep Dive** (Week 2-3)
   - Model architecture explained
   - Training methodology
   - Evaluation results

3. **Demo Series** (Week 4)
   - Live detection demos
   - Real vs Fake examples
   - Performance benchmarks

4. **Deployment Guide** (Week 5)
   - Docker setup
   - API usage
   - Production deployment

5. **Tutorial Series** (Ongoing)
   - How to use the API
   - Integration examples
   - Custom model training

### Thumbnail Design

- Bold title text
- Red/Green Real/Fake indicator
- 92% accuracy badge
- High contrast background

### Video Format

- **Resolution**: 1920x1080 (Full HD)
- **Frame Rate**: 30 fps
- **Duration**: 3-10 minutes per video
- **Format**: MP4 with H.264 codec

---

## 🐦 Social Media Assets

### Twitter/X

```
✨ Just released TRIANGLE - Deepfake Detection Platform
🧠 92% Accuracy | ⚡ <500ms Inference
🔗 Built with PyTorch, FastAPI, Azure
🚀 Open Source: github.com/nahidpn/triangle

#AI #ML #DeepfakeDetection #PyTorch #OpenSource
```

### LinkedIn

```
I'm excited to announce TRIANGLE, my AI/ML project for
deepfake detection!

🎯 Highlights:
• 92% accuracy on FaceForensics++ dataset
• <500ms inference time
• Production-ready with Docker & Azure
• Full-stack: CNN + MTCNN + FastAPI + React

This project demonstrates:
✅ Deep learning expertise (CNN, MTCNN)
✅ Full-stack development (backend + frontend)
✅ DevOps & cloud deployment (Azure, Docker)
✅ Best practices (CI/CD, testing, documentation)

Check it out: github.com/nahidpn/triangle
```

### GitHub Gist

Share code snippets and API examples as gists with syntax highlighting.

---

## 📋 Asset Checklist

### Videos
- [ ] 30-second quick demo
- [ ] 1-minute performance showcase
- [ ] 5-minute technical explanation
- [ ] API usage tutorial
- [ ] Deployment walkthrough

### Images
- [ ] API documentation screenshot
- [ ] Detection result example
- [ ] Performance metrics graph
- [ ] System architecture diagram
- [ ] Model architecture visualization
- [ ] Real vs Fake comparison

### Logos & Branding
- [ ] Primary logo (256x256)
- [ ] Icon (64x64)
- [ ] Banner (1200x630)
- [ ] Favicon (32x32)

### Badges
- [ ] Accuracy badge
- [ ] Speed badge
- [ ] Python version badge
- [ ] PyTorch version badge
- [ ] FastAPI badge
- [ ] Docker badge
- [ ] License badge
- [ ] Status badge

### Documentation
- [ ] Demo guide (this file)
- [ ] Media guide
- [ ] Video tutorials
- [ ] API examples
- [ ] Deployment guide

---

## 🚀 Publishing Timeline

**Week 1**: Generate demo videos + badges
**Week 2**: Create YouTube channel + upload videos
**Week 3**: Share on social media (Twitter, LinkedIn)
**Week 4**: GitHub releases with media
**Week 5**: Portfolio website with embedded videos

---

## 📞 Contact & Support

For questions about media assets or video tutorials:
- GitHub Issues: github.com/nahidpn/triangle/issues
- Email: nahid@example.com
- LinkedIn: linkedin.com/in/muhammed-nahid-pn

---

**Last Updated**: June 30, 2026

