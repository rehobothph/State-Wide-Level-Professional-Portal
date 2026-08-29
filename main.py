from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>State-Wide Level Professional Portal</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f6f9; color: #333; }
        header { background-color: #1e3a8a; color: white; padding: 20px; text-align: center; }
        nav { background: #0f172a; padding: 10px; text-align: center; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
        .container { max-width: 900px; margin: 30px auto; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h2 { color: #1e3a8a; }
        .card-container { display: flex; gap: 15px; margin-top: 20px; }
        .card { flex: 1; padding: 15px; background: #e2e8f0; border-radius: 6px; text-align: center; }
        footer { text-align: center; padding: 15px; background: #1e3a8a; color: white; position: fixed; bottom: 0; width: 100%; }
    </style>
</head>
<body>

<header>
    <h1>State-Wide Level Professional Portal</h1>
    <p>Connecting Professionals & Services Across the State</p>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">Services</a>
    <a href="#">Directory</a>
    <a href="#">Contact</a>
</nav>

<div class="container">
    <h2>Welcome to the Portal</h2>
    <p>This state-wide platform empowers professionals, organizations, and citizens to seamlessly access resources and services.</p>
    
    <h3>Key Features</h3>
    <div class="card-container">
        <div class="card">
            <h4>Professional Verification</h4>
            <p>Verified profile management for skilled experts.</p>
        </div>
        <div class="card">
            <h4>Resource Hub</h4>
            <p>Access guidelines, updates, and state documents.</p>
        </div>
        <div class="card">
            <h4>Network & Connect</h4>
            <p>Direct portal communication for fast collaboration.</p>
        </div>
    </div>
</div>

<footer>
    <p>&copy; 2026 State-Wide Professional Portal | All Rights Reserved</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)
