var isEditButtonClicked = false;

var isSomethingChanged = false;

$("#edit_task").click(function () {
    isEditButtonClicked = true;
});

$("[name='edit_form']").change(function () {
    isSomethingChanged = true;
});

$(window).bind('beforeunload', function () {
    if (!isEditButtonClicked && isSomethingChanged) {
        return 'Leave the site?';
    }
});