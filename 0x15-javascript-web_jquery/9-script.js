$(
  $.get('https://fourtonfish.com/hellosalut/?lang=en', function (data) {
    $('DIV#hello').text(data.hello);
  }));
