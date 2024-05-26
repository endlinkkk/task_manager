$(document).ready(function() {
    // Обработчик клика по кнопке "Изменить"
    $('.btn-edit').on('click', function() {
        // Получаем id задачи из атрибута data-task_id кнопки
        var taskId = $(this).data('task_id');
        // Устанавливаем полученное id в скрытое поле #actualTaskId
        $('#actualTaskId').val(taskId);
        // Показываем модальное окно
        $('#editTaskModal').modal('show');
    });

    $('.edit-task-form').submit(function(e) {
        e.preventDefault();



        let newData = {
            title: $('#taskName').val(),
            date: $('#taskDate').val(),
            taskId: $('#actualTaskId').val(),
        };

        const csrftoken = Cookies.get('csrftoken');

        $.ajax({
            type: 'PUT',
            headers: {'X-CSRFToken': csrftoken},
            url: '/',
            data: JSON.stringify(newData),
            contentType: 'application/json',
            success: function(response) {
                // Обработка успешного ответа от сервера
                $('#editTaskModal').modal('hide');
                location.reload();
            },
            error: function(error) {
                // Обработка ошибки AJAX запроса
                console.error(error);
                $('#actualTaskId').modal('hide');
            }
        });
    });
});



$(document).ready(function() {
    $('#addButton').click(function(event) {
        event.preventDefault();
        const csrftoken = Cookies.get('csrftoken');
        var note = $('#form3').val();
        
        $.ajax({
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            url: '/', // Замените на свой URL API endpoint
            data: JSON.stringify({ note: note }),
            contentType: 'application/json',
            success: function(response) {
                console.log('Note added successfully!');
                // Здесь вы можете добавить дополнительные действия при успешном добавлении заметки
                location.reload();
            },
            error: function(xhr, status, error) {
                console.error('Error adding note:', error);
                // Обработка ошибок, если не удалось добавить заметку
            }
        });
    });
});

$(document).ready(function() {
    $('#submitBtnLogout').click(function() {
        const csrftoken = Cookies.get('csrftoken');


        $.ajax({
            url: '/accounts/logout/',
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            success: function(response) {
                // Обработка успешного ответа от сервера
                console.log('Успех', response);
                location.reload();
            },
            error: function(xhr, status, error) {
                // Обработка ошибки при отправке данных
                console.error('Произошла ошибка при отправке данных:', error);
                
            }
        });
    });
});

$(document).ready(function() {
    $('.done-button').click(function(event) { // Изменено с '#addButton' на '#doneButton'
        event.preventDefault();
        const csrftoken = Cookies.get('csrftoken');
        var taskId = $(this).data('task_id');
        $.ajax({
            method: 'PATCH',
            headers: {'X-CSRFToken': csrftoken},
            url: '/', // Убедитесь, что это правильный URL для вашего API endpoint
            data: JSON.stringify({ done: true, taskId: taskId}), // Отправляем булево значение True
            contentType: 'application/json',
            success: function(response) {
                console.log('Task marked as done successfully!');
                // Добавьте здесь дополнительные действия после успешного выполнения задачи
                location.reload();
            },
            error: function(xhr, status, error) {
                console.error('Error marking task as done:', error);
                // Обработайте ошибки, если не удалось отметить задачу как выполненную
            }
        });
    });
});


$(document).ready(function() {
    $('.delete-button').click(function(event) { // Изменено с '#addButton' на '#doneButton'
        event.preventDefault();
        const csrftoken = Cookies.get('csrftoken');
        var taskId = $(this).data('task_id');
        $.ajax({
            method: 'DELETE',
            headers: {'X-CSRFToken': csrftoken},
            url: '/', // Убедитесь, что это правильный URL для вашего API endpoint
            data: JSON.stringify({ done: true, taskId: taskId}), // Отправляем булево значение True
            contentType: 'application/json',
            success: function(response) {
                console.log('Task marked as done successfully!');
                // Добавьте здесь дополнительные действия после успешного выполнения задачи
                location.reload();
            },
            error: function(xhr, status, error) {
                console.error('Error marking task as done:', error);
                // Обработайте ошибки, если не удалось отметить задачу как выполненную
            }
        });
    });
});