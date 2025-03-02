# AiCal

AiCal is an application that converts user prompts into `.ics` calendar files using AI.

## Demo

Try AiCal online at [www.ai-cal.xyz](https://www.ai-cal.xyz).

## Setup

1. Create virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Set up the environment variables by creating a `.env` file from `.env.example`:
   ```bash
   cp .env.example .env
   ```

3. Update the `.env` file with your OpenAI credentials:
   ```
   OPENAI_API_KEY=your_api_key
   OPENAI_BASE_URL=your_base_url
   MODEL=gpt-4o-mini or a different model
   ```

4. Run the application
   ```bash
   venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
    ```