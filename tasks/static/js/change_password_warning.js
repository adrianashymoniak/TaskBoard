var isSubmitButtonClicked = false;

var isSomethingChanged = false;

$("#submit_btn").click(function () {
    isSubmitButtonClicked = true;
});

$("[name='change_password_from']").change(function () {
    isSomethingChanged = true;
});

$(window).bind('beforeunload', function () {
    if (!isSubmitButtonClicked && isSomethingChanged) {
        return 'Leave the site?';
    }
});