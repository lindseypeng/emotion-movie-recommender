# 🎬 Emotion-Based Movie Recommender

> **✨ This project explores the trade-off between optimizing for accuracy (past behavior) and enabling human discovery (future growth).**
> 
> - Optimizing for clicks and past behavior can limit discovery  
> - Recommenders risk becoming echo chambers of taste  
> - We shift from predicting behavior to supporting emotional growth  
> - This tool helps people **name and explore** feelings — not just repeat them  
> 
> 💡 *Can we build a system that helps people say:*  
> “**That’s exactly how I needed to feel — and I didn’t even know it.**”

---

## 🔍 Problem

Traditional recommender systems often suggest movies by:
- Genre (e.g. "comedy", "thriller")
- User behavior (e.g. watch history, ratings)

But:
- **Genre ≠ emotional experience** — people crave specific emotional textures like "quiet intimacy" or "bittersweet closure"
- **Behavior ≠ true preference** — what users have watched may reflect social norms, not authentic taste

This project aims to recommend movies based on **emotional resonance**, not just past behavior.

---

## 🧠 Methodology

### 1. **Emotional Tagging with LLM**
We used the OpenAI API to tag ~5,000 TMDb movies using four emotional dimensions:

```json
{
  "title": "Movie Title",
  "emotional_experience": ["deep grief", "hopeful release"],
  "relational_themes": ["estranged siblings"],
  "life_moments": ["coming to terms with loss"],
  "aesthetic": ["muted tones", "slow pacing"]
}
```

### 2. **Embedding & Similarity Matching**
- Transformed tags into vector embeddings
- Stored movie vectors locally in a pickle-based database
- Compared user input embedding using **cosine similarity**
- Returned top 3 emotionally aligned movies

### 3. **User Interface**
- Lightweight app (e.g. Streamlit or CLI)
- Users describe the emotion they want to feel
- System recommends emotionally matched films

---

## 💡 Why Cosine Similarity?
Cosine similarity compares **angle** (not length) between vectors — perfect for capturing **semantic alignment** in text-based embeddings.  
Other distances (e.g. Euclidean) can distort meaning by over-weighting magnitude, especially in high-dimensional space.

---

## 📊 Evaluation (or Lack Thereof)

No traditional evaluation (e.g. Precision@K) was performed because:
- Emotional fit is **subjective**
- Standard metrics require labeled ground truth, which we don’t have

### Future Evaluation Ideas:
- Collect **thumbs up/down** feedback from users
- Ask: *“Did this match how you wanted to feel?”*
- Track engagement over time and refine tag quality

---

## 🔄 Lessons & Next Steps

### Optimizing vs. Exploring
- Traditional recommenders optimize for past behavior — but risk limiting discovery
- Our goal: build tools that help users **name and explore** emotional needs, not just reinforce them

> 💬 *“Success isn’t just relevance — it’s resonance.”*

### Next Steps
- Add user feedback loop
- Improve emotional tag consistency with multi-rater checks or LLM validation
- Let users **tag themselves emotionally** to personalize recommendations

---

## 📁 Project Structure

```
emotion_recommender/
├── data/                     # Raw and processed TMDb data
├── tagging/                  # LLM API tagging scripts
├── embedding/                # Embedding generation + similarity matching
├── app/                      # User-facing app (e.g. Streamlit)
├── utils/                    # Helper functions
└── README.md                 # This file
```

---

## 🤝 Acknowledgements

Inspired by conversations about taste, art, and emotional truth — thank you to friends who challenged the algorithmic way of seeing.

---

## 📬 Contact

Feel free to reach out with questions, suggestions, or emotional movie recs!  
[Your Name] – [your.email@example.com] – [LinkedIn or GitHub link]
