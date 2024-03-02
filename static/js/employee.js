async function createEmployee(fullname, age, gender, salary, jobCategory, jobTitle) {
    if (fullname == "")
        return showText("Поле с ФИО не должно быть пустым", 2);

    if (age == "")
        return showText("Поле с возрастом не должно быть пустым", 2);

    if (Number(age) != age)
        return showText("Поле с возрастом должно быть числом", 2);

    if (gender == "")
        return showText("Поле с полом не должно быть пустым", 2);

    if (salary == "")
        return showText("Поле с окладом не должно быть пустым", 2);

    if (Number(salary) != salary)
        return showText("Поле с окладом должно быть числом", 2);

    if (jobCategory == "")
        return showText("Поле с отделением не должно быть пустым", 2);

    if (jobTitle == "")
        return showText("Поле со специальностью не должно быть пустым", 2);

    await api("createEmployee", {
        fullname: fullname,
        age: age,
        gender: gender,
        salary: salary,
        jobCategory: jobCategory,
        jobTitle: jobTitle
    }).then(response => {
        if (response) 
            showText("Сотрудник успешно добавлен", 1);
        else 
            showText("Произошла ошибка", 2);
    })
}


async function getEmployees(id, fullname, age, gender, salary, jobCategory, jobTitle, then) {
    if (Number(id) != id)
        return showText("Поле с номером пациента должно быть числом", 2);

    if (Number(age) != age)
        return showText("Поле с возрастом должно быть числом", 2);

    if (Number(salary) != salary)
        return showText("Поле с окладом должно быть числом", 2);
    
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
        return showText("Поле с ФИО не должно быть пустым", 2);

    if (age == "")
        return showText("Поле с возрастом не должно быть пустым", 2);

    if (Number(age) != age)
        return showText("Поле с возрастом должно быть числом", 2);

    if (gender == "")
        return showText("Поле с полом не должно быть пустым", 2);

    if (salary == "")
        return showText("Поле с окладом не должно быть пустым", 2);

    if (Number(salary) != salary)
        return showText("Поле с окладом должно быть числом", 2);

    if (jobCategory == "")
        return showText("Поле с отделением не должно быть пустым", 2);

    if (jobTitle == "")
        return showText("Поле со специальностью не должно быть пустым", 2);

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
            showText("Информация о сотруднике успешно обновлена", 1);
        else 
            showText("Произошла ошибка", 2);
    })
}


async function deleteEmployee(id) {
    await api("deleteEmployee", {
        id: id
    }).then(response => {
        if (response) {
            showText("Сотрудник успешно удален", 1);

            document.location.href = "/employees";
        }
        else 
            showText("Произошла ошибка", 2);
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
            <span>Оклад</span>
            <span>${salary}</span>
        </div>
        <div class="data-pair">
            <span>Отделение</span>
            <span>${jobCategory}</span>
        </div>
        <div class="data-pair">
            <span>Специальность</span>
            <span>${jobTitle}</span>
        </div>
        <div class="data-pair">
            <span>Ред.</span>
            <a href="/edit-employee?employeeId=${id}">^</a>
        </div>
    `;

    dataElements.append(dataElement);
}


function openEmployee() {
    document.location.href = "/employees";
}
