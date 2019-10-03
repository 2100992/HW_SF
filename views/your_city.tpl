% include('header.html', title='Page Title')
<body>
<div class=''>
% include('navbar.html')
</div>
<main>
    <div class="container grid-wrapper">
        <div class='container main'>
            <h2>Проверка домашнего задания по модулю С3</h2>

            <div class="is-known d-none">

                <p>Ваш город — <span id="your-city"></span></p>
                <form>
                    <button type="submit" class="btn btn-primary" id="rem-city">Забыть город</button>
                </form>
            </div>

            <div class="is-unknown d-none">
                <form>
                    <div class="form-group">
                        <label for="input-city">Укажите Ваш город</label>
                        <input type="text" class="form-control" id="input-city" aria-describedby="emailHelp" placeholder="Ваш город">
                        <small id="cityHelp" class="form-text text-muted">Мы никому не расскажем.</small>
                    </div>
                    <button type="submit" class="btn btn-primary" id="set-city">Запомнить город</button>
                </form>
            </div>
        </div>
        % include('navC3.html')
    </div>
</main>

% include('footer.html')
<script src="/static/js/cookie.js"></script>
<script src="/static/js/your_city.js"></script>
</body>
</html>