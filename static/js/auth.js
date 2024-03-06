async function login(username, password) {
    await postData("/_login", {
        username: username,
        password: password
    }).then(response => {
        if (response && response.status) 
            openAdminPanel()
        else
            showText("Логин немесе құпия сөз қате", 2);
    })
}


function openAdminPanel() {
    document.location.href = "/";
}
