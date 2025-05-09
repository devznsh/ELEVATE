# 🚀 ELEVATE - AI Career Path Recommender

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://elevatesystem.streamlit.app/)
![GitHub last commit](https://img.shields.io/github/last-commit/devznsh/ELEVATE)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

ELEVATE is an AI-powered career guidance system that recommends personalized career paths, required skills, and learning roadmaps based on your interests and goals.

## ✨ Features

- **AI-Powered Recommendations**: BERT-based semantic matching for accurate career suggestions
- **Personalized Roadmaps**: Custom 6-12 month learning paths for each career
- **Skill Gap Analysis**: Identifies key skills needed for your target roles
- **Resource Curation**: Recommends top courses, books, and communities
- **Responsive Design**: Optimized for desktop and mobile

## 🛠️ Tech Stack

| Component          | Technology |
|--------------------|------------|
| Frontend           | Streamlit  |
| AI Models          | BERT, Sentence Transformers |
| Backend            | Python 3.10+ |
| Deployment         | Streamlit Community Cloud |
| Data Processing    | Pandas, NumPy |

## 📂 Project Structure

```
ELEVATE/
├── app/                      # Main application directory
│   ├── __init__.py           # Python package marker
│   ├── main.py               # Streamlit application entry point
│   ├── models/               # AI recommendation models
│   │   ├── __init__.py       # Package initialization
│   │   ├── bert_recommender.py  # BERT-based career recommendation engine
│   │   └── roadmap_generator.py # Learning path generator
│   ├── data/                 # Career datasets and knowledge base
│   │   ├── __init__.py
│   │   ├── careers.csv       # Career profiles and skills data
│   │   └── roadmaps.json     # Learning roadmaps for each career
│   ├── static/               # Static assets
│   │   ├── css/
│   │   │   └── style.css     # Custom styles
│   │   └── images/           # App images/logos
│   └── utils/                # Utility functions
│       ├── __init__.py
│       ├── config.py         # Application configuration
│       └── helpers.py        # Helper functions
├── .gitignore               # Specifies untracked files
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 💻 Local Development

### Prerequisites
- Python 3.10+
- Git
- pip

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/devznsh/ELEVATE.git
   cd ELEVATE
2. Create and activate virtual environment
  ```bash
   python -m venv venv
  # On Windows:
  .\venv\Scripts\activate
  # On Mac/Linux:
  source venv/bin/activate
```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
    ```
    streamlit run app/main.py
    ```
📊 Data Model
The system uses:

50+ career profiles with skill requirements

100+ learning resources

Dynamic roadmap generation based on:

Fundamentals → Specialization → Real-world projects

🎯 Roadmap
Initial Release

Add more career paths

Integrate job market data

User account system

Skill assessment quizzes

