
(function ToastFunction() {
    const toastBody = document.querySelector('.toast-body');
    if (!toastBody) {
        return;
    }
    const messageText = toastBody.textContent.trim();
    if (messageText.length > 0) {
        var toastElement = document.querySelector('.toast');
        var toast = new bootstrap.Toast(toastElement);
        toast.show();
    }
})()