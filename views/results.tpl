% include('header.html', title='Page Title')
<body>
<script type="text/javascript">
    const MyServerURL = '{{ url }}'
    const SFServerURL = '{{ urlSF }}'
</script>
% include('navbar.html')
<main>
    <div class='container'>
        <h1>Результаты голосования</h1>
        <hr class="my-4">

        <div class="wrapper">
            <div class="sf-header"><h3>Результаты на сервере SkillFactory</h3></div>
            <div class="sf-results">
                <p>Собаки</p>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" id="SFDogs">25%</div>
                </div>
                <p>Кошки</p>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" id="SFCats">25%</div>
                </div>
                <p>Попугаи</p>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" id="SFParrots">25%</div>
                </div>
            </div>
            <div class="my-header"><h3>Результаты на нашем сервере</h3></div>
            <div class="my-results">
                <p>Собаки</p>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" id="MyDogs">25%</div>
                </div>
                <p>Кошки</p>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" id="MyCats">25%</div>
                </div>
                <p>Попугаи</p>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"id="MyParrots">25%</div>
                </div>
            </div>

        </div>
    </div>
</main>
% include('footer.html')
<script src="/static/js/results.js"></script>
</body>