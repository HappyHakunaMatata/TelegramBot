



function updateTimer() {
    var htimerElement = document.getElementById("htimer");
    var mintimerElement = document.getElementById("mintimer");
    var sectimerElement = document.getElementById("sectimer");
    var bar = document.getElementById("AnimatedProgressbar");

    var timer = document.getElementById("toggle-timer");
    var timerText = timer.innerText;
    var timeArray = timerText.split(":");
    var timer_hours = parseInt(timeArray[0], 10);
    var timer_minutes = parseInt(timeArray[1], 10);

    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth();
    const day = now.getDate();
    const hour = now.getHours();
    const min = now.getMinutes();

    var tomorrow
    if (hour >= timer_hours && min >= timer_minutes) {
        tomorrow = new Date(year, month, day + 1);
    }
    else {
        tomorrow = new Date(year, month, day);
    }
    tomorrow.setHours(timer_hours, timer_minutes, 0, 0);
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
    var status = document.getElementById("hiddenProgressBarStatus");
    var lable = document.getElementById("toggle-label");

    if (switchCheckbox.checked) {
        updateTimer();
        timerInterval = setInterval(updateTimer, 1000);
        status.value = 1
        lable.innerText = "Удаление включено"
       
    } else {
        clearInterval(timerInterval);
        status.value = 0
        lable.innerText = "Удаление отключено"
       
    }
});



(function GetData() {
    var checkbox = document.getElementById("flexSwitchCheckDefault");
    var status = document.getElementById("hiddenProgressBarStatus");
    var lable = document.getElementById("toggle-label");
    if (status.value == "True") {
        checkbox.setAttribute("checked", "checked");
        updateTimer();
        timerInterval = setInterval(updateTimer, 1000);
        lable.innerText = "Удаление включено"
    }
    else {
        clearInterval(timerInterval);
        checkbox.removeAttribute("checked");
        lable.innerText = "Удаление отключено"
    }
})();

var timerInterval;

