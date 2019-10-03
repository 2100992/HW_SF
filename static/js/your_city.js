const setCity = $('#set-city')
const remCity = $('#rem-city')
const isKnown = $('.is-known')
const isUnknown = $('.is-unknown')
const yourCity = $('#your-city')


function init() {
    // $('#yourCityID').addClass('active');
    let city = getCookie('my_city');
    if (city === null || city === undefined || city === '') {
        isUnknown.removeClass('d-none');
        isKnown.addClass('d-none');
    } else {
        yourCity.text(city)
        isKnown.removeClass('d-none');
        isUnknown.addClass('d-none');
    }


    setCity.click(function() {
        city = $("#input-city").val();
        if (city != '') {
            setCookie('my_city', city, {'max-age': 3600});
            isKnown.removeClass('d-none')
            isUnknown.addClass('d-none')
        };
    });

    remCity.click(function() {
        deleteCookie('my_city')
        isUnknown.removeClass('d-none')
        isKnown.addClass('d-none')
    })
}

$(document).ready(init);
