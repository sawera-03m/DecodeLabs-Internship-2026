# ==========================================================
# PROJECT 3: AI RECOMMENDATION LOGIC
# EcodeLabs Internship 2026
# ==========================================================

# Items with categories/tags
items = [
    {
        "name": "Python Programming Course",
        "category": "Programming",
        "tags": ["python", "coding", "software"]
    },
    {
        "name": "Web Development Course",
        "category": "Web",
        "tags": ["html", "css", "javascript", "coding"]
    },
    {
        "name": "Machine Learning Course",
        "category": "AI",
        "tags": ["ai", "machine learning", "python"]
    },
    {
        "name": "Cyber Security Course",
        "category": "Security",
        "tags": ["security", "cyber", "networking"]
    },
    {
        "name": "Data Science Course",
        "category": "Data",
        "tags": ["data", "python", "analytics"]
    },
    {
        "name": "Graphic Design Course",
        "category": "Design",
        "tags": ["design", "graphics", "creative"]
    }
]


# ----------------------------------------------------------
# RECOMMENDATION FUNCTION
# ----------------------------------------------------------

def recommend(user_preferences):

    recommendations = []

    for item in items:

        score = 0

        # Compare user preferences with item tags
        for preference in user_preferences:

            if preference.lower() in item["tags"]:
                score += 1

            # Also match category
            if preference.lower() == item["category"].lower():
                score += 1

        if score > 0:
            recommendations.append(
                (item["name"], item["category"], score)
            )

    # Sort recommendations by similarity score
    recommendations.sort(
        key=lambda x: x[2],
        reverse=True
    )

    return recommendations


# ----------------------------------------------------------
# DISPLAY RECOMMENDATIONS
# ----------------------------------------------------------

def show_recommendations(recommendations):

    print("\n==========================================")
    print("       RECOMMENDED ITEMS")
    print("==========================================")

    if not recommendations:
        print("No matching recommendations found.")
        return

    for i, recommendation in enumerate(recommendations, 1):

        name = recommendation[0]
        category = recommendation[1]
        score = recommendation[2]

        print(f"{i}. {name}")
        print(f"   Category: {category}")
        print(f"   Similarity Score: {score}")
        print()


# ----------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------

def main():

    print("==========================================")
    print("        AI RECOMMENDATION LOGIC")
    print("          EcodeLabs Internship")
    print("              Project 3")
    print("==========================================")

    print("\nAvailable interests:")
    print("Programming, Web, AI, Security, Data, Design")
    print("You can also enter tags like:")
    print("python, coding, networking, cyber, design")

    while True:

        print("\n------------------------------------------")

        user_input = input(
            "Enter your interests (comma separated): "
        )

        if user_input.lower() == "exit":
            print("\nThank you for using the recommendation system!")
            break

        # Convert input into preferences
        preferences = [
            item.strip().lower()
            for item in user_input.split(",")
        ]

        # Generate recommendations
        recommendations = recommend(preferences)

        # Display results
        show_recommendations(recommendations)

        print("Type 'exit' to close the program.")


# ----------------------------------------------------------
# START PROGRAM
# ----------------------------------------------------------

if __name__ == "__main__":
    main()