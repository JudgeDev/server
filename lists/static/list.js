window.Server = {};  // namespace as property of window global
window.Server.initialize = function () {  // function is attribute of Server namespace
    // find input elements called text, on keypress, hide all elements with class .has_error
    $('input[name="text"]').on('keypress', function () {
        $('.has-error').hide();
    });
};
