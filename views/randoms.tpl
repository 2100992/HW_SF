% include('header.html', title='Page Title')
<body>
<div class='container'>
% include('navbar.html')
</div>
<main>
    <div class='container'>
        <section class="mt-5 d-flex justify-content-center">
            <div class="progress col-4 d-flex justify-content-center">
                <div class="progress-bar" role="progressbar" style="width: 0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
        </section>
    </div>
</main>
<script src="/static/js/randoms.js"></script>
% include('footer.html')