var isSubmitButtonClicked = false;

var isSomethingChanged = false;

$("[type='submit']").click(function () {
    isSubmitButtonClicked = true;
});

$("[name='form']").change(function () {
    isSomethingChanged = true;
});

$(window).bind('beforeunload', function () {
    if (!isSubmitButtonClicked && isSomethingChanged) {
        return 'Leave the site?';
    }
});
