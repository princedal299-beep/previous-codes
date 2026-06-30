from google import genai

API_KEY = "AQ.Ab8RN6Iy5jANjxHg06Iv3Oob-YHzfQm6cYbNN2XXL9Q2TQul6Q"

MODEL = "gemini-2.5-flash"

client = genai.Client(api_key=API_KEY)

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    print("Sending request...")

    response = client.models.generate_content(
        model=MODEL,
        contents=user
    )

    print("Bot:", response.text)