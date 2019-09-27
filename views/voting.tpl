% include('header.html', title='Page Title')
<body>
<script type="text/javascript">const serverURL = '{{ url }}'</script>
<div class='container'>
% include('navbar.html')
</div>
<main>
    <div class='container'>
        <h1>Голосование для сервера {{ url }}</h1>
        <h2>Выберите пожалуйста любимое домашнее животное</h2>
        <hr class="my-4">
        <div class = "container">
            <div class="voting">
                <button class="btn btn-secondary voting-btn" id="cats">Cats</button>
                <button class="btn btn-secondary voting-btn" id="dogs">Dogs</button>
                <button class="btn btn-secondary voting-btn" id="parrots">Parrots</button>
            </div>
        </div>
    </div>
</main>
% include('footer.html')
<script src="/static/js/jQueryMini.js"></script>
<script src="/static/js/voting.js"></script>
</body>