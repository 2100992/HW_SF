% include('header.html', title='Page Title')
<body>
<script type="text/javascript">const serverURL = '{{ url }}'</script>
<div class=''>
% include('navbar.html')
</div>
<main>
    <div class="container grid-wrapper">
        <div class='container main'>
            <h2>Голосование для сервера</h2>
            <h3>{{ url }}</h3>
            <hr class="my-4">
            <h3>Выберите пожалуйста любимое домашнее животное</h3>
            <div class = "container">
                <div class="voting">
                    <button class="btn btn-secondary voting-btn" id="cats">Кот</button>
                    <button class="btn btn-secondary voting-btn" id="dogs">Собака</button>
                    <button class="btn btn-secondary voting-btn" id="parrots">Попугай</button>
                </div>
            </div>
            <hr class="my-4">
        </div>
        % include('navC2.html')
    </div>
</main>

% include('footer.html')
<!-- <script src="/static/js/jQueryMini.js"></script> -->
<script src="/static/js/voting.js"></script>
</body>
</html>