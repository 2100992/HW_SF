<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="static/css/clock.css">
    <link href="https://fonts.googleapis.com/css?family=VT323&display=swap" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    <div class="page-wrapper">
        <div class="site-header">
            <div class="helper">
                <p>
                    ...<br>
                    — Откусишь с одной стороны — подрастешь, с другой — уменьшишься…<br>
                    — С одной стороны чего? И с другой стороны чего?!<br>
                    — ГРИБА!!<br>
                    ...
                </p>
            </div>
        </div>
        <div class="left-sidebar"></div>
        <div class="main">
            <div class="clock">
                <button id="minutes"><span id="tenMinutes">0</span><span id="unitMinutes">0</span></button>
                <button id="colonBut">:</button>
                <button id="seconds"><span id="tenSeconds">0</span><span id="unitSeconds">0</span></button>
            </div>
        </div>
        <div class="right-sidebar"></div>
        <div class="site-footer">
            <h2>hello</h2>
            <div class="htmlTest"></div>
        </div>
    </div>
    <h1></h1>
    <script src="static/js/jQueryMini.js"></script>
    <script src="static/js/clock.js"></script>
</body>
</html>