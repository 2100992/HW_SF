% include('header.html', title='Page Title')
<body>
<div class=''>
% include('navbar.html')
</div>
<main>
    <div class="container grid-wrapper">
        <div class='container main'>
            <h2>Голосование за любимое домашнее животное</h2>
            <p>Выберите где вы хотите оставить свой голос</p>
            <!-- <hr class="my-4"> -->
            <!-- <a href="/sfvoting" class="btn btn-secondary btn-lg active" role="button" aria-pressed="true">Сервер SkillFactory</a>
            <a href="/voting" class="btn btn-secondary btn-lg active" role="button" aria-pressed="true">Этот сервер</a> -->
        </div>
        % include('navC2.html')
    </div>
</main>

% include('footer.html')
</body>
</html>