% include('header.html', title='Page Title')
<body>
<main>
    <div class='container'>
        % include('navbar.html')
        <div class="jumbotron">
            <h1 class="display-4">Результаты голосования</h1>
            <p class="lead">Нужны результаты</p>
            <hr class="my-4">
            <p> {{ url }}
            </p>
            <ul class="list-group">
            </ul>
        </div>
    </div>
</main>
% include('footer.html')
</body>