template = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
    <div class="top-bar" style="background-color:#DCDCDC; height: 50px; width: 100%; position: fixed"></div>
    <!--
    <h2 style="color:#32CD32; justify-content: center; ">Success!</h2>
    <h2>Your token is: {{ token }}</h2><br><br>
    It expires at {{ expires }}
    -->
    <div style="margin-top: 0px; padding: 50px;"> <!-- 60px to account for top bar and some extra space -->
        <h2 style="color:#32CD32; text-align: center;">Success!</h2>
        <!--<h2 style="text-align: center;">Your token is: {{ token }}</h2>-->
        <div class="container">
            <div class="input-group">
                <span class="input-group-addon hidden-xs linkname">
                    <strong>My link</strong>
                </span>
                <span id="copyButton" class="input-group-addon btn" title="Click to copy">
                    <i class="fa fa-clipboard" aria-hidden="true"></i>
                </span>
                <input type="text" id="copyTarget" class="form-control" value="{{ token }}">
                <span class="copied">Copied !</span>
            </div>
        </div>
        <p style="text-align: center;">It expires at {{ expires }}</p>
    </div>
</body>
    <style>
        .input-group {
            margin-top: 30px;
            position: relative;
        }

        .input-group-addon {
            border: none;
        }

        .linkname {
            display: none;
        }

        #copyButton {
            cursor: pointer;
            background: #f1bb3a;
        }

        #copyTarget {
            border-left: none;
        }

        .copied {
            opacity: 1;
            position: absolute;
            left: 55px;
        }

        @media (min-width: 768px) {
            .copied {
                left: 135px;
            }

            .linkname {
                display: block;
                background: #3b3e45;
                color: #fff;
            }
        }
    </style>
</html>

"""