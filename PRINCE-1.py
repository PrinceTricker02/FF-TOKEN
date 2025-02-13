<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Token Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-image: url('/static/fara.jpg'); /* Replace with your image URL */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
            min-height: 100vh;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            background-color: rgna(0, 255, 0, 1); /* Semi-transparent background */
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgna(0, 0, 0, 0.5);
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
            font-weight: bold;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            font-size: 16px;
            margin-bottom: 8px;
            display: block;
            color: #ddd;
        }
        .form-group input, .form-group select {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 6px;
            background-color: #f2f2f2;
        }
        .form-group select {
            cursor: pointer;
        }
        .form-group button {
            width: 100%;
            padding: 12px;
            background-color: #0d6efd;
            color: white;
            border: none;
            font-size: 16px;
            cursor: pointer;
            border-radius: 6px;
            transition: all 0.3s ease;
        }
        .form-group button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background-color: rgba(0, 128, 0, 0.8);
            border-radius: 6px;
            word-wrap: break-word;
        }
        hr {
            border: 1px solid #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Facebook Token Generator</h1>
        
        <!-- Dropdown to Select Option -->
        <div class="form-group">
            <label for="action">Choose an Action:</label>
            <select id="action" name="action" class="form-select" onchange="showForm()">
                <option value="">Select Action</option>
                <option value="generate_token">Generate Token from Cookie</option>
                <option value="generate_page_tokens">Generate Page Tokens from Token</option>
                <option value="generate_page_tokens_from_cookie">Generate Page Tokens from Cookie</option>
            </select>
        </div>

        <!-- Form for generating token from cookie -->
        <form action="/generate_token" method="POST" id="generate_token_form" class="form-group" style="display:none;">
            <label for="cookie">Enter Your Cookie</label>
            <input type="text" id="cookie" name="cookie" class="form-control" required>
            <button type="submit" class="btn btn-primary mt-3">Generate Token</button>
        </form>
        
        <!-- Form for generating page tokens from token -->
        <form action="/generate_page_tokens" method="POST" id="generate_page_tokens_form" class="form-group" style="display:none;">
            <label for="access_token">Enter Your Access Token</label>
            <input type="text" id="access_token" name="access_token" class="form-control" required>
            <button type="submit" class="btn btn-primary mt-3">Generate Page Tokens</button>
        </form>
        
        <!-- Form for generating page tokens from cookie -->
        <form action="/generate_page_tokens_from_cookie" method="POST" id="generate_page_tokens_from_cookie_form" class="form-group" style="display:none;">
            <label for="cookie">Enter Your Cookie</label>
            <input type="text" id="cookie" name="cookie" class="form-control" required>
            <button type="submit" class="btn btn-primary mt-3">Generate Page Tokens</button>
        </form>

        

        
    </div>

    <script>
        function showForm() {
            var action = document.getElementById("action").value;
            
            // Hide all forms first
            document.getElementById("generate_token_form").style.display = "none";
            document.getElementById("generate_page_tokens_form").style.display = "none";
            document.getElementById("generate_page_tokens_from_cookie_form").style.display = "none";
            
            // Show the selected form
            if (action === "generate_token") {
                document.getElementById("generate_token_form").style.display = "block";
            } else if (action === "generate_page_tokens") {
                document.getElementById("generate_page_tokens_form").style.display = "block";
            } else if (action === "generate_page_tokens_from_cookie") {
                document.getElementById("generate_page_tokens_from_cookie_form").style.display = "block";
            }
        }
    </script>
</body>
</html>