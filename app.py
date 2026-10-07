from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)


# ============================================================
# LOAD MACHINE LEARNING MODEL
# ============================================================

try:
    with open("career_model.pkl", "rb") as file:
        model_data = pickle.load(file)

    model = model_data["model"]
    encoder = model_data["encoder"]
    features = model_data["features"]

    print("Career model loaded successfully!")

except Exception as error:
    model = None
    encoder = None
    features = []

    print("Error loading model:", error)


# ============================================================
# CAREER INFORMATION
# ============================================================

career_profiles = {

    "AI/ML Engineer": {
        "category": "Artificial Intelligence",
        "description": "AI/ML Engineers build intelligent applications using artificial intelligence, machine learning and data.",
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "Mathematics",
            "Statistics",
            "Problem Solving"
        ],
        "projects": [
            "AI Chatbot",
            "Disease Prediction System",
            "Image Classification",
            "Recommendation System"
        ],
        "roadmap": [
            "Learn Python",
            "Learn NumPy and Pandas",
            "Learn Machine Learning",
            "Learn Deep Learning",
            "Build AI Projects",
            "Apply for AI/ML Internships"
        ]
    },

    "Machine Learning Engineer": {
        "category": "Artificial Intelligence",
        "description": "Machine Learning Engineers create, train and deploy machine learning models.",
        "skills": [
            "Python",
            "Machine Learning",
            "Statistics",
            "Data Processing",
            "Scikit-learn",
            "Model Deployment"
        ],
        "projects": [
            "House Price Prediction",
            "Spam Detection",
            "Customer Churn Prediction",
            "Recommendation System"
        ],
        "roadmap": [
            "Learn Python",
            "Learn Data Analysis",
            "Learn Machine Learning",
            "Learn Model Evaluation",
            "Build ML Projects",
            "Learn Model Deployment"
        ]
    },

    "Software Developer": {
        "category": "Software Development",
        "description": "Software Developers design, develop, test and maintain software applications.",
        "skills": [
            "Programming",
            "Data Structures",
            "Algorithms",
            "Problem Solving",
            "Git",
            "Software Development"
        ],
        "projects": [
            "Student Management System",
            "E-Commerce Website",
            "Library Management System",
            "Task Management Application"
        ],
        "roadmap": [
            "Learn Programming",
            "Learn Data Structures",
            "Learn Algorithms",
            "Learn Git and GitHub",
            "Build Projects",
            "Prepare for Interviews"
        ]
    },

    "Data Scientist": {
        "category": "Data Science",
        "description": "Data Scientists analyze data and use statistics and machine learning to discover useful insights.",
        "skills": [
            "Python",
            "Statistics",
            "Pandas",
            "Machine Learning",
            "Data Visualization",
            "SQL"
        ],
        "projects": [
            "Sales Prediction",
            "Customer Segmentation",
            "Sentiment Analysis",
            "Financial Data Analysis"
        ],
        "roadmap": [
            "Learn Python",
            "Learn Statistics",
            "Learn Pandas and NumPy",
            "Learn SQL",
            "Learn Machine Learning",
            "Build Data Science Projects"
        ]
    },

    "Data Analyst": {
        "category": "Data Science",
        "description": "Data Analysts transform raw data into useful business insights through analysis and visualization.",
        "skills": [
            "Excel",
            "SQL",
            "Python",
            "Pandas",
            "Data Visualization",
            "Statistics"
        ],
        "projects": [
            "Sales Dashboard",
            "Student Performance Analysis",
            "Customer Analysis",
            "Business Intelligence Dashboard"
        ],
        "roadmap": [
            "Learn Excel",
            "Learn SQL",
            "Learn Statistics",
            "Learn Python",
            "Learn Power BI or Tableau",
            "Build Data Analysis Projects"
        ]
    },

    "Business Analyst": {
        "category": "Business",
        "description": "Business Analysts use data and business knowledge to solve business problems and improve processes.",
        "skills": [
            "Communication",
            "Analytical Thinking",
            "Business Knowledge",
            "Data Analysis",
            "Problem Solving",
            "Presentation"
        ],
        "projects": [
            "Business Performance Dashboard",
            "Market Analysis",
            "Customer Requirement Analysis",
            "Sales Analysis"
        ],
        "roadmap": [
            "Understand Business Concepts",
            "Improve Communication",
            "Learn Excel",
            "Learn SQL",
            "Learn Data Visualization",
            "Practice Case Studies"
        ]
    },

    "UI/UX Designer": {
        "category": "Design",
        "description": "UI/UX Designers create user-friendly and visually appealing digital experiences.",
        "skills": [
            "Creativity",
            "UI Design",
            "UX Research",
            "Wireframing",
            "Prototyping",
            "Communication"
        ],
        "projects": [
            "Mobile App Design",
            "Website Redesign",
            "E-Commerce UI",
            "Portfolio Website"
        ],
        "roadmap": [
            "Learn Design Principles",
            "Learn Figma",
            "Practice Wireframing",
            "Learn UX Research",
            "Build Design Portfolio",
            "Apply for Internships"
        ]
    },

    "Graphic Designer": {
        "category": "Design",
        "description": "Graphic Designers create visual content for digital and print media.",
        "skills": [
            "Creativity",
            "Typography",
            "Color Theory",
            "Graphic Design",
            "Branding",
            "Visual Communication"
        ],
        "projects": [
            "Brand Identity",
            "Poster Design",
            "Social Media Designs",
            "Logo Design"
        ],
        "roadmap": [
            "Learn Design Basics",
            "Learn Photoshop or Illustrator",
            "Practice Typography",
            "Practice Branding",
            "Create Portfolio",
            "Apply for Design Jobs"
        ]
    },

    "Project Manager": {
        "category": "Management",
        "description": "Project Managers plan, organize and manage projects, teams, deadlines and resources.",
        "skills": [
            "Leadership",
            "Communication",
            "Planning",
            "Problem Solving",
            "Team Management",
            "Time Management"
        ],
        "projects": [
            "Project Planning Dashboard",
            "Team Management System",
            "Agile Project Simulation",
            "Task Tracking Application"
        ],
        "roadmap": [
            "Improve Communication",
            "Learn Project Management",
            "Learn Agile and Scrum",
            "Develop Leadership",
            "Manage Small Projects",
            "Prepare for Certifications"
        ]
    },

    "Web Developer": {
        "category": "Web Development",
        "description": "Web Developers create websites and web applications using frontend and backend technologies.",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "Python",
            "Flask",
            "Database"
        ],
        "projects": [
            "Portfolio Website",
            "E-Commerce Website",
            "Blog Application",
            "Student Portal"
        ],
        "roadmap": [
            "Learn HTML",
            "Learn CSS",
            "Learn JavaScript",
            "Learn Backend Development",
            "Learn Databases",
            "Build Full Projects"
        ]
    },

    "Marketing Analyst": {
        "category": "Marketing",
        "description": "Marketing Analysts use data to understand customers, markets and marketing performance.",
        "skills": [
            "Communication",
            "Analytics",
            "Statistics",
            "Market Research",
            "Data Visualization",
            "Business Knowledge"
        ],
        "projects": [
            "Customer Segmentation",
            "Marketing Campaign Analysis",
            "Social Media Analytics",
            "Market Research Dashboard"
        ],
        "roadmap": [
            "Learn Marketing Basics",
            "Learn Data Analysis",
            "Learn Statistics",
            "Learn Customer Analytics",
            "Practice Market Research",
            "Build Marketing Portfolio"
        ]
    }
}


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# ASSESSMENT
# ============================================================

