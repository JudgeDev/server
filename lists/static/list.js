var initialize = function () {
    console.log('initialize called');
    // find input elements called text, on keypress, hide all elements with class .has_error
    $('input[name="text"]').on('keypress', function () {
        $('.has-error').hide();
    });
};
console.log('list.js loaded');
