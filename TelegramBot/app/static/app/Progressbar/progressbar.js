

var htimerElement = document.getElementById("htimer");
var mintimerElement = document.getElementById("mintimer");
var sectimerElement = document.getElementById("sectimer");
var bar = document.getElementById("AnimatedProgressbar");

function updateTimer() {
    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth();
    const day = now.getDate();
    var tomorrow
    const hour = now.getHours();
    if (hour >= 2) {
        tomorrow = new Date(year, month, day + 1);
    }
    else {
        tomorrow = new Date(year, month, day);
    }
    tomorrow.setHours(2, 0, 0, 0);
    var timeDiff = tomorrow - now
    const hours = Math.floor(timeDiff / (1000 * 60 * 60));
    const minutes = Math.floor((timeDiff / (1000 * 60)) % 60);
    const seconds = Math.floor((timeDiff / 1000) % 60);
    htimerElement.innerHTML = hours;
    mintimerElement.innerHTML = minutes;
    sectimerElement.innerHTML = seconds;

    const totalSeconds = 24 * 60 * 60
    var progressBarWidth = 100 - (timeDiff / 1000) / (totalSeconds / 100);
    bar.style.width = progressBarWidth + "%";
}

document.getElementById("flexSwitchCheckDefault").addEventListener("change", function () {
    var switchCheckbox = this;

    var dataToSend = {
        ProgressbarStatus: null
    };
    if (switchCheckbox.checked) {
        timerInterval = setInterval(updateTimer, 1000);
        dataToSend.ProgressbarStatus = true
        ConnectToDatabase('/api/PostProgressbar/', 'POST', dataToSend)
    } else {
        clearInterval(timerInterval);
        dataToSend.ProgressbarStatus = false
        ConnectToDatabase('/api/PostProgressbar/', 'POST', dataToSend)
    }
});

function ConnectToDatabase(link, type, status) {
    $.ajax({
        url: link,
        type: type,
        dataType: 'json',
        data: status,
        success: function (data) {
            console.log(data)
            if (type == 'GET') {
                GetData(data);
            }
        },
        error: function (error) {
            console.error(error);
        }
    });
}

function GetData(data) {
    var checkbox = document.getElementById("flexSwitchCheckDefault");
    var firstItemOrNull = data.length > 0 ? data[0] : null;
    var progressbarStatus = firstItemOrNull.ProgressbarStatus;
    if (progressbarStatus == true) {
        checkbox.setAttribute("checked", "checked");
    }
    else {
        clearInterval(timerInterval);
        checkbox.removeAttribute("checked");
    }
}


ConnectToDatabase('/api/GetProgressbar/', 'GET')
updateTimer();
var timerInterval = setInterval(updateTimer, 1000);