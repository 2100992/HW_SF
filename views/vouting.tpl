% include('header.html', title='Page Title')
<body>
<main>
    <div class='container'>
        % include('navbar.html')
        <div class="jumbotron">
            <h1 class="display-4">Музопоиск!</h1>
            <p class="lead">Здесь вы найдете информацию о альбомах записанных музыкальными группами.</p>
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