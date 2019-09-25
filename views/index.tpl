% include('header.html', title='Page Title')
<body>
% include('navbar.html')
<main>
    <div class='container'>
        <h1>Голосовалка</h1>
        <p>Выберите где вы хотите проголосовать</p>
        <hr class="my-4">
        <a href="/sfvoting" class="btn btn-secondary btn-lg active" role="button" aria-pressed="true">Сервер SkillFactory</a>
        <a href="/voting" class="btn btn-secondary btn-lg active" role="button" aria-pressed="true">Этот сервер</a>
    </div>
</main>
% include('footer.html')
</body>