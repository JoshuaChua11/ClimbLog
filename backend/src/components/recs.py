from flask import Flask, jsonify, request
import pandas as pd

def recs():
    app = Flask(__name__)

    # Endpoint to retrieve the logbook
    @app.route("/logbook", methods=["GET"])
    def get_logbook():
        """
        Fetch the logbook as a JSON response.
        """
        try:
            data = pd.read_csv("logbook.csv").to_dict(orient="records")
            return jsonify(data)
        except FileNotFoundError:
            return jsonify({"error": "Logbook not found"}), 404

    # Endpoint to get recommendations based on climbing grade
    @app.route("/recommendations", methods=["GET"])
    def get_recommendations():
        """
        Provides climbing recommendations based on the user's current climbing data.
        """
        try:
            # Load the logbook
            logbook = pd.read_csv("logbook.csv")

            if logbook.empty:
                return jsonify({"error": "Logbook is empty. Log some climbs first."}), 400

            # Determine the user's highest logged grade
            grades = {
                "V0": 1, "V1": 2, "V2": 4, "V3": 8, "V4": 16, "V5": 32,
                "V6": 64, "V7": 128, "V8": 256, "V9": 512, "V10": 1024,
                "V11": 2048, "V12": 4096, "V13": 8192, "V14": 16384
            }
            logbook['difficulty'] = logbook['logged_grade'].map(grades)
            max_difficulty = logbook['difficulty'].max()
            current_grade = logbook.loc[logbook['difficulty'] == max_difficulty, 'logged_grade'].iloc[0]

            # Suggest climbs at the next grade level
            next_difficulty = max_difficulty * 2
            next_grade = next((grade for grade, diff in grades.items() if diff == next_difficulty), None)

            if not next_grade:
                return jsonify({"message": "You've reached the highest grade we can recommend. Congratulations!"})

            # Dummy recommendations for demonstration
            recommendations = [
                {"board": "kilter", "angle": 45, "climb_name": "Advanced Sloper", "grade": next_grade},
                {"board": "tension", "angle": 40, "climb_name": "Dynamic Reach", "grade": next_grade},
            ]

            return jsonify({
                "current_grade": current_grade,
                "next_grade": next_grade,
                "recommendations": recommendations
            })

        except FileNotFoundError:
            return jsonify({"error": "Logbook not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Run the Flask app
    app.run(debug=True, port=5000)