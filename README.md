# Hindi AI Assistant 🇮🇳🎙️

A voice-enabled AI assistant that understands and responds in Hindi, featuring real-time facial expression detection and emotion-aware responses.

![Hindi AI Assistant](https://img.shields.io/badge/Language-Hindi-orange) ![Status](https://img.shields.io/badge/Status-Active-success)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [How It Works](#how-it-works)
- [Challenges & Solutions](#challenges--solutions)
- [Future Improvements](#future-improvements)
- [Project Structure](#project-structure)

## 🎯 Overview

This project is a full-stack Hindi AI assistant that processes voice input in Hindi (Devanagari script), generates intelligent responses using OpenAI's GPT, and provides audio output in Hindi. It features real-time facial expression detection to provide emotion-aware, contextually relevant responses.

## ✨ Features

- **🎤 Hindi Voice Recognition**: Real-time speech-to-text for Hindi using Google Speech Recognition API
- **🗣️ Hindi Text-to-Speech**: Natural-sounding Hindi audio responses using Google Text-to-Speech (gTTS)
- **😊 Facial Expression Detection**: Real-time emotion detection using OpenCV (Happy, Sad, Surprised, Thinking, Sleepy, Serious, Content, Neutral)
- **🤖 AI-Powered Responses**: Context-aware responses using OpenAI GPT-4 through LangChain
- **💬 Multi-turn Conversations**: Maintains conversation history for contextual understanding
- **🎨 Modern UI**: Beautiful, responsive interface built with Next.js and Tailwind CSS
- **📊 Visual Feedback**: Audio visualization and animated sphere for better user experience
- **🔄 Real-time Updates**: WebSocket-like updates for smooth user experience

## 🛠️ Technologies Used

### Backend
| Technology | Version | Purpose | Why Chosen |
|------------|---------|---------|------------|
| **FastAPI** | 0.115.0 | Web framework | High-performance, async support, excellent for APIs |
| **OpenCV** | 4.10.0 | Computer vision | Industry-standard for facial detection, Haar Cascades |
| **SpeechRecognition** | 3.11.0 | Speech-to-text | Best free option for Hindi STT with Google backend |
| **gTTS** | 2.5.3 | Text-to-speech | Natural Hindi voice synthesis, simple API |
| **LangChain** | 0.3.7 | LLM framework | Simplifies LLM integration, message management |
| **LangGraph** | 0.2.45 | Conversation state | Graph-based state management for conversations |
| **OpenAI** | via langchain-openai | LLM provider | GPT-4 for high-quality Hindi understanding |
| **Uvicorn** | 0.32.0 | ASGI server | Fast, production-ready Python server |
| **pygame** | 2.6.1 | Audio playback | Reliable cross-platform audio handling |

### Frontend
| Technology | Version | Purpose | Why Chosen |
|------------|---------|---------|------------|
| **Next.js** | 16.0.0 | React framework | SSR, excellent DX, built-in routing |
| **TypeScript** | Latest | Type safety | Catch errors early, better IDE support |
| **Tailwind CSS** | Latest | Styling | Rapid UI development, utility-first |
| **Radix UI** | Latest | UI components | Accessible, unstyled components |
| **React Webcam** | Latest | Camera access | Simple webcam integration |
| **Lucide React** | Latest | Icons | Beautiful, consistent icon set |

### APIs & Services
- **Google Speech Recognition API**: Free Hindi speech recognition
- **Google Text-to-Speech (gTTS)**: Hindi audio generation
- **OpenAI GPT-4 API**: Natural language understanding and generation
- **OpenCV Haar Cascades**: Face and feature detection

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend (Next.js)                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Webcam     │  │    Audio     │  │     UI       │      │
│  │   Component  │  │  Visualizer  │  │  Components  │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │              │
│         └──────────────────┴──────────────────┘              │
│                            │                                 │
│                            ▼                                 │
│                    ┌───────────────┐                        │
│                    │  REST API     │                        │
│                    │  Calls        │                        │
│                    └───────┬───────┘                        │
└────────────────────────────┼─────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                       Backend (FastAPI)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Audio      │  │   OpenCV     │  │  LangChain   │      │
│  │ Processing   │  │  Expression  │  │    Graph     │      │
│  │  (STT/TTS)   │  │  Detection   │  │  (LLM)       │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │              │
│         └──────────────────┴──────────────────┘              │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  External APIs  │
                    │  - Google STT   │
                    │  - gTTS         │
                    │  - OpenAI GPT   │
                    └─────────────────┘
```

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Node.js 18+** ([Download](https://nodejs.org/))
- **pnpm** (or npm/yarn)
- **OpenAI API Key** ([Get it here](https://platform.openai.com/api-keys))
- **Webcam** (for facial expression detection)
- **Microphone** (for voice input)

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Hindi-AI-assistant
```

### 2. Backend Setup

#### Navigate to backend directory
```bash
cd backend
```

#### Create a virtual environment (recommended)
```bash
python -m venv venv
```

#### Activate virtual environment
**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

#### Install Python dependencies
```bash
pip install -r requirements.txt
```

#### Create `.env` file
Create a file named `.env` in the `backend` directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

### 3. Frontend Setup

#### Open a new terminal and navigate to frontend directory
```bash
cd frontend
```

#### Install dependencies
Using pnpm (recommended):
```bash
pnpm install
```

Or using npm:
```bash
npm install
```

#### Create `.env.local` file (optional)
Create a file named `.env.local` in the `frontend` directory if you want to customize the backend URL:

```env
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
```

## 🎮 Running the Application

### Start the Backend Server

From the `backend` directory:

```bash
# Make sure your virtual environment is activated
python api.py
```

The backend will start on `http://localhost:8000`

**Expected output:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Start the Frontend Development Server

From the `frontend` directory (in a new terminal):

```bash
pnpm dev
# or
npm run dev
```

The frontend will start on `http://localhost:3000`

**Expected output:**
```
  ▲ Next.js 16.0.0
  - Local:        http://localhost:3000
  - Ready in 2.3s
```

### Access the Application

Open your browser and navigate to:
```
http://localhost:3000
```

**Grant permissions:**
- Allow microphone access when prompted
- Allow camera access when prompted (for facial expression detection)

## 📖 How It Works

### 1. Voice Input Processing
1. User clicks the microphone button to start recording
2. Audio is captured using the Web Audio API
3. Audio is sent to the backend as a file
4. Backend uses Google Speech Recognition to convert Hindi speech to text

### 2. Facial Expression Detection
1. Webcam captures video frames continuously
2. Frames are sent to backend every 500ms
3. OpenCV detects faces using Haar Cascade Classifier
4. Facial features (eyes, smile) are analyzed
5. Expression is classified into 8 categories: Happy, Sad, Surprised, Thinking, Sleepy, Serious, Content, Neutral
6. Expression is sent back to frontend with confidence score

### 3. AI Response Generation
1. Transcribed text + facial expression context is combined
2. Conversation history is maintained using LangGraph
3. Request is sent to OpenAI GPT-4 with Hindi system prompt
4. AI generates contextually appropriate Hindi response
5. Response includes emotion awareness (e.g., cheers up if user is sad)

### 4. Audio Output
1. Hindi text response is converted to speech using gTTS
2. Audio file is generated and sent to frontend
3. Frontend plays the audio with visual feedback
4. Audio visualizer shows real-time frequency data

### 5. Multi-turn Conversation
- All messages are stored in memory
- Conversation context is preserved across turns
- User can have natural, flowing conversations in Hindi

## 🎨 User Interface Features

- **Animated Sphere**: Dynamic 3D sphere that responds to audio
- **Audio Visualizer**: Real-time frequency visualization during playback
- **Expression Display**: Shows detected facial expression with emoji
- **Transcript Panel**: Displays conversation history with expandable sections
- **Responsive Design**: Works on desktop and mobile devices
- **Dark/Light Mode**: Toggle between themes for comfort


## 📁 Project Structure

```
Hindi-AI-assistant/
│
├── backend/
│   ├── api.py                    # FastAPI server with all endpoints
│   ├── main.py                   # Standalone CLI version with expression monitoring
│   ├── graph.py                  # LangGraph chatbot configuration
│   ├── requirements.txt          # Python dependencies
│   ├── face_detection_test.py    # Face detection testing script
│   ├── tts_test.py               # TTS testing script
│   └── .env                      # Environment variables (OpenAI key)
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx              # Main application page
│   │   ├── layout.tsx            # Root layout with providers
│   │   └── globals.css           # Global styles
│   │
│   ├── components/
│   │   ├── animated-sphere.tsx   # 3D animated sphere component
│   │   ├── audio-visualizer.tsx  # Audio frequency visualizer
│   │   ├── expression-detector.tsx # Facial expression detection
│   │   ├── response-display.tsx  # AI response display
│   │   ├── transcript-panel.tsx  # Conversation history panel
│   │   ├── theme-provider.tsx    # Dark/light mode provider
│   │   └── ui/                   # Reusable UI components (Radix UI)
│   │
│   ├── hooks/
│   │   ├── use-mobile.ts         # Mobile detection hook
│   │   └── use-toast.ts          # Toast notification hook
│   │
│   ├── lib/
│   │   └── utils.ts              # Utility functions
│   │
│   ├── package.json              # Node.js dependencies
│   ├── tsconfig.json             # TypeScript configuration
│   ├── next.config.mjs           # Next.js configuration
│   └── tailwind.config.js        # Tailwind CSS configuration
│
└── README.md                     # This file
```

## 🔧 Configuration

### Backend Configuration

Edit `backend/.env`:
```env
# OpenAI Configuration
OPENAI_API_KEY=your_key_here

# Optional: Model selection
OPENAI_MODEL=gpt-4-turbo-preview

# Optional: Audio settings
AUDIO_SAMPLE_RATE=16000
```

### Frontend Configuration

Edit `frontend/.env.local`:
```env
# Backend URL
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000

# Optional: Feature flags
NEXT_PUBLIC_ENABLE_FACE_DETECTION=true
NEXT_PUBLIC_ENABLE_AUDIO_VISUALIZATION=true
```

## 📊 API Endpoints

### POST `/transcribe`
Upload audio file for speech-to-text conversion.

**Request**: `multipart/form-data` with audio file
**Response**: JSON with transcribed Hindi text

### POST `/generate-response`
Generate AI response for given text and expression.

**Request**: JSON with `text` and optional `expression`
**Response**: JSON with AI response text

### POST `/synthesize`
Convert Hindi text to speech audio.

**Request**: JSON with `text`
**Response**: MP3 audio file

### POST `/detect-expression`
Detect facial expression from image.

**Request**: `multipart/form-data` with image file
**Response**: JSON with expression and confidence

### GET `/health`
Health check endpoint.

**Response**: `{"status": "healthy"}`
