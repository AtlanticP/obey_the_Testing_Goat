console.log('list.js')
var initialize = function () {
  $('input[name="text"]').on('keypress', function () {
    console.log('Miracle! It works!');
    $('.has-error').hide();
  });
};