@app.route("/assessment")
def assessment():
    return render_template("assessment.html")


# ============================================================
# CAREERS
# ============================================================

@app.route("/careers")
def careers():
    return render_template(
        "careers.html",
        career_profiles=career_profiles
    )


# ============================================================
# ROADMAP
# ============================================================

@app.route("/roadmap")
def roadmap():
    return render_template(
        "roadmap.html",
        career_profiles=career_profiles
    )


# ============================================================
# PREDICT CAREER
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ----------------------------------------------------
        # GET USER INPUT
        # ----------------------------------------------------

        math = float(request.form.get("math", 0))
        programming = float(request.form.get("programming", 0))
        communication = float(request.form.get("communication", 0))
        creativity = float(request.form.get("creativity", 0))
        analytical = float(request.form.get("analytical", 0))
        leadership = float(request.form.get("leadership", 0))

        values = [
            math,
            programming,
            communication,
            creativity,
            analytical,
            leadership
        ]

        # ----------------------------------------------------
        # VALIDATE INPUT
        # ----------------------------------------------------

        for value in values:

            if value < 0 or value > 100:

                return """
                <h2>Invalid Input</h2>
                <p>Please enter values between 0 and 100.</p>
                <a href="/assessment">Go Back</a>
                """

        # ----------------------------------------------------
        # CHECK MODEL
        # ----------------------------------------------------

        if model is None or encoder is None:

            return """
            <h2>Model Error</h2>
            <p>The Machine Learning model could not be loaded.</p>
            <a href="/assessment">Go Back</a>
            """

        # ----------------------------------------------------
        # CREATE INPUT DATAFRAME
        # ----------------------------------------------------

        input_data = pd.DataFrame([{

            "math": math,
            "programming": programming,
            "communication": communication,
            "creativity": creativity,
            "analytical": analytical,
            "leadership": leadership

        }])

        # ----------------------------------------------------
        # MACHINE LEARNING PREDICTION
        # ----------------------------------------------------

        prediction = model.predict(input_data)

        career = encoder.inverse_transform(prediction)[0]

        # ----------------------------------------------------
        # PREDICTION PROBABILITIES
        # ----------------------------------------------------

        probabilities = model.predict_proba(input_data)[0]

        classes = encoder.inverse_transform(
            model.classes_
        )

        recommendation_data = []

        for career_name, probability in zip(
            classes,
            probabilities
        ):

            recommendation_data.append({

                "career": career_name,

                "score": round(
                    probability * 100,
                    2
                )

            })

        # Highest scores first

        recommendation_data.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        # Top five recommendations

        recommendations = recommendation_data[:5]

        # ----------------------------------------------------
        # CAREER DETAILS
        # ----------------------------------------------------

        details = career_profiles.get(
            career,
            {
                "category": "Career",
                "description": "Explore this career path and develop the required skills.",
                "skills": [],
                "projects": [],
                "roadmap": []
            }
        )

        # ----------------------------------------------------
        # USER SKILLS
        # ----------------------------------------------------

        skill_scores = {

            "Mathematics": math,

            "Programming": programming,

            "Communication": communication,

            "Creativity": creativity,

            "Analytical Thinking": analytical,

            "Leadership": leadership

        }

        # ----------------------------------------------------
        # SORT SKILLS
        # ----------------------------------------------------

        sorted_skills = sorted(
            skill_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Top three strengths

        strengths = [
            skill
            for skill, score in sorted_skills[:3]
        ]

        # Three skills to improve

        gaps = [
            skill
            for skill, score in sorted_skills[-3:]
        ]

        # ----------------------------------------------------
        # OVERALL SCORE
        # ----------------------------------------------------

        overall_score = round(
            sum(values) / len(values)
        )

        # ----------------------------------------------------
        # MOTIVATIONAL MESSAGE
        # ----------------------------------------------------

        if overall_score >= 85:

            motivation = (
                "Excellent potential! Your skill profile shows "
                "strong career readiness. Keep developing your "
                "skills and build real-world projects."
            )

        elif overall_score >= 70:

            motivation = (
                "Great progress! You have a strong foundation. "
                "Focus on improving your skill gaps and continue "
                "practicing."
            )

        elif overall_score >= 50:

            motivation = (
                "You are on the right path! Keep learning "
                "consistently and strengthen your core skills."
            )

        else:

            motivation = (
                "Every expert starts somewhere. Start with the "
                "basics, practice regularly and improve one "
                "skill at a time."
            )

        # ----------------------------------------------------
        # SHOW RESULT PAGE
        # ----------------------------------------------------

        return render_template(

            "result.html",

            career=career,

            details=details,

            recommendations=recommendations,

            strengths=strengths,

            gaps=gaps,

            motivation=motivation,

            overall_score=overall_score,

            skill_scores=skill_scores

        )

    except Exception as error:

        print("Prediction error:", error)

        return f"""
        <h2>Something went wrong</h2>

        <p>{error}</p>

        <br>

        <a href="/assessment">
            Return to Assessment
        </a>
        """


# ============================================================
# START FLASK SERVER
# ============================================================

if __name__ == "__main__":

    print("")
    print("==============================================")
    print(" AI-Based Smart Career Guidance Portal")
    print("==============================================")
    print("")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )