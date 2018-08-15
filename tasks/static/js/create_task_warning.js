var isSaveButtonClicked = false;

var isSomethingChanged = false;

$("#save_task").click(function () {
    isSaveButtonClicked = true;
});

$("[name='create_form']").change(function () {
    isSomethingChanged = true;
});

$(window).bind('beforeunload', function () {
    if (!isSaveButtonClicked && isSomethingChanged) {
        return 'Leave the site?';
    }
});