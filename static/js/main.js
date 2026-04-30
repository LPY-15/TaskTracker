$(document).ready(function() {
    $('#js-create-task-form').on('submit', function (e) {

        e.preventDefault();
        console.log('Form is being submitted via AJAX');

        const TaskName = $('#task-create-form').val()
        const createTaskUrl = $('#js-create-task-form').data('create-task')
        $.ajax({
            type: 'POST',
            url: createTaskUrl,
            data: {
                task_name: TaskName,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response, data) {
                console.log('task created');
                console.log(response);
                $('#js-create-task-btn').hide();
            },
        });
    });
    $('#js-create-task-btn').on('click', function(e) {
        $('#js-create-task-form').submit();
    });
});