
function RealoadTable() {
    setInterval(function () {
        DestroyTableContent();
        ConnectToDatabase();
    }, 30000);
}


function DestroyTableContent() {
    var tbody = document.getElementById("daily-message-table").getElementsByTagName('tbody')[0];
    tbody.innerHTML = '';
}




function AddRow(data) {
    var table = document.getElementById("daily-message-table").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.rows.length);


    newRow.className = "selectable-row";

    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);


    cell1.className = "border-bottom-0";
    cell2.className = "border-bottom-0";
    cell3.className = "border-bottom-0";
    cell4.className = "border-bottom-0";

    var h6_1 = document.createElement("h6");
    h6_1.className = "fw-semibold mb-0";
    h6_1.textContent = data.primaryKey;
    cell1.appendChild(h6_1);

    var h6_2 = document.createElement("h6");
    h6_2.className = "fw-semibold mb-1";
    h6_2.textContent = data.text;
    cell2.appendChild(h6_2);

    var p = document.createElement("p");
    p.className = "mb-0 fw-normal";
    p.textContent = FormatTimestamp(data.timestamp);
    cell3.appendChild(p);

    var div = document.createElement("div");
    div.className = "d-flex align-items-center gap-2";
    var span = document.createElement("span");
    span.className = "badge bg-primary rounded-3 fw-semibold";
    span.textContent = data.CreateDateTime;
    div.appendChild(span);
    cell4.appendChild(div);
}

function FormatTimestamp(timestampString) {
    var timestamp = new Date(timestampString);
    var hours = timestamp.getHours();
    var minutes = timestamp.getMinutes();
    return hours + ":" + (minutes < 10 ? "0" : "") + minutes;
}




function ConnectToDatabase() {
    $.ajax({
        url: '/api/data/', 
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            BuildTable(data)
            console.log(data);
        },
        error: function (error) {
            console.error(error);
        }
    });
}

    function BuildTable(data) {
        for (var i = 0; i < data.length; i++) {
            AddRow(data[i]);
        }
    }