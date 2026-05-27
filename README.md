# Note Summary and Quiz Generator

A Streamlit web application that uses Google's Gemini AI to generate summaries and quizzes from uploaded note images. The app provides:

- **Note Generation**: AI-powered summaries in Bangla from uploaded images
- **Audio Transcription**: Text-to-speech conversion of the generated notes
- **Quiz Generation**: Customizable quizzes based on the content with difficulty levels (Easy, Medium, Hard)

## Live Demo

Check out the live application: [https://note-generator-q.streamlit.app/](https://note-generator-q.streamlit.app/)

## Features

- Upload up to 3 images of your notes
- Generate concise note summaries (max 100 words) in Bangla
- Convert notes to audio using Google Text-to-Speech
- Create quizzes with three difficulty levels
- Automatic answer key for each quiz

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd streamlit-gemini
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install streamlit google-genai python-dotenv gtts Pillow
   ```

## Configuration

1. Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

2. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

Run the application:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## How It Works

1. **Upload Images**: Select up to 3 images containing your notes
2. **Choose Difficulty**: Select quiz difficulty (Easy, Medium, or Hard)
3. **Generate**: Click the button to initiate AI processing
4. **View Results**: 
   - Note summary in Bangla
   - Audio playback of the summary
   - Quiz questions with correct answers

## Dependencies

- `streamlit` - Web application framework
- `google-genai` - Google Gemini AI API
- `python-dotenv` - Environment variable management
- `gtts` - Google Text-to-Speech
- `Pillow` - Image processing

## Project Structure

```
streamlit-gemini/
├── app.py              # Main Streamlit application
├── api_calling.py      # Gemini API integration functions
├── .env                # API key configuration (not committed)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## License

This project is open source and available under the MIT License.