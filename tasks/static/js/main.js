$(document).ready(function() {
    $('#js-create-task-form').on('submit', function (e) {

        e.preventDefault();

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
            },
        });
    });
});