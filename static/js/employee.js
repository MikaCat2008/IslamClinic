async function createEmployee(fullname, age, gender, salary, jobCategory, jobTitle) {
    if (fullname == "")
        return showText(texts.fullnameEmpty, 2);

    if (age == "")
        return showText(texts.ageEmpty, 2);

    if (Number(age) != age)
        return showText(texts.ageNumber, 2);

    if (gender == "")
        return showText(texts.genderEmpty, 2);

    if (salary == "")
        return showText(texts.salaryEmpty, 2);

    if (Number(salary) != salary)
        return showText(texts.salaryNumber, 2);

    if (jobCategory == "")
        return showText(texts.jobCategoryEmpty, 2);

    if (jobTitle == "")
        return showText(texts.jobTitleEmpty, 2);

    await api("createEmployee", {
        fullname: fullname,
        age: age,
        gender: gender,
        salary: salary,
        jobCategory: jobCategory,
        jobTitle: jobTitle
    }).then(response => {
        if (response) 
            showText(texts.employeeAdded, 1);
        else 
            showText(texts.error, 2);
    })
}


async function getEmployees(id, fullname, age, gender, salary, jobCategory, jobTitle, then) {
    if (Number(id) != id)
        return showText(texts.idNumber, 2);

    if (Number(age) != age)
        return showText(texts.ageNumber, 2);

    if (Number(salary) != salary)
        return showText(texts.salaryNumber, 2);
    
    startLoadingAnimation();
    
    return await api("getEmployees", {
        id: id,
        fullname: fullname,
        age: age,
        gender: gender,
        salary: salary,
        jobCategory: jobCategory,
        jobTitle: jobTitle
    }).then(then);
}


async function editEmployee(id, fullname, age, gender, salary, jobCategory, jobTitle) {
    if (fullname == "")
        return showText(texts.fullnameEmpty, 2);

    if (age == "")
        return showText(texts.ageEmpty, 2);

    if (Number(age) != age)
        return showText(texts.ageNumber, 2);

    if (gender == "")
        return showText(texts.genderEmpty, 2);

    if (salary == "")
        return showText(texts.salaryEmpty, 2);

    if (Number(salary) != salary)
        return showText(texts.salaryNumber, 2);

    if (jobCategory == "")
        return showText(texts.jobCategoryEmpty, 2);

    if (jobTitle == "")
        return showText(texts.jobTitleEmpty, 2);

    await api("editEmployee", {
        id: id,
        fullname: fullname,
        age: age,
        gender: gender,
        salary: salary,
        jobCategory: jobCategory,
        jobTitle: jobTitle
    }).then(response => {
        if (response) 
            showText(texts.employeeEdited, 1);
        else 
            showText(texts.error, 2);
    })
}


async function deleteEmployee(id) {
    await api("deleteEmployee", {
        id: id
    }).then(response => {
        if (response) {
            showText(texts.employeeDeleted, 1);

            openEmployees();
        }
        else 
            showText(texts.error, 2);
    })
}


function addEmployee(dataElements, id, fullname, age, gender, salary, jobCategory, jobTitle) {
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
            <span>${texts.salary}</span>
            <span>${salary}</span>
        </div>
        <div class="data-pair">
            <span>${texts.jobCategory}</span>
            <span>${jobCategory}</span>
        </div>
        <div class="data-pair">
            <span>${texts.jobTitle}</span>
            <span>${jobTitle}</span>
        </div>
        <div class="data-pair">
            <span>${texts.edit}</span>
            <a href="/edit-employee?employeeId=${id}">^</a>
        </div>
    `;

    dataElements.append(dataElement);
}


function setJobTitleOptions(employeeJobTitleElement, options) {
    let innerHTML = `<option value="">-</option>`;

    for (let i = 0; i < options.length; i++) {
        let option = options[i]
        
        innerHTML += `<option value="${i}">${option}</option>`;
    }

    employeeJobTitleElement.innerHTML = innerHTML;
}


function onJobCategoryChange(employeeJobCategoryElement, employeeJobTitleElement) {
    let value = employeeJobCategoryElement.value;
    employeeJobTitleElement.value = "";

    if (value == "") {
        setJobTitleOptions(employeeJobTitleElement, []);
    }
    else {
        setJobTitleOptions(employeeJobTitleElement, texts.jobTitles[value]);
    }
}


function openEmployees() {
    document.location.href = "/employees";
}
