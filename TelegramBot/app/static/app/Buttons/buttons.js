

(function GetSelect() {
    var rows = document.querySelectorAll('.selectable-row');
    var selectedRow = null;

    [...rows].map(function (row) {
        row.addEventListener('click', function () {
            if (row.classList.contains('selected')) {
                row.classList.remove('selected');
                selectedRow = null;
            } else {
                [...rows].map(function (r) {
                    r.classList.remove('selected');
                });
                row.classList.add('selected');
                selectedRow = row;
            }
        });
    });


$('#edit').on('click', function (e) {
    var selectedRow = $('#daily-message-table tbody tr.selected');
    var editDailyMessages = document.getElementById('edit-daily-messages-text');
    var editDailyTimestamp = document.getElementById('edit-daily-timestamp');
    if (!editDailyMessages || !editDailyTimestamp) {
        return
    }
    if (selectedRow.length > 0) {
        var id = selectedRow.find('td:first').text().trim();
        input = document.getElementById('edit-daily-messages-key')
        input.value = id
        var text = selectedRow.find('td:eq(1)').text().trim();
        editDailyMessages.value = text;
        var timestamp = selectedRow.find('td:eq(2)').text().trim();
        editDailyTimestamp.value = timestamp
        modal = new bootstrap.Modal(document.getElementById('edit-modal-daily-message'))
        modal.show()
    }
    else {
        modal = new bootstrap.Modal(document.getElementById('notification-modal-daily-message'))
        modal.show()
    }
});

$('#create').on('click', function (e) {
    modal = new bootstrap.Modal(document.getElementById('add-modal-daily-message'))
    modal.show()
});

$('#create-datetime').on('click', function (e) {

    modal = new bootstrap.Modal(document.getElementById('add-modal-datetime-message'))
    modal.show()
});


    $('#create-weekly').on('click', function (e) {
    modal = new bootstrap.Modal(document.getElementById('add-modal-weekly-message'))
    modal.show()
    });

    $('#delete').on('click', function (e) {
    var selectedRow = $('#daily-message-table tbody tr.selected');
    if (selectedRow.length > 0) {
        var id = selectedRow.find('td:first').text().trim();
        input = document.getElementById('delete-input-message')
        input.value = id
        modal = new bootstrap.Modal(document.getElementById('delete-modal-daily-message'))
        modal.show()
    }
    else {
        modal = new bootstrap.Modal(document.getElementById('notification-modal-daily-message'))
        modal.show()
    }
});

$('#edit-datetime').on('click', function (e) {
    var selectedRow = $('#datetime-message-table tbody tr.selected');
    var editDatetimeMessages = document.getElementById('edit-datetime-messages-text');
    var editDatetimeTimestamp = document.getElementById('edit-datetime-timestamp');
    var editDatetimeDate = document.getElementById('inputdate');

    if (!editDatetimeMessages || !editDatetimeTimestamp || !editDatetimeDate) {
        return
    }

    if (selectedRow.length > 0) {
        var id = selectedRow.find('td:eq(0)').text().trim();
        input = document.getElementById('edit-datetime-messages-key')
        input.value = id

        var text = selectedRow.find('td:eq(1)').text().trim();
        editDatetimeMessages.value = text;
        var timestamp = selectedRow.find('td:eq(2)').text().trim();
        editDatetimeTimestamp.value = timestamp
        var date = selectedRow.find('td:eq(3)').text().trim();
        editDatetimeDate.value = date
        modal = new bootstrap.Modal(document.getElementById('edit-modal-datetime-message'))
        modal.show()
    }
    else {
        modal = new bootstrap.Modal(document.getElementById('notification-modal-daily-message'))
        modal.show()
    }
});

$('#delete-datetime').on('click', function (e) {
    var selectedRow = $('#datetime-message-table tbody tr.selected');
    if (selectedRow.length > 0) {
        var id = selectedRow.find('td:first').text().trim();
        input = document.getElementById('delete-datetime-input-message')
        input.value = id
        modal = new bootstrap.Modal(document.getElementById('delete-modal-datetime-message'))
        modal.show()
    }
    else {
        modal = new bootstrap.Modal(document.getElementById('notification-modal-daily-message'))
        modal.show()
    }
});



    $('#edit-weekly').on('click', function (e) {
        var selectedRow = $('#weekly-message-table tbody tr.selected');
        var editDatetimeMessages = document.getElementById('edit-weekly-messages-text');
        var editDatetimeTimestamp = document.getElementById('edit-weekly-timestamp');
        

        if (!editDatetimeMessages || !editDatetimeTimestamp) {
            return
        }

        if (selectedRow.length > 0) {
            var id = selectedRow.find('td:eq(0)').text().trim();
            input = document.getElementById('edit-weekly-messages-key')
            input.value = id

            var text = selectedRow.find('td:eq(1)').text().trim();
            editDatetimeMessages.value = text;
            var timestamp = selectedRow.find('td:eq(2)').text().trim();
            editDatetimeTimestamp.value = timestamp
            modal = new bootstrap.Modal(document.getElementById('edit-modal-weekly-message'))
            modal.show()
        }
        else {
            modal = new bootstrap.Modal(document.getElementById('notification-modal-daily-message'))
            modal.show()
        }
    });

    $('#delete-weekly').on('click', function (e) {
        var selectedRow = $('#weekly-message-table tbody tr.selected');
        if (selectedRow.length > 0) {
            var id = selectedRow.find('td:first').text().trim();
            input = document.getElementById('delete-weekly-message')
            input.value = id
            modal = new bootstrap.Modal(document.getElementById('delete-modal-weekly-message'))
            modal.show()
        }
        else {
            modal = new bootstrap.Modal(document.getElementById('notification-modal-daily-message'))
            modal.show()
        }
    });

    $('#edit-toggle').on('click', function (e) {
        modal = new bootstrap.Modal(document.getElementById('edit-toggle-time'))
        modal.show()
    });

}())
