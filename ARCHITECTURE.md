# TRIANGLE Architecture Documentation

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Layer                              │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────┐      ┌──────────────────────┐         │
│  │   Web UI (React)     │      │  Python Client SDK   │         │
│  │ - File upload        │      │  - Image detection   │         │
│  │ - Real-time analysis │      │  - Video processing  │         │
│  │ - Visualization      │      │  - Batch inference   │         │
│  └──────────────────────┘      └──────────────────────┘         │
└──────────────┬───────────────────────────────┬───────────────────┘
               │ HTTP/REST                     │ API
               ▼                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐   │
│  │           API Layer (Pydantic Models)                   │   │
│  │  - /health                                              │   │
│  │  - /api/v1/detect/image                                 │   │
│  │  - /api/v1/detect/video                                 │   │
│  │  - /api/v1/batch/process                                │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          │                                       │
│  ┌───────────────────────▼───────────────────────┐              │
│  │      Preprocessing Layer (OpenCV)             │              │
│  │  - Image normalization                        │              │
│  │  - Video frame extraction                     │              │
│  │  - Face detection (MTCNN)                     │              │
│  └───────────────────────┬───────────────────────┘              │
│                          │                                       │
│  ┌───────────────────────▼───────────────────────┐              │
│  │   ML Inference Layer (PyTorch/TensorFlow)    │              │
│  │  ┌─────────────────┐    ┌─────────────────┐  │              │
│  │  │  CNN Model      │    │  MTCNN Model    │  │              │
│  │  │ (Classification)│    │ (Face Detection)│  │              │
│  │  └─────────────────┘    └─────────────────┘  │              │
│  └───────────────────────┬───────────────────────┘              │
│                          │                                       │
│  ┌───────────────────────▼───────────────────────┐              │
│  │    Post-Processing Layer                      │              │
│  │  - Confidence scoring                         │              │
│  │  - Result formatting                          │              │
│  │  - Batch aggregation                          │              │
│  └───────────────────────┬───────────────────────┘              │
│                          │                                       │
└──────────────────────────┼───────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Storage & Caching                             │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────┐      ┌──────────────────────┐         │
│  │   Model Cache        │      │  Results Database    │         │
│  │ - Loaded weights     │      │  - PostgreSQL        │         │
│  │ - GPU memory         │      │  - Query logs        │         │
│  └──────────────────────┘      └──────────────────────┘         │
└─────────────────────────────────────────────────────────────────┘

```

## Data Flow Diagram

```
Image/Video Input
       │
       ▼
┌──────────────────┐
│ File Validation  │
│ - Format check   │
│ - Size check     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ MTCNN Face       │
│ Detection        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Image            │
│ Preprocessing    │
│ - Normalize      │
│ - Resize         │
│ - Augment        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ CNN Inference    │
│ - Forward pass   │
│ - Get logits     │
│ - Compute probs  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Post-Process     │
│ - Score smoothing│
│ - Thresholding   │
│ - Format output  │
└────────┬─────────┘
         │
         ▼
   JSON Response
```

## CNN Model Architecture

```
Input: (B, 3, 224, 224)
       │
       ▼
Conv2d(3, 64, 3x3) + BatchNorm + ReLU
       │
       ▼
MaxPool(2x2)  → (B, 64, 112, 112)
       │
       ▼
Conv2d(64, 128, 3x3) + BatchNorm + ReLU
       │
       ▼
MaxPool(2x2)  → (B, 128, 56, 56)
       │
       ▼
Conv2d(128, 256, 3x3) + BatchNorm + ReLU
       │
       ▼
Conv2d(256, 256, 3x3) + BatchNorm + ReLU
       │
       ▼
MaxPool(2x2)  → (B, 256, 28, 28)
       │
       ▼
Conv2d(256, 512, 3x3) + BatchNorm + ReLU
       │
       ▼
MaxPool(2x2)  → (B, 512, 14, 14)
       │
       ▼
GlobalAvgPool  → (B, 512)
       │
       ▼
Linear(512, 256) + ReLU + Dropout(0.5)
       │
       ▼
Linear(256, 128) + ReLU + Dropout(0.5)
       │
       ▼
Linear(128, 2) + Softmax  → (B, 2)
       │
       ▼
Output: [Real_prob, Fake_prob]
```

## Deployment Architecture (Azure)

```
┌──────────────────────────────────────────────────────────────┐
│                    Azure Cloud                                │
├──────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────────┐  │
│  │              Azure Container Registry                   │  │
│  │  - triangle:latest                                      │  │
│  │  - triangle:v1.0.0                                      │  │
│  └────────────────────────────────────────────────────────┘  │
│                         │                                     │
│                         ▼                                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │           Azure App Service (Linux)                     │  │
│  │  - Multiple instances for load balancing                │  │
│  │  - Auto-scaling based on CPU/Memory                     │  │
│  └────────────────────────────────────────────────────────┘  │
│                         │                                     │
│              ┌──────────┴──────────┐                          │
│              ▼                     ▼                          │
│  ┌──────────────────────┐  ┌──────────────────────┐         │
│  │  Azure SQL Database  │  │  Azure Blob Storage  │         │
│  │  - Result logs       │  │  - Models            │         │
│  │  - User data         │  │  - Temp files        │         │
│  └──────────────────────┘  └──────────────────────┘         │
│              │                     │                         │
│              └──────────┬──────────┘                         │
│                         ▼                                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │          Azure Application Insights                     │  │
│  │  - Performance monitoring                               │  │
│  │  - Error tracking                                       │  │
│  │  - Analytics                                            │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

## CI/CD Pipeline

```
Developer Push to main
       │
       ▼
┌──────────────────┐
│  GitHub Actions  │
│  Triggered       │
└────────┬─────────┘
         │
    ┌────┴────┐
    │          │
    ▼          ▼
Tests      Security
 │             │
 ├─ pytest     ├─ bandit
 ├─ flake8     ├─ CodeQL
 └─ mypy       └─ SAST
    │             │
    └────┬────────┘
         │
         ▼
    ┌──────────────┐
    │ All Pass? YES│
    └────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Docker Build     │
│ & Push           │
└────────┬─────────┘
         │
         ▼
   Deploy to Azure
```

## Performance Profile

- **Single Image**: 50ms - 500ms (CPU: 2s, GPU: 50ms)
- **Video (30fps)**: Parallel frame processing
- **Memory**: ~2GB GPU, ~500MB Server RAM
- **Model Size**: ~150MB
- **Accuracy**: ~92% on test set

---

*For implementation details, see README.md and API documentation in the repository.*
