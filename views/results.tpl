% include('header.html', title='Page Title')
<body>
<script type="text/javascript">
    const MyServerURL = '{{ url }}'
    const SFServerURL = '{{ urlSF }}'
</script>
<div class='container'>
% include('navbar.html')
</div>
<main>
    <div class="container grid-wrapper">
        % include('navC2.html')
        <div class='container main'>
            <h1>Результаты голосования</h1>
            <hr class="my-4">

            <div class="wrapper">
                <div class="sf-header"><h3>Результаты на сервере SkillFactory</h3></div>
                <div class="sf-results">
                    <p>Собаки</p>
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" id="SFDogs">0</div>
                    </div>
                    <p>Кошки</p>
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" id="SFCats">0</div>
                    </div>
                    <p>Попугаи</p>
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" id="SFParrots">0</div>
                    </div>
                </div>
                <div class="my-header"><h3>Результаты на нашем сервере</h3></div>
                <div class="my-results">
                    <p>Собаки</p>
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 0;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" id="MyDogs">0</div>
                    </div>
                    <p>Кошки</p>
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 0;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" id="MyCats">0</div>
                    </div>
                    <p>Попугаи</p>
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 0;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"id="MyParrots">0</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</main>
<script src="/static/js/results.js"></script>
% include('footer.html')