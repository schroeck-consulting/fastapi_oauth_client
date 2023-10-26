template = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
    <div class="top-bar" style="background-color:#DCDCDC; height: 50px; width: 100%; position: fixed"></div>
    <div style="margin-top: 0px; padding: 50px;">
        <h2 style="color:#32CD32; text-align: center;">Success!</h2>
        <div class="container">
            <div class="input-group">
                <span id="copyButton" onclick="copyText()" class="input-group-addon btn" title="Click to copy">Copy
                    <i class="fa fa-clipboard" aria-hidden="true"></i>
                    <script>
                    function copyText() {
                    
                        // Get the div element
                        var divElement = document.getElementById("copyTarget");

                        // Create a range object
                        var range = document.createRange();

                        // Select the contents of the div element
                        range.selectNode(divElement);

                        // Add the range to the user's selection
                        window.getSelection().addRange(range);

                        // Copy the selected text to the clipboard
                        document.execCommand("copy");

                        // Give a visual feedback to the user that the text has been copied
                        alert("Token has been copied!");
                        
                    }
                    </script>
                </span>

                <input type="text" id="copyTarget" class="form-control" value="{{ token }}">
            </div>
        </div>
        <p style="text-align: center;">It expires at {{ expires }}</p>
        <h5 style="text-align: center;">How to use</h5>
        <p style="text-align: center;">
        How to use - placeholder
        </p>
    </div>
</body>
    <style>
        .input-group {
            margin-top: 30px;
            position: relative;
        }
        
        #copyButton {
            cursor: pointer;
            background: #f1bb3a;
        }
    </style>
</html>

"""