async function login(username, password) {
    await api("login", {
        username: username,
        password: password
    }).then(response => {
        if (response && response.status) 
            openAdminPanel()
        else
            showText("Неправильный логин или пароль", 2);
    })
}


function openAdminPanel() {
    document.location.href = "/";
}
