async function createPatient(fullname, age, gender, familyDoctorFullname) {
    if (fullname == "")
        return showText(texts.fullnameEmpty, 2);

    if (age == "")
        return showText(texts.ageEmpty, 2);

    if (Number(age) != age)
        return showText(texts.ageNumber, 2);

    if (gender == "")
        return showText(texts.genderEmpty, 2);

    if (familyDoctorFullname == "")
        return showText(texts.familyDoctorEmpty, 2);

    await api("createPatient", {
        fullname: fullname,
        age: age,
        gender: gender,
        familyDoctorFullname: familyDoctorFullname
    }).then(response => {
        if (response) 
            showText(texts.patientAdded, 1);
        else 
            showText(texts.error, 2);
    })
}


async function getPatients(id, fullname, age, gender, familyDoctorFullname, then) {
    if (Number(id) != id)
        return showText(texts.idNumber, 2);

    if (Number(age) != age)
        return showText(texts.ageNumber, 2);
    
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
        return showText(texts.fullnameEmpty, 2);

    if (age == "")
        return showText(texts.ageEmpty, 2);

    if (Number(age) != age)
        return showText(texts.ageNumber, 2);

    if (gender == "")
        return showText(texts.genderEmpty, 2);

    if (familyDoctorFullname == "")
        return showText(texts.familyDoctorEmpty, 2);

    await api("editPatient", {
        id: id,
        fullname: fullname,
        age: age,
        gender: gender,
        familyDoctorFullname: familyDoctorFullname
    }).then(response => {
        if (response) 
            showText(texts.patientEdited, 1);
        else 
            showText(texts.error, 2);
    })
}


async function deletePatient(id) {
    await api("deletePatient", {
        id: id
    }).then(response => {
        if (response) {
            showText(texts.patientDeleted, 1);

            openPatients();
        }
        else 
            showText(texts.error, 2);
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
            <span>${texts.fullname}</span>
            <span>${fullname}</span>
        </div>
        <div class="data-pair">
            <span>${texts.age}</span>
            <span>${age}</span>
        </div>
        <div class="data-pair">
            <span>${texts.gender}</span>
            <span>${gender}</span>
        </div>
        <div class="data-pair">
            <span>${texts.familyDoctor}</span>
            <span>${familyDoctorFullname}</span>
        </div>
        <div class="data-pair">
            <span>${texts.edit}</span>
            <a href="/edit-patient?patientId=${id}">^</a>
        </div>
    `;

    dataElements.append(dataElement);
}


function openPatients() {
    document.location.href = "/patients";
}
