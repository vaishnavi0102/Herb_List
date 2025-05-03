import mysql.connector # type: ignore

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="18022006@Hyd",
    database="medicinal_plants"
)
cursor = conn.cursor()

# Fetch plant data
cursor.execute("SELECT name, benefits FROM plants")
plants = cursor.fetchall()

# Overwrite or create the HTML file
with open("plants.html", "w", encoding="utf-8") as f:
    f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Healing Nature: The Power of Medicinal Plants</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { text-align: center; }
        .plant {
            border: 2px solid black;
            padding: 10px;
            margin: 10px auto;
            width: 300px;
            border-radius: 10px;
        }
        .plant-details {
            padding: 10px;
            margin-top: 10px;
            background-color: #f9f9f9;
            border-radius: 5px;
        }
        p { cursor: pointer; }
        p:hover { color: #008000; }
    </style>
</head>
<body>
    <h1>Healing Nature: The Power of Medicinal Plants 🌿✨</h1>
""")

    for name, benefits in plants:
        safe_id = name.lower().replace(" ", "-")
        f.write(f"""
    <div class="plant">
        <p onclick="toggleDetails('{safe_id}-details')">🌿 {name}</p>
        <div id="{safe_id}-details" class="plant-details" style="display: none;">
            <p><em>Benefits:</em> {benefits}</p>
        </div>
    </div>
""")

    f.write("""
    <script>
        function toggleDetails(plantId) {
            var details = document.getElementById(plantId);
            if (details.style.display === "none" || details.style.display === "") {
                details.style.display = "block";
            } else {
                details.style.display = "none";
            }
        }
    </script>
</body>
</html>
""")

print("✅ plants.html has been updated successfully!")

cursor.close()
conn.close()
