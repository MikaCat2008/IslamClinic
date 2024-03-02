function setDate(dateElement, date) {
    let timezoneOffset = date.getTimezoneOffset();
    let adjustedDate = new Date(date.getTime() - (timezoneOffset * 60 * 1000));
    
    dateElement.value = adjustedDate.toISOString().slice(0, 10);
}


function setDatetime(datetimeElement, date) {
    let timezoneOffset = date.getTimezoneOffset();
    let adjustedDate = new Date(date.getTime() - (timezoneOffset * 60 * 1000));
    
    datetimeElement.value = adjustedDate.toISOString().slice(0, 16);
}


function startLoadingAnimation() {
    document.querySelector(".loading-animation").style.display = "block";
}


function stopLoadingAnimation() {
    document.querySelector(".loading-animation").style.display = "none";
}


function openWindow(windowElement) {
    windowElement.style.display = "flex"
    setTimeout(() => {windowElement.style.opacity = 1}, 20);
}


function closeWindow(windowElement) {
    windowElement.style.opacity = 0;
    setTimeout(() => {windowElement.style.display = "none";}, 200);
}


function showText(text, type) {
    let showTextElement = document.querySelector("#show-text");
    let showTextWindowElement = document.createElement("div");

    showTextWindowElement.innerHTML = "<span></span>"

    showTextElement.append(showTextWindowElement);

    showTextWindowElement.querySelector("span").innerHTML = text;
    showTextWindowElement.classList.add("show-text-window");

    if (type == 1) {
        showTextWindowElement.classList.add("show-text-window-success");
    }
    else if (type == 2) {
        showTextWindowElement.classList.add("show-text-window-error");
    }

    setTimeout(() => {
        showTextWindowElement.classList.add("show-text-window-out");
    }, 20)
    setTimeout(() => {
        showTextWindowElement.classList.remove("show-text-window-out");
    }, 2500);
    setTimeout(() => {
        showTextWindowElement.remove();
    }, 3300)
}


async function postData(url, data) {
    return await (await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })).json();
}


async function api(method, data) {
    return await postData("/api", {
        method: method,
        data: data
    }).catch(response => showText("Произошла ошибка", 2))
}
