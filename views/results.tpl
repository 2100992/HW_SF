% include('header.html', title='Page Title')
<body>
<script type="text/javascript">
    const serverURL = '{{ url }}'
    const serverSFURL = '{{ urlSF }}'
</script>
<main>
    <div class='container'>
        % include('navbar.html')
        <div class="jumbotron">
            <h1 class="display-4">Результаты голосования</h1>
            <p class="lead">Нужны результаты</p>
            <hr class="my-4">
            <ul class="list-group">
            </ul>
        </div>
    </div>
</main>
% include('footer.html')
</body>