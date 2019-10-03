function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
};


// Пример использования: setCookie('user', 'John', {secure: true, 'max-age': 3600});
function setCookie(name, value, options = {}) {

    // let date = new Date(Date.now() + 86400e3);
    // date = date.toUTCString();

    options = {
        path: '/',
        // при необходимости добавьте другие значения по умолчанию
        //expires: date,
    };

    //if (options.expires.toUTCString) {
    if (options.expires) {
        options.expires = options.expires.toUTCString();
    }
  
    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);
  
    for (let optionKey in options) {
        updatedCookie += "; " + optionKey;
        let optionValue = options[optionKey];
        if (optionValue !== true) {
            updatedCookie += "=" + optionValue;
        }
    }
  
    document.cookie = updatedCookie;
}


function deleteCookie(name) {
    setCookie(name, "", {
        'max-age': -1
    })
}