async function createPatient(fullname, age, gender, familyDoctorFullname) {
    if (fullname == "")
        return showText("Поле с ФИО не должно быть пустым", 2);

    if (age == "")
        return showText("Поле с возрастом не должно быть пустым", 2);

    if (Number(age) != age)
        return showText("Поле с возрастом должно быть числом", 2);

    if (gender == "")
        return showText("Поле с полом не должно быть пустым", 2);

    if (familyDoctorFullname == "")
        return showText("Поле с ФИО семейного врача не должно быть пустым", 2);

    await api("createPatient", {
        fullname: fullname,
        age: age,
        gender: gender,
        familyDoctorFullname: familyDoctorFullname
    }).then(response => {
        if (response) 
            showText("Пациент успешно добавлен", 1);
        else 
            showText("Произошла ошибка", 2);
    })
}


async function getPatients(id, fullname, age, gender, familyDoctorFullname, then) {
    startLoadingAnimation();
    
    return await api("getPatients", {
        id: id,
        fullname: fullname,
        age: age,
        gender: gender,
        familyDoctorFullname: familyDoctorFullname
    }).then(then);
}


async function editPatient(id, fullname, age, gender, familyDoctorFullname) {
    if (fullname == "")
        return showText("Поле с ФИО не должно быть пустым", 2);

    if (age == "")
        return showText("Поле с возрастом не должно быть пустым", 2);

    if (Number(age) != age)
        return showText("Поле с возрастом должно быть числом", 2);

    if (gender == "")
        return showText("Поле с полом не должно быть пустым", 2);

    if (familyDoctorFullname == "")
        return showText("Поле с ФИО семейного врача не должно быть пустым", 2);

    await api("editPatient", {
        id: id,
        fullname: fullname,
        age: age,
        gender: gender,
        familyDoctorFullname: familyDoctorFullname
    }).then(response => {
        if (response) 
            showText("Информация о пациенте успешно обновлена", 1);
        else 
            showText("Произошла ошибка", 2);
    })
}


async function deletePatient(id) {
    await api("deletePatient", {
        id: id
    }).then(response => {
        if (response) {
            showText("Пациент успешно удален", 1);

            document.location.href = "/patients";
        }
        else 
            showText("Произошла ошибка", 2);
    })
}


function addPatient(dataElements, id, fullname, age, gender, familyDoctorFullname) {
    let dataElement = document.createElement("div");

    dataElement.classList.add("data-element");
    dataElement.innerHTML = `
        <div class="data-pair">
            <span>ID</span>
            <span>${id}</span>
        </div>
        <div class="data-pair">
            <span>ФИО</span>
            <span>${fullname}</span>
        </div>
        <div class="data-pair">
            <span>Возраст</span>
            <span>${age}</span>
        </div>
        <div class="data-pair">
            <span>Пол</span>
            <span>${gender}</span>
        </div>
        <div class="data-pair">
            <span>Семейный врач</span>
            <span>${familyDoctorFullname}</span>
        </div>
        <div class="data-pair">
            <span>Ред.</span>
            <a href="/edit-patient?patientId=${id}">^</a>
        </div>
    `;

    dataElements.append(dataElement);
}


function openPatients() {
    document.location.href = "/patients";
}
