function parseDatetime(datetime) {
    let [date, time] = datetime.split("T");
    let [year, month, day] = date.split("-");

    hours = 0, minutes = 0;

    if (time)
        [hours, minutes] = time.split(":");

    return new Date(year, month - 1, day, hours, minutes);
}


async function createSession(patientFullname, employeeFullname, datetime) {
    if (datetime == "")
        return showText("Поле с датой и временем сеанса не должно быть пустым", 2);

    await api("createSession", {
        patientFullname: patientFullname,
        employeeFullname: employeeFullname,
        datetimeTimestamp: parseDatetime(datetime).valueOf() / 1000
    }).then(response => {
        if (response)
            showText("Сеанс успешно назначен", 1);
        else 
            showText("Произошла ошибка", 2);
    });
}


async function editSession(id, patientFullname, employeeFullname, datetime) {
    if (datetime == 0)
        return showText("Поле с датой и временем сеанса не должно быть пустым", 2)

    await api("editSession", {
        id: id,
        patientFullname: patientFullname,
        employeeFullname: employeeFullname,
        datetimeTimestamp: parseDatetime(datetime).valueOf() / 1000
    }).then(response => {
        if (response) 
            showText("Информация о сеансе успешно обновлена", 1);
        else 
            showText("Произошла ошибка", 2);
    });
}


async function deleteSession(id) {
    await api("deleteSession", {
        id: id
    }).then(response => {
        if (response) {
            showText("Сеанс успешно отменен", 1);

            document.location.href = "/schedule";
        }
        else 
            showText("Произошла ошибка", 2);
    });
}


async function getSchedules(patientFullname, employeeFullname, datetime, then) {
    if (datetime == "")
        return showText("Поле с датой не должно быть пустым", 2);

    startLoadingAnimation();

    return await api("getSchedules", {
        patientFullname: patientFullname,
        employeeFullname: employeeFullname,
        datetimeTimestamp: parseDatetime(datetime).valueOf() / 1000 || ""
    }).then(then);
}


function addSchedule(schedulesElement, employeeFullname, sessions) {
    let scheduleElement = document.createElement("div");

    scheduleElement.classList.add("schedule");
    scheduleElement.innerHTML = `
        <span class="employee-fullname">${employeeFullname}</span>
        <div class="sessions">
            <div class="session-number">
                <span>№</span>
            </div>
            <div class="session-time">
                <span>Время</span>
            </div>
            <div class="session-patient-fullname">
                <span>Пациент</span>
            </div>
            <div class="session-edit">
                <span>Ред.</span>
            </div>
        </div>
    `;

    let sessionNumberElement = scheduleElement.querySelector(".session-number");
    let sessionTimeElement = scheduleElement.querySelector(".session-time");
    let sessionPatientFullnameElement = scheduleElement.querySelector(".session-patient-fullname");
    let sessionEditElement = scheduleElement.querySelector(".session-edit");

    for (let i = 0; i < sessions.length; i++) {
        let session = sessions[i];

        let numberElement = document.createElement("span");
        numberElement.innerHTML = i + 1;

        let timeElement = document.createElement("span");
        timeElement.innerHTML = session.time;

        let patientFullnameElement = document.createElement("span");
        patientFullnameElement.innerHTML = session.patientFullname;

        let editElement = document.createElement("span");
        editElement.innerHTML = `<a href="/edit-session?sessionId=${session.id}">^</a>`

        sessionNumberElement.append(numberElement);
        sessionTimeElement.append(timeElement);
        sessionPatientFullnameElement.append(patientFullnameElement);
        sessionEditElement.append(editElement);
    }

    schedulesElement.append(scheduleElement);
}
