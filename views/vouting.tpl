% include('header.html', title='Page Title')
<body>
<main>

    <script type="text/javascript">const serverURL = '{{ url }}'</script>

    <div class='container'>
        % include('navbar.html')
        <div class="jumbotron">
            <h1 class="display-4">Выберите пожалуйста любимое домашнее животное</h1>
            <p class="lead">______</p>
            <hr class="my-4">
            <div class = "container">
                <div class="voting">
                    <button id="cats">Cats</button>
                    <button id="dogs">Dogs</button>
                    <button id="perrots">Perrots</button>
                </div>
            </div>
            <ul class="list-group">
            </ul>
        </div>
    </div>
</main>
% include('footer.html')
</body>