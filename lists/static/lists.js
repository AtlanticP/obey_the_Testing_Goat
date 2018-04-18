console.log('loaded lists.js')
window.Superlists = {};
window.Superlists.initialize = function () {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
    console.log('error has been hided')
  });
};