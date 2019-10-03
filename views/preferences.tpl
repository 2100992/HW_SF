% include('header.html', title='Page Title')
<body>
<div class=''>
% include('navbar.html')
</div>
<main>
    <div class="container grid-wrapper">
        <div class='container main'>
            <h2>Проверка домашнего задания по модулю С3</h2>
            <p>Галочки предпочтений</p>

            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
                <label class="form-check-label" for="defaultCheck1">
                    Вы можете поставить тут галочку
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="defaultCheck2">
                <label class="form-check-label" for="defaultCheck2">
                    И тут тоже
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="defaultCheck3">
                <label class="form-check-label" for="defaultCheck3">
                    И еще одну
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="defaultCheck4">
                <label class="form-check-label" for="defaultCheck4">
                    А эта галочка ничего не значит
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="defaultCheck5">
                <label class="form-check-label" for="defaultCheck5">
                    Как и эта
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="defaultCheck6">
                <label class="form-check-label" for="defaultCheck6">
                    Самая неважная галочка
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="defaultCheck7">
                <label class="form-check-label" for="defaultCheck7">
                    Запомнить ваше мнение
                </label>
            </div>
            <!-- <hr class="my-4"> -->
            <!-- <a href="/sfvoting" class="btn btn-secondary btn-lg active" role="button" aria-pressed="true">Сервер SkillFactory</a>
            <a href="/voting" class="btn btn-secondary btn-lg active" role="button" aria-pressed="true">Этот сервер</a> -->
        </div>
        % include('navC3.html')
    </div>
</main>


% include('footer.html')
<script src="/static/js/cookie.js"></script>
<script src="/static/js/preferences.js"></script>
</body>
</html>