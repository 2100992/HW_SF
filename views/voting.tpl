% include('header.html', title='Page Title')
<body>
<script type="text/javascript">const serverURL = '{{ url }}'</script>
% include('navbar.html')
<main>
    <div class='container'>
        <h1>Голосование для сервера {{ url }}</h1>
        <h2>Выберите пожалуйста любимое домашнее животное</h2>
        <hr class="my-4">
        <div class = "container">
            <div class="voting">
                <button class="btn btn-secondary voting-btn" id="cats">Cats</button>
                <button class="btn btn-secondary voting-btn" id="dogs">Dogs</button>
                <button class="btn btn-secondary voting-btn" id="perrots">Perrots</button>
            </div>
        </div>
    </div>
</main>
% include('footer.html')
</body>