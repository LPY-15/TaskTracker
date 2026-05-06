$(document).ready(function() {
    
    $('#js-create-task-form').on('submit', function (e) {

        e.preventDefault();
        const taskName = $('#task-create-form').val();
        const createTaskUrl = $('#js-create-task-form').data('create-task');

        $.ajax({
            type: 'POST',
            url: createTaskUrl,
            data: {
                action: 'create-task',
                task_name: taskName,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                $('#task-list').append(`
                    <div id="task-${response.id}">
                        <p>${response.task_name}</p>
                        <form method="POST" class="js-delete-task-form" data-delete-task="${createTaskUrl}">
                            <input type="hidden" name="csrfmiddlewaretoken" value="${$('input[name="csrfmiddlewaretoken"]').val()}">
                            <input type="hidden" class="js-task-id" value="${response.id}">
                            <input type="hidden" class="js-task-name" value="${response.task_name}">
                            <button type="submit">Delete</button>
                        </form>
                    </div>
                `);
                console.log(taskName + ' created');
                console.log(response)
                $('#task-create-form').val('');
            },
            error: function(err) {
                console.error('Error deleting task', err);
            }
        });
    });

    $('#task-list').on('submit', '.js-delete-task-form', function(e) {

        e.preventDefault();
        const form = $(this);
        const taskId = form.find('.js-task-id').val();
        const deleteUrl = form.data('delete-task');

        $.ajax({
            type: 'POST',
            url: deleteUrl,
            data: {
                action: 'delete-task',
                task_id: taskId,
                csrfmiddlewaretoken: form.find('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function() {
                form.closest('div[id^="task-"]').remove();
                console.log('deleted task ' + taskId)
            },
            error: function(err) {
                console.error('Error deleting task', err);
            }
        });
    });
});


