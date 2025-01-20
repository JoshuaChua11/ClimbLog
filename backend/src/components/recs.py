import openai
from components import roi

apiKey = None

def recs():
    """
    Utilises ROI function and data gained to prompt chatgpt and return with a recommended video/article based on user's
    current goal and current climbing grade. 

    Time Complexity: 
    - Best: O(1)
    - Worst: O(n) where n is the complexity of the response prompt return 
    """
    global apiKey

    if not apiKey:
        apiKey = input("Please enter your OpenAI API key: ").strip()
        openai.apiKey = apiKey  
    
    data = roi()  

    if not data:
        print("Cannot generate recommendations due to insufficient data.")
        return

    currentGrade = data["currentGrade"]
    nextGrade = data["nextGrade"]
    predictedDays = data["predictedDays"]

    prompt = (f"Based on the following climbing improvement data:\n"
              f"Current grade: {currentGrade}\n"
              f"Next target grade: {nextGrade}\n"
              f"Estimated time to achieve next grade: {predictedDays} days\n"
              "Recommend this boulderer a youtube video or an article that for their grade and the next targede can aid in their improvement.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a climbing coach providing detailed advice."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        print(f"\nAI Recommendations:\n{response.choices[0].message['content'].strip()}")

    except openai.error.AuthenticationError:
        print("Non-valid/Incorrect Key. Please check your OpenAI API key.")
        apiKey = None  